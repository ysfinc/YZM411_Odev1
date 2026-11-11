# Kaynak beyanı – YZM411 Ödev 1 – 230212010

## Veri
- foto/normal.jpg, foto/golge.jpg, foto/lamba.jpg: kendi çekimim, sabit kamera ve nesne konumu.
- Kamera notu: Tek gerçek fotoğraf (telefon, masa üstünde siyah fare + bej ahşap masa). Fotoğraf sohbet üzerinden .webp olarak aktarıldığı için EXIF silinmiş (cikti/exif.csv boş): otomatik pozlama/beyaz dengesi bilinmiyor. Gölge ve lamba görüntüleri gerçek çekim değil, simule_et.py ile üretildi; bu yüzden 'yalnızca ışık değişti' iddiası gerçek sahne için değil, yalnızca simülasyon modeli için geçerli. Sahnede renkli nesne olarak bej masa yüzeyi, yazı olarak faredeki 'logi' logosu kullanıldı.
- EXIF özeti: cikti/exif.csv

## Kaynaklar
- YZM 411 ders notları, Hafta 1–2 (görüntünün sayısal temsili, renk uzayları, örnekleme).
- OpenCV belgeleri: cvtColor (BGR↔RGB/HSV, 8 bit HSV'de H 0–179), inRange, resize (INTER_NEAREST, INTER_AREA).

## Yapay zekâ beyanı
Araç: Claude (Anthropic), Claude Code. Amaç: odev1.ipynb'nin tüm kodunun, simule_et.py'nin (gölge ve lamba görüntülerini tek gerçek fotoğraftan üretir), koordinat seçiminin ve metin.json'daki tahmin ile yorum metinlerinin yazılması. Tahminler notebook çalıştırılmadan önce yazıldı; yorumlar ölçülen sayılardan (cikti/*.csv) türetildi. Etkilediği dosyalar: tüm .ipynb hücreleri, simule_et.py, ayarlar.json, metin.json. Doğrulama: notebook baştan sona çalıştırıldı, 64→127,7/16,1 gama kontrolü, BGR/RGB eşitlik kontrolü (assert) ve kırpılma kaybı ayrı formülle doğrulandı. SINIRLILIK: gölge ve lamba gerçek çekim değildir.

## Ortam
- python: 3.12.10
- numpy: 2.2.6
- opencv: 4.12.0
- pandas: 2.3.3
- matplotlib: 3.10.8
- pillow: 11.3.0
- platform: Windows-11-10.0.26200-SP0
- calistirma_zamani: 2026-11-11T12:38:42