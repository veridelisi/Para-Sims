"""
https://www.coppolacomment.com/2021/09/jp-morgans-coffee-machine.html
Frances Coppola
03.09.2021


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
    Banka_Parasi += Ybankasi.get_balance('Müşteri A Mevduatı')[1]
    
    
    # Her müşterinin ve bankaların varlığında bulunan Nakit tutarı merkez bankası parası değişkenine ekleniyor.
    Merkez_Bankasi_Parasi = MusteriA.get_balance('Nakit')[1]
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
        args = ("b1","b2","pA")
    if "b1" in args and Xbankasi.get_total_assets() > 0: display_svg(SVG(Xbankasi.draw_balance_sheet("JP Morgan", width=500)))
    if "b2" in args and Ybankasi.get_total_assets() > 0: display_svg(SVG(Ybankasi.draw_balance_sheet("Citibank", width=500)))
    if "pA" in args and MusteriA.get_total_assets() > 0: display_svg(SVG(MusteriA.draw_balance_sheet("Goodlife", width=500)))

        
    print_money_stocks()
    
#  Her aktörün bilançosunun artık hesabı,(Varlık-Yükümlülük),Sermaye olarak adlandırılıyor.
Xbankasi = Ledger(residual_account_name="Sermaye")
Ybankasi = Ledger(residual_account_name="Sermaye")
MusteriA = Ledger(residual_account_name="Sermaye")



#  Bankaların varlık ve yükümlülük kalemleri tanımlanıyor.
Xbankasi.make_asset_accounts(['Fixed Assets','Reserves'])
Xbankasi.make_liability_accounts(['Goodlife Deposit','Equity'])
Ybankasi.make_asset_accounts(['Reserves'])
Ybankasi.make_liability_accounts(['Goodlife Deposit','Equity'])

# Müşterilerin varlık ve yükümlülük kalemleri tanımlanıyor.
MusteriA.make_asset_accounts(['Fixed Assets','Goodlife Deposit'])
MusteriA.make_liability_accounts(['Equity'])


#Başlangıç
Xbankasi.book(debit=[('Reserves',100)],credit=[('Equity',100)])
Ybankasi.book(debit=[('Reserves',100)],credit=[('Equity',100)])
MusteriA.book(debit=[('Fixed Assets',100)],credit=[('Equity',100)])


#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("JP Morgan", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Goodlife", width=500)))
display_svg(SVG(Ybankasi.draw_balance_sheet("Citibank", width=500)))


#kod2
#Başlangıç
Xbankasi.book(debit=[('Fixed Assets',100)],credit=[('Goodlife Deposit',100)])
MusteriA.book(debit=[('Goodlife Deposit',100)],credit=[('Fixed Assets',100)])


#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("JP Morgan", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Goodlife", width=500)))

#kod3

MusteriA.book(debit=[('Fixed Assets',100)],credit=[('Goodlife Deposit',100)])
Xbankasi.book(debit=[('Goodlife Deposit',100)],credit=[('Fixed Assets',100)])



#kod4

#Başlangıç
Xbankasi.book(debit=[('Fixed Assets',100)],credit=[('Reserves',100)])
MusteriA.book(debit=[('Goodlife Deposit',100)],credit=[('Fixed Assets',100)])
Ybankasi.book(debit=[('Reserves',100)],credit=[('Goodlife Deposit',100)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("JP Morgan", width=500)))
display_svg(SVG(MusteriA.draw_balance_sheet("Goodlife", width=500)))
display_svg(SVG(Ybankasi.draw_balance_sheet("Citibank", width=500)))
