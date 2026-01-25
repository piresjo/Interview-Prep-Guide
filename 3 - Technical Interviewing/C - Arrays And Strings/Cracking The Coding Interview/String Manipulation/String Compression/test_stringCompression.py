import pytest
from stringCompression import *


class Test:

    def testWithNone(self):
        assert compress(None) == None

    def testWithEmptyString(self):
        assert compress("") == ""

    def testWithSingletonString(self):
        assert compress("a") == "a"

    def testWithUncompressableString(self):
        assert compress("asdfghjkl") == "asdfghjkl"

    def testCompress(self):
        assert compress("aaasssddddff") == "a3s3d4f2"
