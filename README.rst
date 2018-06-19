Linqp
======

.. image:: https://img.shields.io/pypi/v/Linqp.svg
        :alt: Release Status
        :target: https://pypi.python.org/pypi/Linqp

.. image:: https://img.shields.io/github/license/F1ashhimself/linqp.svg
        :alt: License
        :target: https://github.com/F1ashhimself/Linqp/blob/master/LICENSE


**Simple LINQ implementation for python.**

**Usage example:**

.. code:: python

 Linqp(foo).where(lambda x: x.bar == 'bar').select_all()

or

.. code:: python

 Linqp(foo).where(lambda x: x.bar == 'bar').select(lambda x: x.foobar)
