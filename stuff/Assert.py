# =====================================================================================================================
# sys
import sys

from inspect import getframeinfo, stack
# =====================================================================================================================
# PyQuantum.Tools
from PyQuantum.Tools.Print import cprint
# =====================================================================================================================


# =====================================================================================================================
def excepthook(type, value, traceback):
    print(value)
# =====================================================================================================================


# =====================================================================================================================
def FILE():
    cf = sys._getframe(len(stack())-1)

    return getframeinfo(cf).filename


def LINE():
    cf = sys._getframe(len(stack())-1)

    return cf.f_lineno
# =====================================================================================================================


# =====================================================================================================================
def Assert(condition, err_msg, file, line):
    # sys.excepthook = excepthook

    if not condition:
        # if 'ipykernel' not in sys.modules:
            # cprint('File: ', 'yellow', attrs=['bold'], end='')
            # print(file)

            # cprint('Line: ', 'yellow', attrs=['bold'], end='')
            # print(line)

            # print()

            # cprint('Error: ', 'red', attrs=['bold'], end='')

        raise AssertionError(err_msg)
# =====================================================================================================================


# =====================================================================================================================
# Example: Assert(1 == 2, '1 != 2', FILE(), LINE())
# =====================================================================================================================
# STUFF
#
# sys.tracebacklimit = 0
#
# ipython = get_ipython()
# ipython._showtraceback = excepthook
#
# cf = sys._getframe(0)
# cf = sys._getframe(len(stack())-2)
#
# print(getframeinfo(cf).filename, cf.f_lineno)
# =====================================================================================================================