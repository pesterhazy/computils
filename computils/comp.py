#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

ACTIONS = ["slurp"]

def split_list(lst, e, maxi):
    n = 0
    chunks = []
    cur = []
    while True:
        if not lst:
            chunks.append(cur)
            break

        if lst[0] == e and n < maxi:
            chunks.append(cur)
            n += 1
            cur = []
        else:
            cur.append(lst[0])

        lst = lst[1:]

    return chunks


def slurp(*args):
    chunks = split_list(args, "--", 1)

    if len(chunks) > 1:
        cat = Popen(["/bin/cat"] + chunks[0], stdout=PIPE)
        nextp = Popen(chunks[1], stdin=cat.stdout)
        cat.stdout.close()
        cat.wait()
        nextp.wait()
    else:
        cat = Popen(["/bin/cat"] + chunks[0])
        cat.wait()

def run(*args):
    assert len(args)>1
    action = args[0]
    assert action in ACTIONS
    globals()[action](*args[1:])

def main():
    run(*sys.argv[1:])

if __name__ == "__main__":
    main()
