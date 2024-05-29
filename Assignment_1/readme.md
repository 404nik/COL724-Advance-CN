# Network Performance Analysis

This repository contains an analysis of network performance with varying router buffer sizes. The analysis is performed using emulation techniques to understand the impact of buffer sizes on webpage fetch times, and it explores the concept of bufferbloat and its mitigation strategies.

## Analysis Summary

### Q1: Difference in Webpage Fetch Times with Short and Large Router Buffers

**Observation:**
- **Small Queue Size (q = 20):**
  - **Average Download Time:** 0.471766336667 seconds
  - **Standard Deviation:** 0.1142553523452
- **Large Queue Size (q = 100):**
  - **Average Download Time:** 1.05357666667 seconds
  - **Standard Deviation:** 0.532673052904

**Explanation:**
When the queue size is large, TCP's congestion window expands, sending more packets, which increases download times due to additional delays. Conversely, with a small queue size, TCP reduces its congestion window frequently, resulting in faster webpage fetch times.

### Q2: Transmit Queue Length on Network Interface

**Observation:**
The maximum transmit queue length on the network interface (e.g., eth0) is reported by `ifconfig`.

**Calculation:**
- **Transmit Queue Length:** 1000 packets
- **Packet Size:** 1500 bytes
- **Buffered Data:** 1.5 * 10^6 bytes
- **Network Speed:** 100 Mbps (1.25 * 10^7 bytes/s)
- **Maximum Wait Time:** 0.12 seconds

### Q3: RTT Variation with Queue Size

**Observation:**
RTT increases with queue size.

**Explanation:**
RTT = queue_size * propagation_delay. As the propagation delay is constant, increasing the queue size directly increases the RTT.

### Q4: Mitigating Bufferbloat

**Strategies:**
1. **Adjust Maximum Queue Size:**
   - Reducing the maximum queue size limits buffering and reduces RTT.
2. **Active Queue Management (AQM):**
   - Techniques like Random Early Detection (RED) drop packets early based on probability, preventing bufferbloat.

### Q5: Results after Re-running Emulation with Mitigation Strategies

**Observation:**
Re-running the emulation with buffer size control and AQM techniques shows reduced latency and improved network responsiveness.

**Explanation:**
By controlling queue size and implementing AQM, congestion is better managed, leading to a more efficient network.

## Conclusion

The analysis demonstrates the impact of router buffer sizes on network performance, highlighting the problem of bufferbloat and effective mitigation strategies. Implementing these strategies results in significant improvements in network latency and responsiveness.
