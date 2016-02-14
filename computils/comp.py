#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

ACTIONS = ["slurp"]

def slurp(*args):
    try:
        idx = args.index("--")
        before = args[:idx]
        after = args[(idx+1):]
    except ValueError:
        before = args
        after = ()

    assert len(after) > 0, "Need nextp"

    cat = Popen(["/bin/cat"] + list(before), stdout=PIPE)
    nextp = Popen(after, stdin=cat.stdout)
    cat.stdout.close()
    cat.wait()
    nextp.wait()

def run(*args):
    assert len(args)>1
    action = args[0]
    assert action in ACTIONS
    globals()[action](*args[1:])

def main():
    run(*sys.argv[1:])

if __name__ == "__main__":
    main()