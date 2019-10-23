from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from package2.subpackageA import moduleB as mB


def methodA():
    print("B.A.methodA")


def methodB():
    mB.methodA()
    print("B.A.methodB")
