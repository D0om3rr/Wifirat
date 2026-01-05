import os
import sys
from interfaces.interface_startup import interface_startup
from menu import MenuStarter

def check_root():
    return os.getuid() == 0

def main():
    print("[+] WIFIRAT")
    print("=" * 50)

    if not check_root():
        print("[!] Script must be run as root!!!")
        sys.exit(1)

    print("[+] Running script with root privileges")
    print("[+] Scanning and selecting interfaces...")
    
    interface_startup()

    menu = MenuStarter()
    menu.objetive_selector()
    menu.print_menu()

if __name__ == '__main__':
    main()
