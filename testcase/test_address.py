from api.address import Address

class TestCase:

    def setup(self):
        self.address = Address()


    def test_token(self):
        print(self.address.token())


    def test_create(self):
        print(self.address.create_contacts("wangwu","王武","17890984622"))

    def test_get(self):
        print(self.address.get_contacts("wangwu"))

    def test_update(self):
        print(self.address.update_contacts("wangwu","赵六"))

    def test_delete(self):
        print(self.address.delete_contacts("wangwu"))

        