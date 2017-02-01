# -*- coding: utf-8 -*-

import pytest

from pastel.style import Style


def test_push(stack):
    s1 = Style('white', 'black')
    s2 = Style('yellow', 'blue')
    stack.push(s1)
    stack.push(s2)

    assert s2 == stack.get_current()

    s3 = Style('green', 'red')
    stack.push(s3)

    assert s3 == stack.get_current()


def test_pop(stack):
    s1 = Style('white', 'black')
    s2 = Style('yellow', 'blue')
    stack.push(s1)
    stack.push(s2)

    assert s2 == stack.pop()
    assert s1 == stack.pop()


def test_pop_empty(stack):
    assert isinstance(stack.pop(), Style)


def test_pop_not_last(stack):
    s1 = Style('white', 'black')
    s2 = Style('yellow', 'blue')
    s3 = Style('green', 'red')
    stack.push(s1)
    stack.push(s2)
    stack.push(s3)

    assert s2 == stack.pop(s2)
    assert s1 == stack.pop()


def test_invalid_pop(stack):
    s1 = Style('white', 'black')
    s2 = Style('yellow', 'blue')
    stack.push(s1)

    with pytest.raises(ValueError):
        stack.pop(s2)
