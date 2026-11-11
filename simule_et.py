"""Gölge ve lamba koşullarını TEK gerçek fotoğraftan (foto/normal.jpg) dijital olarak simüle eder.

UYARI: Bu görüntüler gerçek çekim DEĞİLDİR. Işık etkisi doğrusal (lineer) ışık uzayında
kanal kazançlarıyla çarpılarak modellenmiştir; gerçek gölgedeki yumuşak kenar, çoklu yansıma,
kameranın otomatik pozlama/beyaz dengesi tepkisi ve sensör davranışı yalnızca kabaca taklit edilir.
Bu nedenle Adım 4–5'te gölge/lamba ölçümleri, gerçek ışığı değil buradaki modeli ölçer.

Çalıştırma: python simule_et.py   (foto/golge_SIMULE.jpg ve foto/lamba_SIMULE.jpg üretir)
"""
import numpy as np
import cv2

TOHUM = 411
GOLGE_KAZANC = (0.30, 0.33, 0.40)   # R, G, B – lineer ışıkta; gölgede gökyüzü ışığı baskın -> maviye kayma
LAMBA_KAZANC = (1.10, 0.80, 0.45)   # R, G, B – lineer ışıkta; ~3000 K akkor/sıcak lamba benzeri
LAMBA_MERKEZ = (0.15, 0.10)         # lamba sol üstte (göreli x, y) -> ışık azalması
GURULTU_STD = 2.0                   # 8 bit gürültü (sensör)


def srgb_to_lin(u8):
    c = u8.astype(np.float64) / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def lin_to_srgb(lin):
    lin = np.clip(lin, 0, 1)
    c = np.where(lin <= 0.0031308, lin * 12.92, 1.055 * lin ** (1 / 2.4) - 0.055)
    return c * 255.0


def kaydet(yol, rgb_float, rng):
    out = np.clip(np.round(rgb_float + rng.normal(0, GURULTU_STD, rgb_float.shape)), 0, 255).astype(np.uint8)
    cv2.imencode(".jpg", cv2.cvtColor(out, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 95])[1].tofile(yol)


def main():
    rng = np.random.default_rng(TOHUM)
    bgr = cv2.imdecode(np.fromfile("foto/normal.jpg", np.uint8), cv2.IMREAD_COLOR)
    lin = srgb_to_lin(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))
    H, W = lin.shape[:2]
    yy, xx = np.mgrid[0:H, 0:W] / max(H, W)

    # Gölge: sahnenin büyük kısmını kaplayan, yumuşak kenarlı (bulanık) bir gölge; sağ üst köşe gölge dışında
    maske = np.ones((H, W), np.float32)
    maske[: int(0.18 * H), int(0.80 * W):] = 0
    maske = cv2.GaussianBlur(maske, (0, 0), sigmaX=0.03 * W)[..., None]
    kazanc = 1 + maske * (np.array(GOLGE_KAZANC) - 1)
    kaydet("foto/golge_SIMULE.jpg", lin_to_srgb(lin * kazanc), rng)

    # Lamba: sıcak renk + noktasal kaynaktan uzaklıkla azalan ışık
    d2 = (xx - LAMBA_MERKEZ[0]) ** 2 + (yy - LAMBA_MERKEZ[1]) ** 2
    azalma = (1.0 / (1.0 + 2.5 * d2))[..., None]
    kaydet("foto/lamba_SIMULE.jpg", lin_to_srgb(lin * np.array(LAMBA_KAZANC) * azalma * 1.25), rng)
    print("yazıldı: foto/golge_SIMULE.jpg, foto/lamba_SIMULE.jpg")


if __name__ == "__main__":
    main()
