# Hesap Makinesi

from time import sleep
from colorama import Fore

from os import name
from os import system

class GetStartingControl(object):
    def __init__(self):
        try:
            if name == "win32" or name == "win64":
                system("cls")
            else:
                system("clear")
        except:
            print("{0}[!]{1} Geçersiz bir sistemde çalıştırdınız lütfen tekrar deneyin.".forrmat(Fore.RED, Fore.RESET))
            exit()
        finally:
            print("{0}[*]{1} Hesap Makinesi: {2}".format(Fore.LIGHTYELLOW_EX, Fore.RESET, name))
            print("{0}[*]{1} Başlatılıyor...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
            sleep(3.7)
            if name == "win32" or name == "win64":
                system("cls")
            else:
                system("clear")

class menu(object):
    def __init__(self):
        print(r"""
                    {0}** HESAP MAKİNESİ **{1}

                    {2}1-{1} Toplama
                    {2}2-{1} Çıkarma
                    {2}3-{1} Çarpma
                    {2}4-{1} Bölme
                    {2}5-{1} Mod Alma
                    {2}6-{1} Exit

                """.format(Fore.GREEN, Fore.RESET, Fore.RED))
       # İşlem yaptıralım
        
class Calculator(object):
    def Collection(self, n1, n2, total, choice):
        self.choice = choice
        if self.choice == 1:
            self.n1 = n1
            self.n2 = n2
            self.total = total
            self.total = int(self.n1) + int(self.n2)
            print("{0}[Hesap Makinesi]{1} {2} + {3} = : {4}".format(Fore.LIGHTGREEN_EX, Fore.RESET, str(self.n1), str(self.n2), str(self.total)))
        elif self.choice == 2:
            self.n1 = n1
            self.n2 = n2
            self.total = total
            self.total = int(self.n1) - int(self.n2)
            print("{0}[Hesap Makinesi]{1} {2} - {3} = : {4}".format(Fore.LIGHTGREEN_EX, Fore.RESET, str(self.n1), str(self.n2), str(self.total)))
        elif self.choice == 3:
            self.n1 = n1
            self.n2 = n2
            self.total = total
            self.total = int(self.n1) * int(self.n2)
            print("{0}[Hesap Makinesi]{1} {2} * {3} = : {4}".format(Fore.LIGHTGREEN_EX, Fore.RESET, str(self.n1), str(self.n2), str(self.total)))
        elif self.choice == 4:
            self.n1 = n1
            self.n2 = n2
            self.total = total
            self.total = int(self.n1) / int(self.n2)
            print("{0}[Hesap Makinesi]{1} {2} / {3} = : {4}".format(Fore.LIGHTGREEN_EX, Fore.RESET, str(self.n1), str(self.n2), str(self.total)))
        elif self.choice == 5:
            self.n1 = n1
            self.n2 = n2
            self.total = total
            self.total = int(self.n1) % int(self.n2)
            print("{0}[Hesap Makinesi]{1} {2} % {3} = : {4}".format(Fore.LIGHTGREEN_EX, Fore.RESET, str(self.n1), str(self.n2), str(self.total)))
        else:
            print("{0}[!!]{1} Beklenmeyen bir hata oluştu.".format(Fore.RED, Fore.RESET))

            # İşlemlerin gerçekleştiği son bölüm
            
st = GetStartingControl()
start = menu()
Calc = Calculator()
counter = 0
while True:
    counter += 1
    choice = input("{0}[?] {1}Lütfen seçiminizi yapın : ".format(Fore.LIGHTYELLOW_EX, Fore.RESET, Fore.LIGHTGREEN_EX))
    total = 0
    try:
        if choice.isdigit():
            choice = int(choice)
            if choice == 6:
                counter -= 1
                sleep(0.5)
                print("{0}[Hesap Makinesi]{1} {2}Çıkışınız tamamlandı...".format(Fore.LIGHTGREEN_EX, Fore.RESET, Fore.LIGHTGREEN_EX))
                sleep(1)
                print("{0}[**]{1} Toplam işlem sayısı : {2}{3}{1}".format(Fore.LIGHTYELLOW_EX, Fore.RESET, Fore.LIGHTGREEN_EX, str(counter), Fore.RESET))
                break
            elif choice > 6 or choice < 1 or choice < 0 is False:
                print("{0}[404]{1} Lütfen sadece sayı giriniz - [1-5]".format(Fore.RED, Fore.RESET))
                break
            else:
                n1 = input("{0}[**]{1} İlk numarayı girin: ".format(Fore.LIGHTGREEN_EX, Fore.RESET))
                n2 = input("{0}[**]{1} İkinci numarayı girin: ".format(Fore.LIGHTGREEN_EX, Fore.RESET))
                if choice == 1:
                    sleep(2)
                    print("{0}[*]{1} sayılar toplanıyor...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(1)
                    print("{0}[*]{1} Lütfen bekleyiniz...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(2)
                    Calc.Collection(n1, n2, total, choice)
                elif choice == 2:
                    sleep(2)
                    print("{0}[*]{1} çıkarma işlemini seçtiniz...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(1)
                    print("{0}[*]{1} Lütfen bekleyiniz...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(2)
                    Calc.Collection(n1, n2, total, choice)
                elif choice == 3:
                    sleep(2)
                    print("{0}[*]{1} sayılar çarpılıyor...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(1)
                    print("{0}[*]{1} Lütfen bekleyiniz...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(2)
                    Calc.Collection(n1, n2, total, choice)
                elif choice == 4:
                    sleep(2)
                    print("{0}[*]{1} sayılar bölünüyor...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(1)
                    print("{0}[*]{1} Lütfen bekleyiniz...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(2)
                    Calc.Collection(n1, n2, total, choice)
                elif choice == 5:
                    sleep(2)
                    print("{0}[*]{1} sayılar modlanıyor...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(1)
                    print("{0}[*]{1} Lütfen bekleyiniz...".format(Fore.LIGHTYELLOW_EX, Fore.RESET))
                    sleep(2)
                    Calc.Collection(n1, n2, total, choice)
                else:
                    print("{0}[404]{1} Lütfen sadece sayı giriniz - [1-6]".format(Fore.RED, Fore.RESET))
                    exit()
    except:
        print("{0}[404]{1} Lütfen sadece sayı giriniz -  [1-6]".format(Fore.RED, Fore.RESET))
