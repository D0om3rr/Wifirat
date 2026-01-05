import subprocess
import signal
import sys
from interfaces import interface_manager
from interfaces.interface_manager import NetworkInterfaceManager


def interface_startup():
    
    def bring_interface_up(interface):
        # Bring network interface up
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
    
    manager = NetworkInterfaceManager()
    
    def signal_handler(sig, frame):
        print("\n[!] Ctrl + C Detected! Restoring values...")
        current_interface = manager.get_current_interface
        if current_interface:
            manager.cleanup(current_interface)
        print("[+] Cleanup completed, exiting...")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    selected_interface = manager.scan_and_select()
    
    if not selected_interface:
        print("[!] No interface was selected")
        sys.exit(1)
    
    print(f"[+] Selected interface: {selected_interface}")
    
    # Check if the interface is UP
    if not manager.check_status():
        print(f"[!] Interface {selected_interface} is DOWN, bringing it up...")
        # Selected_interface should be a string, not a list
        success = bring_interface_up(selected_interface)
        if not success:
            print("[!] Failed to bring interface up")
            sys.exit(1)
    else:
        print(f"[+] Interface {selected_interface} is UP")
    
    print("=" * 50)
    
    success = manager.monitor_mode()
    
    if success:
        print("[+] Monitor mode enabled successfully!")
    else:
        print("[-] Failed to enable monitor mode")
        sys.exit(1)

    # Get the current interface using the property
    current_interface = manager.get_current_interface
    
    if not current_interface:
        print("[-] ERROR: current_interface is None!")
        print(f"    Selected interface: {manager.selected_interface}")
        sys.exit(1)
