
![Project Banner](assets/banner.png)

# 🛡️ KRİTİK-EŞİK-TUZGÖLÜ: Ekolojik Asimetri ve LCHI Tarım Manifestosu

> *"Doğa ile olan savaşımızda galip gelirsek, kaybedeceğiz. Bize gereken şey doğayı yenmek değil, onun asimetrik kurallarına düşük maliyetli, yüksek etkili (LCHI) ve akılcı bir tasarımla uyum sağlamaktır."*

## 📜 1. Felsefi Temel ve Doktrin: Ekolojik Asimetri
Tuz Gölü Havzası'ndaki çöküş, sadece su kıtlığı değil, **sistemsel bir simetri hatasıdır.** İnsanlık, doğanın doğrusal olmayan (non-linear) ve asimetrik gücüne karşı hantal, pahalı ve merkezi (simetrik) çözümlerle karşılık vermeye çalışmıştır. Bu manifesto, bu paradigmayı kökten reddeder.

### ⚔️ Simetri vs. Asimetri
*   **Simetrik Yaklaşım (Geleneksel):** Milyar dolarlık barajlar, kıtalararası su taşıma projeleri, yoğun enerji tüketen kimyasal gübreleme. Bu sistemler, doğanın kaosu karşısında kırılgandır (Fragile).
*   **Asimetrik Yaklaşım (LCHI):** Düşük maliyetli sensörler, uydu verisi ile otonom karar verme, doğanın "tuz" silahını ona karşı kullanan biyolojik ajanlar (Halofitler). Bu sistem, krizden beslenir ve uyum sağlar (Antifragile).

Bu araştırma deposu; "Tasarım Yoluyla Güvenlik" (Security by Design) ve "LCHI (Low-Cost-High-Impact)" prensiplerini tarıma uyarlayan bir mühendislik manifestosudur.

---

## 🚨 2. Krizin Anatomisi: Hidrolojik ve Kimyasal Kuşatma

### 💧 2.1. Hidrolojik İflas: Akifer Çöküşü
Havzada mısır ve şeker pancarı gibi yabancı türlerin dayatılması, yeraltı sularının "stratejik rezerv" statüsünden "tüketim metası" statüsüne indirilmesine yol açmıştır.
*   **Fiziksel Kanıt:** Yıllık 2-3 metrelik su düşüşleri, jeolojik stabiliteyi bozarak devasa obruklar (sinkholes) oluşturmaktadır. Obruklar, sistemin imdat çığlığıdır.
*   **Veri Körlüğü:** Sahada gerçek zamanlı veri akışı olmadığı için, kriz ancak "yüzeyde delik açıldığında" fark edilmektedir.

### 🧂 2.2. Beyaz Ölüm: Antropojenik Salinizasyon
Aşırı sulama, toprağın derinliklerindeki tuzu yüzeye taşıyarak "Kimyasal bir Albedo Etkisi" yaratmıştır.
*   **Taktiksel Tehdit:** Beyaz tuz tabakası güneş ışığını yansıtarak toprak sıcaklığını artırır ve mikro-klimayı çöle çevirir.
*   **Asimetrik Yayılım:** Kuruyan göl yatağından kalkan tuzlu tozlar, rüzgarla taşınarak "kimyasal bir sis" gibi verimli arazileri zehirler.

---

## ⚙️ 3. LCHI (Low-Cost-High-Impact) Çözüm Mimarisi

Sistem, üç ana asimetrik sütun üzerine inşa edilmiştir:

### 🌱 A. Biyolojik Taarruz: Halofit Doktrini
Tuzla savaşmak yerine, tuzu **ekonomik bir girdi** olarak kabul ediyoruz.
*   **Salicornia (Deniz Börülcesi):** Toprağı rehabilite eden asimetrik bir temizlik ajanı. Sıfır tatlı su ihtiyacı ile biyodizel ve gıda üretimi.
*   **Kinoa & Atriplex:** Kuraklık ve tuzluluğa karşı genetik bir savunma hattı.
*   **Fitoremediasyon:** Toprağın kimyasal yapısını biyolojik yolla "hacklemek".

### 📡 B. Dijital Gözlem: Edge-AI ve Dağıtık IoT
Milyonluk istasyonlar yerine, sahaya dağıtılan 10 dolarlık "su dervişleri":
*   **Donanım:** ESP32 tabanlı, LoRaWAN ile kilometrelerce veri basabilen, Deep Sleep modunda aylar boyu çalışan otonom düğümler.
*   **LCHI Sensör:** Kapasitif nem ve EC (iletkenlik) sensörleri ile toprağın nabzını tutmak.
*   **Asimetri:** Bir baraj maliyetine 10 milyon sensör sahaya sürülebilir; bu, sahanın mutlak veri hakimiyetidir.

### 🧠 C. Stratejik Karar: Core Engine (Sentinel & Water-AI)
*   **Sentinel Edge Engine:** Sentinel-2 verilerini işleyerek MSI (Moisture Stress Index) ve NDVI haritaları üretir. Gökyüzündeki gözümüzdür.
*   **Water-Rationing AI:** Q-Learning algoritmaları kullanarak, mevcut su bütçesini "en etkili asimetrik darbe" olacak şekilde sahaya dağıtır. Su, bir ihtiyaç değil, stratejik bir mühimmattır.

---

## 📂 4. Repo Hiyerarşisi (Directory Structure)

```text
├── 📊 data/                
│   ├── raw_satellite/         # Sentinel-2 ham spektral verileri
│   ├── ground_truth_iot/      # Dağıtık LCHI sensörlerinden gelen telemetri
│   └── climate_baseline/      # Sentetik ve gerçek iklim referansları (MGM/NASA)
├── 🔬 lchi_solutions/
│   ├── halophyte_manifesto.md # Tuzcul bitki üretim, genetik ve savunma rehberi
│   ├── open_sensor_hw/        # 10$ altı IoT sensör BOM listesi ve tasarımları
│   └── asymmetric_agri.md     # Kriz bölgeleri için ekonomik eylem planı
├── 💻 core_engine/
│   ├── sentinel_edge_calc.py  # MSI/NDVI/EVI hesaplayan spektral analiz motoru
│   ├── water_rationing_ai.py  # Otonom su kısıtlama optimizasyonu (Q-Learning)
│   └── firmware_esp32/        # Düşük güç tüketimli sensör yazılımları
├── 🎨 assets/                 # Görsel materyaller ve banner
├── 🗺️ risk_maps/               # GIS çıktıları ve risk analiz raporları
└── README.md
```

---

## 🗺️ 5. Taktiksel Yol Haritası (Roadmap)

1.  **Faz 1: Veri Keşfi:** Havzanın son 20 yıllık spektral değişiminin "Time-Lapse" analizi.
2.  **Faz 2: Dijital Baraj:** Pilot bölgelerde 100+ LCHI sensörünün konuşlandırılması ve LoRa ağının aktivasyonu.
3.  **Faz 3: Biyolojik Restorasyon:** Kritik eşiği aşan bölgelerde halofit ekim simülasyonları ve saha uygulaması.
4.  **Faz 4: Otonom Ekosistem:** Sistemin insan müdahalesinden bağımsız, veri akışına göre sulama ve rehabilitasyon kararları alması.
5.  **Faz 5: Biyo-Rafineri:** Hasat edilen halofitlerin yerinde (in-situ) işlenerek biyodizel ve protein izolatına dönüştürülmesi.

---

## 🛡️ 6. Tasarım Yoluyla Güvenlik (Security by Design)
Ekolojik sistemlerin savunması, siber güvenlik prensipleriyle yönetilmelidir:
*   **Zero Trust:** Sahadaki her veri düğümü, diğerleriyle kriptografik olarak doğrulanmalıdır.
*   **Redundancy (Yedeklilik):** Veri akışı kesilse bile, otonom vanalar "son güvenli durum" (safe mode) protokolüne geçmelidir.
*   **Defense in Depth:** Uydu verisi, yer sensörleri ve manuel gözlemlerle çok katmanlı bir doğrulama ağı.

---

## 🚀 7. Katılım Protokolü (Açık Çağrı)

Bu proje, bürokratik bir kurum değil, asimetrik bir mühendislik topluluğudur.
1.  **Kod ile Destek:** `core_engine` algoritmalarını optimize edin, daha hafif modeller geliştirin.
2.  **Donanım ile Destek:** LCHI sensör tasarımlarını daha ucuz ve dayanıklı hale getirin.
3.  **Veri ile Destek:** Yerel tohum verilerini ve toprak analizlerini `data` klasörüne işleyin.

---

## 📜 8. Gelecek Vizyonu: Halofit Karbon Yakalama
Tuz Gölü Havzası, sadece bir tarım alanı değil, dünyanın en büyük **mavi-karbon (blue-carbon)** yakalama merkezlerinden biri olma potansiyeline sahiptir. Halofit bitkiler, tuzu hapsederken atmosferdeki karbonu da toprağın derinliklerine gömer. LCHI doktrini ile bu süreci hızlandırıyoruz.

> *"Tuz Gölü, bir çöküşün değil; asimetrik mühendislik ile doğayı yeniden anlamanın sıfır noktası olacaktır."*
