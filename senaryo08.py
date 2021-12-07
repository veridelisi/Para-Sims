"""
@vefinans hocamızın web sayfasındaki anlatıları kod üzerinden tekrar edilmiştir.
https://paravefinans595106776.wordpress.com/

Dr. Engin YILMAZ
14.03.2021
Ankara
"""

pip install abcFinance

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
        args = ("b1","b2","pA","pB","pC","cb","ts")
    if "b1" in args and Xbankasi.get_total_assets() > 0: display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
    if "b2" in args and Ybankasi.get_total_assets() > 0: display_svg(SVG(Ybankasi.draw_balance_sheet("Banka Y", width=500)))
    if "pA" in args and MusteriA.get_total_assets() > 0: display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))
    if "pB" in args and MusteriB.get_total_assets() > 0: display_svg(SVG(MusteriB.draw_balance_sheet("Müşteri B", width=500)))
    if "pC" in args and MusteriC.get_total_assets() > 0: display_svg(SVG(MusteriC.draw_balance_sheet("Müşteri C", width=500)))
    if "cb" in args and Merkez_Bankasi.get_total_assets() > 0: display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))
    if "ts" in args and Hazine.get_total_assets() > 0: display_svg(SVG(Hazine.draw_balance_sheet("Hazine", width=500)))  # Bu satır eklendi.  
    print_money_stocks()
    
#  Her aktörün bilançosunun artık hesabı,(Varlık-Yükümlülük),Sermaye olarak adlandırılıyor.
Xbankasi = Ledger(residual_account_name="Sermaye")
Ybankasi = Ledger(residual_account_name="Sermaye")
MusteriA = Ledger(residual_account_name="Sermaye")
MusteriB = Ledger(residual_account_name="Sermaye")
MusteriC = Ledger(residual_account_name="Sermaye")
Merkez_Bankasi = Ledger(residual_account_name="Sermaye")
Hazine = Ledger(residual_account_name="Sermaye")  # Bu satır eklendi.


#  Bankaların varlık ve yükümlülük kalemleri tanımlanıyor.
Xbankasi.make_asset_accounts(['Nakit','Devlet Tahvili','Kredi','Rezervler','Bankalararası Alacak','Dış Varlıklar','TCMBdeki Döviz Rezervleri'])
Xbankasi.make_liability_accounts(['Müşteri A Mevduatı','Müşteri B Mevduatı','Müşteri C Mevduatı','Bankalararası Borç', 'Tahvil İhracı', 'Merkez Bankasına Borçlar'])
Ybankasi.make_asset_accounts(['Nakit','Kredi','Rezervler','Bankalararası Alacak'])
Ybankasi.make_liability_accounts(['Müşteri A Mevduatı','Müşteri B Mevduatı','Müşteri C Mevduatı','Bankalararası Borç', 'Tahvil İhracı', 'Merkez Bankasına Borçlar'])

# Müşterilerin varlık ve yükümlülük kalemleri tanımlanıyor.
MusteriA.make_asset_accounts(['Nakit','Mevduat','Banka Tahvili'])
MusteriA.make_liability_accounts(['Kredi'])
MusteriB.make_asset_accounts(['Nakit','Mevduat','Banka Tahvili'])
MusteriB.make_liability_accounts(['Kredi'])
MusteriC.make_asset_accounts(['Nakit','Mevduat','Banka Tahvili'])
MusteriC.make_liability_accounts(['Kredi'])

# Hazinenin varlık ve yükümlülük kalemleri tanımlanıyor.
Hazine.make_asset_accounts(['Kamu Mevduatı','Dış Varlıklar'])  # Bu satır eklendi.
Hazine.make_liability_accounts(['Devlet Tahvili','Dış Borçlar'])  # Bu satır eklendi.


# Merkez Bankasının varlık ve yükümlülük kalemleri tanımlanıyor.
Merkez_Bankasi.make_asset_accounts(['Dış Varlıklar','İç Varlıklar','Degerleme','APİ'])
Merkez_Bankasi.make_liability_accounts(['Bankaların Döviz Rezervleri','Hazinenin Döviz Rezervleri','Emisyon','Kamu Mevduatı','Rezervler'])



#Başlangıç
Xbankasi.book(debit=[('Dış Varlıklar',50)],credit=[('Sermaye',50)])
Xbankasi.book(debit=[('Devlet Tahvili',50)],credit=[('Sermaye',50)])
Merkez_Bankasi.book(debit=[('Dış Varlıklar',50)],credit=[('Sermaye',50)])


#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))



"""
Kod1
https://paravefinans595106776.wordpress.com/2021/03/05/
bolum-ii-para-politikasi-islemlerinden-alacaklar-ve-borclar/

"""


#Kod1

Xbankasi.book(debit=[('Rezervler',200)],credit=[('Merkez Bankasına Borçlar',200)])
Merkez_Bankasi.book(debit=[('APİ',200)],credit=[('Rezervler',200)])

#Kod1- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))



"""
#Kod2
https://paravefinans595106776.wordpress.com/2021/03/05/bolum-iii-emisyon/

"""

#Kod2
Xbankasi.book(debit=[('Nakit',30)],credit=[('Rezervler',30)])
Merkez_Bankasi.book(debit=[('Rezervler',30)],credit=[('Emisyon',30)])

#Kod2- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))


"""
#Kod3
https://paravefinans595106776.wordpress.com/2021/03/05/bolum-iii-emisyon/

"""

#Kod3-1
Xbankasi.book(debit=[('Nakit',20)],credit=[('Rezervler',20)])
Merkez_Bankasi.book(debit=[('Rezervler',20)],credit=[('Emisyon',20)])

#Kod3-1- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))

print("---------------------------------------------------------")

"""
#Kod3-2
https://paravefinans595106776.wordpress.com/2021/03/05/bolum-iv-zorunlu-karsiliklar/

"""

#Kod3-2
Xbankasi.book(debit=[('TCMBdeki Döviz Rezervleri',20)],credit=[('Dış Varlıklar',20)])
Merkez_Bankasi.book(debit=[('Dış Varlıklar',20)],credit=[('Bankaların Döviz Rezervleri',20)])

#Kod3-2- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))




"""
#Kod4
https://paravefinans595106776.wordpress.com/2021/03/05/bolum-v-reeskont-kredileri/
Kredinin alınması

"""

#Kod4-1
Xbankasi.book(debit=[('Rezervler',30)],credit=[('Merkez Bankasına Borçlar',30)])
Merkez_Bankasi.book(debit=[('İç Varlıklar',30)],credit=[('Rezervler',30)])


#Kod4-2- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))

print("---------------------------------------------------------")


"""
#Kod4-2
https://paravefinans595106776.wordpress.com/2021/03/05/bolum-v-reeskont-kredileri/
Kredinin Ödenmesi
"""

#Kod4-2
Xbankasi.book(debit=[('Merkez Bankasına Borçlar',30)],credit=[('Dış Varlıklar',30)])
Merkez_Bankasi.book(debit=[('Dış Varlıklar',30)],credit=[('İç Varlıklar',30)])

#Kod4-2- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))



"""
#Kod5
https://paravefinans595106776.wordpress.com/2021/03/05/bolum-vi-tahvil-alimi-ve-kar-dagitimi/

"""

#Kod5
Xbankasi.book(debit=[('Rezervler',30)],credit=[('Devlet Tahvili',30)])
Merkez_Bankasi.book(debit=[('İç Varlıklar',30)],credit=[('Rezervler',30)])

#Kod5- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))






"""
#Kod6
https://paravefinans595106776.wordpress.com/2021/03/05/bolum-vii-hazine-borclanmasi-ve-harcamalari/

"""


#Kod6-1

Xbankasi.book(debit=[('Rezervler',50)],credit=[('Merkez Bankasına Borçlar',50)])
Merkez_Bankasi.book(debit=[('APİ',50)],credit=[('Rezervler',50)])

#Kod6-1- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))

print("---------------------------------------------")


#Kod6-2
Hazine.book(debit=[('Kamu Mevduatı',50)],credit=[('Devlet Tahvili',50)])
Xbankasi.book(debit=[('Devlet Tahvili',50)],credit=[('Rezervler',50)])
Merkez_Bankasi.book(debit=[('Rezervler',50)],credit=[('Kamu Mevduatı',50)])

#Kod6-2- Bilançolar
display_svg(SVG(Hazine.draw_balance_sheet("Hazine", width=500)))
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))

print("--------------------------------------------")
#Kod6-3
MusteriA.book(debit=[('Mevduat',50)],credit=[('Sermaye',50)])
Xbankasi.book(debit=[('Rezervler',50)],credit=[('Müşteri A Mevduatı',50)])
Merkez_Bankasi.book(debit=[('Kamu Mevduatı',50)],credit=[('Rezervler',50)])

#Kod6-3- Bilançolar
display_svg(SVG(MusteriA.draw_balance_sheet("Musteri A", width=500)))
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))

print("---------------------------------------------")

#Kod6-4

Xbankasi.book(debit=[('Merkez Bankasına Borçlar',50)],credit=[('Rezervler',50)])
Merkez_Bankasi.book(debit=[('Rezervler',50)],credit=[('APİ',50)])

#Kod6-4- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))


