import requests

headers = {"Accept": "application/json"}
base_uri = 'https://parabank.parasoft.com/parabank/services/bank'
account_id = 12345
amount = 5000


class TestGet(BaseClass):

    def test_get_account_by_id(self):
        response = requests.get(f"{base_uri}/accounts/{account_id}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for account by id"

    def test_get_list_transaction_for_account(self):
        response = requests.get(f"{base_uri}/accounts/{account_id}/transactions", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for the list transaction for the account"

    def test_get_create_transactions_by_amount_for_account(self):
        response = requests.get(f"{base_uri}/accounts/{account_id}/transactions/amount/{amount}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for create " \
                                            "transactions by amount for account"
