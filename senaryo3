"""Hazine’nin TCMB’den Borçlanması""

#kod0
pip install abcFinance

#kod1 Hazine’nin TCMB’den Borçlanması 

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
        args = ("b1","b2","pA","pB","pC","cb","ts") #ts ekledik.
    if "b1" in args and Xbankasi.get_total_assets() > 0: display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
    if "b2" in args and Ybankasi.get_total_assets() > 0: display_svg(SVG(Ybankasi.draw_balance_sheet("Banka Y", width=500)))
    if "pA" in args and MusteriA.get_total_assets() > 0: display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))
    if "pB" in args and MusteriB.get_total_assets() > 0: display_svg(SVG(MusteriB.draw_balance_sheet("Müşteri B", width=500)))
    if "pC" in args and MusteriC.get_total_assets() > 0: display_svg(SVG(MusteriC.draw_balance_sheet("Müşteri C", width=500)))
    if "cb" in args and Merkez_Bankasi.get_total_assets() > 0: display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))
    if "ts" in args and Hazine.get_total_assets() > 0: display_svg(SVG(Hazine.draw_balance_sheet("Hazine", width=500)))  #bu satırı ekledik.
    print_money_stocks()
    
#  Her aktörün bilançosunun artık hesabı,(Varlık-Yükümlülük),Sermaye olarak adlandırılıyor.
Xbankasi = Ledger(residual_account_name="Sermaye")
Ybankasi = Ledger(residual_account_name="Sermaye")
MusteriA = Ledger(residual_account_name="Sermaye")
MusteriB = Ledger(residual_account_name="Sermaye")
MusteriC = Ledger(residual_account_name="Sermaye")
Merkez_Bankasi = Ledger(residual_account_name="Sermaye")
Hazine = Ledger(residual_account_name="Sermaye") #Bu satırı ekledik.

#  Bankaların varlık ve yükümlülük kalemleri tanımlanıyor.
Xbankasi.make_asset_accounts(['Nakit','Kredi','Rezervler','Bankalararası Alacak','Devlet Tahvili'])  # Devlet tahvili eklendi.
Xbankasi.make_liability_accounts(['Müşteri A Mevduatı','Müşteri B Mevduatı','Müşteri C Mevduatı','Bankalararası Borç', 'Tahvil İhracı', 'Merkez Bankasına Borçlar'])
Ybankasi.make_asset_accounts(['Nakit','Kredi','Rezervler','Bankalararası Alacak','Devlet Tahvili']) # Devlet tahvili eklendi.
Ybankasi.make_liability_accounts(['Müşteri A Mevduatı','Müşteri B Mevduatı','Müşteri C Mevduatı','Bankalararası Borç', 'Tahvil İhracı', 'Merkez Bankasına Borçlar'])

# Müşterilerin varlık ve yükümlülük kalemleri tanımlanıyor.
MusteriA.make_asset_accounts(['Nakit','Mevduat','Banka Tahvili'])
MusteriA.make_liability_accounts(['Kredi'])
MusteriB.make_asset_accounts(['Nakit','Mevduat','Banka Tahvili'])
MusteriB.make_liability_accounts(['Kredi'])
MusteriC.make_asset_accounts(['Nakit','Mevduat','Banka Tahvili'])
MusteriC.make_liability_accounts(['Kredi'])


# Merkez Bankasının varlık ve yükümlülük kalemleri tanımlanıyor.
Merkez_Bankasi.make_asset_accounts(['Devlet Tahvili','Bankalara Verilen Krediler'])
Merkez_Bankasi.make_liability_accounts(['Nakit','Rezervler','Kamu Mevduatı'])  # Kamu Mevduatı eklendi.

# Hazinenin varlık ve yükümlülük kalemleri tanımlanıyor.
Hazine.make_asset_accounts(['Kamu Mevduatı'])      #Bu satırı ekledik.
Hazine.make_liability_accounts(['Devlet Tahvili']) #Bu satırı ekledik.


#Hazine’nin TCMB’den Borçlanması İşlemi
Hazine.book(debit=[('Kamu Mevduatı',100)],credit=[('Devlet Tahvili',100)])         #Bu satırı ekledik.
Merkez_Bankasi.book(debit=[('Devlet Tahvili',100)],credit=[('Kamu Mevduatı',100)]) #Bu satırı ekledik.

#Başlangıç- Bilançolar
display_svg(SVG(Hazine.draw_balance_sheet("Hazine", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))

#Başlangıç- Para Arzı
print_money_stocks()

#kod2 Hazine Müşteri A'ya ödeme yapar

#Hazine Müşteri A'ya ödeme yapar.
Hazine.book(debit=[('Sermaye',100)],credit=[('Kamu Mevduatı',100)])
Merkez_Bankasi.book(debit=[('Kamu Mevduatı',100)],credit=[('Rezervler',100)])
Xbankasi.book(debit=[('Rezervler',100)],credit=[('Müşteri A Mevduatı',100)])
MusteriA.book(debit=[('Mevduat',100)],credit=[('Sermaye',100)])


#Bilançolar
display_svg(SVG(Hazine.draw_balance_sheet("Hazine", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))


#Para Arzı
print_money_stocks()
