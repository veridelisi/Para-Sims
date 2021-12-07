"""
TCMB, Hazineye döviz satıyor.
Botaş bu dövizi Hazineden satın alıyor.
Botaş ödemesini yapıyor.

Dr. Engin YILMAZ
07/12/2021

@vefinans hocama teşekkür ederim.


"""

from abcFinance import Ledger

from IPython.core.display import SVG
from IPython.display import display_svg

def print_money_stocks():
    # Her müşterinin hesabında bulunan mevduat tutarı,banka parası değişkenine ekleniyor.
    Banka_Parasi = Xbankasi.get_balance('Müşteri A Mevduatı')[1]
    Banka_Parasi += Xbankasi.get_balance('Müşteri B Mevduatı')[1]
    Banka_Parasi += Xbankasi.get_balance('Müşteri C Mevduatı')[1]
   
    
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
  
    if len(args)==0:
        args = ("b1","b2","pA","pB","pC","cb","ts")
    if "b1" in args and Xbankasi.get_total_assets() > 0: display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
    if "b2" in args and Ybankasi.get_total_assets() > 0: display_svg(SVG(Ybankasi.draw_balance_sheet("Banka Y", width=500)))
    if "pA" in args and MusteriA.get_total_assets() > 0: display_svg(SVG(MusteriA.draw_balance_sheet("Müşteri A", width=500)))
    if "cb" in args and Merkez_Bankasi.get_total_assets() > 0: display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))
   
    print_money_stocks()
    
#  Her aktörün bilançosunun artık hesabı,(Varlık-Yükümlülük),Sermaye olarak adlandırılıyor.
Xbankasi = Ledger(residual_account_name="Sermaye")
MusteriA = Ledger(residual_account_name="Sermaye")
Merkez_Bankasi = Ledger(residual_account_name="Sermaye")



#  Bankaların varlık ve yükümlülük kalemleri tanımlanıyor.
Xbankasi.make_asset_accounts(['Nakit','Devlet Tahvili','Kredi','Rezervler','Bankalararası Alacak','Dış Varlıklar','TCMBdeki Döviz Rezervleri'])
Xbankasi.make_liability_accounts(['Botaş Mevduatı/TL','Botaş Mevduatı/$','Kamu Mevduatı/TL','Kamu Mevduatı/$','Müşteri B Mevduatı','Müşteri C Mevduatı','Bankalararası Borç', 'Tahvil İhracı', 'Merkez Bankasına Borçlar'])


# Müşterilerin varlık ve yükümlülük kalemleri tanımlanıyor.
MusteriA.make_asset_accounts(['Nakit','Mevduat/TL','Mevduat/$','Banka Tahvili'])
MusteriA.make_liability_accounts(['Kredi'])


# Merkez Bankasının varlık ve yükümlülük kalemleri tanımlanıyor.
Merkez_Bankasi.make_asset_accounts(['Dış Varlıklar','İç Varlıklar','Degerleme','APİ'])
Merkez_Bankasi.make_liability_accounts(['Hazinenin Döviz Rezervleri','Emisyon','Kamu Mevduatı/TL','Kamu Mevduatı/$','Rezervler'])


#Başlangıç
MusteriA.book(debit=[('Mevduat/TL',100)],credit=[('Kredi',100)])
Xbankasi.book(debit=[('Rezervler',100)],credit=[('Kamu Mevduatı/$',100)])
Xbankasi.book(debit=[('Kredi',100)],credit=[('Botaş Mevduatı/TL',100)])
Merkez_Bankasi.book(debit=[('Dış Varlıklar',100)],credit=[('Rezervler',100)])
Merkez_Bankasi.book(debit=[('İç Varlıklar',100)],credit=[('Kamu Mevduatı/TL',100)])
Merkez_Bankasi.book(debit=[('Dış Varlıklar',100)],credit=[('Kamu Mevduatı/$',100)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Botaş", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))



"""
TCMB, Hazine'ye döviz satıyor. Hazine ödemeyi TL cinsinden yapıyor. 
Döviz, Hazinenin kamu bankasındaki hesabına geçiyor.
"""
#Kod-1
Merkez_Bankasi.book(debit=[('Kamu Mevduatı/TL',50)],credit=[('Dış Varlıklar',50)])
Xbankasi.book(debit=[('Dış Varlıklar',50)],credit=[('Kamu Mevduatı/$',50)])

display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))



"""
BOTAŞ, TL karşılığında Hazineden bu dövizi alıyor.
İki kurumda aynı bankayla çalışıyor. 
"""
#Kod-2
Xbankasi.book(debit=[('Kamu Mevduatı/$',50)],credit=[('Kamu Mevduatı/TL',50)])
Xbankasi.book(debit=[('Botaş Mevduatı/TL',50)],credit=[('Botaş Mevduatı/$',50)])
MusteriA.book(debit=[('Mevduat/$',50)],credit=[('Mevduat/TL',50)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Botaş", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))



"""
BOTAŞ, döviz ödemesini yapıyor. 
"""
#Kod-3

Xbankasi.book(debit=[('Botaş Mevduatı/$',50)],credit=[('Dış Varlıklar',50)])
MusteriA.book(debit=[('Sermaye',50)],credit=[('Mevduat/$',50)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Botaş", width=500)))





