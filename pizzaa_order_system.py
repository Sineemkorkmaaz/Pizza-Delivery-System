import csv
import datetime




#Üst sınıf oluşturulması "pizza"
class Pizza:
    def get_description(self): 
        return self.__class__.__name__

    def get_cost(self): 
        return self.__class__.cost
    

#Alt sınıf oluşturma "pizza"
class Klasik(Pizza):
    cost = 85.0
    def __init__(self):
        self.description = "Klasik Pizza Malzemeler : Pizza sosu, Mısır, Kaşar ,Sosis"
        print(self.description+"\n")


class Margarita(Pizza):
    cost = 70.0
    def __init__(self):
        self.description = "Margarita Pizza Malzemeler : Pizza sosu, Mozarella, Fesleğen"
        print(self.description+"\n")
        


class TurkPizza(Pizza):
    cost = 90.0
    def __init__(self):
        self.description = "Türk Pizza Malzemeler : Pizza sosu, Kaşar, Sucuk, Yeşil Biber, Zeytin"
        print(self.description+"\n")


class SadePizza(Pizza):
    cost = 70.0
    def __init__(self):
        self.description = "Sade Pizza Malzemeler : Pizza sosu, Kaşar "
        print(self.description+"\n")


class Kavurmalı(Pizza):
    cost = 95.0
    def __init__(self):
        self.description = "Kavurmalı Pizza Malzemeler : Pizza sosu, Kaşar, Kavurma, Domates"
        print(self.description+"\n")



#Üst sınıf oluşturma "Decorator"
class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping
    def get_cost(self):
        return self.component.get_cost() + \
        Pizza.get_cost(self)
    def get_description(self):
        return self.component.get_description() + \
        ';' + Pizza.get_description(self)

#Sosları oluşturma
class Zeytin(Decorator):
    cost = 2.0
    def __init__(self, topping):
        Decorator.__init__(self, topping)        


class Mantar(Decorator):
    cost = 2.5
    def __init__(self, topping):
        Decorator.__init__(self, topping)   


class KeciPeyniri(Decorator):
    cost = 4.0
    def __init__(self, topping):
        Decorator.__init__(self, topping)   


class Et(Decorator):
    cost = 12.0
    def __init__(self, topping):
        Decorator.__init__(self, topping)  


class Soğan(Decorator):
    cost = 3.0
    def __init__(self, topping):
        Decorator.__init__(self, topping)   


class Mısır(Decorator):
    cost = 5.0
    def __init__(self, topping):
        Decorator.__init__(self, topping)   


class HindiFume(Decorator):
    cost = 7.0
    def __init__(self, topping):
        Decorator.__init__(self, topping)   

# Menüyü ekrana bastırma işlemi 
with open("menu.txt", "w") as file :
    file.write("* Lütfen Pizzanızı Seçiniz:\n1: Klasik\n2: Margarita\n3: Türk Pizza \n4: Sade Pizza\n5: Kavurmalı Pizza\n")
    file.write("* Ekstra Malzemeler :\n11: Zeytin\n12: Mantar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n17:Hindi Füme\n")
    file.write("* Teşekkür ederiz !")

f = open("menu.txt", "r")
print(f.read())

#Siparişler için listeleme
class_dict = {1: Klasik, 
2: Margarita, 
3: TurkPizza, 
4: SadePizza, 
5: Kavurmalı,
11: Zeytin,
12: Mantar,
13: KeciPeyniri,
14: Et,
15: Soğan,
16: Mısır,
17: HindiFume}



code = input("Lütfen Pizzanızı Seçiniz: ")
while code not in ["1", "2", "3", "4", "5"]:
    code = input("Yanlış Tuşlama Yaptınız,Tekrar Deneyiniz: ")
    
order = class_dict[int(code)]()

while code != "!":
        code = input("Ek Malzemeler İçin Tuşlama Yapınız (Direkt Siparişinizi Onaylamak İçin '!' Tuşuna Basınız): ")
        if code in ["11","12","13","14","15","16","17"]:
            order = class_dict[int(code)](order)




#Sipariş Kart Bilgileri
print("-----------Sipariş Bilgileri--------\n")
name = input("Adınız : ")
while(not(name.isalpha())):
    name = input("Geçersiz ad !\n Tekrar Adınızı Giriniz  : ")

ID = input("TC Kimlik Numaranızı Giriniz : ")
while((not(ID.isnumeric())) or len(ID) is not 11):
    ID = input("Geçersiz TC kimlik !\n Tekrar TC Kimlik Numaranızı Giriniz : ")

kk_no = input("Kredi Kartı Numaranızı Yazınız : ")
while((not(kk_no.isnumeric())) or len(kk_no) is not 16):
    kk_no = input("Geçersiz Kredi Kartı Numarası !\n Tekrar Kredi Kartı Numaranızı Yazınız : ")

kk_psw = input ("Kredi Kartı Şifrenizi Yazınız : ")
while((not(kk_psw.isnumeric())) or len(kk_psw) is not 4):
    kk_psw = input("Geçersiz Kredi Kartı Şifresi !\n Tekrar Kredi Kartı Şifrenizi Yazınız : ")
time_of_order = datetime.datetime.now()



#Database oluşumu 
with open ('Orders_Database.csv' , 'a' ) as orders :
    orders = csv.writer(orders, delimiter=',')
    orders.writerow([name, ID, kk_no, kk_psw, order.get_description(), time_of_order])
    print ("Siparişiniz Onaylanmıştır. Bizi Seçtiğiniz İçin Teşekkür Ederiz ")