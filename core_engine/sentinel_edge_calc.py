import numpy as np

def calculate_ndvi(red_band, nir_band):
    """
    Normalize Difference Vegetation Index (NDVI)
    Bitki canlılığı ve yoğunluğu.
    """
    return (nir_band - red_band) / (nir_band + red_band + 1e-8)

def calculate_ndwi(green_band, nir_band):
    """
    Normalized Difference Water Index (NDWI)
    Yüzey suyu ve bitki su içeriği.
    """
    return (green_band - nir_band) / (green_band + nir_band + 1e-8)

def calculate_msi(swir_band, nir_band):
    """
    Moisture Stress Index (MSI)
    Bitki yapraklarındaki su stresi (Yüksek değer = Yüksek stres).
    Formula: SWIR / NIR
    """
    return swir_band / (nir_band + 1e-8)

def calculate_evi(blue_band, red_band, nir_band):
    """
    Enhanced Vegetation Index (EVI)
    Atmosferik etkileri normalize edilmiş bitki indeksi.
    """
    C1, C2, L = 6.0, 7.5, 1.0
    return 2.5 * ((nir_band - red_band) / (nir_band + C1 * red_band - C2 * blue_band + L + 1e-8))

def process_sentinel_data(bands):
    """
    Havza geneli spektral analiz ve LCHI raporlama.
    """
    red = bands['B04']
    nir = bands['B08']
    green = bands['B03']
    blue = bands['B02']
    swir = bands['B11']
    
    ndvi = calculate_ndvi(red, nir)
    ndwi = calculate_ndwi(green, nir)
    msi = calculate_msi(swir, nir)
    evi = calculate_evi(blue, red, nir)
    
    # Çok Boyutlu Risk Eşiği
    # NDVI düşük, MSI yüksekse bitki hem cansız hem de susuzdur.
    critical_stress = (ndvi < 0.25) & (msi > 1.2)
    
    return {
        'indices': {
            'NDVI': ndvi,
            'NDWI': ndwi,
            'MSI': msi,
            'EVI': evi
        },
        'risk_assessment': {
            'critical_areas_count': np.sum(critical_stress),
            'mean_water_stress': np.mean(msi),
            'vegetation_health_score': np.mean(evi)
        }
    }

if __name__ == "__main__":
    # Test Verisi (Düşük bitki örtüsü, yüksek su stresi senaryosu)
    print("--- LCHI Sentinel Edge Engine Testing ---")
    dummy_bands = {
        'B04': np.random.uniform(0.1, 0.4, (100, 100)), # Red
        'B08': np.random.uniform(0.1, 0.5, (100, 100)), # NIR
        'B03': np.random.uniform(0.1, 0.3, (100, 100)), # Green
        'B02': np.random.uniform(0.05, 0.2, (100, 100)),# Blue
        'B11': np.random.uniform(0.2, 0.6, (100, 100))  # SWIR
    }
    
    report = process_sentinel_data(dummy_bands)
    print(f"Risk Assessment: {report['risk_assessment']}")
