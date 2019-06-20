# Nama
KKP-OCR

## Deskripsi
KKP-OCR adalah sebuah program OCR untuk mengambil data bujur(Degree, Minute, Second) dan Lintang(Degree, Minute, Second) dari Peta Prakiraan Daerah Penangkapan Ikan (PPDPI) Kementrian Kelautan dan Perikanan (KKP) Republik Indonesia.
untuk PPDI bisa didapatkan dari website resmi [KKP](https://kkp.go.id/kategori/164-Peta-Prakiraan-Daerah-Penangkapan-Ikan)

## Instalasi
```bash
pip install pillow pytesseract
```
## Cara Menggunakan
```bash
python crop.py
```
output dari file ini adalah file longlat.txt. file longlat.txt berisi data longitude,latitude yang didapatkan dari konversi nilai bujur dan lintang
