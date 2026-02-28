# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 19:18:51 2026

@author: henri
"""

# The Posterior

import scipy as sp

unnormalized_posterior = likehood_out * uniform_dist
plt.plot(mu, unnormalized_posterior)
plt.xlabel("$\mu$ in meters")
plt.ylabel("Unnormalized Posterior")
plt.show()