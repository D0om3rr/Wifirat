import os
import sys
from interfaces.interface_startup import interface_startup

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

if __name__ == '__main__':
    main()
