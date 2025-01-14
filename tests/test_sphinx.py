# -*- coding: utf-8 -*-
import subprocess


def test_sphinx_build():
    result = subprocess.run(
        ["sphinx-build", "-b", "html", "../source", "../build"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Build failed with errors: {result.stderr}"
