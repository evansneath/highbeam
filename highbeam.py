#!/usr/bin/env python

"""Highbeam

Simple, lightweight Python method debugging.

Author: Evan Sneath <evansneath@gmail.com>
"""

import logging


__all__ = ['highbeam']


# Create the logger for this module
hb_logger = logging.getLogger('highbeam')


def highbeam(func):
	'''Highbeam decorator

	The highbeam decorator call.

	@param func: The decorated function.
	@returns: The highbeam function wrapper.
	'''
	def func_wrapper(*args, **kwargs):
		'''Highbeam function wrapper

		The function wrapper that does it all. Highbeam gathers as much
		information about the wrapped function that you would ever want.
		It then displays that information alongside function execution.

		@param *args: The list of arguments
		'''
		hb_logger.debug(' %s(...)', func.__name__)

		# Show argument information
		for i, val in enumerate(args):
			name = '_'
			hb_logger.debug(' > arg %d   : %s=%s', i, name, val)

		# Show keyword argument information
		for name, val in kwargs.iteritems():
			hb_logger.debug(' > kwarg   : %s=%s', name, val)

		# Cache global variables prior to call
		# TODO: Do this...

		ret_val = func(*args, **kwargs)

		# Show modified global variables post-call
		# TODO: Do this...

		# Show return value information
		hb_logger.debug(' > returns : %s', ret_val)

		# Drop out of here like nothing ever happened
		return ret_val

	return func_wrapper


if __name__ == '__main__':
	pass
