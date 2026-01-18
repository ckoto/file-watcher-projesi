# 🧪 Deep Research Report: File Integrity Monitoring (FIM) Systems

**Project:** Sentries (File Watcher)
**Date:** January 18, 2026
**Topic:** Building a Lightweight SecOps Automation Tool

---

## 1. Araştırma Özeti (Executive Summary)
Bu proje kapsamında, dosya bütünlüğünü izleyen (File Integrity Monitoring - FIM) ve değişiklik anında aksiyon alan bir otomasyon aracı geliştirilmesi hedeflenmiştir. Farklı yapay zeka modelleri ile yapılan teknik analizler sonucunda, performans ve taşınabilirlik açısından **Python** tabanlı bir çözümde karar kılınmıştır.

---

## 2. AI Model Analizleri (Multi-Model Analysis)

Proje mimarisine karar verirken aşağıdaki yapay zeka modellerinden teknik görüş alınmıştır:

### 🤖 Gemini Advanced (Google) Analizi
**Sorgu:** "Modern SecOps süreçlerinde dosya izleme (file watching) araçlarının önemi ve kullanım alanları nedir?"
**Analiz Özeti:**
Gemini, siber güvenlikte "FIM" (File Integrity Monitoring) kavramının kritik olduğunu belirtti. Özellikle konfigürasyon dosyalarının (`/etc/`, `web.config` vb.) izinsiz değiştirilmesinin, bir siber saldırının ilk işareti olabileceğini vurguladı.
* **Öneri:** Aracın sadece log tutması yetmez, çıktılarının **JSON** formatında olması gerekir. Böylece bu çıktılar SIEM (Security Information and Event Management) sistemlerine beslenebilir.

### 🤖 ChatGPT 4o (OpenAI) Analizi
**Sorgu:** "Python ile dosya takibi yapmak için kütüphane karşılaştırması: Watchdog vs Native OS vs Polling"
**Analiz Özeti:**
ChatGPT, üç farklı yöntemi karşılaştırdı:
1.  **Native APIs (inotify/ReadDirectoryChangesW):** En hızlısı ama platforma bağımlı (Linux/Windows ayrı kod gerektirir).
2.  **Watchdog Kütüphanesi:** Çok popüler ama ekstra kurulum (`pip install`) gerektirir.
3.  **Polling (os.listdir ile döngü):** En basiti ve dış bağımlılık gerektirmez.
* **Öneri:** Bir öğrenci projesi ve "taşınabilirlik" için 3. yöntem (Polling) veya basit bir `diff` algoritması başlangıç için en uygunudur.

### 🤖 Claude 3.5 Sonnet (Anthropic) Analizi
**Sorgu:** "CLI araçlarında 'Auto-Test' ve 'Self-Check' özellikleri nasıl tasarlanmalı?"
**Analiz Özeti:**
Claude, güvenilir bir SecOps aracının "fail-safe" olması gerektiğini belirtti.
* **Strateji:** Kodun içine `--test` bayrağı eklenmeli. Bu bayrak çalıştığında program ana döngüye girmeden önce:
    * Okuma/Yazma izinlerini kontrol etmeli.
    * Log dosyasının oluşturulabilir olduğunu doğrulamalıdır.
    * Sistem kaynaklarını (RAM/CPU) kontrol etmelidir.

---

## 3. Teknik Karar (Final Decision)

Yapılan araştırmalar sonucunda **Zero-Dependency (Bağımlılıksız)** yaklaşımı benimsenmiştir.

* **Dil:** Python 3.x (Her sistemde yüklü olduğu için).
* **Yöntem:** `os.listdir` ve `Set` (Küme) veri yapıları kullanılarak değişiklik algılama.
* **Veri Formatı:** Tüm çıktılar JSON standardında (Gemini önerisi).
* **Test:** `--test` parametresi ile entegre self-check mekanizması (Claude önerisi).

## 4. Referanslar
* *Python Docs - OS Interface*
* *OWASP File Integrity Monitoring Guidelines*
* *SANS Institute - SecOps Automation Papers*