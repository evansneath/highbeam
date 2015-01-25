#!/usr/bin/env python

"""Highbeam Test

Tests the highbeam module.

Author: Evan Sneath <evansneath@gmail.com>
"""

from highbeam import highbeam
import logging


def test():
	arg1 = 1
	arg2 = 2
	kwarg1 = 'hi'

	success = beamed_func(arg1, arg2, kwarg1)

	arg1 = 2
	arg2 = 2
	kwarg1 = 'bye'

	success = beamed_func(arg1, arg2, beamed_kwarg=kwarg1)


@highbeam
def beamed_func(arg1, arg2, beamed_kwarg=None):
	return arg1 == arg2


class TestClass:
	def __init__(self):
		self.my_class_attr = True

	@highbeam
	def beamed_method(self):
		self.my_class_attr = False

		return not self.my_class_attr


def setup_logger():
	logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
	setup_logger()
	test()
