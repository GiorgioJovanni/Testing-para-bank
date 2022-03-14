from Tests.Tests_REST_API.BaseClass import ParaBankHomePage
from Tests.Tests_REST_API.TestData import DataEndPoints, DataTest


class TestParaBank(ParaBankHomePage):

    def test_get_account_by_id(self):
        response = self.get(f"{DataEndPoints.base_uri}{DataEndPoints.getAccountId}")
        assert response.status_code == 200, "           Can't get response 200 for account by id"

    def test_get_list_transaction_for_account(self):
        response = self.get(f"{DataEndPoints.base_uri}{DataEndPoints.getListTransactionForAccount}")
        assert response.status_code == 200, "           Can't get response 200 for the list transaction for the account"

    def test_get_create_transactions_by_amount_for_account(self):
        response = self.get(f"{DataEndPoints.base_uri}{DataEndPoints.createTransactionsByAmountForAccount}")
        assert response.status_code == 200, "           Can't get response 200 for create " \
                                            "transactions with amount for account"

    def test_post_new_deposit(self):
        response = self.post(f"{DataEndPoints.base_uri}{DataEndPoints.newDeposit}")
        assert response.status_code == 200, "           Can't get response 200 for new deposit"

    def test_post_new_account(self):
        response = self.post(f"{DataEndPoints.base_uri}{DataEndPoints.newAccount}")
        assert response.text == f'Could not create new account for customer {DataTest.new_account_id}' \
                                f' from account 12656'
        assert response.status_code == 200, "           Can't get response 200 for new account"

    def test_get_login(self):
        response = self.get(f"{DataEndPoints.base_uri}{DataEndPoints.login}")
        assert response.status_code == 200, "           Can't get response 200 for login"
