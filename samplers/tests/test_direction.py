""" This module will test the functionality of samplers.DirectionalSampler
"""
import unittest
import samplers
from scipy.stats import kstest, uniform
import numpy as np
import math


class TestDirectionalSampler(unittest.TestCase):
    """ Class for testing the Directional sampler
    """

    def setup(self):
        """
        """
        pass

    def test_2D(self):
        """
        """
        sampler = samplers.DirectionalSampler(2)
        samples = sampler.generate_samples(10000)
        norms = np.linalg.norm(samples, axis=1)
        deltas = np.fabs(norms - 1.)
        msg = "At least one sample does not represent a unit vector"
        self.assertLessEqual(np.max(deltas), 1e-6, msg)

        thetas = np.arctan2(samples[:, 1], samples[:, 0])
        thetas /= 2*math.pi
        thetas += 0.5
        p = kstest(thetas, uniform.cdf)[1]
        msg = "The ditribution of angles is not representative of a uniform distribution (p={})".format(p)
        self.assertGreaterEqual(p, 0.05, msg)


if __name__ == "__main__":
    unittest.main()