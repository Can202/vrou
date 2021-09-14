import sys
import os
from sys import exit
import subprocess

INSTALL="install"
INSTALL2="in"
INSTALL3="-S"

REMOVE="remove"
REMOVE2="rm"
REMOVE3="-R"

SEARCH="search"
SEARCH2="se"
SEARCH3="-Ss"
PROGRAM=""
def main():
	for i in range(len(sys.argv)):
		valueos = other_simple(sys.argv[i])
		if valueos == "yes":
			print("yes")
		if sys.argv[i] == INSTALL or sys.argv[i] == INSTALL2 or sys.argv[i] == INSTALL3:
			if detect_root() == False:
				print("need root")
				exit()
			print("install")
			if len(sys.argv) <= i+1:
				print("program")
			else:
				installpak = 1+i
				while installpak < len(sys.argv):
					if "--" not in sys.argv[installpak]:
						install(str(sys.argv[installpak]))
					installpak +=1

		if sys.argv[i] == REMOVE or sys.argv[i] == REMOVE2 or sys.argv[i] == REMOVE3:
			if detect_root() == False:
				print("need root")
				exit()
			print("remove")
			if len(sys.argv) <= i+1:
				print("program")
			else:
				pak = 1+i
				while pak < len(sys.argv):
					if "--" not in sys.argv[pak]:
						remove(str(sys.argv[pak]))
					pak +=1

		if sys.argv[i] == SEARCH or sys.argv[i] == SEARCH2 or sys.argv[i] == SEARCH3:
			print("remove")
			if len(sys.argv) <= i+1:
				print("program")
			else:
				pak = 1+i
				while pak < len(sys.argv):
					if "--" not in sys.argv[pak]:
						search(str(sys.argv[pak]))
					pak +=1

def install(program = "none"):
	if program == "none":
		return 1
	dpm = detect_pm()
	# Detect snap
	if os.path.exists("/usr/bin/snap"):
		print("you can use snap, or your current package manager (" + dpm +")")
		anr = input("Use snap? (Y/n)")
		if "Y" in anr or "y" in anr:
			os.system("snap install " + program)
	#Detect flatpak
	if os.path.exists("/usr/bin/flatpak"):
		print("you can use flatpak (flathub), or your current package manager (" + dpm +")")
		anr = input("Use flatpak? (Y/n)")
		if "Y" in anr or "y" in anr:
			os.system("flatpak install flathub " + program)

	if dpm == "choco":
		print("choco detect")
		os.system("powershell -Command choco install " + program + " & pause")
	elif dpm == "zypper":
		print("zypper detect")
		os.system("zypper in " + program)
	elif dpm == "apt":
		print("apt detect")
		os.system("apt install " + program)
	elif dpm == "dnf":
		print("dnf detect")
		os.system("dnf install " + program)
	elif dpm == "pacman":
		print("pacman detect")
		os.system("pacman -S " + program)
	return 0

def remove(program = "none"):
	if program == "none":
		return 1
	dpm = detect_pm()
	# Detect snap
	if os.path.exists("/usr/bin/snap"):
		print("you can use snap, or your current package manager (" + dpm +")")
		anr = input("Use snap? (Y/n)")
		if "Y" in anr or "y" in anr:
			os.system("snap remove " + program)
	#Detect flatpak
	if os.path.exists("/usr/bin/flatpak"):
		print("you can use flatpak, or your current package manager (" + dpm +")")
		anr = input("Use flatpak? (Y/n)")
		if "Y" in anr or "y" in anr:
			os.system("flatpak uninstall " + program)

	if dpm == "choco":
		print("choco detect")
		os.system("powershell -Command choco uninstall " + program + " & pause")
	elif dpm == "zypper":
		print("zypper detect")
		os.system("zypper rm " + program)
	elif dpm == "apt":
		print("apt detect")
		os.system("apt remove " + program)
	elif dpm == "dnf":
		print("dnf detect")
		os.system("dnf remove " + program)
	elif dpm == "pacman":
		print("pacman detect")
		os.system("pacman -R " + program)
	return 0

def search(program = "none"):
	if program == "none":
		return 1
	dpm = detect_pm()
	# Detect snap
	if os.path.exists("/usr/bin/snap"):
		print("you can use snap, or your current package manager (" + dpm +")")
		anr = input("Use snap? (Y/n)")
		if "Y" in anr or "y" in anr:
			os.system("snap search " + program)
	#Detect flatpak
	if os.path.exists("/usr/bin/flatpak"):
		print("you can use flatpak, or your current package manager (" + dpm +")")
		anr = input("Use flatpak? (Y/n)")
		if "Y" in anr or "y" in anr:
			os.system("flatpak uninstall " + program)

	if dpm == "choco":
		print("choco detect")
		os.system("powershell -Command choco search " + program + " & pause")
	elif dpm == "zypper":
		print("zypper detect")
		os.system("zypper search " + program)
	elif dpm == "apt":
		print("apt detect")
		os.system("apt search " + program)
	elif dpm == "dnf":
		print("dnf detect")
		os.system("dnf search " + program)
	elif dpm == "pacman":
		print("pacman detect")
		os.system("pacman -Ss " + program)
	return 0

def other_simple(command):
	if command == "-h" or command == "--help":
		print("xD")
		return "none"
		exit()
	elif command == "-v" or command == "--version":
		print("v0.1-dev.1")
		return "none"
		exit()
	elif command == "-y":
		return "yes"
def detect_root():
	if os.name == "posix":
		if "root" not in str(subprocess.check_output(["whoami"])):
			return False
		else:
			return True
	else:
		return True


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
