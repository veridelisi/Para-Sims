
#https://x.com/KeloglanBM/status/1816188063615442954

"""
Başlayacağı iddia edilen “sterilizasyon amaçlı” yeni swap işleminin TCMB ve ilgili banka bilançoları üzerindeki etkisi dört sütundan oluşan Şekil 1’in ilk iki sütununda gösterildiği şekilde olacak:
i)TCMB işlemin ilk bacağında (haberde valör diye geçiyor) bankalara döviz (haberde altının da kullanılabileceği yazıyor) verecek ve karşılığında bankaların TCMB’de tuttukları rezerv paraları azalacak. Böylece TCMB bilançosunun aktifinde dış varlıklar azalırken yani TCMB brüt rezervleri düşerken pasifinde ise rezerv para azalacak. Bu ilk bacak işlemi sonucunda ilgili banka bilançosunun aktifinde ise dış varlıklar artarken TCMB mevduatı yani rezerv para mevcudu azalacak. Zaten işlemin temel amacı da, piyasadaki likidite/rezerv para fazlasının bu şekilde temizlenmesi/sterilize edilmesi.
ii)Ancak bu işlemin bir de ikinci bacağı yani vade bacağı var. Bu bacağı da bilanço dışında yani nazım hesaplarda izliyoruz. Vade geldiğinde TCMB ilk bacak işlemi sonucu çektiği TL’yi geri verecek ve karşılığında verdiği dövizi geri alacak; elbette bankada bu ikinci bacak işleminde TL alacak ve döviz verecek. Lakin önemli bir husus var göz önüne alınması gereken: Bu ikinci bacak işlemi sonucunda ortaya çıkacak rezerv para miktarı ilk bacak işlemi sonucundan çekilen rezerv para miktarından daha yüksek olacak. Bu durumun nedeni, 
TCMB’nin ilk bacak işlemi ile sterilize ettiği TL’ye faiz ödeyecek olması. Üstelik bu faiz oranı, kendi politika faizi olan %50 “etrafında” oluşacak
"""
pip install abcFinance
from abcFinance import Ledger
from IPython.core.display import SVG
from IPython.display import display_svg

from abcFinance import Ledger
from IPython.core.display import SVG
from IPython.display import display_svg

    
#  Her aktörün bilançosunun artık hesabı,(Varlık-Yükümlülük),Sermaye olarak adlandırılıyor.
Xbankasi = Ledger(residual_account_name="Sermaye")
Merkez_Bankasi = Ledger(residual_account_name="Sermaye")
XbankasiNazim = Ledger(residual_account_name="Sermaye")
Merkez_BankasiNazim = Ledger(residual_account_name="Sermaye")


#  Bankaların varlık ve yükümlülük kalemleri tanımlanıyor.
Xbankasi.make_asset_accounts(['Döviz','Tahvil', 'Rezerv'])
Xbankasi.make_liability_accounts(['Mevduat'])
XbankasiNazim.make_asset_accounts(['Döviz Alacak','Rezerv Alacak'])
XbankasiNazim.make_liability_accounts(['Döviz Borç','Rezerv Borç'])


# Merkez Bankasının varlık ve yükümlülük kalemleri tanımlanıyor.
Merkez_Bankasi.make_asset_accounts(['Döviz'])
Merkez_Bankasi.make_liability_accounts(['Rezerv'])
Merkez_BankasiNazim.make_asset_accounts(['Döviz Alacak','Rezerv Alacak'])
Merkez_BankasiNazim.make_liability_accounts(['Döviz Borç','Rezerv Borç'])

#Başlangıç
Xbankasi.book(debit=[('Rezerv',100)],credit=[('Sermaye',100)])
Merkez_Bankasi.book(debit=[('Döviz',100)],credit=[('Rezerv',100)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X Bilanço", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası Bilanço", width=500)))






# 1 dolar= 1 TL (Yiğit BULUT)
# TCMB işlemin ilk bacağında bankalara 60 dolar döviz verecek bankalarda 60 TL rezerv ile ödeyecek
# TCMB bilançosunda hem aktif hem pasif azalırken
# Banka bilançosunda aktifte döviz artarken rezerv azalacak
# Nazım da TCMB döviz alacağı ve rezerv borcu artarken
# Nazım da bankanın Rezerv alacağı ve Döviz borcu artacaktır.

Xbankasi.book(debit=[('Döviz',60)],credit=[('Rezerv',60)])
Merkez_Bankasi.book(debit=[('Rezerv',60)],credit=[('Döviz',60)])
XbankasiNazim.book(debit=[('Rezerv Alacak',60)],credit=[('Döviz Borç',60)])
Merkez_BankasiNazim.book(debit=[('Döviz Alacak',60)],credit=[('Rezerv Borç',60)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X Bilanço", width=500)))
display_svg(SVG(XbankasiNazim.draw_balance_sheet("Banka X Nazım", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası Bilanço", width=500)))
display_svg(SVG(Merkez_BankasiNazim.draw_balance_sheet("Merkez Bankası Nazım", width=500)))






# 1 dolar= 1 TL (Yiğit BULUT)
# TCMB işlemin sonunda bankalara 60 dolar döviz geri alacak bankalara 60 TL rezerv ile ödeyecek
# TCMB bilançosunda hem aktif hem pasif artarken
# Banka bilançosunda aktifte rezerv artarken döviz azalacak
# Nazım da TCMB döviz alacağı ve rezerv borcu azalırken
# Nazım da bankanın Rezerv alacağı ve Döviz borcu azalacaktır

Xbankasi.book(debit=[('Rezerv',60)],credit=[('Döviz',60)])
Merkez_Bankasi.book(debit=[('Döviz',60)],credit=[('Rezerv',60)])
XbankasiNazim.book(debit=[('Döviz Borç',60)],credit=[('Rezerv Alacak',60)])
Merkez_BankasiNazim.book(debit=[('Rezerv Borç',60)],credit=[('Döviz Alacak',60)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X Bilanço", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası Bilanço", width=500)))
print("......................................................................")
display_svg(SVG(XbankasiNazim.draw_balance_sheet("Banka X Nazım Temizlendi", width=500)))
display_svg(SVG(Merkez_BankasiNazim.draw_balance_sheet("Merkez Bankası Nazım Temizlendi", width=500)))
