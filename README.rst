======
lineno
======

.. image:: https://img.shields.io/pypi/v/lineno.svg
        :target: https://pypi.python.org/pypi/lineno

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black


Outputs the lines from specified file


Features
--------

.. code:: bash

    $ lineno -l 1-3,15,16 README.rst
    ======
    lineno
    ======
    Features
    --------

Usage in vim:

.. code:: vim

    :r! lineno -l 1-3,15,16 -l 27-31 README.rst
