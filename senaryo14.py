//https://www.paraanaliz.com/2021/yazarlar/veri-delisi/fed-bilancosunda-ters-repo-neden-artiyor-g-8472/
//https://twitter.com/FedGuy12/status/1645409217799688193
//https://fedguy.com/primer-a-deposits-life/
  
#install it
pip install abcFinance 

#instructions
  
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
    if "ts" in args and MMF.get_total_assets() > 0: display_svg(SVG(Treasury.draw_balance_sheet("MMF", width=500)))  
   
    
#  Net Financial Value
Bank = Ledger(residual_account_name="Net Financial Value")
Household = Ledger(residual_account_name="Net Financial Value")
MMF = Ledger(residual_account_name="Net Financial Value")
Fed = Ledger(residual_account_name="Net Financial Value")

# Bank 
Bank.make_asset_accounts(['Reserves'])
Bank.make_liability_accounts(['Deposits']) 
Bank.make_liability_accounts(['MMF Deposits']) 

#Fed
Fed.make_asset_accounts(['Securities'])
Fed.make_liability_accounts(['Reserves','Reverse Repo'])

# Household
Household.make_asset_accounts(['Deposits'])
Household.make_liability_accounts(['Repo', 'Loans']) 

# MMF 
MMF.make_asset_accounts(['Deposits', 'Reverse Repo'])
MMF.make_liability_accounts(['MMF Shares'])


#Code0, initial balances
Fed.book(debit=[('Securities',250)],credit=[('Reserves',250)])
Bank.book(debit=[('Reserves',250)],credit=[('Deposits',250)])
Household.book(debit=[('Deposits',250)],credit=[('Net Financial Value',250)])


#Balance Sheet
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))
display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))



#Code1, MMF increase their deposits in banking system
Bank.book(debit=[('Deposits',150)],credit=[('MMF Deposits',150)])
MMF.book(debit=[('Deposits',150)],credit=[('MMF Shares',150)])


#Balance Sheet
display_svg(SVG(MMF.draw_balance_sheet("MMF", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))


#Code2, Fed makes a reverse repo with MMF
Fed.book(debit=[('Reserves',100)],credit=[('Reverse Repo',100)])
MMF.book(debit=[('Reverse Repo',100)],credit=[('Deposits',100)])
Bank.book(debit=[('MMF Deposits',100)],credit=[('Reserves',100)])



#Balance Sheet
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))
display_svg(SVG(MMF.draw_balance_sheet("MMF", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
