from random import randint

import requests

from Tests.Tests_REST_API.HomePage import ParaBankHomePage

base_uri = 'https://parabank.parasoft.com/parabank/services/bank'
customerId = 12656
amount = 5000
new_account_id = randint(10000, 99999)
newAccountType = 0
username = 'ivan'
password = 'ivan123'


class TestParaBank:

    def test_get_account_by_id(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{base_uri}/accounts/{customerId}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for account by id"

    def test_get_list_transaction_for_account(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{base_uri}/accounts/{customerId}/transactions", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for the list transaction for the account"

    def test_get_create_transactions_by_amount_for_account(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{base_uri}/accounts/{customerId}/transactions/amount/{amount}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for create " \
                                            "transactions with amount for account"

    def test_post_new_deposit(self):
        headers = {"Accept": "application/json"}
        response = requests.post(f"{base_uri}/deposit?accountId={customerId}&amount={amount}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for new deposit"

    def test_post_new_account(self):
        headers = {"Accept": "application/json"}
        response = requests.post(f"{base_uri}/createAccount?customerId={new_account_id}&newAccountType={newAccountType}"
                                 f"&fromAccountId={customerId}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for new account"

    def test_get_login(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{base_uri}/login/{username}/{password}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for login"
