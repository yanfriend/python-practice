from contextlib import contextmanager
import os
import glob

@contextmanager
def working_directory(path):
    current_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_dir)


with working_directory("/tmp"):
    print glob.glob("*")
    # do something within data/stuff
    
# here I am back again in the original working directory
