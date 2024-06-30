cmake_minimum_required(VERSION 3.0.2)
project(antropomorphic_project)


find_package(catkin REQUIRED COMPONENTS
  rospy
)

install(DIRECTORY launch/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

catkin_python_setup()

catkin_package()