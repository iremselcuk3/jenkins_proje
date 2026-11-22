#!/bin/bash
set -e

echo "1. On kosullar kontrol ediliyor..."
if ! command -v python3 &> /dev/null; then
    echo "HATA: Sistemde python3 yuklu degil!"
    exit 1
fi

if [ ! -f "veriler.txt" ]; then
    echo "HATA: veriler.txt dosyasi bulunamadi!"
    exit 1
fi

echo "2. Otomatik testler calistiriliyor..."
python3 -m unittest discover -v

echo "3. Testler basarili! Uygulama paketleniyor..."
mkdir -p dist
tar -czf dist/uygulama_paketi.tar.gz app.py test_app.py veriler.txt calistir.sh
echo "BASARILI: Paket dist/uygulama_paketi.tar.gz konumunda olusturuldu."
