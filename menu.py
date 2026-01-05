import subprocess


class MenuStarter():
    
    def __init__(self):
        self.selected_bssid = None

    def objective_selector(self):
        try:
            self.selected_bssid = input(
                "[+] Select BSSID to attack: "
            )
            return True
        except Exception as e:
            print(f"[-] An error occurred when selecting BSSID: \n {e}")
            return False

    def print_menu(self):
        bssid = self.selected_bssid

        while True:
            print(f"[+] BSSID to attack: {bssid}")
            print(f"\n[1] Attack 1\n[2] Attack 2\n[3] Attack 3")
            selection = input(f"\n[+] >>> ") 

            if selection == "1":
                print("[+] You selected attack 1")
                print("[!!] Enter 1 (yes) or 2 (no) if you want to proceed with the attack:")
                
                yesorno = input(f"[!!] >>>>> ")

                if yesorno == "1":
                    print(f"[+] Starting attack on: {bssid}")
                    subprocess.run(["tree"])
                elif yesorno == "2":
                    print("[+] Understood, have a nice day") 
