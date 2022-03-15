from Tests.Tests_REST_API.BaseClass import ParaBankHomePage
from Tests.Tests_REST_API.TestData import DataEndPoints, DataTest


class TestParaBank(ParaBankHomePage):

    def test_get_account_by_id(self):
        response = self.get(f"{DataEndPoints.base_uri + DataEndPoints.getAccountId + DataTest.new_account_id}")
        assert response.status_code == 200, "           Can't get response 200 for account by id"

    def test_get_list_transaction_for_account(self):
        response = self.get(f"{DataEndPoints.base_uri + DataEndPoints.getListTransactionForAccount1}"
                            f"{DataTest.new_account_id}")
        assert response.status_code == 200, "           Can't get response 200 for the list transaction for the account"

    def test_get_create_transactions_by_amount_for_account(self):
        response = self.get(f"{DataEndPoints.base_uri + DataEndPoints.createTransactionsByAmountForAccount1}"
                            f"{DataTest.new_account_id + DataEndPoints.createTransactionsByAmountForAccount2}"
                            f"{DataTest.amount}")
        assert response.status_code == 200, "           Can't get response 200 for create " \
                                            "transactions with amount for account"

    def test_post_new_deposit(self):
        response = self.post(f"{DataEndPoints.base_uri + DataEndPoints.newDeposit1 + DataTest.new_account_id}"
                             f"{DataEndPoints.newDeposit2 + DataTest.amount}")
        assert response.status_code == 200, "           Can't get response 200 for new deposit"

    def test_post_new_account(self):
        response = self.post(f"{DataEndPoints.base_uri + DataEndPoints.newAccount1 + DataTest.new_account_id}"
                             f"{DataEndPoints.newAccount2 + DataTest.newAccountType}"
                             f"{DataEndPoints.newAccount2 + DataTest.customerId}")
        assert response.text == f'Could not create new account for customer {DataTest.new_account_id} from account ' \
                                f'{DataTest.newAccountType}'
        assert response.status_code == 200, "           Can't get response 200 for new account"

    def test_get_login(self):
        response = self.get(f"{DataEndPoints.base_uri + DataEndPoints.login}")
        assert response.status_code == 200, "           Can't get response 200 for login"
