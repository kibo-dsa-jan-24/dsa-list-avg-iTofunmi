import unittest
from listavg import ListAverage

class TestListAverage(unittest.TestCase):
    def test(self):
        lavg = ListAverage([1, 2, 3])
        assert lavg.compute_avg() == 2.0

    # add more unit tests below
    def test_faster(self):
        faster_avg = ListAverage([1,2,3])
        assert faster_avg.compute_avg_faster() == 2.0

    def test_faster_add(self):
        faster_add = ListAverage([1,2,3])
        faster_add.add(6)
        assert faster_add.compute_avg_faster() == 3.0


    
