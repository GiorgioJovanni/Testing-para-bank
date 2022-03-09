from random import randint


class DataTest:
    customerId = 12656
    amount = 5000
    new_account_id = randint(10000, 99999)
    newAccountType = 0
    username = 'ivan'
    password = 'ivan123'


class DataEndPoints:
    base_uri = 'https://parabank.parasoft.com/parabank/services/bank'
    getAccountId = f"/accounts/{DataTest.customerId}"
    getListTransactionForAccount = f"/accounts/{DataTest.customerId}/transactions"
    createTransactionsByAmountForAccount = f"/accounts/{DataTest.customerId}/transactions/amount/{DataTest.amount}"
    newDeposit = f"/deposit?accountId={DataTest.customerId}&amount={DataTest.amount}"
    newAccount = f"/createAccount?customerId={DataTest.new_account_id}&newAccountType={DataTest.newAccountType}" \
                 f"&fromAccountId={DataTest.customerId}"
    login = f"/login/{DataTest.username}/{DataTest.password}"
