import requests


class TestBasePage:

    def test_get_locations_for_us_check_status_code_equals_200(self):
        response = requests.get("http://parabank.parasoft.com")
        assert response.status_code == 200, "Base page para-bank is not working"

    def test_get_locations_for_check_status_code_equals_200(self):
        response = requests.get("https://parabank.parasoft.com/parabank/register.htm")
        assert response.status_code == 200, "Page register is not working"

    # def test_get_locations_for_us_90210_check_content_type_equals_json(self):
    #     res = requests.get('http://parabank.parasoft.com')
    #     print(res)
    #     if res:
    #         print('Response OK')
    #     else:
    #         print('Response Failed')

        # print(res.json())
