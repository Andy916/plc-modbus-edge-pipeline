# Industrial PLC-to-Edge Data Pipeline

A simulated end-to-end industrial control and data pipeline demonstrating Modbus TCP communication, edge processing, local HMI visualization, and enterprise MQTT publishing.

## Architecture
1. **Control Layer (Tier 2):** AutomationDirect Do-more PLC simulator running ladder logic to handle tank level monitoring and high-level safety alarms (`C0`).
2. **Field Simulation (Tier 1):** Python (`pymodbus`) script acting as an active sensor injector writing to holding register `MHR1`.
3. **Edge Processing (Tier 3):** Node-RED polling data over Modbus TCP, executing JavaScript state evaluation, and serving a real-time local HMI dashboard.
4. **Enterprise Integration (Tier 4):** Bifurcated data stream publishing structured JSON payloads to an MQTT broker.

## Tech Stack
* **PLC / Logic:** AutomationDirect Do-more Designer (Ladder Logic)
* **Protocols:** Modbus TCP, MQTT, JSON
* **Edge / UI:** Node-RED, FlowFuse Dashboard
* **Driver:** Python (`pymodbus`)
