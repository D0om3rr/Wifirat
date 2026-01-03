import subprocess
import re


"""DISCLAMER"""

# Comments in this proyect are made for my own understanding of the code and for prior debbuging as i used AI to help me with the code.  
# Im councious about the fact that comments should explain why not what but for the moment this helps me understand  and debug the code better! 


""" 

To call the interface from another part of the code, get_current_interface() method from NetworkInterfaceManager needs to be called, this in't as simply as it could be but its functional
and allows global acces to the variable and has a lot of error handiling functions. Also the state stays the same througth the code. As this is a ""bigger"" proyect
it might be better to do it this way (i think).

"""


def get_interfaces():

    #Returns a list of available wireless interfaces

    """ Generates a list of interfaces so that the NetworkInterfaceManager class can take this list of interfaces as an argument and operate with it. 
    It also includes error handling just in case and to appear more professional."""

    try:
        result = subprocess.run(
            ["iwconfig"],
            capture_output=True,
            text=True,
            timeout=5,
            check=True
        )   

        interfaces = []
        for line in result.stdout.split('\n'):
            if 'IEEE 802.11' in line:
                iface = line.split()[0]
                interfaces.append(iface)
        
        return interfaces
            
    except FileNotFoundError:
        print("[!] Command not found!: -> iwconfig <-\n¡ try installing: wireless-tools !")
        return []
    except subprocess.TimeoutExpired:
        print("[!] Command timed out!")
        return []
    except subprocess.CalledProcessError as e:
        print(f"[!] Command failed with return code: {e.returncode}")
        print(f"[-] Error output: {e.stderr}")
        return []

def interface_is_up(interface):
    #Checks if a specific interface is UP

    """ This function checks if the interface passed as an argument: "interface_is_up(wlan0)" is operational (up or down)"""
    try: 
        result = subprocess.run(
            ["ip", "link", "show", interface],
            capture_output=True,
            text=True,
            check=True
        )

        return 'state UP' in result.stdout

    except Exception as e:
        print(f"[!] Error checking interface status for {interface}: {e}")
        return False

class NetworkInterfaceManager:
    def __init__(self):
        #Sets initial value to None, to be modified later.
        self.selected_interface = None
        self.available_interfaces = []

    def scan_interfaces(self):
        #Scans for available interfaces using the previously created function (get_interfaces) and returns them with return.
        self.available_interfaces = get_interfaces() #Here a list of interfaces has been generated and saved as a class argument.
        return self.available_interfaces

    def select_interface(self, interface_name=None):
        #Selects an interface. If no name provided, uses first available
        
        if not self.available_interfaces:
            #If no available interfaces were found, it notifies and returns a Null value.
            print("[!] No interfaces available.")
            return None
        
        if interface_name is None:
            #selects and adds to the selected_interfaces list the first interface that available_interfaces received from the get_interfaces() function
            self.selected_interface = self.available_interfaces[0]

        elif interface_name in self.available_interfaces:
            self.selected_interface = interface_name
        else:
            print(f"[!] Interface '{interface_name}' not found in available interfaces")
            return None
        
        return self.selected_interface

    def scan_and_select(self):
        interfaces = self.scan_interfaces()
        
        if not interfaces:
            print("[!] No wireless interfaces found!")
            return None
        
        # Select the first interface
        return self.select_interface(interfaces[0])

    def check_status(self):
        #If no interface is selected, for any reason, it notifies and returns False as a boolean value
        if not self.selected_interface:
            print("[!] No interface selected!")
            return False
        
        return interface_is_up(self.selected_interface)

    @property
    def get_current_interface(self):
        #Returns the selected interface as the value
        return self.selected_interface

    def get_available_interfaces(self):
        """Returns all available interfaces"""
        return self.available_interfaces
    
    def parse_monitor_interface(self, output):
        """Parse airmon-ng output to get the monitor interface name"""
        for line in output.split('\n'):
            if 'monitor mode vif enabled for' in line:
                # Look for the pattern: on [phyX]interfaceName
                # Example: on [phy0]wlan0mon
                match = re.search(r'on \[phy\d+\](\w+)', line)
                if match:
                    return match.group(1)
        return None
    def monitor_mode(self):
        #Turns on monitor mode on the wirles interface
        
        print("[+] Turnin on monitor mode")

        try:
            print("[+] Killing interfeering proceses")
            #Killing conflictin processes
            kill_result = subprocess.run(
                    ["airmon-ng", "check", "kill"],
                    check = True,
                    text = True,
                    capture_output=True,
                )

            start_result = subprocess.run(
                ["airmon-ng", "start", self.selected_interface ],
                check=True,
                capture_output=True,
                text=True
            )

            new_interface = self.parse_monitor_interface(start_result.stdout)
            if new_interface:
                print(f"[+] Interface renamed to: {new_interface}")
                self.selected_interface = new_interface
            else:
                print(f"[+] Monitor mode enabled on {self.selected_interface}")
            
            return True
        
        except subprocess.CalledProcessError as e:
            print("[!] An error has ocurred when starting monitor mode!")
            print(f"[-] Error: {e.stderr}")
        except FileNotFoundError:
            print("[!] airmon-ng Not installed!")
            print("[-] Error: ")
    
    def cleanup(self, interface):

        #Takes the wireless interface back to normal
        subprocess.run(
            ["airmon-ng", "stop", interface]
        )
        subprocess.run(["systemctl", "restart", "NetworkManager"])
