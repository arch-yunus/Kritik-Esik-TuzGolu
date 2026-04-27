# 🛠️ LCHI Sensor Node V1 - Bill of Materials (BOM)

Bu liste, $10 bütçe hedefine sadık kalarak oluşturulmuş, yüksek etkili toprak izleme düğümü için gerekli bileşenleri içerir.

| Bileşen | Model/Açıklama | Tahmini Maliyet | Fonksiyon |
| :--- | :--- | :--- | :--- |
| **MCU** | ESP32-WROOM-32 | $3.50 | Ana işlemci ve WiFi/BT |
| **İletişim** | Ra-02 LoRa Module (SX1278) | $3.00 | Uzun mesafe düşük güç veri iletimi |
| **Nem Sensörü** | Capacitive Soil Moisture V1.2 | $1.00 | Korozyona dirençli toprak nem ölçümü |
| **Tuzluluk (EC)** | DIY Stainless Steel Probe + ADC | $0.50 | Toprak iletkenliği (Tuzluluk) |
| **Güç Yönetimi** | TP4056 + 18650 Holder | $1.00 | Solar şarj ve batarya yönetimi |
| **Gövde** | 3D Printed PETG / PVC Pipe | $1.00 | Saha koruması |
| **TOPLAM** | | **$10.00** | |

## Montaj ve Devre Notları
- **Güç Tasarrufu:** ESP32 Deep Sleep modu kullanılarak pil ömrü 6+ aya çıkarılmalıdır.
- **Kalibrasyon:** EC sensörü, distile su ve standart tuz çözeltileri ile sahaya çıkmadan önce kalibre edilmelidir.
- **Anten:** LoRa modülü için 433MHz/868MHz yay (spring) anten verimi artıracaktır.
