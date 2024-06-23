#!/usr/bin/env python3

from sympy import preview, simplify
from sympy.interactive import printing 
from antropomorphic_project.dh_matrix import AntromorphicDhMatrices

def main():
  dh_matrices = AntromorphicDhMatrices()

  printing.init_printing(use_latex = True) 
  
  preview(dh_matrices.dh_matrix.dh_matrix_generic, 
          viewer='file', filename="out.png", dvioptions=['-D','300'])
  preview(dh_matrices.A01, viewer='file', filename="A0_1.png", dvioptions=['-D','300'])
  preview(dh_matrices.A12, viewer='file', filename="A1_2.png", dvioptions=['-D','300'])
  preview(dh_matrices.A23, viewer='file', filename="A2_3.png", dvioptions=['-D','300'])
  preview(dh_matrices.A03, viewer='file', filename="A0_3.png", dvioptions=['-D','300'])
  preview(simplify(dh_matrices.A03), viewer='file', filename="A0_3_simplified.png", dvioptions=['-D','300'])


if __name__ == "__main__":
  main()