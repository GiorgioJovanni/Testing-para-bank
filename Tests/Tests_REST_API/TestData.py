from random import randint


class DataTest:
    customerId = '12345'
    amount = '5000'
    new_account_id = str(randint(10000, 99999))
    newAccountType = '0'
    username = 'ivan'
    password = 'ivan123'


class DataEndPoints:
    base_uri = 'https://parabank.parasoft.com/parabank/services/bank'
    getAccountId = f"/accounts/"
    getListTransactionForAccount1 = f"/accounts/"
    getListTransactionForAccount2 = "/transactions"
    createTransactionsByAmountForAccount1 = f"/accounts/"
    createTransactionsByAmountForAccount2 = "/transactions/amount/"
    newDeposit1 = f"/deposit?accountId="
    newDeposit2 = "&amount="
    newAccount1 = f"/createAccount?customerId="
    newAccount2 = f"&newAccountType="
    newAccount3 = f"&fromAccountId="
    login = f"/login/"
