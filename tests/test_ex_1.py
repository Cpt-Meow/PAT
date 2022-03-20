class TestMainClass:

    def get_local_number(self):
        return 14

    def test_get_local_number(self):
        assert self.get_local_number() == 14, "This number is equal to 14"