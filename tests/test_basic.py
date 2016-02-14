# -*- coding: utf-8 -*-

from .context import comp

sample = "foo\n"

def test_comp(tmpdir, capfd):
    f = tmpdir.join("input")
    f.write(sample)
    comp.run("slurp", str(f), "--", "cat")

    assert sample == capfd.readouterr()[0]
