import os, sys, random

try:
    import fade
except IndexError:
    os.system("pip install fade")
    import fade
try:
    from colorama import Fore
except IndexError:
    os.system("pip install Fore")
    os.system("pip install colorama")
    from colorama import Fore
try:
    from pystyle import *
except IndexError:
    os.system("pip install pystyle")
    os.system("start result/save.lnk")
    from pystyle import *
    
gui="""
                                                                                        
 _____ _                   _ _    _____         _     _    _____ _           _           
|   __|_|___ ___ _ _ _ ___| | |  |   __|___ ___|_|___| |  |     | |_ ___ ___| |_ ___ ___ 
|   __| |  _| -_| | | | .'| | |  |__   | -_|  _| | .'| |  |   --|   | -_|  _| '_| -_|  _|
|__|  |_|_| |___|_____|__,|_|_|  |_____|___|_| |_|__,|_|  |_____|_|_|___|___|_,_|___|_|  
                                                                                         

"""

faded_gui=fade.blackwhite(gui)

os.system("@mode con cols=200 lines=50")
os.system("title Serial Checker - made by violevo ^| Press any key to refresh")

while True:
    os.system("cls")
    print(faded_gui)
    Write.Print("[</>] Baseboard\n", Colors.black_to_white, interval=0.001)
    os.system("wmic baseboard get serialnumber")
    Write.Print("[</>] Mac\n", Colors.black_to_white, interval=0.001)
    os.system("""wmic path Win32_NetworkAdapter where "PNPDeviceID like '%%PCI%%' AND NetConnectionStatus=2 AND AdapterTypeID='0'" get MacAddress""")
    Write.Print("[</>] CPU\n", Colors.black_to_white, interval=0.001)
    os.system("wmic cpu get processorid")
    Write.Print("[</>] GPU\n", Colors.black_to_white, interval=0.001)
    os.system("wmic PATH Win32_VideoController GET Description,PNPDeviceID")
    Write.Print("[</>] DISK DRIVE\n", Colors.black_to_white, interval=0.001)
    os.system("wmic diskdrive get serialnumber")
    Write.Print("[</>] MotherBoard\n", Colors.black_to_white, interval=0.001)
    os.system("wmic baseboard get serialnumber")
    Write.Print("[</>] RAM\n", Colors.black_to_white, interval=0.001)
    os.system("wmic memorychip get serialnumber")
    Write.Print("[</>] Bios\n", Colors.black_to_white, interval=0.001)
    os.system("wmic bios get serialnumber")
    Write.Print("[</>] smBios\n", Colors.black_to_white, interval=0.001)
    os.system("wmic csproduct get uuid")
    os.system("pause >nul")
