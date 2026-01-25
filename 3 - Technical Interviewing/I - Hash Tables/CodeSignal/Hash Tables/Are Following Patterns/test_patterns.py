import pytest
from patterns import *


class Test:
    def test(self):
        stringsA = ["cat", "dog", "dog"]
        patternsA = ["a", "b", "b"]
        stringsB = ["re", "jjinh", "rnz", "frok", "frok", "hxytef", "hxytef", "frok"]
        patternsB = [
            "kzfzmjwe",
            "fgbugiomo",
            "ocuijka",
            "gafdrts",
            "gafdrts",
            "ebdva",
            "ebdva",
            "gafdrts",
        ]
        stringsC = ["cat", "dog", "doggy"]
        patternsC = ["a", "b", "b"]

        assert areFollowingPatterns(stringsA, patternsA)
        assert areFollowingPatterns(stringsB, patternsB)
        assert not areFollowingPatterns(stringsC, patternsC)
