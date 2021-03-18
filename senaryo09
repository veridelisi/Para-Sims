"""
Vatandaş vergisini ödüyor. Mevduat, vatandaşın bankasından Ziraat Bankasına (Banka X) gidiyor.
Ziraat Bankası, bu mevduatı TCMB'ye aktarıyor. Mevduat, kamu mevduatı oluyor.
Hazine, kamu mevduatını harcıyor.

Dr. Engin YILMAZ
18/03/2021

@vefinans hocama teşekkür ederim.


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
Xbankasi.make_liability_accounts(['Müşteri A Mevduatı','Kamu Mevduatı','Müşteri B Mevduatı','Müşteri C Mevduatı','Bankalararası Borç', 'Tahvil İhracı', 'Merkez Bankasına Borçlar'])
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
Merkez_Bankasi.make_liability_accounts(['Hazinenin Döviz Rezervleri','Emisyon','Kamu Mevduatı','Rezervler'])

#Başlangıç
MusteriA.book(debit=[('Mevduat',50)],credit=[('Kredi',50)])
Ybankasi.book(debit=[('Kredi',50)],credit=[('Müşteri A Mevduatı',50)])
Ybankasi.book(debit=[('Rezervler',50)],credit=[('Merkez Bankasına Borçlar',50)])
Xbankasi.book(debit=[('Rezervler',50)],credit=[('Merkez Bankasına Borçlar',50)])
Merkez_Bankasi.book(debit=[('APİ',100)],credit=[('Rezervler',100)])


#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Ybankasi.draw_balance_sheet("Banka Y", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))

"""
Müşteri A, 30 TL vergi ödemesini Banka Y üzeriden yapıyor.
Banka Y'den çıkan mevduat, Ziraat Bankasına (Banka X) gidiyor.



"""


#Kod-1
MusteriA.book(debit=[('Sermaye',30)],credit=[('Mevduat',30)])
Ybankasi.book(debit=[('Müşteri A Mevduatı',30)],credit=[('Rezervler',30)])
Xbankasi.book(debit=[('Rezervler',30)],credit=[('Müşteri A Mevduatı',30)])

display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Ybankasi.draw_balance_sheet("Banka Y", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))

"""
Ziraat Bankası (Banka X), bu mevduatı TCMB'ye gönderiyor.
Rezervler azalıp, kamu mevduatı artıyor.

"""

#Kod-2

Xbankasi.book(debit=[('Müşteri A Mevduatı',30)],credit=[('Rezervler',30)])
Merkez_Bankasi.book(debit=[('Rezervler',30)],credit=[('Kamu Mevduatı',30)])

display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))

"""
Hazine, kamu mevduatını harcıyor. Müşteri A'nın tüm vatandaşları temsil ettiğini düşünün.
Devlet, kamu harcamasını buradan yapıyor.

"""


#Kod-3

MusteriA.book(debit=[('Mevduat',30)],credit=[('Sermaye',30)])
Merkez_Bankasi.book(debit=[('Kamu Mevduatı',30)],credit=[('Rezervler',30)])
Xbankasi.book(debit=[('Rezervler',30)],credit=[('Müşteri A Mevduatı',30)])


display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))







