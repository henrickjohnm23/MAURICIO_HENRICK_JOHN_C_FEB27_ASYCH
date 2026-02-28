# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 19:10:25 2026

@author: henri
"""

# The Likehood

def likehood_func(datum, mu):
    likehood_out = sts.norm.pdf(datum, mu, scale = 0.1)
    return likehood_out/likehood_out.sum()

likehood_out = likehood_func(1.7, mu)

plt.plot(mu, likehood_out)
plt.title("Likehood of $\mu$ given observation 1.7m")
plt.ylabel("Probability Density/Likehood")
plt.xlabel("Value of $\mu$")
plt.show()
