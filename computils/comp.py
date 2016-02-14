#!/usr/bin/env python

from __future__ import print_function
import sys
import subprocess
from subprocess import Popen, PIPE

ACTIONS = ["slurp", "spit", "apply"]

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

def chain(xs):
    n = len(xs)
    ps = []
    prev = None

    for i, x in enumerate(xs):
        d = {}

        if i != (n - 1):
            d["stdout"] = subprocess.PIPE
        if i != 0:
            d["stdin"] = prev.stdout

        prev = subprocess.Popen(x, **d)
        ps.append(prev)

    for p in ps:
        p.wait()

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

def spit(*args):
    chunks = split_list(args, "--", 1)

    assert 1==len(chunks[0]), "Only one output file expected"

    outfn = chunks[0][0]

    if len(chunks) <= 1:
        raise ValueError("Expecting nextp")

    with open(outfn, "w") as outf:
        nextp = Popen(chunks[1], stdout=outf)
        nextp.wait()

def apply(*args):
    chunks = split_list(args, "--", 2)

    if len(chunks) == 3:
        chain([chunks[1],chunks[0],chunks[2]])
    else:
        assert False, "Unexpected number of argument chunks"

def run(*args):
    assert len(args)>1
    action = args[0]
    assert action in ACTIONS
    globals()[action](*args[1:])

def main():
    run(*sys.argv[1:])

if __name__ == "__main__":
    main()
