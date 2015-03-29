
import os
TESTER = os.environ.get("TESTER", "demo")


import importlib
tester_module = importlib.import_module("ag101.learners."+TESTER)


def test_hello():
    assert tester_module.hello() == "hello, ag101!"
    