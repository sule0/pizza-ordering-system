import csv
import datetime


# MENÜ TXT DOSYASINDAN OKUNUR.
def menu_oku():
    with open("Menu.txt", "r") as menu:
        print(menu.read())

def main():
    menu_oku()

menu_oku()

#İŞLEM YAPILAN TARİH HESAPLANIR.
now1 = datetime.datetime.now()
tarih = now1.strftime("%d/%m/%Y %H:%M:%S")

#PİZZA ÜST VE ALT SINIFLARI OLUŞTURULUR.
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    # AÇIKLAMA VE FİYAT DEĞERİ DÖNDÜRÜLÜR.
    def get_description(self):
        return self.description
    def get_cost(self):
        return self.cost


class klasik_pizza(Pizza):
    
    def __init__(self):
        super().__init__("Klasik Pizza", 90)

class margarita_pizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza",100 )

class turk_pizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 90)

class sade_pizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 85)

#SOSLARIN ÜST SINIFI OLUŞTURULUR.
class Decorator(Pizza):
    def __init__(self, sos , description, cost):
        super().__init__(description, cost)
        self.sos = sos

    # TUTAR VE AÇIKLAMA GERİ DÖNDÜRÜLÜR.
    def get_cost(self):
        return self.sos.get_cost() + super().get_cost()
    
    def get_description(self):
        return super().get_description() + ' ' + self.sos.get_description()

#DECARATOR'UN ALT SINIFLARI (SOSLAR) OLUŞTURULUR.
class zeytinli(Decorator):
    def __init__(self, sos):
        super().__init__(sos, "Zeytinli", 6)

class mantarli(Decorator):
    def __init__(self, sos):
        super().__init__(sos, "Mantarl",8)

class keci_peynirli(Decorator):
    def __init__(self, sos):
        super().__init__(sos, "Keçi peynirli",15)

class etli(Decorator):
    def __init__(self, sos):
        super().__init__(sos, "Etli",20)

class soganli(Decorator):
    def __init__(self, sos):
        super().__init__(sos, "Soğanlı",5)

class misirli(Decorator):
    def __init__(self, sos):
        super().__init__(sos, "Mısırlı",7)

#PİZZA VERİLERİ KULLANICIDAN ALINIR , DOĞRU DEĞİLSE TEKRAR SORAR.
while True:
    
    pizza_tabani = int(input('Pizza tabanı seçiniz (1-4): '))

    if pizza_tabani== 1:
        pizza = klasik_pizza()
        break
    elif pizza_tabani== 2:
        pizza = margarita_pizza()
        break
    elif pizza_tabani== 3:
        pizza = turk_pizza()
        break
    elif pizza_tabani== 4:
        pizza = sade_pizza()
        break
    else:
        print("Yanlış tuşladınız. Tekrar deneyiniz.\n")

    
while True:
    
    pizza_sosu = int(input("Pizza sosu seçiniz (11-16): "))

    if pizza_sosu == 11:
        sos = zeytinli(pizza)
        break
    elif pizza_sosu == 12:
        sos = mantarli(pizza)
        break
    elif pizza_sosu == 13:
        sos = keci_peynirli(pizza)
        break
    elif pizza_sosu == 14:
        sos = etli(pizza)
        break
    elif pizza_sosu == 15:
        sos = soganli(pizza)
        break
    elif pizza_sosu == 16:
        sos = misirli(pizza)
        break
    else:   
        print("Yanlış tuşladınız.Tekrar deneyiniz.\n")


toplam_tutar = sos.get_cost()


print(f"\nSeçiminiz : {sos.get_description()}\nToplam tutar: {toplam_tutar:.2f} TL\n")

#İSİM İSTENİR. 
isim = input("\nLütfen isminizi giriniz: ")

#DOĞRU GİRENE KADAR TC VE KREDİ KARTI BİLGİLERİ İSTENİR İSTENİR.
while True:
   
        tc_no = int(input("Lütfen TC kimlik numaranızı giriniz: "))
        if len(str(tc_no)) == 11:
            break
        else:
                print("TC kimlik numarası 11 haneli ve rakamlardan oluşmalıdır\n")
        
while True:
       
            kart_no = int(input("Lütfen kredi kartı numaranızı giriniz: "))
            if len(str(kart_no)) == 16:
                break
            else:
                print("Kart numarası 16 haneli ve rakamlardan oluşmalıdır\n")
            
while True:
    
    kart_sifre = input("Lütfen kredi kartı şifrenizi giriniz: ")
    if len(str(kart_sifre))==4:
        break
    else:
         print("Kart şifresi 4 haneli olmalıdır\n")


#İŞLEMİN GERÇEKLEŞME SÜRESİ HESAPLANIR.
now2=datetime.datetime.now()
islem_suresi=now2-now1

    
#CSV DOSYASI OLUŞTURULUR VE BİLGİLER ORADA TUTULUR.
with open('Orders_Database.csv', 'a') as database:
        veriler = csv.writer(database)
        veriler.writerow(["isim: ",isim ,"\nTc no: ",tc_no,"\nPizza türü: " ,sos.get_description(),"\nTutar: ", toplam_tutar, "\nKart no: ",kart_no,"\nKart şifresi: " ,kart_sifre,"\nİşlem süresi: ",islem_suresi,"\ntarih: ",tarih])
    
print(f'\n{sos.get_description()} siparişiniz alınmıştır. Bizi tercih ettiğin için teşekkürler {isim}!')




