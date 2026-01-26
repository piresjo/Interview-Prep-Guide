import pytest
from pascalTriangle import *


class Test:

    def testGeneral(self):
        assert generate(1) == [[1]]
        assert generate(2) == [[1], [1, 1]]
        assert generate(3) == [[1], [1, 1], [1, 2, 1]]
        assert generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
