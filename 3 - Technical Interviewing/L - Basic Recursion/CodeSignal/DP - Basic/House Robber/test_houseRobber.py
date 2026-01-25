import pytest
from houseRobber import *


class Test:

    def testWithEdgeCases(self):
        assert houseRobber(None) == 0
        assert houseRobber([]) == 0
        assert houseRobber([1]) == 1
        assert houseRobber([1, 4]) == 4

    def testGeneralCases(self):
        assert houseRobber([1, 1, 1]) == 2
        assert houseRobber([1, 2, 1, 0]) == 2
        assert (
            houseRobber(
                [
                    55,
                    72,
                    209,
                    143,
                    216,
                    220,
                    122,
                    115,
                    87,
                    227,
                    220,
                    161,
                    79,
                    230,
                    55,
                    56,
                    56,
                    178,
                    124,
                    88,
                    202,
                    65,
                    102,
                ]
            )
            == 1758
        )
