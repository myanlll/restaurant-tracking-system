import sys
import math
import random

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_RestorantTakip
from ui_fiyatlar import Ui_Fiyatlar


class Restorant_takipsis(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RestorantTakip()
        self.ui.setupUi(self)
        self.fiyat_liste_widget = None
        self.ui.push_fiyat.clicked.connect(self.fiyat_listesini_goster)
        self.ui.push_toplam.clicked.connect(self.random_sayi_yaz)
        self.ui.push_toplam.clicked.connect(self.topla)
        self.ui.push_toplam.clicked.connect(self.kayit_ekle)
        self.ui.push_sifirla.clicked.connect(self.sifirla_hesapla)
        
        self.ui.p9.clicked.connect(lambda: self.PushtButton("9"))
        self.ui.p8.clicked.connect(lambda: self.PushtButton("8"))
        self.ui.p7.clicked.connect(lambda: self.PushtButton("7"))
        self.ui.p6.clicked.connect(lambda: self.PushtButton("6"))
        self.ui.p5.clicked.connect(lambda: self.PushtButton("5"))
        self.ui.p4.clicked.connect(lambda: self.PushtButton("4"))
        self.ui.p3.clicked.connect(lambda: self.PushtButton("3"))
        self.ui.p2.clicked.connect(lambda: self.PushtButton("2"))
        self.ui.p1.clicked.connect(lambda: self.PushtButton("1"))
        self.ui.p0.clicked.connect(lambda: self.PushtButton("0"))
        self.ui.pdiv.clicked.connect(lambda: self.PushtButton("/"))
        self.ui.pX.clicked.connect(lambda: self.PushtButton("*"))
        self.ui.pMod.clicked.connect(lambda: self.PushtButton("%"))
        self.ui.pdot.clicked.connect(lambda: self.PushtButton("."))
        self.ui.pPos.clicked.connect(lambda: self.PushtButton("+"))
        self.ui.pMin.clicked.connect(lambda: self.PushtButton("-"))
        ###
        self.ui.pRootSq.clicked.connect(lambda: self.KokunuAl())

        self.ui.pxSq.clicked.connect(lambda: self.KaresiniAl())

        self.ui.pequals.clicked.connect(lambda: self.Hesapla())

        self.ui.pDel.clicked.connect(lambda: self.Sil())

        self.ui.pWipe.clicked.connect(lambda: self.Temizle())

        self.ui.pPN.clicked.connect(lambda: self.TerseCevir())
        ###
        self.ui.arti.clicked.connect(self.sayiyi_arrtir)
        self.ui.arti_2.clicked.connect(self.sayiyi_arrtir)
        self.ui.arti_3.clicked.connect(self.sayiyi_arrtir)
        self.ui.arti_4.clicked.connect(self.sayiyi_arrtir)
        self.ui.arti_5.clicked.connect(self.sayiyi_arrtir)
        self.ui.arti_6.clicked.connect(self.sayiyi_arrtir)
        self.ui.eksi.clicked.connect(self.eksilt)
        self.ui.eksi_2.clicked.connect(self.eksilt)
        self.ui.eksi_3.clicked.connect(self.eksilt)
        self.ui.eksi_4.clicked.connect(self.eksilt)
        self.ui.eksi_5.clicked.connect(self.eksilt)
        self.ui.eksi_6.clicked.connect(self.eksilt)
        self.ui.push_sifirla.clicked.connect(self.sifirla_hesapla)
        self.ui.push_cikis.clicked.connect(self.close)
        
    def isOperator(self,char):
        return char in ["+","-","/","*","%"];

    def isDigit(self,char):
        return not (char in ["+","-","/","*","%"]);

    def PushtButton(self,number):
        suanki_deger = self.ui.sonuc.text();

        if suanki_deger != "" and self.isOperator(number):
            son_karakter = suanki_deger[-1]

            if self.isOperator(son_karakter):
                return;

        self.ui.sonuc.setText(suanki_deger  + number)
        print(number)

    def Hesapla(self):
        suanki_deger = self.ui.sonuc.text();

        if suanki_deger != "":

            son_karakter = suanki_deger[-1]

            if self.isOperator(son_karakter):
                return;


        sonuc = eval(suanki_deger);

        self.ui.sonuc.setText(str(sonuc));

    def KaresiniAl(self):
        suanki_deger = self.ui.sonuc.text();

        sonuc = eval(suanki_deger)**2

        self.ui.sonuc.setText(str(sonuc));


    def KokunuAl(self):
        suanki_deger = self.ui.sonuc.text();

        sonuc = math.sqrt(eval(suanki_deger))

        self.ui.sonuc.setText(str(sonuc));

    def Temizle (self):
        self.ui.sonuc.setText("")

    def Sil (self):

        suanki_deger = self.ui.sonuc.text();

        if suanki_deger != "":
            suanki_deger = suanki_deger[:-1]
            self.ui.sonuc.setText(suanki_deger)
        else:
            return;

    def TerseCevir(self):
        suanki_deger = self.ui.sonuc.text();

        sonuc = eval(suanki_deger)

        if sonuc > 0:
            sonuc = -sonuc
        else:
            sonuc = abs(sonuc)

        self.ui.sonuc.setText(str(sonuc));

        
    def sayiyi_arrtir(self):
        sender = self.sender()
        if sender == self.ui.arti:
            line_edit = self.ui.lin_kiz
        elif sender == self.ui.arti_2:
            line_edit = self.ui.lin_ogl
        elif sender == self.ui.arti_3:
            line_edit = self.ui.lin_bur
        elif sender == self.ui.arti_4:
            line_edit = self.ui.lin_piz
        elif sender == self.ui.arti_5:
            line_edit = self.ui.lin_che
        elif sender == self.ui.arti_6:
            line_edit = self.ui.lin_ice

        if line_edit:
            value = int(line_edit.text())
            value += 1
            line_edit.setText(str(value))

    def eksilt(self):
        sender = self.sender()
        if sender == self.ui.eksi:
            line_edit = self.ui.lin_kiz
        elif sender == self.ui.eksi_2:
            line_edit = self.ui.lin_ogl
        elif sender == self.ui.eksi_3:
            line_edit = self.ui.lin_bur
        elif sender == self.ui.eksi_4:
            line_edit = self.ui.lin_piz
        elif sender == self.ui.eksi_5:
            line_edit = self.ui.lin_che
        elif sender == self.ui.eksi_6:
            line_edit = self.ui.lin_ice

        if line_edit:
            value = int(line_edit.text())
            value -= 1
            line_edit.setText(str(value))

    def random_sayi_yaz(self):

        random_sayi = random.randint(1000, 2000)
        self.ui.lin_sip.setText(str(random_sayi))
    
    def fiyat_listesini_goster(self):
        if self.fiyat_liste_widget is None:
            self.fiyat_liste_widget = Fiyat_liste()
        self.fiyat_liste_widget.show()

    def topla(self):
            kizartma = int(self.ui.lin_kiz.text())
            ogle_yemegi = int(self.ui.lin_ogl.text())
            burger = int(self.ui.lin_bur.text())
            pizza = int(self.ui.lin_piz.text())
            cheese_burger = int(self.ui.lin_che.text())
            icecekler = int(self.ui.lin_ice.text())

            dosya_yolu = ("fiyat_listesi\\flist.txt")

            fiyatlar = {}
            with open(dosya_yolu, "r") as file:
                lines = file.readlines()
                fiyatlar = dict(line.strip().split(":") for line in lines)

            toplam_fiyat = (
                kizartma * float(fiyatlar.get("Kizartma", 0)) +
                ogle_yemegi * float(fiyatlar.get("Ogle_Yemegi", 0)) +
                burger * float(fiyatlar.get("Burger", 0)) +
                pizza * float(fiyatlar.get("Pizza", 0)) +
                cheese_burger * float(fiyatlar.get("Cheese Burger", 0)) +
                icecekler * float(fiyatlar.get("Icecekler", 0))
            )

            self.ui.lin_fiy.setText(str(toplam_fiyat))
            self.ui.lin_ser.setText(str((toplam_fiyat*1)/10))
            self.ui.lin_kdv.setText(str(((toplam_fiyat*0.10)+toplam_fiyat)*0.18))
            self.ui.lin_alt.setText(str(((toplam_fiyat*0.10)+((toplam_fiyat+(toplam_fiyat*0.10))*0.18))))
            self.ui.lin_top.setText(str((((toplam_fiyat*0.10)+((toplam_fiyat+(toplam_fiyat*0.10))*0.18)))+toplam_fiyat))



    def get_label_name(self, line_edit_name):
        label_names = {"kiz": "Kızartma", "ogl": "Oğlak", "bur": "Burger", "piz": "Pizza", "che": "Cheeseburger", "ice": "İçecek", "fiy": "Fiyat", "ser": "Servis", "kdv": "KDV", "alt": "Alış Fiyatı", "top": "Toplam Fiyat", "sip": "Sipariş No"}
        return label_names.get(line_edit_name, line_edit_name.capitalize())

    def kayit_ekle(self):
        with open("fiyat_listesi\\log.txt", "a", encoding="utf-8") as file:
            for line_edit_name in ["kiz", "ogl", "bur", "piz", "che", "ice", "fiy", "ser", "kdv", "alt", "top", "sip"]:
                label_name = self.get_label_name(line_edit_name)
                value = round(float(getattr(self.ui, f'lin_{line_edit_name}').text()), 2)
                file.write(f" --- {label_name}: {value}")
            file.write("\n\n")
    
    def sifirla_hesapla(self):

        for line_edit_name in ["kiz", "ogl", "bur", "piz", "che", "ice", "fiy", "ser", "kdv", "alt", "top", "sip"]:
            getattr(self.ui, f"lin_{line_edit_name}").setText("0")

    
class Fiyat_liste(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Fiyatlar()
        self.ui.setupUi(self)
        self.load_prices()
        self.ui.push_cikis.clicked.connect(self.close)
        self.ui.push_kaydet.clicked.connect(self.close)

        self.ui.push_kaydet.clicked.connect(self.save_prices)

    def load_prices(self):
        try:
            with open('fiyat_listesi/flist.txt', 'r') as file:
                prices = file.read().splitlines()
                for price, line_edit in zip(prices, [self.ui.lin_kiz, self.ui.lin_ogl, self.ui.lin_bur, self.ui.lin_piz, self.ui.lin_che, self.ui.lin_ice]):
                    _, numeric_price = price.split(':')
                    line_edit.setText(numeric_price.strip())
        except FileNotFoundError:
            print("flist.txt not found. Make sure the file exists in the specified directory.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_prices(self):
        
        new_prices = [line_edit.text() for line_edit in [self.ui.lin_kiz, self.ui.lin_ogl, self.ui.lin_bur, self.ui.lin_piz, self.ui.lin_che, self.ui.lin_ice]]
            
        with open('fiyat_listesi/flist.txt', 'w') as file:
            for label, new_price in zip(['Kizartma', 'Ogle_Yemegi', 'Burger','Pizza', 'Cheese Burger', 'Icecekler'], new_prices):
                file.write(f"{label}: {new_price}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Restorant_takipsis()
    widget.show()
    sys.exit(app.exec())
