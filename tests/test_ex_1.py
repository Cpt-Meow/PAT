from fixture.main import MainClass


class TestMainClass(MainClass):

    def test_get_local_number(self):
        assert self.get_local_number() == 14, "This number is equal to 14"

    def test_get_class_number(self):
        assert self.get_lass_number() > 45, f"Actual value is not more than Expected value"

    def test_get_class_string(self):
        assert 'hello' in self.get_class_string() or 'Hello' in self.get_class_string(), \
            f"Class string does not contain 'hello' or 'Hello' "
