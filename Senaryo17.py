
#https://x.com/KeloglanBM/status/1816188063615442954

"""
Başlayacağı iddia edilen “sterilizasyon amaçlı” yeni swap işleminin TCMB ve ilgili banka bilançoları üzerindeki etkisi dört sütundan oluşan Şekil 1’in ilk iki sütununda gösterildiği şekilde olacak:
i)TCMB işlemin ilk bacağında (haberde valör diye geçiyor) bankalara döviz (haberde altının da kullanılabileceği yazıyor) verecek ve karşılığında bankaların TCMB’de tuttukları rezerv paraları azalacak. Böylece TCMB bilançosunun aktifinde dış varlıklar azalırken yani TCMB brüt rezervleri düşerken pasifinde ise rezerv para azalacak. Bu ilk bacak işlemi sonucunda ilgili banka bilançosunun aktifinde ise dış varlıklar artarken TCMB mevduatı yani rezerv para mevcudu azalacak. Zaten işlemin temel amacı da, piyasadaki likidite/rezerv para fazlasının bu şekilde temizlenmesi/sterilize edilmesi.
ii)Ancak bu işlemin bir de ikinci bacağı yani vade bacağı var. Bu bacağı da bilanço dışında yani nazım hesaplarda izliyoruz. Vade geldiğinde TCMB ilk bacak işlemi sonucu çektiği TL’yi geri verecek ve karşılığında verdiği dövizi geri alacak; elbette bankada bu ikinci bacak işleminde TL alacak ve döviz verecek. Lakin önemli bir husus var göz önüne alınması gereken: Bu ikinci bacak işlemi sonucunda ortaya çıkacak rezerv para miktarı ilk bacak işlemi sonucundan çekilen rezerv para miktarından daha yüksek olacak. Bu durumun nedeni, 
TCMB’nin ilk bacak işlemi ile sterilize ettiği TL’ye faiz ödeyecek olması. Üstelik bu faiz oranı, kendi politika faizi olan %50 “etrafında” oluşacak
"""

from abcFinance import Ledger
from IPython.core.display import SVG
from IPython.display import display_svg


    
#  Her aktörün bilançosunun artık hesabı,(Varlık-Yükümlülük),Sermaye olarak adlandırılıyor.
Xbankasi = Ledger(residual_account_name="Sermaye")
Merkez_Bankasi = Ledger(residual_account_name="Sermaye")


#  Bankaların varlık ve yükümlülük kalemleri tanımlanıyor.
Xbankasi.make_asset_accounts(['Döviz','Tahvil', 'Döviz Alacak','Rezerv Alacak','Rezerv'])
Xbankasi.make_liability_accounts(['Döviz Borç','Rezerv Borç'])


# Merkez Bankasının varlık ve yükümlülük kalemleri tanımlanıyor.
Merkez_Bankasi.make_asset_accounts(['Döviz','Döviz Alacak','Rezerv Alacak'])
Merkez_Bankasi.make_liability_accounts(['Döviz Borç','Rezerv Borç','Rezerv'])


#Başlangıç
Xbankasi.book(debit=[('Rezerv',100)],credit=[('Sermaye',100)])
Merkez_Bankasi.book(debit=[('Döviz',100)],credit=[('Rezerv',100)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))


#Swap
Xbankasi.book(debit=[('Döviz',100)],credit=[('Rezerv',100)])
Merkez_Bankasi.book(debit=[('Rezerv',100)],credit=[('Döviz',100)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))


#Swap Nazım
Xbankasi.book(debit=[('Rezerv Alacak',100)],credit=[('Döviz Borç',100)])
Merkez_Bankasi.book(debit=[('Döviz Alacak',100)],credit=[('Rezerv Borç',100)])

#Başlangıç- Bilançolar
display_svg(SVG(Xbankasi.draw_balance_sheet("Banka X", width=500)))
display_svg(SVG(Merkez_Bankasi.draw_balance_sheet("Merkez Bankası", width=500)))



"""
Şekil 1’in son iki sütununda ise özellikle 2023 Mayıs seçimleri öncesi yoğun bir şekilde kullanılmış önce bir spot satım ve sonra alım yönlü bir döviz swapından oluşan ve bir sentetik forward yaratan eski swap işlemlerinin kaydı sunuluyor:
i)Spot bacakta TCMB kurun yükselmesini engellemek için yerel bankaya döviz satar, karşılığında rezerv para yok eder3.
ii)TCMB spot bacakta sattığı dövizi, alım yönlü döviz swapının valör bacağında geri alıp, spot bacakta aldığı TL’yi geri verir. Böylece TCMB ve banka bilançoları başlangıç durumuna döner. Dolayısıyla TCMB brüt rezervi değişmez
iii)Ortaya çıkan sentetik forwardın vade bacağında ise TCMB swapın valör bacağında aldığı döviz için faiz öderken verdiği TL (rezerv para) için faiz alır. Bu faiz de, yine o dönemki kendi politika faizi olan %8.5 “etrafında” oluşur

"""
