# -*- coding: utf-8 -*-

import pytest

from pastel import Pastel
from pastel.style import Style
from pastel.stack import StyleStack


@pytest.fixture
def pastel():
    return Pastel(True)


@pytest.fixture
def non_decorated_pastel():
    return Pastel(False)


@pytest.fixture
def style():
    return Style()


@pytest.fixture
def stack():
    return StyleStack()
