import unittest


from main import encrypt, decrypt

class TestCryptoFunctions(unittest.TestCase):

    def test_encrypt(self):
        # Test encryption with various cases
        self.assertEqual(encrypt("HELLO", 3), "KHOOR")
        self.assertEqual(encrypt("hello", 3), "khoor")
        self.assertEqual(encrypt("Hello World", 3), "Khoor Zruog")
        self.assertEqual(encrypt("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(encrypt("HELLO", -3), "EBIIL")
        self.assertEqual(encrypt("HELLO", 30), "LIPPS")
        self.assertEqual(encrypt("", 3), "")

    def test_decrypt(self):
        # Test decryption with various cases
        self.assertEqual(decrypt("KHOOR", 3), "HELLO")
        self.assertEqual(decrypt("khoor", 3), "hello")
        self.assertEqual(decrypt("Khoor Zruog", 3), "Hello World")
        self.assertEqual(decrypt("Khoor, Zruog!", 3), "Hello, World!")
        self.assertEqual(decrypt("EBIIL", -3), "HELLO")
        self.assertEqual(decrypt("LIPPS", 30), "HELLO")
        self.assertEqual(decrypt("", 3), "")

if __name__ == '__main__':
    unittest.main()

