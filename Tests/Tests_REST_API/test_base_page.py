from random import randint

import requests

from Tests.Tests_REST_API.BaseClass import BaseParaBank

base_uri = 'https://parabank.parasoft.com/parabank/services/bank'
account_id = 12345
amount = 5000
new_account_id = randint(10000, 99999)
newAccountType = 0


class TestParaBank:

    def test_get_account_by_id(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{base_uri}/accounts/{account_id}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for account by id"

    def test_get_list_transaction_for_account(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{base_uri}/accounts/{account_id}/transactions", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for the list transaction for the account"

    def test_get_create_transactions_by_amount_for_account(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{base_uri}/accounts/{account_id}/transactions/amount/{amount}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for create " \
                                            "transactions by amount for account"

    def test_post_new_deposit(self):
        headers = {"Accept": "application/json"}
        response = requests.post(f"{base_uri}/deposit?accountId={account_id}&amount={amount}", headers=headers)
        assert response.status_code == 200

    def test_post_new_account(self):
        headers = {"Accept": "application/json"}
        response = requests.post(f"{base_uri}/createAccount?customerId={new_account_id}&newAccountType={newAccountType}"
                                 f"&fromAccountId={account_id}", headers=headers)
        print(f"{response.text}")
        # assert response.status_code == 200
