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

	extra=""
	# Detect snap
	if os.path.exists("/usr/bin/snap"):
		extra += " snap "
	#Detect flatpak
	if os.path.exists("/usr/bin/flatpak"):
		extra += " flatpak "


	#Detect Choco
	if os.path.exists("C:\\ProgramData\\chocolatey\\bin\\choco.exe"):
		print("choco detect")
		cpm = "choco"
		os.system("powershell -Command choco install " + program)

	#Detect zypper
	if os.path.exists("/usr/bin/zypper"):
		os.system("zypper in -n " + program)
		cpm = "zypper"

	#Detect apt
	if os.path.exists("/usr/bin/apt"):
		os.system("apt install -y " + program)
		cpm = "apt"

	# Detect dnf
	if os.path.exists("/usr/bin/dnf"):
		os.system("dnf -y install " + program)
		cpm = "dnf"

	#Detect pacman
	if os.path.exists("/usr/bin/pacman"):
		os.system("pacman -S " + program)
		cpm = "pacman"

	if extra != "":
		if "snap" in extra:
			print("you can use snap, or your current package manager (" + cpm + ")")
			anr = input("Use snap? (Y/n)")
			if "Y" in anr or "y" in anr:
				os.system("snap install " + program)
		if "flatpak" in extra:
			print("you can use flatpak, or your current package manager (" + cpm + ")")
			anr = input("Use snap? (Y/n)")
			if "Y" in anr or "y" in anr:
				os.system("flatpak install flathub " + program)
if __name__ == "__main__":
	main()
