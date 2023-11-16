from faker import Faker


class User:
    first_name: str
    last_name: str
    full_name: str
    postal_code: str

    def generate_user(self):
        faker = Faker()
        self.first_name = faker.user_name()
        self.last_name = faker.last_name()
        self.full_name = f'{self.first_name} {self.last_name}'
        self.postal_code = str(faker.random_int(min=1, max=9999999))
        return self
