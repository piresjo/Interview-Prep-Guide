import pytest
from maxContainerArea import *


class Test:

    def testImplementation(self):
        assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
        assert maxArea([1, 1]) == 1
        assert maxArea([1, 2, 3, 4, 5]) == 6
