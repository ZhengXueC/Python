import unittest

from noshift import brute_force_decrypt
from noshift import decrypt
from noshift import encrypt


class TestEncryptionDecryption(unittest.TestCase):

    def test_encrypt(self):
        # Test cases for the encrypt function
        self.assertEqual(encrypt("Hello", shift=3), "Khoor")
        self.assertEqual(encrypt("abc XYZ", shift=1), "bcd YZA")
        self.assertEqual(encrypt("123", shift=5), "123")

    def test_decrypt(self):
        # Test cases for the decrypt function
        self.assertEqual(decrypt("Khoor", shift=3), "Hello")
        self.assertEqual(decrypt("bcd YZA", shift=1), "abc XYZ")
        self.assertEqual(decrypt("123", shift=5), "123")

    def test_brute_force_decrypt(self):
        # Test case for the brute_force_decrypt function
        # Note: Since brute_force_decrypt prints output, we need to capture and check the printed result
        import io
        from contextlib import redirect_stdout

        message = "abc XYZ"
        expected_output = "Shift 0: abc XYZ\nShift 1: zab WXY\nShift 2: yza VWX\n...\nShift 25: zab WXY\n"

        with io.StringIO() as buffer, redirect_stdout(buffer):
            brute_force_decrypt(message)
            actual_output = buffer.getvalue()

        # Compare the stripped versions of the outputs to ignore differences in whitespaces
        self.assertEqual(actual_output.strip(), expected_output.strip())

    if __name__ == '__main__':
        unittest.main()

