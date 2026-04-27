# 🌾 Tuz Gölü Havzası Tarım Rehberi (LCHI Doktrini)

Bu rehber, Tuz Gölü Havzası'ndaki ekolojik çöküşü durdurmak ve bölge ekonomisini asimetrik yöntemlerle yeniden canlandırmak için hazırlanmıştır.

---

## 🧐 1. Neden LCHI Tarım?
Geleneksel tarım (mısır, şeker pancarı) havzayı kuruturken, LCHI (Düşük Maliyetli, Yüksek Etkili) tarım:
- **Su Tüketimini %90 Azaltır.**
- **Toprağı Tuzdan Arındırır.**
- **Maksimum Ekonomik Getiri Sağlar.**

---

## 🌱 2. Hangi Bitkiler Ekilmeli? (Tür Seçimi)

Havzanın "Kritik Eşik" durumuna göre 3 ana katman belirlenmiştir:

| Tür | Uygunluk | Fonksiyon | Ekonomik Çıktı |
| :--- | :--- | :--- | :--- |
| **Salicornia (Deniz Börülcesi)** | Ekstrem Tuzlu (Göl Kenarı) | Tuz Emici (Fitoremediasyon) | Biyodizel, Premium Gıda |
| **Kinoa (Real/Puno Varyeteleri)** | Orta/Yüksek Tuzlu | Dayanıklı Gıda Mahsulü | İhracatlık Tahıl, Glütensiz Gıda |
| **Atriplex (Tuz Çalısı)** | Orta Tuzlu / Rüzgarlı | Yeşil Duvar & Erozyon Kontrolü | Yüksek Proteinli Hayvan Yemi |
| **Hordeum vulgare (Tuzcul Arpa)** | Düşük/Orta Tuzlu | Geleneksel Tarım Dönüşümü | Maltlık Arpa, Yem |

---

## ⚙️ 3. Nasıl Yapılmalı? (Uygulama Protokolü)

### 🛰️ A. Spektral Haritalama (Önce Görüntüle)
Ekim yapmadan önce `core_engine/sentinel_edge_calc.py` kullanarak arazinizin MSI (Nem Stresi) ve NDVI (Bitki Sağlığı) haritalarını çıkarın.

### 💧 B. Su Yönetimi (Damla Sulama + AI)
- Asla vahşi sulama yapmayın.
- `core_engine/water_rationing_ai.py` üzerinden önerilen sulama bütçesine sadık kalın.

### 📡 C. IoT Sensör Takibi
- Her 10 dekara en az bir `LCHI-IoT` düğümü yerleştirin.
- EC (İletkenlik) değerini takip ederek toprağın tuzlanma hızını izleyin.

---

## 📈 4. Ekonomik Strateji ve Pazarlama
1. **Sertifikasyon:** LCHI tarımı ile üretilen ürünler "Ekolojik Restorasyon Ürünü" olarak markalanmalıdır.
2. **Biyo-Rafineri:** `Salicornia` hasat edildikten sonra ya gıda endüstrisine (taze/kurutulmuş) ya da biyodizel üretimine yönlendirilmelidir.
3. **Pazara Erişim:** Yerel kooperatifler aracılığıyla büyük zincir marketlere "Tuz Gölü Koruyucusu" etiketiyle sunulmalıdır.

---

> *"Tuz, bir lanet değil; doğru mühendislik ile geleceğin beyaz mirasıdır."*
