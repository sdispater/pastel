Pastel: Bring colors to your terminal
#####################################

Pastel is a simple library to help you colorize strings in your terminal.

It comes bundled with predefined styles:

* ``info``: green
* ``comment``: yellow
* ``question``: black on cyan
* ``error``: white on red

.. image:: https://raw.githubusercontent.com/sdispater/pastel/master/assets/screenshot.png


Features
========

* Use predefined styles or add you own.
* Disable colors all together by calling ``with_colors(False)``.
* Automatically disables colors if the output is not a TTY.
* Used in `cleo <https://github.com/sdispater/cleo>`_.
* Supports Python **2.7+**, **3.5+** and **PyPy**.


Usage
=====

.. code-block:: python

    >>> import pastel
    >>> print(pastel.colorize('<info>Information</info>'))
    'Information'  # Green string by default
    >>> print(pastel.colorize('<fg=red;options=bold>This is bold red</>'))
    'This is bold red'


Installation
============

.. code-block::

    pip install pastel
