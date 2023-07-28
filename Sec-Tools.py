import os
import sys

os.system("clear")

def afficher_page_accueil():
    print("""   _____               _______          _     
  / ____|             |__   __|        | |    
 | (___   ___  ___ ______| | ___   ___ | |___ 
  \___ \ / _ \/ __|______| |/ _ \ / _ \| / __|
  ____) |  __/ (__       | | (_) | (_) | \__ |
 |_____/ \___|\___|      |_|\___/ \___/|_|___/ by xTyzenツ.py
                            
                                                                                      
 [1]: Install Repo Kali Linux     [5]: JohnTheRipper       [9]: SkipFish and WPScan

 [2]: Metasploit                  [6]: BurpSuite           [10]: Hydra

 [3]: Nmap                        [7]: Aircrack-ng         [11]: Maltego

 [4]: Wireshark                   [8]: Nikto               [12]: Ettercap             
                                                    
                                                        
                                                        
                                                                                                 """)

def afficher_page_secondaire():
    print("""   _____               _______          _     
  / ____|             |__   __|        | |    
 | (___   ___  ___ ______| | ___   ___ | |___ 
  \___ \ / _ \/ __|______| |/ _ \ / _ \| / __|
  ____) |  __/ (__       | | (_) | (_) | \__ |
 |_____/ \___|\___|      |_|\___/ \___/|_|___/ by xTyzenツ.py
                                                  
                                                  
  [13]: Sqlmap                      [17]: Crunch           [21]: Armitage (Metasploit graphics)
                                                        
  [14]: Hashcat                     [18]: Kismet           [22]: TheHarvester

  [15]: Netcat                      [19]: Powershell       [23]: Autospy

  [16]: Gobuster                    [20]: Netdiscover      [24]: Beef-XSS                

      <[2]> ou <[3]> selection de pages                                                        

                                                                        """)

def afficher_derniere_page():
    print("""   _____               _______          _     
  / ____|             |__   __|        | |    
 | (___   ___  ___ ______| | ___   ___ | |___ 
  \___ \ / _ \/ __|______| |/ _ \ / _ \| / __|
  ____) |  __/ (__       | | (_) | (_) | \__ |
 |_____/ \___|\___|      |_|\___/ \___/|_|___/ by xTyzenツ.py
 
 <[2]> ou <[3]> selection de pages
 
 
                    [25]: Install all kali tools
 
                    [#] l'installation risque être long...
                                                                    """)

def installer_choix_page_accueil(outil):
    if outil == 1:
        os.system("grep -v '#' /etc/apt/sources.list | sort -u deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware")
        os.system('echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list')
        os.system('echo "deb http://http.kali.org/kali kali-last-snapshot main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list')
        os.system('echo "deb http://http.kali.org/kali kali-experimental main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list.d/kali-experimental.list')
        os.system('echo "deb http://http.kali.org/kali kali-bleeding-edge main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list.d/kali-bleeding-edge.list')
        os.system("cat /etc/apt/sources.list")
        os.system("wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-key.asc")
        os.system("apt-get upgrade -y")
        os.system("reboot")
    elif outil == 2:
        os.system("wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run")
        os.system("chmod 777 metasploit-latest-linux-x64-installer.run")
        os.system("./metasploit-latest-linux-x64-installer.run")
    elif outil == 3:
        os.system("apt-get update")
        os.system("apt-get install nmap -y")
    elif outil == 4:
        os.system("apt-get update")
        os.system("apt-get install wireshark -y")
    elif outil == 5:
        os.system("apt-get update")
        os.system("apt-get install john -y")
    elif outil == 6:
        os.system("apt-get update")
        os.system("apt-get install burpsuite -y")
    elif outil == 7:
        os.system("apt-get update")
        os.system("apt-get install aircrack-ng -y")
    elif outil == 8:
        os.system("apt-get update")
        os.system("apt-get install nikto -y")
    elif outil == 9:
        os.system("apt-get update")
        os.system("apt-get install skipfish -y && apt-get install wpscan -y")
    elif outil == 10:
        os.system("apt-get update")
        os.system("wget http://ports.ubuntu.com/pool/universe/h/hydra/hydra-gtk_9.2-1ubuntu1_arm64.deb")
        os.system("wget http://old-releases.ubuntu.com/ubuntu/pool/universe/h/hydra/hydra_4.1-1_i386.deb")
        os.system("dpkg -i hydra-gtk_9.2-1ubuntu1_arm64.deb")
        os.system("dpkg -i hydra_4.1-1_i386.deb")
    elif outil == 11:
        os.system("apt-get update")
        os.system("sudo add-apt-repository ppa:darklordpaunik8880/darkminttrustytahr")
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get install maltego -y")
    elif outil == 12:
        os.system("apt-get update")
        os.system("apt-get install ettercap")
        os.system("apt-get install ettercap-graphical")

def installer_choix_page_secondaire(outil):
    if outil == 13:
        os.system("apt-get update")
        os.system("apt-get install sqlmap")
    elif outil == 14:
        os.system("apt-get update")
        os.system("apt-get install hashcat")
    elif outil == 15:
        os.system("apt-get update")
        os.system("apt-get install netcat-traditional")
    elif outil == 16:
        os.system("apt-get update")
        os.system("sudo apt install gobuster")
    elif outil == 17:
        os.system("apt-get update")
        os.system("apt-get install crunch")
    elif outil == 18:
        os.system("apt-get update")
        os.system("apt-get kismet")
    elif outil == 19:
        os.system("apt-get update")
        os.system("apt-get powershell")
    elif outil == 20:
        os.system("apt-get update")
        os.system("apt-get install netdiscover")
    elif outil == 21:
        os.system("apt-get install git -y")
        os.system("git clone https://github.com/Matt-London/Install-Armitage-on-Linux.git")
        os.system("cd Install-Armitage-on-Linux-master")
        os.system("./ArmitageInstaller")
    elif outil == 22:
        os.system("git clone https://github.com/laramies/theHarvester")
        os.system("cd theHarvester")
        os.system("apt-get install python3-pip")
        os.system("pip install -r requirements/dev.txt")
        os.system("pip install -r requirements/base.txt")
        os.system("python3 theHarvester.py -h")
    elif outil == 23:
        os.system("wget https://objects.githubusercontent.com/github-production-release-asset-2e65be/2562873/e41ba0dc-6a67-49e2-a9d9-288f63192f8c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230716%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230716T123629Z&X-Amz-Expires=300&X-Amz-Signature=1a8e26b0d2c0a97b3a6ae2cf0cdf77afd356037ffd7cc752f1df48551e7d4656&X-Amz-SignedHeaders=host&actor_id=95149824&key_id=0&repo_id=2562873&response-content-disposition=attachment%3B%20filename%3Dsleuthkit-java_4.12.0-1_amd64.deb&response-content-type=application%2Foctet-stream")
        os.system("dpkg -i sleuthkit-java_4.12.0-1_amd64.deb")
    elif outil == 24:
        os.system("apt-get install ruby ruby-dev")
        os.system("apt-get install git")
        os.system("git clone https://github.com/beefproject/beef")
        os.system("cd beef")
        os.system("./install")
        os.system("./beef")
        
def installer_choix_derniere_page(outil):
    if outil == 25:
        os.system("grep -v '#' /etc/apt/sources.list | sort -u deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware")
        os.system('echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list')
        os.system('echo "deb http://http.kali.org/kali kali-last-snapshot main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list')
        os.system('echo "deb http://http.kali.org/kali kali-experimental main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list.d/kali-experimental.list')
        os.system('echo "deb http://http.kali.org/kali kali-bleeding-edge main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list.d/kali-bleeding-edge.list')
        os.system("cat /etc/apt/sources.list")
        os.system("wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-key.asc")
        os.system("apt-get upgrade -y")
        os.system("apt-get install sqlmap")
        os.system("apt-get install hashcat")
        os.system("apt-get install netcat-traditional")
        os.system("sudo apt install gobuster")
        os.system("apt-get install crunch")
        os.system("apt-get kismet")
        os.system("apt-get powershell")
        os.system("apt-get install netdiscover")
        os.system("apt-get install git -y")
        os.system("git clone https://github.com/Matt-London/Install-Armitage-on-Linux.git")
        os.system("cd Install-Armitage-on-Linux-master")
        os.system("./ArmitageInstaller")
        os.system("apt-get install theharvester")
        os.system("wget https://objects.githubusercontent.com/github-production-release-asset-2e65be/2562873/e41ba0dc-6a67-49e2-a9d9-288f63192f8c?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230716%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230716T123629Z&X-Amz-Expires=300&X-Amz-Signature=1a8e26b0d2c0a97b3a6ae2cf0cdf77afd356037ffd7cc752f1df48551e7d4656&X-Amz-SignedHeaders=host&actor_id=95149824&key_id=0&repo_id=2562873&response-content-disposition=attachment%3B%20filename%3Dsleuthkit-java_4.12.0-1_amd64.deb&response-content-type=application%2Foctet-stream")
        os.system("dpkg -i sleuthkit-java_4.12.0-1_amd64.deb")
        os.system("apt-get install ruby ruby-dev")
        os.system("apt-get install git")
        os.system("git clone https://github.com/beefproject/beef")
        os.system("cd beef")
        os.system("./install")
        os.system("./beef")
        os.system("apt-get install ettercap")
        os.system("apt-get install ettercap-graphical")
        os.system("apt-get update")
        os.system("sudo add-apt-repository ppa:darklordpaunik8880/darkminttrustytahr")
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get install maltego -y")
        os.system("apt-get install hydra")
        os.system("apt-get install skipfish -y && apt-get install wpscan -y")
        os.system("apt-get install nikto -y")
        os.system("apt-get install aircrack-ng -y")
        os.system("apt-get install burpsuite -y")
        os.system("apt-get install john -y")
        os.system("apt-get install wireshark -y")
        os.system("apt-get install nmap -y")
        os.system("apt-get install metasploit-framework")
        os.system("apt-get install arpwatch ")
        os.system("apt-get install tcpdump")
        os.system("apt-get install mimikatz")
        os.system("apt-get install responder")
        os.system("apt-get install ffuf")
        os.system("apt-get install wifite")
        os.system("apt-get install dirb")
        os.system("apt-get install medusa")
        os.system("apt-get install impacket-scripts")
        os.system("apt-get install dmitry")
        os.system("apt-get install dirbuster")
        os.system("apt-get install airgeddon")
        os.system("apt-get install airgeddon")
        os.system("apt-get install parsero")
        os.system("apt-get install metagoofil")
        os.system("apt-get install hping3")
        os.system("apt-get install commix")
        os.system("apt install cewl")
        os.system("apt-get install assetfinder")
        os.system("apt-get install subfinder")
        os.system("apt-get install recon-ng")
        os.system("apt-get install goldeneye")
        os.system("apt-get install fern-wifi-cracker")
        os.system("apt-get install bettercap")
        os.system("apt-get install whatweb")
        os.system("apt-get install spiderfoot")
        os.system("apt-get install scapy")
        os.system("apt-get install reaver")
        os.system("apt-get install rainbowcrack")
        os.system("apt-get install netdiscover")
        os.system("aapt-get install fcrackzip")
        os.system("apt-get install dnsrecon")
        os.system("apt-get install socat")
        os.system("apt-get install rkhunter")
        os.system("apt-get install redeye")
        os.system("apt-get install nuclei")
        os.system("apt-get install macchanger")
        os.system("apt-get install httrack")
        os.system("apt-get install ghidra")
        os.system("apt-get install foremost")
        os.system("apt-get install dnsenum")
        os.system("apt-get install wordlists")
        os.system("apt-get install sublist3r")
        os.system("apt-get install sslstrip")
        os.system("apt-get install set")
        os.system("apt-get install scalpel")
        os.system("apt-get install johnny")
        os.system("apt-get install guymager")
        os.system("apt-get install fierce")
        os.system("apt-get install eyewitness")
        os.system("apt-get install dvwa")
        os.system("apt-get install cryptsetup")
        os.system("apt-get install cisco-torch")
        os.system("apt-get install chntpw")
        os.system("apt-get install btscanner")
        os.system("apt-get install arjun")
        os.system("apt-get install amass")
        os.system("apt-get install xsser")
        os.system("apt-get install wifiphister")
        os.system("apt-get install wfuzz")
        os.system("apt-get install testdisk")
        os.system("apt-get install reglookup")
        os.system("apt-get install pipal")
        os.system("apt-get install ollydbg")
        os.system("apt-get install nbtscan")
        os.system("apt-get install masscan")
        os.system("apt-get install legion")
        os.system("apt-get install jadx")
        os.system("apt-get install hakrawler")
        os.system("apt-get install fping")
        os.system("apt-get install evil-winrm")
        os.system("apt-get install driftnet")
        os.system("apt-get install dradis")
        os.system("apt-get install dirsearch")
def main():
    if os.geteuid() != 0:
        print("Veuillez exécuter le script en tant que root.")
        return

    choix_valide_page_accueil = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 80]
    choix_valide_page_secondaire = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 90]
    choix_valide_derniere_page = [25]

    while True:
        afficher_page_accueil()
        choix = int(input("[Choisi une page]==>(1-3): "))

        if choix == 1:
            outil = int(input("[Sec-Tools]~#"))
            installer_choix_page_accueil(outil)
        elif choix == 2:
            afficher_page_secondaire()
            outil = int(input("[Sec-Tools]~#"))
            installer_choix_page_secondaire(outil)
        elif choix == 3:
            afficher_derniere_page()
            outil = int(input("[Sec-Tools]~#"))
            installer_choix_derniere_page(outil)
        else:
            print("Choisi une page valide.")

if __name__ == "__main__":
    main()

