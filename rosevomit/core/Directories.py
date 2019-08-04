import glob
import os
import pathlib


def get_cwd_name_only():
    """Returns only the folder name of the current working directory, not the full path."""
    _cwd = pathlib.Path.cwd()
    _path_split = os.path.split(_cwd)
    return _path_split[-1]


def get_data_dir():
    """Returns the path of the 'programdata' directory. This function should work anywhere within the 'rosevomit' module or the associated repository."""
    # Let's assume we don't know where this function is being called from or to, and we don't know what the exact directory structure is that we're navigating through. Generally, all we know is that (1) our program Rosevomit is contained in a directory named 'rosevomit', and (2) the 'rosevomit' directory plus whatever directories we've created for documentation/testing/general development purposes should be contained in a directory called 'rosevomitrepo'.
    # Specific to this function, we also know that (3) we're looking looking for Rosevomit's data directory, which should be named 'programdata' and should be contained somewhere within the 'rosevomit' directory.
    #
    # We begin by finding our where we are.
    _cwd = pathlib.Path.cwd()
    # We need a known starting place to begin navigating. This can be either our 'rosevomit' directory or our 'rosevomitrepo' directory.
    _path_parts = pathlib.PurePath (_cwd).parts
    if "rosevomit" in _path_parts:
        _path_partslist = list(_path_parts)
        while _path_partslist[-1] != "rosevomit":
            _path_partslist.pop()
        _path = os.path.join (*_path_partslist)  # The '*' is a "splat" operator
        ROSEVOMIT_DIR = pathlib.PurePath (_path)
        os.chdir ("..")
        REPO_DIR = pathlib.PurePath (pathlib.Path.cwd())
    # If the 'rosevomit' directory isn't in _path_parts, then that's a problem. We'll attempt to work around it by looking for the 'rosevomitrepo' directory. At the end of the day, we need *some* sort of place to begin navigating around the filesystem.
    elif "rosevomitrepo" in _path_parts:
        _path_partslist = list(_path_parts)
        while _path_partslist[-1] != "rosevomitrepo":
            _path_partslist.pop()
        _path = os.path.join (*_path_partslist)  # The '*' is a "splat" operator
        REPO_DIR = pathlib.PurePath (_path)
    else:
        # If neither 'rosevomit' nor 'rosevomitrepo' show up in our path, we're well and truly lost. Let's raise an exception (a Python error).
        raise FileNotFoundError

    # TODO: Honestly, we should split the part of the function above this comment into it's own function. Otherwise, we're exceeding a single responsibility for this function.

    # Now that we've established which parts of the expected Rosevomit filesystem we can find, we navigate to the best available location to look for the 'programdata' subdirectory.
    # TODO: There's a *lot* of advice online about how checking for variable existence in Python is not a good way to handle flow control... so this next part probably needs refactoring.
    if "ROSEVOMIT_DIR" in locals():  # exists
        os.chdir (ROSEVOMIT_DIR)
        os.chdir ("programdata")
    elif "REPO_DIR" in locals():  # exists
        os.chdir (REPO_DIR)
        possible_paths = glob.glob ("*/programdata", recursive=True)
        if len(possible_paths) is 1:
            os.chdir (possible_paths[0])
        elif len (possible_paths) is 0:
            raise FileNotFoundError
        else:
            # If multiple paths are returned, something has gone wrong and we need to stop.
            # TODO: Check if this is the proper exception to raise.
            raise KeyError
    else:
        # this should definitely 100% never happen
        # TODO: Possible 'RealityError' candidate?
        raise FileNotFoundError
    _datapath = pathlib.Path.cwd()
    return _datapath

if __name__ == "__main__":
    get_data_dir()