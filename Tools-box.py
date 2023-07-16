#Tools-box
#Created by xTyzenツ.py / Thitou kas ツ 

os.system("clear")

print(""" _____           _            _               
|_   _|         | |          | |              
  | | ___   ___ | |___ ______| |__   _____  __
  | |/ _ \ / _ \| / __|______| '_ \ / _ \ \/ /
  | | (_) | (_) | \__ \      | |_) | (_) >  < 
  \_/\___/ \___/|_|___/      |_.__/ \___/_/\_\ by xTyzenツ.py
                                                  
                                                  
  [1]: install Repo Kali Linux    [5]: JohnTheRipper    [9]: SkipFish and WPScan
                                                        
  [2]: Metasploit                 [6]: BurpSuite        [10]: Hydra

  [3]: Nmap                       [7]: Aircrack-ng      [11]: Maltego

  [4]: Wireshark                  [8]: Nikto            [12]: Ettercap                

                                                  
                                                  """)

#Add
import os
import sys                                                                                                                                                                                                       #Created by xTyzenツ.py / Thitou kas ツ 
                                                                                                                                                                                                                                              

def main():
    # Vérifier si l'utilisateur est root
    if os.geteuid() != 0:
        print("Veuillez exécuter le script en tant que root.")
        return

#Code
def main():
    choix_valide = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12]
    User_choice = 0

    try:
        while User_choice not in choix_valide:
            User_choice = int(input("Quel outil veux-tu installer ? : "))

        if User_choice == 1:
            os.system("grep -v '#' /etc/apt/sources.list | sort -u deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware")
            os.system('echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list')
            os.system('echo "deb http://http.kali.org/kali kali-last-snapshot main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list')
            os.system('echo "deb http://http.kali.org/kali kali-experimental main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list.d/kali-experimental.list')
            os.system('echo "deb http://http.kali.org/kali kali-bleeding-edge main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list.d/kali-bleeding-edge.list')
            os.system("cat /etc/apt/sources.list")
            os.system("wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-key.asc")
            os.system("apt-get upgrade -y")
            os.system("reboot")
        elif User_choice == 2:
            os.system("wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run")
            os.system("chmod 777 metasploit-latest-linux-x64-installer.run")
            os.system("./metasploit-latest-linux-x64-installer.run")
        elif User_choice == 3:
            os.system("apt-get install nmap -y")
        elif User_choice == 4:
            os.system("apt-get install wireshark -y")
        elif User_choice == 5:
            os.system("apt-get install john -y")
        elif User_choice == 6:
            os.system("apt-get install burpsuite -y")
        elif User_choice == 7:
            os.system("apt-get install aircrack-ng -y")
        elif User_choice == 8:
            os.system("apt-get install nikto -y")
        elif User_choice == 9:
            os.system("apt-get install skipfish -y && apt-get install wpscan -y")
        elif User_choice == 10:
            os.system("wget http://ports.ubuntu.com/pool/universe/h/hydra/hydra-gtk_9.2-1ubuntu1_arm64.deb")
            os.system("wget http://old-releases.ubuntu.com/ubuntu/pool/universe/h/hydra/hydra_4.1-1_i386.deb")
            os.system("dpkg -i hydra-gtk_9.2-1ubuntu1_arm64.deb")
            os.system("dpkg -i hydra_4.1-1_i386.deb")
        elif User_choice == 11:
            os.system("sudo add-apt-repository ppa:darklordpaunik8880/darkminttrustytahr")
            os.system("sudo apt-get update -y")
            os.system("sudo apt-get install maltego -y")
        elif User_choice == 12:
            os.system("apt-get install ettercap")
            os.system("apt-get install ettercap-graphical")

    except KeyboardInterrupt:
        print("\nExit (Ctrl+C)")

if __name__ == "__main__":
    main()

                                                                                                                                                                                                                                                

#Created by xTyzenツ.py / Thitou kas ツ 
