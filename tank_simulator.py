from pymodbus.client import ModbusTcpClient
import time
import random

PLC_IP = "172.24.240.1"
PLC_PORT = 502

client = ModbusTcpClient(PLC_IP, port=PLC_PORT)
if not client.connect():
    print("Failed to connect to Do-more simulator.")
    exit()

print("Connected to PLC! Simulating tank level...")

try:
    tank_level = 20
    while True:
        # Simulate fluid rising and falling naturally
        tank_level += random.randint(-2, 5)
        if tank_level > 95:
            tank_level = 20  # Reset cycle when 'full'
        if tank_level < 10:
            tank_level = 10

        # Write current level to Holding Register address 0 (MHR1)
        write_result = client.write_register(address=0, value=int(tank_level), device_id=1)
        
        if write_result.isError():
            print("Error writing to PLC register.")
        else:
            print(f"Injected Tank Level -> MHR1: {tank_level}%")

        time.sleep(2)

except KeyboardInterrupt:
    client.close()
    print("Simulation stopped.")