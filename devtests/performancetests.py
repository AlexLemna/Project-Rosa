import timeit

from testmiscstuff import Suppressor
# Import Rosevomit for testing
from context import rosevomit
from rosevomit import programlogic


def timetest_name_generation(ARG_number_of_names: int = 10, ARG_globals=globals()):
    _resultsdict = {}
    _results: list = timeit.repeat (stmt=f"programlogic.logiccontroller.gen ('first', {ARG_number_of_names})", number=1, globals=ARG_globals)
    _resultsdict['first'] = _results

    _results: list = timeit.repeat (stmt=f"programlogic.logiccontroller.gen ('firstfemale', {ARG_number_of_names})", number=1, globals=ARG_globals)
    _resultsdict['firstfemale'] = _results

    _results: list = timeit.repeat (stmt=f"programlogic.logiccontroller.gen ('firstmale', {ARG_number_of_names})", number=1, globals=ARG_globals)
    _resultsdict['firstmale'] = _results

    _results: list = timeit.repeat (stmt=f"programlogic.logiccontroller.gen ('last', {ARG_number_of_names})", number=1, globals=ARG_globals)
    _resultsdict['last'] = _results

    _results: list = timeit.repeat (stmt=f"programlogic.logiccontroller.gen ('fullfemale', {ARG_number_of_names})", number=1, globals=ARG_globals)
    _resultsdict['fullfemale'] = _results

    _results: list = timeit.repeat (stmt=f"programlogic.logiccontroller.gen ('fullmale', {ARG_number_of_names})", number=1, globals=ARG_globals)
    _resultsdict['fullmale'] = _results

    return (_resultsdict)

if __name__ == "__main__":
    with Suppressor():
        results = timetest_name_generation()
    print (results)