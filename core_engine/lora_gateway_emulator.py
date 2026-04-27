import random
import json
import time

class LoRaGatewayEmulator:
    """
    Havza geneline yayılmış 100+ LCHI sensöründen veri toplayan gateway emülatörü.
    """
    def __init__(self, node_count=100):
        self.node_count = node_count
        self.regions = ["ZONE_A_NORTH", "ZONE_B_CENTER", "ZONE_C_SOUTH"]
        
    def generate_sensor_payload(self, node_id):
        region = random.choice(self.regions)
        return {
            "node_id": f"LCHI-{node_id:03d}",
            "region": region,
            "telemetry": {
                "soil_moisture": round(random.uniform(5.0, 45.0), 2),
                "salinity_ec": round(random.uniform(0.1, 4.5), 2),
                "battery_v": round(random.uniform(3.3, 4.2), 2)
            },
            "timestamp": int(time.time()),
            "rssi": random.randint(-120, -60)
        }

    def run_batch_cycle(self):
        print(f"--- 📡 LoRaWAN Gateway Emulator: Batch Cycle Start ({self.node_count} nodes) ---")
        payloads = []
        for i in range(self.node_count):
            payloads.append(self.generate_sensor_payload(i))
        
        # Kritik Eşik Filtreleme (Salinity > 3.0 or Moisture < 10.0)
        alerts = [p for p in payloads if p['telemetry']['salinity_ec'] > 3.0 or p['telemetry']['soil_moisture'] < 10.0]
        
        print(f"Total Nodes Received: {len(payloads)}")
        print(f"Critical Alerts Triggered: {len(alerts)}")
        
        if alerts:
            print("\nSAMPLE ALERT DATA (LCHI-Protocol Violation):")
            print(json.dumps(alerts[0], indent=2))

if __name__ == "__main__":
    gw = LoRaGatewayEmulator(node_count=120)
    gw.run_batch_cycle()
