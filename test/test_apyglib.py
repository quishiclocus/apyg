import io
import unittest
import unittest.mock
from apyglib import phoenetic
from apyglib.crypt_print import CryptPrint
from apyglib.random_password_stack import RandomPasswordStack


class TestPhoenetic(unittest.TestCase):

    def test_print_new_password_phoenetic(self):
        p = phoenetic.Phoenetic()
        result = p.print_new_password_phoenetic("a")
        assert result == " alpha"

    def test_phoenetic_function(self):
        pass


class TestCryptPrint(unittest.TestCase):

    def test_print_new_password_crypt(self):
        pass

    def test_crypt_function(self):
        pass


class TestRandomPasswordStack(unittest.TestCase):

    def test_genpool(self):
        pass

    def test_cleanpool(self):
        pass

    def test_strictpool(self):
        pass

    def test_genpword(self):
        pass

    def test_push(self):
        pass

    def test_pop(self):
        pass
