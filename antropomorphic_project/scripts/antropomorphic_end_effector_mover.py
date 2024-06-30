#!/usr/bin/env python3

from antropomorphic_project.move_joints import JointMover
from antropomorphic_project.rviz_marker import MarkerBasics
from antropomorphic_project.ik import AntropomorphicIk

from planar_3dof_control.msg import EndEffector
from geometry_msgs.msg import Vector3

import rospy

from math import dist


class AntopomorphicEEMover(object):
  def __init__(self, wait_reach_goal=True):
    rospy.loginfo("Initializing AntropomorphicEEMover...")

    self.ee_pose_sub = rospy.Subscriber("/end_effector_real_pose", Vector3, self.eePoseCallback)
    self.ee_pose = self.getFirstMessage("/end_effector_real_pose", Vector3)

    self.ee_cmd_sub = rospy.Subscriber("/ee_pose_commands", EndEffector, self.eeCommandsCallback)
    self.ee_cmd = self.getFirstMessage("/ee_pose_commands", EndEffector)

    self.markerbasics_object = MarkerBasics()
    self.unique_marker_index = 0
    self.robot_mover = JointMover()
    self.ik_solver = AntropomorphicIk()

    rospy.loginfo("AntropomorphicEEMover initialized.")

  def getFirstMessage(self, topic_name, topic_type):
    data = None

    while data is None and not rospy.is_shutdown():
      try:
        data = rospy.wait_for_message(topic_name, topic_type, timeout=0.5)
      except:
        rospy.logwarn("Waiting for message on topic \"" + str(topic_name) + "\"")
        pass

    return data

  def getClosestThetas(self, ee_cmd):
    thetas_array, possible_solutions_array = self.ik_solver.computeIk(
      Pee_x = ee_cmd.ee_xy_theta.x,
      Pee_y = ee_cmd.ee_xy_theta.y,
      Pee_z = ee_cmd.ee_xy_theta.z
    )

    thetas_possible = [thetas
      for thetas, possible
      in zip(thetas_array, possible_solutions_array)
      if possible
    ]

    if not thetas_possible:
      return None
    else:
      return min(thetas_possible,
        key=lambda v: dist(v, [self.ee_pose.x, self.ee_pose.y, self.ee_pose.z]))

  def eePoseCallback(self,msg):
    self.ee_pose = msg

  def eeCommandsCallback(self, msg):
    self.ee_cmd = msg

    thetas_closest = self.getClosestThetas(msg)

    if thetas_closest:
      self.robot_mover.move_all_joints(*thetas_closest)
      self.markerbasics_object.publish_point(x=self.ee_cmd.ee_xy_theta.x,
                                             y=self.ee_cmd.ee_xy_theta.y,
                                             z=self.ee_cmd.ee_xy_theta.z,
                                             index=self.unique_marker_index)
      self.unique_marker_index += 1
    else:
      rospy.logerr("No possible IK solution found, the pose is unreachable by the robot.")


def main():
    rospy.init_node('antropomorphic_end_effector_mover')
    antropomorphic_end_effector_mover = AntopomorphicEEMover()
    rospy.spin()

if __name__ == '__main__':
    main()