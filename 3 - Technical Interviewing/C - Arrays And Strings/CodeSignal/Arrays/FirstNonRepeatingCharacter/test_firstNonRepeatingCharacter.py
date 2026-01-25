import pytest
from firstNonRepeatingCharacter import *


class Test:

    def testWithEmptyString(self):
        assert firstNotRepeatingCharacter("") == "_"

    def testWithSingleString(self):
        assert firstNotRepeatingCharacter("a") == "a"

    def testWithNoNonRepeating(self):
        assert firstNotRepeatingCharacter("aassddff") == "_"

    def testWithNonRepeating(self):
        assert firstNotRepeatingCharacter("aassdff") == "d"
