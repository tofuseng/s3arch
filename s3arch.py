#!/usr/bin/env python3
import sys
if sys.version_info < (3, 0):
	sys.stdout.write("Sorry, requires Python 3.x\n")
	sys.exit(1)

from thirdparty.beautifulsoup import *
import urllib.parse
from lib.search import *
from lib.core.Controller import Controller
from lib.core.ArgumentsParser import ArgumentsParser

class Program:
	def __init__(self):
		self.arguments = ArgumentsParser()

	def run(self):
		self.controller = Controller(self.arguments)
	

if __name__ == '__main__':
    print("s3arch v0.1")
    main = Program()
    main.run()
	
