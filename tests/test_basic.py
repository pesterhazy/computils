# -*- coding: utf-8 -*-

import pytest
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

def test_spit(tmpdir):
    f = tmpdir.join("output")
    comp.run("spit", str(f), "--", "echo", "foo")

    assert sample == f.read()

def test_spit_without_nextp(tmpdir, capfd):
    f = tmpdir.join("output")

    with pytest.raises(ValueError):
        comp.run("spit", str(f))

def test_apply(capfd):
    comp.run("apply", "sed", "s/due/two/","--","echo","one due three","--","cat")

    assert "one two three" == capfd.readouterr()[0].strip()

def test_split_list():
    ex = ["a", "b", "a", "b", "a"]

    assert [ex] == comp.split_list(ex, "b", 0)
    assert [["a"], ["a","b","a"]] == comp.split_list(ex, "b", 1)
    assert [["a"], ["a"],["a"]] == comp.split_list(ex, "b", 2)


    assert [[]] == comp.split_list([], "b", 2)
    assert [[],[]] == comp.split_list(["b"], "b", 2)
    assert [[],["a"]] == comp.split_list(["b","a"], "b", 2)
