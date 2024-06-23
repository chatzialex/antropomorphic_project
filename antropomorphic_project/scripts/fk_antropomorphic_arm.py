#!/usr/bin/env python3

from sympy import preview, simplify
from sympy.interactive import printing 
from antropomorphic_project.dh_matrix import AntromorphicDhMatrices

def main():
  dh_matrices = AntromorphicDhMatrices()
     
  theta_1_val = input("Enter the value for theta_1: ")
  theta_2_val = input("Enter the value for theta_2: ")
  theta_3_val = input("Enter the value for theta_3: ")
  r_2_val = 1.0
  r_3_val = 1.0
  
  A03_evaluated = (simplify(dh_matrices.A03)
    .subs(dh_matrices.theta_1,theta_1_val)
    .subs(dh_matrices.theta_2,theta_2_val)
    .subs(dh_matrices.theta_3, theta_3_val)
    .subs(dh_matrices.r_2, r_2_val)
    .subs(dh_matrices.r_3, r_3_val)
  ).evalf(15)

  print("Position Matrix:")
  print(A03_evaluated[0:3,3])
  print("Orientation Matrix:")
  print(A03_evaluated[0:3,0:3])

  printing.init_printing(use_latex = True)
  preview(A03_evaluated, viewer='file', filename="A03_simplify_evaluated.png", dvioptions=['-D','300'])

if __name__ == "__main__":
  main()