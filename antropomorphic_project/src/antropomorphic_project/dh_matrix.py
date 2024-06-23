#!/usr/bin/env python3

from sympy import Matrix, cos, sin, Symbol, simplify, trigsimp, pi

class DhMatrix:  
  theta_i = Symbol("theta_i")
  alpha_i = Symbol("alpha_i")
  r_i = Symbol("r_i")
  d_i = Symbol("d_i")

  dh_matrix_generic = simplify(
    Matrix([
      [cos(theta_i), -sin(theta_i)*cos(alpha_i), sin(theta_i)*sin(alpha_i), r_i*cos(theta_i)],
      [sin(theta_i), cos(theta_i)*cos(alpha_i), -cos(theta_i)*sin(alpha_i), r_i*sin(theta_i)],
      [0, sin(alpha_i), cos(alpha_i), d_i],
      [0,0,0,1]
  ]))

  def compute_dh_matrix(self, theta, alpha, r, d):
    return trigsimp(
      self.dh_matrix_generic
        .subs(self.r_i,r).subs(self.alpha_i,alpha).subs(self.d_i,d).subs(self.theta_i, theta)
    )


class AntromorphicDhMatrices:
  dh_matrix = DhMatrix()

  theta_1 = Symbol("theta_1")
  theta_2 = Symbol("theta_2")
  theta_3 = Symbol("theta_3")

  alpha_planar = 0.0
  alpha_1 = pi/2
  alpha_2 = alpha_planar
  alpha_3 = alpha_planar

  r_1 = 0.0
  r_2 = Symbol("r_2")
  r_3 = Symbol("r_3")

  d_planar = 0.0
  d_1 = d_planar
  d_2 = d_planar
  d_3 = d_planar    

  A01 = dh_matrix.compute_dh_matrix(theta_1, alpha_1, r_1, d_1)
  A12 = dh_matrix.compute_dh_matrix(theta_2, alpha_2, r_2, d_2)
  A23 = dh_matrix.compute_dh_matrix(theta_3, alpha_3, r_3, d_3)

  A03 = A01 * A12 * A23