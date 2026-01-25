import pytest
from stackMin import *


class Test:
    def test(self):
        assert minimumOnStack(
            [
                "push 10",
                "min",
                "push 5",
                "min",
                "push 8",
                "min",
                "pop",
                "min",
                "pop",
                "min",
            ]
        ) == [10, 5, 5, 5, 10]

        assert minimumOnStack([]) == []
        assert minimumOnStack(["push 10"]) == []
        assert minimumOnStack(["min"]) == []
        assert minimumOnStack(["pop"]) == []
