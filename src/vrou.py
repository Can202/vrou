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
				installpak = 1+i
				while installpak < len(sys.argv):
					if "--" not in sys.argv[installpak]:
						install(str(sys.argv[installpak]))
					installpak +=1

def install(program = "none"):
	print("installing " + program)
if __name__ == "__main__":
	main()
