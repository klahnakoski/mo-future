# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from __future__ import unicode_literals
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 5 - Production/Stable","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)","Programming Language :: Python :: 3.7","Programming Language :: Python :: 3.8","Programming Language :: Python :: 3.9"],
    description='More future! Make Python 2/3 compatibility a bit easier',
    license='MPL 2.0',
    long_description='# More Future!\n\nFor old code written against Python2, plus some tiny useful functions\n\n## Recent Changes\n\n**December 2022** - No longer points to Python2 modules. \n\n\n## Description\n\n### Problem \n\n`future` or `six` are hard to use: It is easy to google how to import an object in Python2, or Python3, but finding the full path to the same in these compatibility libraries is difficult. \n\n## Solution\n\nAll the modules and types required for compatibility are put into the `mo-future` top-level module so they are  easy to find.\n\n\n### Flat namespace\n\nInstead of \n\n```python\n    from future.utils import text\n```\n\nyou get the same, but without having to discover what sub-module the `text` is hiding:  \n\n```python\n    from mo_future import text\n```\n\n\n### Simpler imports\n\nInstead of writing conditional imports like \n\n```python\n    try:\n        from io import StringIO\n    except:\n        from StringIO import StringIO\n```\n\nor \n\n```python\n    if PY3:\n        from io import StringIO\n    else:\n        from StringIO import StringIO\n```\n\nyou can use `mo-future`:\n\n```python\n    from mo_future import StringIO\n```\n\n\n',
    long_description_content_type='text/markdown',
    name='mo-future',
    packages=["mo_future"],
    url='https://github.com/klahnakoski/mo-future',
    version='7.298.22349'
)