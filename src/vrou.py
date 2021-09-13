import sys
import os
from sys import exit

INSTALL="install"
INSTALL2="in"
INSTALL3="-S"
PROGRAM=""
def main():
	print("Welcome to vrou")
	for i in range(len(sys.argv)):
		if sys.argv[i] == INSTALL or sys.argv[i] == INSTALL2 or sys.argv[i] == INSTALL3:
			print("install")
			if len(sys.argv) <= i+1:
				print("program")
			else:
				PROGRAM = str(sys.argv[i+1])

if __name__ == "__main__":
	main()
