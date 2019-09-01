import sys


def fibonnacciRecursivo(n):
	if(n==1):
		return 0
	if(n==2):
		return 1
	return fibonnacciRecursivo(n-1)+fibonnacciRecursivo(n-2)