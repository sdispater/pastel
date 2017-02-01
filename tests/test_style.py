# -*- coding: utf-8 -*-

import pytest

from pastel.style import Style


def test_init():
    style = Style('green', 'black', ['bold', 'underscore'])
    assert '\033[32;40;1;4mfoo\033[0m' == style.apply('foo')
    assert 'green' == style.foreground
    assert 'black' == style.background
    assert ['bold', 'underscore'] == style.options

    style = Style('red', None, ['blink'])
    assert '\033[31;5mfoo\033[0m' == style.apply('foo')

    style = Style(None, 'white')
    assert '\033[47mfoo\033[0m' == style.apply('foo')

    style = Style('red', None, 'blink')
    assert '\033[31;5mfoo\033[0m' == style.apply('foo')


def test_foreground(style):
    style.set_foreground('black')
    assert '\033[30mfoo\033[0m' == style.apply('foo')

    style.set_foreground('blue')
    assert '\033[34mfoo\033[0m' == style.apply('foo')

    with pytest.raises(ValueError):
        style.set_foreground('undefined-color')


def test_background(style):
    style.set_background('black')
    assert '\033[40mfoo\033[0m' == style.apply('foo')

    style.set_background('yellow')
    assert '\033[43mfoo\033[0m' == style.apply('foo')

    with pytest.raises(ValueError):
        style.set_background('undefined-color')


def test_options(style):
    style.set_options(['reverse', 'conceal'])
    assert '\033[7;8mfoo\033[0m' == style.apply('foo')

    style.set_option('bold')
    assert '\033[7;8;1mfoo\033[0m' == style.apply('foo')

    style.unset_option('reverse')
    assert '\033[8;1mfoo\033[0m' == style.apply('foo')

    style.set_option('bold')
    assert '\033[8;1mfoo\033[0m' == style.apply('foo')

    style.set_options(['bold'])
    assert '\033[1mfoo\033[0m' == style.apply('foo')

    with pytest.raises(ValueError) as e:
        style.set_option('foo')

    assert 'Invalid option specified: "foo"' in str(e.value)

    with pytest.raises(ValueError) as e:
        style.unset_option('foo')

    assert 'Invalid option specified: "foo"' in str(e.value)
