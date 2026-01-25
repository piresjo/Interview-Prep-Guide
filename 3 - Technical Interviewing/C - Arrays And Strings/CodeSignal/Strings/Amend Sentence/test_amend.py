import pytest
from amend import *


class Test:
    def testGeneral(self):
        assert amendTheSentence(None) == ""
        assert amendTheSentence("") == ""
        assert amendTheSentence("CodesignalIsAwesome") == "codesignal is awesome"
        assert (
            amendTheSentence("tfRZGdYurvrVyEuHbOJcaXnZrsEUr")
            == "tf r z gd yurvr vy eu hb o jca xn zrs e ur"
        )
        assert amendTheSentence("Hello") == "hello"
