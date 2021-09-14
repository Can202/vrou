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
	dpm = detect_pm()
	# Detect snap
	if os.path.exists("/usr/bin/snap"):
		extra += " snap "
		print("you can use snap, or your current package manager (" + dpm +")")
		anr = input("Use snap? (Y/n)")
		if "Y" in anr or "y" in anr:
			os.system("snap install " + program)
	#Detect flatpak
	if os.path.exists("/usr/bin/flatpak"):
		extra += " flatpak "
		print("you can use flatpak (flathub), or your current package manager (" + dpm +")")
		anr = input("Use flatpak? (Y/n)")
		if "Y" in anr or "y" in anr:
			os.system("flatpak install flathub " + program)

	if dpm == "choco":
		print("choco detect")
		os.system("powershell -Command choco install " + program)
	elif dpm == "zypper":
		print("zypper detect")
		os.system("zypper in -n " + program)
	elif dpm == "apt":
		print("apt detect")
		os.system("apt install -y " + program)
	elif dpm == "dnf":
		print("dnf detect")
		os.system("dnf -y install " + program)
	elif dpm == "pacman":
		print("pacman detect")
		os.system("pacman -S " + program)

def detect_pm():
	if os.path.exists("C:\\ProgramData\\chocolatey\\bin\\choco.exe"):
		return "choco"
	if os.path.exists("/usr/bin/zypper"):
		return "zypper"
	if os.path.exists("/usr/bin/apt"):
		return "apt"
	if os.path.exists("/usr/bin/dnf"):
		return "dnf"
	if os.path.exists("/usr/bin/pacman"):
		return "pacman"


if __name__ == "__main__":
	main()
