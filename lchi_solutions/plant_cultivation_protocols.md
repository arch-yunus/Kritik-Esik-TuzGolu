# 🚜 Bitki Üretim ve Yetiştirme Protokolleri (LCHI-Agri)

Tuz Gölü Havzası'nın asimetrik koşullarında başarılı bir üretim için düşük maliyetli ama yüksek hassasiyetli bu protokoller uygulanmalıdır.

---

## 1. Salicornia (Deniz Börülcesi) Protokolü
*   **Toprak Hazırlığı:** Ağır tuzlanmış (Albedo > 0.7) arazilerde minimum toprak işleme.
*   **Ekim Zamanı:** Mart - Nisan sonu (Don riski geçtikten sonra).
*   **Ekim Derinliği:** 0.5 - 1 cm.
*   **Sulama:** Sadece çimlenme aşamasında hafif nemlendirme. Sonrasında kanal suları veya tuzlu yeraltı suyu ile devam edilebilir.
*   **LCHI Notu:** Hiçbir kimyasal gübre gerekmez; bitki ihtiyacı olan mineralleri tuzlu topraktan çeker.

## 2. Kinoa (Chenopodium quinoa) Protokolü
*   **Tür Seçimi:** Tuz toleransı yüksek "Real" veya "Puno" varyeteleri.
*   **Ekim Sıklığı:** Dekara 400-600 gram tohum (LCHI felsefesi: Tohum israfını önle).
*   **Su Yönetimi:** `core_engine/water_rationing_ai.py` kararlarına göre sulama. Çiçeklenme döneminde su stresi minimize edilmelidir.
*   **Hasat:** Bitki sararıp tohumlar tırnakla ezilmeyecek sertliğe ulaştığında.

## 3. Atriplex (Tuz Çalısı) Protokolü
*   **Konumlandırma:** Hakim rüzgar yönüne dik, tarla sınırlarına set (Hedge) şeklinde.
*   **Fidan Üretimi:** LCHI prensibi gereği, tohumdan sera yerine doğrudan sahada fideleme tercih edilir.
*   **Hayvan Yemi:** Hasat edilen yapraklar doğrudan kurutularak veya silaj yapılarak yüksek proteinli yem olarak kullanılır.

---

## 🛡️ LCHI Güvenlik ve Verimlilik Notları
1.  **Drenaj:** Sahada su birikmesi (Göllenme) halofitlerin köklerini çürütür; drenaj kanalları minimal ama efektif tutulmalıdır.
2.  **Veri Takibi:** Her üretim parseli en az bir `LCHI-IoT` düğümü ile anlık izlenmelidir.
3.  **Tohum Saklama:** Hasat edilen ürünlerin bir kısmı, asimetrik bir yedeklilik (Redundancy) sağlamak için tohum bankasına ayrılmalıdır.
