======
lineno
======

.. image:: https://img.shields.io/pypi/v/lineno.svg
        :target: https://pypi.python.org/pypi/lineno

.. image:: https://img.shields.io/travis/bulv1ne/lineno.svg
        :target: https://travis-ci.org/bulv1ne/lineno


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
