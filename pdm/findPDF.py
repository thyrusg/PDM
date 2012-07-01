""" 
pdm.findPDF

This module finds all the pdfs inside the home directory and reorganizes them into a new one.
"""

import os
import os.path

def goHome():
	"""Changes the current working directory to the home directory."""
	os.chdir('/home/'+os.getlogin())

def findPDF():
	"""This function walks through the current directory and locates all files 
	    with the .pdf ending."""
	for r,d,f in os.walk(os.curdir):
		for file in f:
			if file.endswith(".pdf"):
				print file


def main():
	goHome()
	findPDF()

if __name__ == '__main__':
	main()