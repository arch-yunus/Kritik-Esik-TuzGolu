import numpy as np
import time

def simulate_spectral_trend(baseline_ndvi, intervention_type="LCHI"):
    """
    12 aylık NDVI ve MSI trend simülasyonu.
    Intervention types: 'TRADITIONAL', 'LCHI', 'NONE'
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    ndvi_trend = []
    msi_trend = []
    
    current_ndvi = baseline_ndvi
    current_msi = 1.2
    
    for i in range(12):
        # Seasonal noise
        noise = np.random.normal(0, 0.02)
        
        if intervention_type == "LCHI":
            # Halofit etkisi: Yavaş ama istikrarlı iyileşme
            current_ndvi += 0.03 + noise
            current_msi -= 0.05 + noise
        elif intervention_type == "TRADITIONAL":
            # Geleneksel tarım: Ani su tüketimi, yazın çöküş
            if 4 <= i <= 8: # Yaz ayları
                current_ndvi += 0.1 + noise
                current_msi += 0.15 + noise
            else:
                current_ndvi -= 0.05 + noise
                current_msi += 0.02 + noise
        else: # NONE
            current_ndvi -= 0.02 + noise
            current_msi += 0.04 + noise
            
        ndvi_trend.append(max(0, min(1, current_ndvi)))
        msi_trend.append(max(0, current_msi))
        
    return months, ndvi_trend, msi_trend

def display_simulation():
    print("--- 🛰️ KRITIK-ESIK: Spektral Zaman-Dizini Simülatörü ---")
    print("Senaryo: LCHI (Halofit Restorasyonu) vs Geleneksel (Mısır Tarımı)\n")
    
    months, lchi_n, lchi_m = simulate_spectral_trend(0.2, "LCHI")
    _, trad_n, trad_m = simulate_spectral_trend(0.2, "TRADITIONAL")
    
    print(f"{'Ay':<6} | {'LCHI NDVI':<10} | {'TRAD NDVI':<10} | {'LCHI MSI':<10} | {'TRAD MSI':<10}")
    print("-" * 60)
    for i in range(12):
        print(f"{months[i]:<6} | {lchi_n[i]:.3f}      | {trad_n[i]:.3f}      | {lchi_m[i]:.3f}      | {trad_m[i]:.3f}")

    print("\n[Analiz]: LCHI müdahalesi MSI (Moisture Stress) değerini 12 ay sonunda %.2f azaltırken," % (lchi_m[0] - lchi_m[-1]))
    print("Geleneksel tarım su stresini %.2f oranında artırmıştır (Akifer çöküş riski)." % (trad_m[-1] - trad_m[0]))

if __name__ == "__main__":
    display_simulation()
