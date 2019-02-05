import json

def try_print():

    aa = json.loads('{"text":"first word", "text":"second"}')
    # error 1, json should use ", not '
    # error 2, it's a dict, so text is overriden
    # error 3, don't use test in file name. it only run tests.
    print aa

try_print()

