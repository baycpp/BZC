from colorama import Fore, init
from time import sleep
from os import system
import platform
import pyzipper
import sys

init(autoreset="true")

# Created by baycpp
# Instagram: bay.cpp

def clear():
	if platform.system == "Windows":
		system("cls")
	else:
		system("clear")

def banner():
	clear()

	print(Fore.RED + """
 ▄▄▄▄    ▄▄▄     ▓██   ██▓   ▒███████▒ ██▓ ██▓███      ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓█████▄ ▒████▄    ▒██  ██▒   ▒ ▒ ▒ ▄▀░▓██▒▓██░  ██▒   ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▒██  ▀█▄   ▒██ ██░   ░ ▒ ▄▀▒░ ▒██▒▓██░ ██▓▒   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██░█▀  ░██▄▄▄▄██  ░ ▐██▓░     ▄▀▒   ░░██░▒██▄█▓▒ ▒   ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓ ▓█   ▓██▒ ░ ██▒▓░   ▒███████▒░██░▒██▒ ░  ░   ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░▒▓███▀▒ ▒▒   ▓▒█░  ██▒▒▒    ░▒▒ ▓░▒░▒░▓  ▒▓▒░ ░  ░   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░   ▒   ▒▒ ░▓██ ░▒░    ░░▒ ▒ ░ ▒ ▒ ░░▒ ░          ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░    ░   ░   ▒   ▒ ▒ ░░     ░ ░ ░ ░ ░ ▒ ░░░          ░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
 ░            ░  ░░ ░          ░ ░     ░              ░ ░         ░           ░  ░░ ░      ░  ░      ░  ░   ░     
      ░           ░ ░        ░                        ░                           ░                               
------------------------------------------------------------------------------------------------------------------
AUTHOR: baycpp                                      VERSION: 1.2                                INSTAGRAM: bay.cpp
""")

def print_options():
	print(Fore.CYAN + """
PARAMETRELER  	AÇIKLAMALARI
-----------------------------------------------------
-h		Bu pencereyi gösterir.
-f		Zip dosyasını belirtmek için kullanılır.
-w		Wordlist dosyasını belirtmek için kullanılır.
	   
KULLANIM:
python3 bzc.py -w <wordlist_dosyası> -f <zip_dosyası>
	     """)

def zip_cracker_with_wordlist():
	zip_file = sys.argv[4]
	wordlist = sys.argv[2]

	clear()
	print(Fore.GREEN + "ZIP DOSYASI KIRILIYOR!!\n")
	print(Fore.GREEN + f"Zip dosyası: {zip_file}\nWordlist dosyası: {wordlist}")
	
	wordlist = open(wordlist, 'r')
	password_found = False

	for line in wordlist:
		denenen_sifre = line.rstrip('\n')

		try:
			with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as extracted_zip:
				extracted_zip.extractall(pwd=str.encode(line.rstrip('\n')))
				sleep(2)
				print("\033[K", end='')
				print(Fore.GREEN + f"Şifre bulundu: {denenen_sifre}")
				password_found = True
				break
		
		except:
			print(Fore.RED + f"Denenen şifre: {denenen_sifre}", end='\r')
	
	if password_found == False:
		print("\033[K", end='')
		print(Fore.RED + "Şifre bulunamadı!")
		print(Fore.RED + f"Son denenen: {denenen_sifre}")


def main():
	try:
		if len(sys.argv) != 5:
			banner()
			print_options()
		else:
			zip_cracker_with_wordlist()
	except:
		banner()
		print_options()

main()
