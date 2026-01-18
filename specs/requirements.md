# 📐 Teknik Şartname (Technical Specs)

## 1. Proje Tanımı
**Sentries**, işletim sistemi güvenliği için tasarlanmış, dosya bütünlüğünü gerçek zamanlı izleyen bir otomasyon aracıdır.

## 2. Teknik Gereksinimler
- **Dil:** Python 3.8 ve üzeri
- **Platform:** Windows, Linux ve macOS uyumlu
- **Bağımlılıklar:** Harici kütüphane gerektirmez (Zero-Dependency).

## 3. Otomasyon Yetenekleri (Automation Specs)
Bu proje aşağıdaki SecOps yeteneklerini barındırır:

- **🛠️ Auto-Test (Self-Check):**
  Program `--test` parametresi ile başlatıldığında; disk okuma/yazma izinlerini ve dosya yolu erişimini otomatik olarak test eder.

- **📊 JSON-First Logging:**
  Tüm güvenlik olayları ve hata mesajları, makine tarafından okunabilir standart JSON formatında üretilir.

## 4. Güvenlik Sınırları
- Araç, sistem dosyalarını sadece "Okuma" (Read-Only) modunda izler, değişiklik yapmaz.
- CPU kullanımını optimize etmek için 2 saniyelik uyku (sleep) döngüsü kullanır.