import os
import unittest
from app import veri_oku, ozet_hesapla, rapor_kaydet


class TestUygulama(unittest.TestCase):
    def test_1_normal_calisma(self):
        sayilar = veri_oku("veriler.txt")
        sonuc = ozet_hesapla(sayilar)
        rapor_kaydet(sonuc, "test_rapor.txt")
        self.assertEqual(sonuc["adet"], 4)
        self.assertEqual(sonuc["toplam"], 99)
        self.assertEqual(sonuc["ortalama"], 25.0)
        self.assertTrue(os.path.exists("test_rapor.txt"))
        os.remove("test_rapor.txt")

    def test_2_bos_veri(self):
        sonuc = ozet_hesapla([])
        self.assertEqual(sonuc["adet"], 0)
        self.assertEqual(sonuc["ortalama"], 0.0)

    def test_3_hatali_veri(self):
        with open("bozuk.txt", "w", encoding="utf-8") as f:
            f.write("10\nabc\n30\n")
        with self.assertRaises(ValueError):
            veri_oku("bozuk.txt")
        os.remove("bozuk.txt")


if __name__ == "__main__":
    unittest.main()
