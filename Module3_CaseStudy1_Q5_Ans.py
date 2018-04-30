# Design a software for bank system.
# There should be options like cash withdraw, cash credit and change password.
# According to user input, the software should provide required output.

def CashWithdrawal():
    PIN=input('Enter ATM or CARD PIN to proceed:')
    if PIN==123:
        print '***Thank You For Banking With Us***'
    else:
        print 'You Have Enterd Invalid PIN. Try Again'

def CashCredit():
    PIN=input('Enter ATM or CARD PIN to proceed:')
    if PIN==123:
        AMT=input('Enter Amount That You Wish to Credit To Bank:')
        print '***Thank You For Banking With Us***'
    else:
        print 'You Have Enterd Invalid PIN. Try Again'

def ChangePassword():
    PIN=input('Enter ATM or CARD PIN to proceed:')
    if PIN==123:
        OLD_PWD=raw_input('Please Enter Your Old Password:')
        print '***Thank You For Banking With Us***'
    else:
        print 'You Have Enterd Invalid PIN. Try Again'

def Main():
    print 'Welcome to XYZ Bank\nChoose from below options'
    print '1. Case withdrawal\n2. Cash credit\n3. Change password'
    opt=input('Enter your option:')
    if opt==1:
        CashWithdrawal()
    if opt==2:
        CashCredit()
    if opt==3:
        ChangePassword()

Main()

