from fixture.main import MainClass


class TestMainClass(MainClass):

    def test_get_local_number(self):
        assert self.get_local_number() == 14, "This number is equal to 14"

    def test_get_class_number(self):
        assert self.get_lass_number() > 45, f"Actual value is not more than Expected value"
