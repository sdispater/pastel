# -*- coding: utf-8 -*-

import sys
import pastel

from contextlib import contextmanager


class PseudoTTY(object):

    def __init__(self, underlying):
        self._underlying = underlying

    def __getattr__(self, name):
        return getattr(self._underlying, name)

    def isatty(self):
        return True


@contextmanager
def mock_stdout():
    original = sys.stdout
    sys.stdout = PseudoTTY(sys.stdout)

    yield

    sys.stdout = original


def test_text():
    with mock_stdout():
        assert '\033[32msome info\033[0m' == pastel.colorize('<info>some info</info>')


def test_colorize():
    with mock_stdout():
        pastel.with_colors(False)
        assert 'some info' == pastel.colorize('<info>some info</info>')

        pastel.with_colors(True)
        assert '\033[32msome info\033[0m' == pastel.colorize('<info>some info</info>')


def test_add_remove_style():
    with mock_stdout():
        pastel.add_style('success', 'green')

        assert '\033[32msome info\033[0m' == pastel.colorize('<success>some info</success>')

        pastel.remove_style('success')

        assert '<success>some info</success>' == pastel.colorize('<success>some info</success>')


def test_pastel():
    p = pastel.pastel()
    assert isinstance(p, pastel.Pastel)
