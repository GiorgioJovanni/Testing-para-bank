import faker


class EndPoint:
    base_link = "http://parabank.parasoft.com"


class Data:
    fake = faker.Faker()
    password = fake.password()
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = 'New York'
    zipcode = '0007'
    phone = '+01234241231'
    snn = '23412341234123'
