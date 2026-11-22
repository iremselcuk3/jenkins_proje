import os


def veri_oku(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        raise FileNotFoundError(f"Hata: '{dosya_yolu}' dosyasi bulunamadi.")
    sayilar = []
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        for satir_no, satir in enumerate(f, start=1):
            temiz = satir.strip()
            if not temiz:
                continue
            try:
                sayilar.append(float(temiz))
            except ValueError:
                raise ValueError(f"Hata: {satir_no}. satirda gecersiz sayi var -> '{temiz}'")
    return sayilar


def ozet_hesapla(sayilar):
    if not sayilar:
        return {"adet": 0, "toplam": 0.0, "ortalama": 0.0, "min": 0.0, "max": 0.0}
    toplam = sum(sayilar)
    return {
        "adet": len(sayilar),
        "toplam": toplam,
        "ortalama": toplam / len(sayilar),
        "min": min(sayilar),
        "max": max(sayilar),
    }


def rapor_kaydet(ozet, cikti_yolu="ozet_rapor.txt"):
    with open(cikti_yolu, "w", encoding="utf-8") as f:
        f.write(f"Adet: {ozet['adet']}\n")
        f.write(f"Toplam: {ozet['toplam']}\n")
        f.write(f"Ortalama: {ozet['ortalama']}\n")
        f.write(f"Min: {ozet['min']}\n")
        f.write(f"Max: {ozet['max']}\n")


if __name__ == "__main__":
    veriler = veri_oku("veriler.txt")
    sonuc = ozet_hesapla(veriler)
    rapor_kaydet(sonuc)
    print("Islem tamamlandi:", sonuc)
    print("Rapor icerigi:")
    with open("ozet_rapor.txt", "r", encoding="utf-8") as r:
        print(r.read())
