//https://fedguy.com/primer-a-deposits-life/

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
Bank.make_asset_accounts(['Credits'])
Bank.make_liability_accounts(['Deposits']) 
Bank.make_liability_accounts(['MMF Deposits']) 

#Fed
Fed.make_asset_accounts(['Securities'])
Fed.make_liability_accounts(['Reserves','Reverse Repo','Treasury Account'])

# Household
Household.make_asset_accounts(['Deposits'])
Household.make_asset_accounts(['Securities'])
Household.make_asset_accounts(['Reverse Repo'])
Household.make_liability_accounts(['Repo', 'Loans']) 

# Treasury
Treasury.make_asset_accounts(['Treasury Account'])
Treasury.make_liability_accounts(['Tax', 'Securities'])



#Code0

Bank.book(debit=[('Credits',250)],credit=[('Deposits',250)])
Household.book(debit=[('Deposits',250)],credit=[('Loans',250)])
Household.book(debit=[('Securities',150)],credit=[('Net Financial Value',150)])


#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))


#Code1
Fed.book(debit=[('Securities',150)],credit=[('Reserves',150)])
Bank.book(debit=[('Reserves',150)],credit=[('Deposits',150)])
Household.book(debit=[('Deposits',150)],credit=[('Securities',150)])




#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))

#Code2, 
Bank.book(debit=[('Deposits',250)],credit=[('Credits',250)])
Household.book(debit=[('Loans',250)],credit=[('Deposits',250)])



#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))

#Code3
Bank.book(debit=[('Deposits',50)],credit=[('Reserves',50)])
Household.book(debit=[('Securities',50)],credit=[('Deposits',50)])
Fed.book(debit=[('Reserves',50)],credit=[('Treasury Account',50)])
Treasury.book(debit=[('Treasury Account',50)],credit=[('Securities',50)])


#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Treasury.draw_balance_sheet("Treasury", width=500)))
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))

#Code4
Bank.book(debit=[('Deposits',50)],credit=[('Reserves',50)])
Household.book(debit=[('Net Financial Value',50)],credit=[('Deposits',50)])
Fed.book(debit=[('Reserves',50)],credit=[('Treasury Account',50)])
Treasury.book(debit=[('Treasury Account',50)],credit=[('Tax',50)])


#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Treasury.draw_balance_sheet("Treasury", width=500)))
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))

#Code5
Bank.book(debit=[('Deposits',20)],credit=[('Reserves',20)])
Household.book(debit=[('Reverse Repo',20)],credit=[('Deposits',20)])
Fed.book(debit=[('Reserves',20)],credit=[('Reverse Repo',20)])



#Balance Sheet

display_svg(SVG(Household.draw_balance_sheet("Household", width=500)))
display_svg(SVG(Bank.draw_balance_sheet("Bank", width=500)))
display_svg(SVG(Fed.draw_balance_sheet("Fed", width=500)))
