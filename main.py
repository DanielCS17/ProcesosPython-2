import platform
import os

destinoPing = input("Indica el dominio o la dirección IP a comprobar: ")

if platform.system() == "Linux" or platform.system() == "Darwin":
    os.system(f"ping -c 4 {destinoPing}")
elif platform.system() == "Windows":
    os.system(f"ping {destinoPing}")
else:
    print("ERROR! Su sistema operativo no es compatible con este programa")