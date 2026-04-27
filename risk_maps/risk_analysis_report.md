# 🗺️ Tuz Gölü Havzası Risk Analiz Raporu

Bu rapor, `core_engine/sentinel_edge_calc.py` tarafından işlenen spektral veriler ve sahada konuşlandırılan LCHI sensörlerinden gelen (simüle edilmiş) veriler ışığında hazırlanmıştır.

## 1. Mevcut Durum Özeti
- **Kritik Eşik (Tipping Point) Analizi:** Havzanın %18'lik bir bölümü "Geri Dönülemez Kuraklık" eşiğine girmiştir. 
- **Su Stresi (MSI):** Ortalama MSI değeri 1.45 (Normal eşik: < 0.8). Bitki örtüsü hayatta kalma sınırındadır.
- **Tuzlanma Etkisi:** Beyaz Albedo bölgeleri son 2 yılda %12 genişlemiştir.

## 2. Bölgesel Riskler
| Bölge ID | Bitki Sağlığı (EVI) | Su Stresi (MSI) | Risk Seviyesi | Önerilen Müdahale |
| :--- | :--- | :--- | :--- | :--- |
| **Zone_A (Kuzey)** | 0.12 | 1.85 | 🚨 KRİTİK | Acil Salicornia ekimi ve su kısıtlaması. |
| **Zone_B (Merkez)** | 0.35 | 1.10 | ⚠️ ORTA | Kinoa hibrit üretimi ve IoT takip. |
| **Zone_C (Güney)** | 0.55 | 0.75 | ✅ DÜŞÜK | Mevcut ekosistemin korunması (Halophyte Green Wall). |

## 3. LCHI Projeksiyonu
Asimetrik tarım yöntemleri (halofit rehabilitasyonu) uygulanması durumunda:
- **Su Tasarrufu:** Yıllık 4.2 milyon m³ (Geleneksel mısır tarımına kıyasla).
- **Toprak Rehabilitasyonu:** 3 yıl içinde tuz konsantrasyonunda %15 azalma öngörülmektedir.
