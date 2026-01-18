# 📘 Sentries - Kullanıcı ve Kurulum Kılavuzu

## 1. Proje Hakkında
**Sentries**, işletim sistemindeki kritik dosyaların güvenliğini sağlamak amacıyla geliştirilmiş açık kaynaklı bir "Dosya Bütünlüğü İzleme" (FIM) aracıdır.

## 2. Kurulum
Bu aracı çalıştırmak için ekstra bir kütüphane kurmanıza gerek yoktur (Zero-Dependency). Python yüklü olması yeterlidir.

1. Projeyi indirin.
2. Terminali açın ve proje klasörüne girin.

## 3. Kullanım Komutları

### 🟢 İzleme Modu (Canlı Takip)
Programı normal modda çalıştırmak için:
`python src/main.py`
> Bu modda araç, klasöre eklenen veya silinen dosyaları anlık olarak algılar ve ekrana basar.

### 🟡 Test Modu (Self-Check)
Sistemin düzgün çalışıp çalışmadığını kontrol etmek için:
`python src/main.py --test`
> Bu komut, okuma/yazma izinlerini kontrol eder ve `[BASARILI]` sonucunu döndürür.

## 4. Sorun Giderme
- **Hata:** "Permission Denied"
  - **Çözüm:** Terminali yönetici olarak çalıştırın.
- **Hata:** "Python bulunamadı"
  - **Çözüm:** Python'un PATH'e ekli olduğundan emin olun.

---
**Geliştirici:** Ali Baran Berktas
**Versiyon:** 1.0.0