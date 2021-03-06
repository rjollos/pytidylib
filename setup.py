# Copyright 2009-2015 Jason Stitt
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from setuptools import setup

longdesc = """\
`PyTidyLib`_ is a Python package that wraps the `HTML Tidy`_ library. This
allows you, from Python code, to "fix" invalid (X)HTML markup. Some of the
library's many capabilities include:

* Clean up unclosed tags and unescaped characters such as ampersands
* Output HTML 4 or XHTML, strict or transitional, and add missing doctypes
* Convert named entities to numeric entities, which can then be used in XML
  documents without an HTML doctype.
* Clean up HTML from programs such as Word (to an extent)
* Indent the output, including proper (i.e. no) indenting for ``pre`` elements,
  which some (X)HTML indenting code overlooks.

Changes
=======

* 0.4.0: Updated to setuptools. Updated tox testing to 3.6 (from 3.5) and 2.7.
  Added a property to get the library path.

* 0.3.2: Initialization bug fix

* 0.3.1: find_library support while still allowing a list of library names

* 0.3.0: Refactored to use Tidy and PersistentTidy classes while keeping the
  functional interface (which will lazily create a global Tidy() object) for
  backward compatibility. You can now pass a list of library names and base
  options when instantiating Tidy. The keep_doc argument is now deprecated
  and does nothing; use PersistentTidy.

* 0.2.4: Bugfix for a strange memory allocation corner case in Tidy.

* 0.2.3: Python 3 support (2 + 3 cross compatible) with passing Tox tests.

Small example of use
====================

The following code cleans up an invalid HTML document and sets an option::

    from tidylib import tidy_document
    document, errors = tidy_document('''<p>f&otilde;o <img src="bar.jpg">''',
      options={'numeric-entities':1})
    print document
    print errors

Docs
====

Documentation is shipped with the source distribution and is available at
the `PyTidyLib`_ web page.

.. _`HTML Tidy`: http://www.html-tidy.org/
.. _`PyTidyLib`: http://countergram.github.io/pytidylib/
"""

VERSION = "0.4.0"

setup(
    name="pytidylib",
    version=VERSION,
    description="Python wrapper for HTML Tidy (tidylib) on Python 2 and 3",
    long_description=longdesc,
    author="Jason Stitt",
    author_email="js@jasonstitt.com",
    url="http://countergram.github.io/pytidylib/",
    packages=['tidylib'],
    keywords="html tidy tidylib",
    license="MIT",
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: XML',
    ],
)
