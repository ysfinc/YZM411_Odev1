# YZM411 Ödev 1 – Renk, Aydınlatma ve Örnekleme

## Klasör
| Dosya | İçerik |
|---|---|
| `odev1.ipynb` | Tüm deneyler (Adım 4–7), rapor PDF'i ve teslim ZIP'ini üretir |
| `ayarlar.json` | Fotoğraf yolları, nesne/piksel/yazı koordinatları, b, γ, küçültme oranı |
| `metin.json` | **Sizin** tahminleriniz, yorumlarınız, iki sorunun cevabı, YZ beyanı |
| `foto/` | `normal.jpg`, `golge.jpg`, `lamba.jpg` (kendi çekiminiz) |
| `cikti/` | Notebook'un ürettiği ham sonuçlar (CSV, maskeler, şekiller, esikler.json) |

## Çalıştırma sırası
1. **Çekim:** Masaya renkli bir nesne + beyaz/gri kâğıt + küçük yazılı/çizgili bir bölge koyun. Telefonu sabitleyin, 3 fotoğraf çekin: normal ışık, gölge, farklı lamba. Mümkünse "Pro/Manuel" modda pozlama ve beyaz dengesini kilitleyin; kilitleyemiyorsanız `metin.json → kamera_notu`'na yazın. Kişi görünmesin.
2. Fotoğrafları `foto/normal.jpg`, `foto/golge.jpg`, `foto/lamba.jpg` adıyla koyun.
3. `metin.json` içindeki 4 **tahmin** alanını *çalıştırmadan önce* kendi cümlelerinizle yazın (TASLAK yazısını silin).
4. Paketler: `pip install numpy opencv-python pandas matplotlib pillow jupyter`
5. Notebook'u bir kez çalıştırın → `cikti/koordinat_izgarasi.png`'ye bakıp `ayarlar.json`'daki
   `nesne_ornek_kutu` (nesnenin içinden küçük kare), `nesne_tam_kutu` (nesnenin tamamı, isteğe bağlı), `pikseller` (3 nokta, `[x, y]`) ve `yazi_kutu`'yu doldurun.
   `ogrenci_no`'yu yazın.
6. *Restart & Run All*. Sonuçları okuyun, `metin.json`'da `ne_gordum / neden / kontrol`, iki soru, `tutmayan_tahmin` alanlarını doldurun.
7. Son iki hücreyi tekrar çalıştırın → `YZM411_Odev1_<No>_rapor.pdf` ve `YZM411_Odev1_<No>.zip`.
   PDF'te kırmızı yazı kalmadığından emin olun. PDF'i GitHub'a da yükleyin.

Komut satırından tek seferde: `jupyter nbconvert --to notebook --execute --inplace odev1.ipynb`
