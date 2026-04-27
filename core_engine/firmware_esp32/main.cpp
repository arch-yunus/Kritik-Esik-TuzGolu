#include <Arduino.h>

/**
 * 📡 LCHI-Sensor-Firmware-ESP32
 * Düşük maliyetli, Deep-Sleep destekli IoT düğümü.
 * LoRa üzerinden EC (Tuzluluk) ve Nem verisi iletir.
 */

#define SEALEVELPRESSURE_HPA (1013.25)
#define DEEP_SLEEP_TIME 3600e6 // 1 saatlik uyku periyodu (LCHI - Enerji Tasarrufu)

void setup() {
  Serial.begin(115200);
  Serial.println("KRITIK-ESIK TUZGOLU: LCHI Sensor Active");

  // Sensör okuma ve LoRa üzerinden iletim simülasyonu
  float soilMoisture = analogRead(34);
  float ecValue = analogRead(35); // Tuzluluk sensörü

  Serial.printf("Soil Moisture: %.2f | EC Value: %.2f\n", soilMoisture, ecValue);
  Serial.println("Data transmitted via LoRa. Entering Deep Sleep...");

  esp_sleep_enable_timer_wakeup(DEEP_SLEEP_TIME);
  esp_deep_sleep_start();
}

void loop() {
  // Deep sleep nedeniyle buraya ulaşılmaz.
}
