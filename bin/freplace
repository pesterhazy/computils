#!/usr/bin/env python

import sys

def run(old, new, inp, out):
    filedata = inp.read()
    newdata = filedata.replace(old, new)
    out.write(newdata)

def syntax():
    print '''
freplace: simply replace fixed strings in text

Usage: freplace old new [input-file] [output-file]

`freplace` writes its input to output, replacing "old" with "new". Both *old*
and *new* are fixed strings rather than regular expressions, no quoting (other
than that reuired by the shell) is needed.

`old` and `new` can include arbitrary characters, including newlines. Not that,
as `freplace` reads the entire input into memory, it may not be appropriate for
large data sets.

If `output-file` is omitted, write to `stdout`; if `input-file` is omitted, read
from `stdin`.
    '''.strip()

def main():
    nargs = len(sys.argv)
    if not (nargs >= 3 and nargs <= 5):
        syntax()
        sys.exit(1)

    inp = open(sys.argv[3], "r") if nargs >= 4 else sys.stdin
    out = open(sys.argv[4], "w") if nargs >= 5 else sys.stdout

    run(sys.argv[1], sys.argv[2], inp, out)

    if inp != sys.stdin:
        inp.close()
    if out != sys.stdout:
        out.close()

if __name__ == "__main__":
    main()
