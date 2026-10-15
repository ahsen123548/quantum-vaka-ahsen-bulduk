# quantum-vaka-ahsen-bulduk
# Quantum Team - Yazılım Birimi | İHA Hedef Tespiti Projesi (Vaka Çalışması 2026-2027)

Bu proje, Quantum Team Yazılım Birimi aday vaka çalışması kapsamında geliştirilmiştir. Projenin temel amacı, İHA kamerasından alınan görüntüler üzerinde **OpenCV** kullanarak belirli bir hedef alanı (kırmızı kare) otomatik olarak tespit etmek ve gerekli görsel/sayısal çıktıları sağlamaktır.

---

## 🚀 Proje Özellikleri

* **Görüntü İşleme:** OpenCV kütüphanesi kullanılarak renk uzayı dönüşümleri (örn. RGB -> HSV) ve maskeleme işlemleri gerçekleştirilmesi.
* **Hedef Tespiti:** İHA görüntülerindeki kırmızı kare hedef bölgelerinin filtrelenmesi, kontur (contour) analizi ile tespiti ve merkez koordinatlarının hesaplanması.
* **Modüler Mimari:** Kolay okunabilir, sürdürülebilir ve geliştirilebilir Python kod yapısı.

---

## 📁 Proje Klasör Yapısı

```text
ihare hedef-tespiti/
│
├── src/                  # Kaynak kodlar (Python betikleri)
│   ├── __init__.py
│   └── detector.py       # Görüntü işleme ve hedef tespiti modülü
│
├── assets/               # Test görselleri, örnek videolar ve çıktı sonuçları
│   └── test_image.jpg
│
├── .gitignore            # Git tarafından takip edilmeyecek dosyalar
├── requirements.txt      # Proje bağımlılıkları ve kütüphaneler
└── README.md             # Proje dokümantasyonu

