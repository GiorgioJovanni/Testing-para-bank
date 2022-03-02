import requests

def test_check_status_code_equals_200():
    response_restore_password_page = requests.get("https://parabank.parasoft.com/parabank/lookup.htm")
     assert response_restore_password_page.status_code == 200, 'Response Failed'
    assert response_restore_password_page.status_code == 200
    if response_restore_password_page:
        print('Response OK')
    else:
        print('Response Failed')
