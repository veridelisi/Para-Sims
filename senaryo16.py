# https://www.paraanaliz.com/2023/yazarlar/veri-delisi/devlet-harcamasi-vergi-toplama-ve-devlet-borclanmasi-uzerine-bir-degerlendirme-g-53538/

from abcFinance import Ledger

from IPython.core.display import SVG
from IPython.display import display_svg


def print_balance_sheets_and_money_stocks(*args):
    MusteriA.book_end_of_period()
    MusteriB.book_end_of_period()
    MusteriC.book_end_of_period()
    
    if len(args)==0:
        args = ("bk","hd","fd","ts","pd")
    
    if "bk" in args and Bank.get_total_assets() > 0: display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
    if "hh" in args and Household.get_total_assets() > 0: display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
    if "fd" in args and Fed.get_total_assets() > 0: display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))
    if "ts" in args and MMF.get_total_assets() > 0: display_svg(SVG(Treasury.draw_balance_sheet("Treasury", width=500)))  
   
    
#  Net Financial Value
Bank = Ledger(residual_account_name="Net Financial Value")
Household = Ledger(residual_account_name="Net Financial Value")
Treasury = Ledger(residual_account_name="Net Financial Value")
Fed = Ledger(residual_account_name="Net Financial Value")

# Bank 
Bank.make_asset_accounts(['Reserves'])
Bank.make_liability_accounts(['Deposits']) 
# Bank.make_asset_accounts(['Credits'])
# Bank.make_liability_accounts(['MMF Deposits']) 

#Fed
Fed.make_asset_accounts(['Securities'])
Fed.make_liability_accounts(['Reserves','Reverse Repo','Treasury Account'])

# Household
Household.make_asset_accounts(['Deposits'])
Household.make_asset_accounts(['Securities'])
Household.make_liability_accounts(['Repo', 'Loans']) 
# Household.make_asset_accounts(['Reverse Repo'])


# Treasury
Treasury.make_asset_accounts(['Treasury Account'])
Treasury.make_liability_accounts(['Tax', 'Securities'])



# Code0 
# 11 Mayıs 2023 günü Gerçek ABD Hazinesi Mali Dengesi verileri.

Bank.book(debit=[('Reserves',250)],credit=[('Deposits',250)])
Household.book(debit=[('Deposits',250)],credit=[('Net Financial Value',250)])
Fed.book(debit=[('Securities',404)],credit=[('Treasury Account',154),('Reserves',250) ])
Treasury.book(debit=[('Treasury Account',154)],credit=[('Net Financial Value',154) ])


#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Treasury.draw_balance_sheet("Treasury", width=500)))
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))



# Code1 
# 11 Mayıs 2023 günü Gerçek ABD Hazinesi Mali Dengesi verileri 125 Milyar dolar vergi tahsilatı ve borçlanma yapıldı.

Bank.book(debit=[('Deposits',125)],credit=[('Reserves',125)])
Household.book(debit=[('Net Financial Value',125)],credit=[('Deposits',125)])
Treasury.book(debit=[('Treasury Account',125)],credit=[('Net Financial Value',125) ])
Fed.book(debit=[('Reserves',125)],credit=[('Treasury Account',125) ])



#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Treasury.draw_balance_sheet("Treasury", width=500)))
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))




# Code2 
# 11 Mayıs 2023 günü Gerçek ABD Hazinesi Mali Dengesi verileri 136 Milyar dolar harcama yapıldı.

Bank.book(debit=[('Reserves',136)],credit=[('Deposits',136)])
Household.book(debit=[('Deposits',136)],credit=[('Net Financial Value',136)])
Fed.book(debit=[('Treasury Account',136)],credit=[('Reserves',136) ])
Treasury.book(debit=[('Net Financial Value',136)],credit=[('Treasury Account',136) ])



#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Treasury.draw_balance_sheet("Treasury", width=500)))
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))




# Code3 
# 12 Mayıs 2023 günü Gerçek ABD Hazinesi Mali Dengesi verileri 15 Milyar dolar vergi tahsilatı ve borçlanma yapıldı.

Bank.book(debit=[('Deposits',15)],credit=[('Reserves',15)])
Household.book(debit=[('Net Financial Value',15)],credit=[('Deposits',15)])
Treasury.book(debit=[('Treasury Account',15)],credit=[('Net Financial Value',15) ])
Fed.book(debit=[('Reserves',15)],credit=[('Treasury Account',15) ])



#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Treasury.draw_balance_sheet("Treasury", width=500)))
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))




# Code4 
# 11 Mayıs 2023 günü Gerçek ABD Hazinesi Mali Dengesi verileri 19 Milyar dolar harcama yapıldı.

Bank.book(debit=[('Reserves',19)],credit=[('Deposits',19)])
Household.book(debit=[('Deposits',19)],credit=[('Net Financial Value',19)])
Fed.book(debit=[('Treasury Account',19)],credit=[('Reserves',19) ])
Treasury.book(debit=[('Net Financial Value',19)],credit=[('Treasury Account',19) ])



#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Treasury.draw_balance_sheet("Treasury", width=500)))
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))




