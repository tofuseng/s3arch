#!/usr/bin/env python3
import urllib.parse
import sys
try:
        from bs4 import BeautifulSoup
except:
        print ("Need BeautifulSoup4 to run")
        print ("pip3 install BeautifulSoup4")
        print ("or")
        print ("Download from http://www.crummy.com/software/BeautifulSoup/#Download && python3 setup.py install")
        sys.exit (1)
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
	
