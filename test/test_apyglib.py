import io
import unittest
import unittest.mock
from apyglib import phoenetic
from apyglib import crypt_print
from apyglib import random_password_stack


class TestPhoenetic(unittest.TestCase):

    def test_print_new_password_phoenetic(self):
        p = phoenetic.Phoenetic()
        result_p = p.print_new_password_phoenetic("a")
        assert result_p == " alpha"

    def test_phoenetic_function(self):
        pass


class TestCryptPrint(unittest.TestCase):

    def test_print_new_password_crypt(self):
        c = crypt_print.CryptPrint()
        result_c = c.print_new_password_crypt("a", "", "4")
        assert result_c == "ca234c55"

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
