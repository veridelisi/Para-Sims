"""
    veridelisi/para üzerinde Kod0'ı çalıştırın.
    Kod1 üzerinde, Tüm banka ve müşterilere "Altın" değişkenini ekleyin. Varlık mı yükümlülük mü?
    Kod1 üzerinde, açılış bilançolarının tanımlandığı yerde EK olarak Banka X ve Banka Y'ye 20 TL değerinde Altın ekleyin.
    Sizin yazacağınız yeni kodlar üzerinde, 
            Kod2 : Müşteri A elindeki nakitin hepsini Banka X'e yatırsın.
            Kod3 : Müşteri A, 5 TL değerinde altını Banka X'den alsın.
            Kod4 : Müşteri A, 5 TL değerinde altını Banka Y'ye satsın.
            
            20.11.2020
            Engin YILMAZ
            Ankara
            
            Kodu ilk cevaplayan : https://github.com/belgirgin
"""            
            
#kod0
pip install abcFinance

#kod1
from abcFinance import Ledger

from IPython.core.display import SVG
from IPython.display import display_svg

def print_money_stocks():
    # Her müşterinin hesabında bulunan mevduat tutarı,banka parası değişkenine ekleniyor.
    Banka_Parasi = Xbankasi.get_balance('Müşteri A Mevduatı')[1]
    Banka_Parasi += Xbankasi.get_balance('Müşteri B Mevduatı')[1]
    Banka_Parasi += Xbankasi.get_balance('Müşteri C Mevduatı')[1]
    Banka_Parasi += Ybankasi.get_balance('Müşteri A Mevduatı')[1]
    Banka_Parasi += Ybankasi.get_balance('Müşteri B Mevduatı')[1]
    Banka_Parasi += Ybankasi.get_balance('Müşteri C Mevduatı')[1]
    
    # Her müşterinin ve bankaların varlığında bulunan Nakit tutarı merkez bankası parası değişkenine ekleniyor.
    Merkez_Bankasi_Parasi = MusteriA.get_balance('Nakit')[1]
    Merkez_Bankasi_Parasi += MusteriB.get_balance('Nakit')[1]
    Merkez_Bankasi_Parasi += MusteriC.get_balance('Nakit')[1]
    Merkez_Bankasi_Parasi += Xbankasi.get_balance('Nakit')[1]
    Merkez_Bankasi_Parasi += Ybankasi.get_balance('Nakit')[1]
    
    print("Banka Parası:",Banka_Parasi)
    if Merkez_Bankasi_Parasi>0:
        print("Merkez Bankası Parası:",Merkez_Bankasi_Parasi)
        
    # Banka parası ile merkez bankası parasının toplamı, para arzı  değişkenini veriyor.
    print("Para Arzı:",Banka_Parasi+Merkez_Bankasi_Parasi)

def print_balance_sheets_and_money_stocks(*args):
    MusteriA.book_end_of_period()
    MusteriB.book_end_of_period()
    MusteriC.book_end_of_period()
    
    if len(args)==0:
        args = ("b1","b2","pA","pB","pC","cb")
    if "b1" in args and Xbankasi.get_total_assets() > 0: display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
    if "b2" in args and Ybankasi.get_total_assets() > 0: display_svg(SVG(Ybankasi.draw_balance_sheet("Banka Y", width=500)))
    if "pA" in args and MusteriA.get_total_assets() > 0: display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))
    if "pB" in args and MusteriB.get_total_assets() > 0: display_svg(SVG(MusteriB.draw_balance_sheet("Müşteri B", width=500)))
    if "pC" in args and MusteriC.get_total_assets() > 0: display_svg(SVG(MusteriC.draw_balance_sheet("Müşteri C", width=500)))
    if "cb" in args and Merkez_Bankasi.get_total_assets() > 0: display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))
        
    print_money_stocks()
    
#  Her aktörün bilançosunun artık hesabı,(Varlık-Yükümlülük),Sermaye olarak adlandırılıyor.
Xbankasi = Ledger(residual_account_name="Sermaye")
Ybankasi = Ledger(residual_account_name="Sermaye")
MusteriA = Ledger(residual_account_name="Sermaye")
MusteriB = Ledger(residual_account_name="Sermaye")
MusteriC = Ledger(residual_account_name="Sermaye")
Merkez_Bankasi = Ledger(residual_account_name="Sermaye")


#  Bankaların varlık ve yükümlülük kalemleri tanımlanıyor.
Xbankasi.make_asset_accounts(['Nakit','Kredi','Rezervler','Bankalararası Alacak', 'Altın'])
Xbankasi.make_liability_accounts(['Müşteri A Mevduatı','Müşteri B Mevduatı','Müşteri C Mevduatı','Bankalararası Borç', 'Tahvil İhracı', 'Merkez Bankasına Borçlar'])
Ybankasi.make_asset_accounts(['Nakit','Kredi','Rezervler','Bankalararası Alacak','Altın'])
Ybankasi.make_liability_accounts(['Müşteri A Mevduatı','Müşteri B Mevduatı','Müşteri C Mevduatı','Bankalararası Borç', 'Tahvil İhracı', 'Merkez Bankasına Borçlar'])

# Müşterilerin varlık ve yükümlülük kalemleri tanımlanıyor.
MusteriA.make_asset_accounts(['Nakit','Mevduat','Banka Tahvili','Altın'])
MusteriA.make_liability_accounts(['Kredi'])
MusteriB.make_asset_accounts(['Nakit','Mevduat','Banka Tahvili','Altın'])
MusteriB.make_liability_accounts(['Kredi'])
MusteriC.make_asset_accounts(['Nakit','Mevduat','Banka Tahvili','Altın'])
MusteriC.make_liability_accounts(['Kredi'])


# Merkez Bankasının varlık ve yükümlülük kalemleri tanımlanıyor.
Merkez_Bankasi.make_asset_accounts(['Devlet Tahvili','Bankalara Verilen Krediler'])
Merkez_Bankasi.make_liability_accounts(['Nakit','Rezervler'])


#Başlangıç
Xbankasi.book(debit=[('Nakit',50), ('Altın',20)],credit=[('Sermaye',70)])
Ybankasi.book(debit=[('Nakit',50), ('Altın',20)],credit=[('Sermaye',70)])
MusteriA.book(debit=[('Nakit',100),('Altın',0)],credit=[('Sermaye',100)])
Merkez_Bankasi.book(debit=[('Devlet Tahvili',200)],credit=[('Nakit',200)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Ybankasi.draw_balance_sheet("Banka Y", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))

#Başlangıç- Para Arzı
print_money_stocks()



#kod2
#Müşteri A, Banka X'e Nakit Para Yatırır
Xbankasi.book(debit=[('Nakit',100),],credit=[('Müşteri A Mevduatı',100)])
MusteriA.book(debit=[('Mevduat',100)],credit=[('Nakit',100)])
#bilanço
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))
#paraarzı
print_money_stocks()

#kod3
#Müşteri A, Banka X'den altın alır
Xbankasi.book(debit=[('Müşteri A Mevduatı',5)],credit=[('Altın',5)])
MusteriA.book(debit=[('Altın',5)],credit=[('Mevduat',5)])
#bilanço
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))
#paraarzı
print_money_stocks()

#kod4
#Müşteri A, Banka Y'ye altın satar
Ybankasi.book(debit=[('Altın',5)],credit=[('Nakit',5)])
MusteriA.book(debit=[('Nakit',5)],credit=[('Altın',5)])
#Bilanço
display_svg(SVG(Ybankasi.draw_balance_sheet("Banka Y", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))

#paraarzı
print_money_stocks()             
