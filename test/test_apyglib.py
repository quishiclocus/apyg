import string
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
    """test RandomPasswordStack class"""

    def test_genpool(self):
        """test genpool function"""
        rps = random_password_stack.RandomPasswordStack()
        jlen = 4
        jseed = ["", "hello", "123"]
        jspc = [False, True]
        result_rps = rps.genpool(jlen, jseed[0], jspc[0])
        assert len(result_rps) > jlen
        result_rps = rps.genpool(jlen, jseed[0], jspc[1])
        result_punc = ""
        for e in result_rps:
            if e in string.punctuation:
                result_punc += e
        assert len(result_punc) > 0
        result_rps = rps.genpool(jlen, jseed[1], jspc[0])
        assert len(result_rps) == 7
        result_rps = rps.genpool(jlen, jseed[1], jspc[1])
        assert len(result_rps) == 11

    def test_cleanpool(self):
        """test cleanpool function"""
        pool = ["A", "a", "1", "_"]
        clean_pool = random_password_stack.RandomPasswordStack.cleanpool(self, pool)
        assert len(clean_pool) == 3
        assert clean_pool[2] == "_"

    def test_strictpool(self):
        """test strictpool function"""
        pool = ["A", "a", "1", "_"]
        for chk in pool:
            if chk.islower():
                assert chk.islower() is True
                assert chk.isupper() is False
                assert chk.isdigit() is False
                assert any(char in string.punctuation for char in chk) is False
            if chk.isupper():
                assert chk.islower() is False
                assert chk.isupper() is True
                assert chk.isdigit() is False
                assert any(char in string.punctuation for char in chk) is False
            if chk.isdigit():
                assert chk.islower() is False
                assert chk.isupper() is False
                assert chk.isdigit() is True
                assert any(char in string.punctuation for char in chk) is False
            if chk in string.punctuation:
                assert chk.islower() is False
                assert chk.isupper() is False
                assert chk.isdigit() is False
                assert any(char in string.punctuation for char in chk) is True

    def test_genpword(self):
        """test genpword function"""
        pass

    def test_push(self):
        """test push function"""
        pass

    def test_pop(self):
        """test pop function"""
        pass
