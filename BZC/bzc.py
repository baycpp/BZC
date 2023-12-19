from itertools import permutations 
from colorama import Fore, init
from os import system
import pyzipper
init(autoreset="true")

# Created by baycpp
# Instagram: bay.cpp
# Discord: baycpp

def banner():
    try:
        system("clear")

    except:
        system("cls")

    print(Fore.RED + """
 ▄▄▄▄    ▄▄▄     ▓██   ██▓    ██▀███   ▄▄▄       ██▀███      ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
▓█████▄ ▒████▄    ▒██  ██▒   ▓██ ▒ ██▒▒████▄    ▓██ ▒ ██▒   ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▒██  ▀█▄   ▒██ ██░   ▓██ ░▄█ ▒▒██  ▀█▄  ▓██ ░▄█ ▒   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██░█▀  ░██▄▄▄▄██  ░ ▐██▓░   ▒██▀▀█▄  ░██▄▄▄▄██ ▒██▀▀█▄     ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓ ▓█   ▓██▒ ░ ██▒▓░   ░██▓ ▒██▒ ▓█   ▓██▒░██▓ ▒██▒   ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░▒▓███▀▒ ▒▒   ▓▒█░  ██▒▒▒    ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░   ▒   ▒▒ ░▓██ ░▒░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░     ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░    ░   ░   ▒   ▒ ▒ ░░       ░░   ░   ░   ▒     ░░   ░    ░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
 ░            ░  ░░ ░           ░           ░  ░   ░        ░ ░         ░           ░  ░░ ░      ░  ░      ░  ░   ░     
      ░           ░ ░                                       ░                           ░                               
------------------------------------------------------------------------------------------------------------------------
AUTHOR: baycpp                                      VERSION: 1.1                                      INSTAGRAM: bay.cpp
          """)
    

def zip_cracker_with_wordlist():
    wordlist = input(Fore.CYAN + "Lütfen wordlist dosyasını giriniz: ")
    print("")
    wordlist = open(wordlist, "r")

    for line in wordlist:
        try:
            with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as extracted_zip:
                extracted_zip.extractall(pwd=str.encode(line.rstrip('\n')))
                print(Fore.GREEN + "Şifre bulundu: ", line.rstrip('\n'))
                break

        except:
            print(Fore.RED + "Denenen şifre: ", line.rstrip('\n'))


def zip_cracker_with_combinations(characters):

    for i in range(1, len(characters)+1):
        for c in permutations(characters, i):
            
            try:
                with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as extracted_zip:
                    extracted_zip.extractall(pwd=str.encode(''.join(c)))
                    print(Fore.GREEN + "Şifre bulundu: ", ''.join(c))
                    break

            except:
                print(Fore.RED + "Denenen şifre: ", ''.join(c))

def zip_cracker_with_combination_options():
    global characters
    global turkish_characters
    global numbers
    global special_characters

    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghıijklmnopqrstuvwxyz"
    turkish_characters = "ÇĞİÖŞÜçğiöşü"
    numbers = "1234567890"
    special_characters = "\"'é!^+%&/()=?_-*"

    print(Fore.GREEN + """
1: Olası tüm kombinasyonlar
2: Sadece harfler (türkçe karakterler ve özel karakterler eklenebilir)
3: Sadece sayılar (türkçe karakterler ve özel karakterler eklenebilir)
""")
    
    option = input(Fore.CYAN + "Lütfen işlem giriniz: ")

    if option == "1":
        characters = characters + turkish_characters + numbers + special_characters
        zip_cracker_with_combinations(characters)

    elif option == "2":
        input_1 = input(Fore.CYAN + "Türkçe karakter eklensin mi E/h: ")
        input_2 = input(Fore.CYAN + "Özel karakter eklensin mi E/h: ")

        if input_1 == "E" and input_2 == "E" or input_1 == "e" and input_2 == "e":
            characters = characters + turkish_characters + special_characters
            zip_cracker_with_combinations(characters)

        elif input_1 == "E" and input_2 != "E" or input_1 == "e" and input_2 != "e":
            characters = characters + turkish_characters
            zip_cracker_with_combinations(characters)

        elif input_1 != "E" and input_2 == "E" or input_1 != "e" and input_2 == "e":
            characters = characters + special_characters
            zip_cracker_with_combinations(characters)

        elif input_1 != "E" and input_2 != "E" or input_1 != "e" and input_2 != "e":
            zip_cracker_with_combinations(characters)


    elif option == "3":
        input_1 = input(Fore.CYAN + "Türkçe karakter eklensin mi E/h: ")
        input_2 = input(Fore.CYAN + "Özel karakter eklensin mi E/h: ")

        if input_1 == "E" and input_2 == "E" or input_1 == "e" and input_2 == "e":
            characters = numbers + turkish_characters + special_characters
            zip_cracker_with_combinations(characters)

        elif input_1 == "E" and input_2 != "E" or input_1 == "e" and input_2 != "e":
            characters = numbers + turkish_characters
            zip_cracker_with_combinations(characters)

        elif input_1 != "E" and input_2 == "E" or input_1 != "e" and input_2 == "e":
            characters = numbers + special_characters
            zip_cracker_with_combinations(characters)

        elif input_1 != "E" and input_2 != "E" or input_1 != "e" and input_2 != "e":
            zip_cracker_with_combinations(numbers)
    
    
    else:
        print(Fore.CYAN + "Hatalı işlem girdiniz!")

def options():
    banner()

    global zip_file

    print(Fore.GREEN + """
1: Wordlist
2: Kombinasyon
""")
    
    option_input = input(Fore.CYAN + "Lütfen işlem giriniz: ")

    if option_input  == "1":
        zip_file = input(Fore.CYAN + "Lütfen zip dosyasını giriniz: ")
        zip_cracker_with_wordlist()

    elif option_input == "2":
        zip_file = input(Fore.CYAN + "Lütfen zip dosyasını giriniz: ")
        zip_cracker_with_combination_options()

    else:
        print("Hatalı işlem girdiniz!")


options()