import sys
import os
from sys import exit
import subprocess

INSTALL="install"
INSTALL2="in"
INSTALL3="-S"
PROGRAM=""
def main():
	
	if os.name == "posix":
		if "root" not in str(subprocess.check_output(["whoami"])):
			print("you need root")
			exit()
		
	
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
	if os.path.exists("/usr/bin/zypper"):
		os.system("zypper in " + program)
	if os.path.exists("/usr/bin/apt"):
		os.system("apt install -y " + program)
	if os.path.exists("/usr/bin/dnf"):
		os.system("dnf -y install " + program)
	if os.path.exists("/usr/bin/pacman"):
		os.system("pacman -S " + program)
if __name__ == "__main__":
	main()
