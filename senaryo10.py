"""
https://www.paraanaliz.com/2021/piyasa/fed-pd-hedgefund-mmf-balance-sheet-approach-repo-reverse-repo-g-10205/


"""





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
    if "hd" in args and HedgeFund.get_total_assets() > 0: display_svg(SVG(Household.draw_balance_sheet("HedgeFund", width=500)))
    if "fd" in args and Fed.get_total_assets() > 0: display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))
    if "ts" in args and MMF.get_total_assets() > 0: display_svg(SVG(Treasury.draw_balance_sheet("MMF", width=500)))  
    if "pd" in args and Primary_Dealer.get_total_assets() > 0: display_svg(SVG(Primary_Dealer.draw_balance_sheet("Primary Dealer", width=500)))
    print_money_stocks()
    
#  Net Financial Value
Bank = Ledger(residual_account_name="Net Financial Value")
HedgeFund = Ledger(residual_account_name="Net Financial Value")
Primary_Dealer = Ledger(residual_account_name="Net Financial Value")
MMF = Ledger(residual_account_name="Net Financial Value")
Fed = Ledger(residual_account_name="Net Financial Value")

# Bank 
Bank.make_asset_accounts(['Reserves'])
Bank.make_liability_accounts(['Deposits']) 

#Fed
Fed.make_asset_accounts(['Repo'])
Fed.make_liability_accounts(['Reserves','Reverse Repo'])

# HedgeFund 
HedgeFund.make_asset_accounts(['Deposits'])
HedgeFund.make_liability_accounts(['Repo', 'Loans']) 

# Primary Dealer 
Primary_Dealer.make_asset_accounts(['Deposits','Reverse Repo'])
Primary_Dealer.make_liability_accounts(['Repo'])  
                                                                      
# MMF 
MMF.make_asset_accounts(['Reverse Repo','Deposits'])
MMF.make_liability_accounts(['Repo','Loans'])




#Code0, Fed makes a repo with Primary Dealer.
Fed.book(debit=[('Repo',200)],credit=[('Reserves',200)])
Bank.book(debit=[('Reserves',200)],credit=[('Deposits',200)])
Primary_Dealer.book(debit=[('Deposits',200)],credit=[('Repo',200)])



#Balance Sheet
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Primary_Dealer.draw_balance_sheet("Primary Dealer", width=500)))



#Code1, Fed makes a reverse repo with Primary Dealer
Fed.book(debit=[('Reserves',50)],credit=[('Reverse Repo',50)])
Bank.book(debit=[('Deposits',50)],credit=[('Reserves',50)])
Primary_Dealer.book(debit=[('Reverse Repo',50)],credit=[('Deposits',50)])



#Balance Sheet
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Primary_Dealer.draw_balance_sheet("Primary Dealer", width=500)))



#Initial Balance Sheets
MMF.book(debit=[('Deposits',200)],credit=[('Loans',200)])
display_svg(SVG(MMF.draw_balance_sheet("MMF", width=500)))



#Code2, Primary Dealer borrows the deposits from MMF

MMF.book(debit=[('Reverse Repo',100)],credit=[('Deposits',100)])
Primary_Dealer.book(debit=[('Deposits',100)],credit=[('Repo',100)])



#Balance Sheet

display_svg(SVG(MMF.draw_balance_sheet("MMF", width=500)))
display_svg(SVG(Primary_Dealer.draw_balance_sheet("Primary Dealer", width=500)))



#Initial Balance Sheet
HedgeFund.book(debit=[('Deposits',200)],credit=[('Loans',200)])
display_svg(SVG(HedgeFund.draw_balance_sheet("HedgeFund", width=500)))


#Code3, Primary Dealer lends the deposits to HedgeFund

HedgeFund.book(debit=[('Deposits',100)],credit=[('Repo',100)])
Primary_Dealer.book(debit=[('Reverse Repo',100)],credit=[('Deposits',100)])



#Balance Sheet

display_svg(SVG(HedgeFund.draw_balance_sheet("HedgeFund", width=500)))
display_svg(SVG(Primary_Dealer.draw_balance_sheet("Primary Dealer", width=500)))


