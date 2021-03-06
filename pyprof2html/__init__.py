"""pyprof2html - Profile data convert to HTML.

This module is converted to HTML file from Python's cProfile and
hotshot profiling data.
"""
from pyprof2html.core import Converter
from pyprof2html.commands import pyprof2html_main
from pyprof2html._version import __version__

__licence__ = 'New BSD License'
__author__ = 'Hideo Hattori <hhatto.jp@gmail.com>'

__all__ = ['Converter', 'pyprof2html_main', '__version__']
