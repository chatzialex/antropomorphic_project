#!/usr/bin/env python3

from antropomorphic_project.ik import AntropomorphicIk

def main():
  Pee_x = float(input("Enter the value for Pee_x: "))
  Pee_y = float(input("Enter the value for Pee_y: "))
  Pee_z = float(input("Enter the value for Pee_z: "))

  ik_solver = AntropomorphicIk()
  thetas_array, possible_solution_array = ik_solver.computeIk(Pee_x, Pee_y, Pee_z)
  
  for thetas, possible in zip(thetas_array, possible_solution_array):
       print("Angles thetas solved =" + str(thetas) + ", solution possible = " + str(possible))

if __name__ == '__main__':
    main()

