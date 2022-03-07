import requests

from Tests.Tests_REST_API.HomePage import ParaBankHomePage
from Tests.Tests_REST_API.TestData import DataEndPoint


class TestParaBank(ParaBankHomePage):

    def test_get_account_by_id(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{DataEndPoint.base_uri}{DataEndPoint.getAccountId}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for account by id"

    def test_get_list_transaction_for_account(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{DataEndPoint.base_uri}{DataEndPoint.getListTransactionForAccount}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for the list transaction for the account"

    def test_get_create_transactions_by_amount_for_account(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{DataEndPoint.base_uri}{DataEndPoint.createTransactionsByAmountForAccount}",
                                headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for create " \
                                            "transactions with amount for account"

    def test_post_new_deposit(self):
        headers = {"Accept": "application/json"}
        response = requests.post(f"{DataEndPoint.base_uri}{DataEndPoint.newDeposit}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for new deposit"

    def test_post_new_account(self):
        headers = {"Accept": "application/json"}
        response = requests.post(f"{DataEndPoint.base_uri}{DataEndPoint.newAccount}", headers=headers)
        # print(response.text)
        assert response.status_code == 200, "           Can't get response 200 for new account"

    def test_get_login(self):
        headers = {"Accept": "application/json"}
        response = requests.get(f"{DataEndPoint.base_uri}{DataEndPoint.login}", headers=headers)
        assert response.status_code == 200, "           Can't get response 200 for login"
