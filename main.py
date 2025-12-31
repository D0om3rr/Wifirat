import os
import sys
import subprocess
import signal
from core.interface_manager import NetworkInterfaceManager
def check_root():
    return os.getuid() == 0

def bring_interface_up(interface):
    #Bring a network interface up
    try:
        print(f"[+] Bringing interface {interface} up...")
        result = subprocess.run(
            ["ip", "link", "set", interface, "up"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"[+] Interface {interface} brought up successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to bring interface up: {e.stderr}")
        return False
    except Exception as e:
        print(f"[!] Error: {e}")
        return False

def main():
    print("[+] WIFIRAT")
    print("=" * 50)

    if not check_root():
        print("[!] Script must be run as root!!!")
        sys.exit(1)

    print("[+] Running script with root privileges")
    print("[+] Scanning and selecting interfaces...")
    
    manager = NetworkInterfaceManager()
    
    # Scan and select interface
    selected_interface = manager.scan_and_select()
    
    if not selected_interface:
        print("[!] No interface was selected")
        sys.exit(1)
    
    print(f"[+] Selected interface: {selected_interface}")
    
    # Check if the interface is UP
    if not manager.check_status():
        print(f"[!] Interface {selected_interface} is DOWN, bringing it up...")
        # Now selected_interface should be a string, not a list
        success = bring_interface_up(selected_interface)
        if not success:
            print("[!] Failed to bring interface up")
            sys.exit(1)
    else:
        print(f"[+] Interface {selected_interface} is UP")
    
    print("=" * 50)
    
    success = manager.monitor_mode()
    
    if success:
        print("Monitor mode enabled successfully!")
    else:
        print("Failed to enable monitor mode")


    def signal_handler(sig,frame):
        print("\n [!] Ctrl + C Detected! Restoring values...")

        manager.cleanup()
        print("[+] Cleanup compleated, restoring")
    signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    main()
