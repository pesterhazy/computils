# -*- coding: utf-8 -*-

from .context import comp

sample = "foo\n"

def test_slurp(tmpdir, capfd):
    f = tmpdir.join("input")
    f.write(sample)
    comp.run("slurp", str(f), "--", "cat")

    assert sample == capfd.readouterr()[0]

def test_slurp2(tmpdir, capfd):
    f = tmpdir.join("input")
    f.write(sample)
    comp.run("slurp", str(f))

    assert sample == capfd.readouterr()[0]

def test_split_list():
    ex = ["a", "b", "a", "b", "a"]

    assert [ex] == comp.split_list(ex, "b", 0)
    assert [["a"], ["a","b","a"]] == comp.split_list(ex, "b", 1)
    assert [["a"], ["a"],["a"]] == comp.split_list(ex, "b", 2)


    assert [[]] == comp.split_list([], "b", 2)
    assert [[],[]] == comp.split_list(["b"], "b", 2)
    assert [[],["a"]] == comp.split_list(["b","a"], "b", 2)
