#!/usr/bin/env python3

from math import atan2, pi, sin, cos, sqrt, isnan

class AntropomorphicIk:
  determinant_tolerance = 1e-5

  def __init__(self, r2 = 1.0, r3 = 1.0):
    if r2 == 0 or r3 == 0:
      raise ValueError("The values r2 and r3 must be nonzero.")
    
    self.r2 = r2
    self.r3 = r3

  def isPossible(self, thetas):
    return (-pi/4 <= thetas[1] and thetas[1] <= 3*pi/4
            and -3*pi/4 <= thetas[2] and thetas[2] <= 3*pi/4)

  def computeIk(self, Pee_x, Pee_y, Pee_z):
    theta_array = []
    possible_solution_array = []
    
    c_3 = ((Pee_x**2 + Pee_y**2 + Pee_z**2 - self.r2**2 - self.r3**2) 
         / (2 * self.r2 * self.r3))
    
    if c_3 > 1  or c_3 < -1:
      return [], []

    for sign_1 in (1, -1):
      for sign_3 in (1, -1):
        theta_3 = atan2(sign_3 * sqrt(1 - c_3**2), c_3)
        theta_1 = atan2(sign_1 * Pee_y, sign_1 * Pee_x)

        A = self.r3 * sin(theta_3)
        B = self.r2 + self.r3 * c_3
        if (A**2 + B**2 > self.determinant_tolerance):
          if sin(theta_1) != 0:
            s_2 = (-A / sin(theta_1)) * Pee_y + B * Pee_z
            c_2 = (B / sin(theta_1)) * Pee_y + A * Pee_z
          else: # cos(theta_1) != 0
            s_2 = (-A / cos(theta_1)) * Pee_x + B * Pee_z
            c_2 = (B / cos(theta_1)) * Pee_x + A * Pee_z
          theta_2 = atan2(s_2, c_2)
        else:
          #theta_2 can be anything
          theta_2=float('nan')

        thetas = [theta_1, theta_2, theta_3]
        theta_array.append(thetas)
        possible_solution_array.append(
          all(not isnan(x) for x in thetas) and self.isPossible(thetas))

    return theta_array, possible_solution_array