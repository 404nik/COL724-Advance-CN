# Total Order Multicasting and Network Management

This repository contains implementations of network management functionalities including total order multicasting, firewall monitoring, and load balancing in a Software-Defined Networking (SDN) environment using the Ryu framework.

## Getting Started

These instructions will help you set up and run the Total Order Multicasting system and other network management functionalities on your local machine.

### Prerequisites

To run this project, you'll need the following software:

- Python (3.x recommended)
- ZeroMQ (ØMQ) library
- Ryu SDN Framework
- Mininet
- `make` (optional, for convenience)

### Installation

1. **Python**: If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/).

2. **ZeroMQ**: You can install ZeroMQ via Python's package manager `pip`. Use the following command:
   ```bash
   pip install pyzmq
   ```

3. **Ryu**: You can install the Ryu SDN framework using `pip`. Use the following command:
   ```bash
   pip install ryu
   ```

4. **Mininet**: You can install Mininet by following the instructions on the [official Mininet website](http://mininet.org/download/).

## Usage

### Total Order Multicasting

- The main functionality of this system is to ensure that all nodes receive and process messages in the same order.
- Clients can specify the messages they want to send by creating a command file, and the system will handle the multicasting and total ordering.
- The results of this multicasting can be found in the `result` folder.
- Use the command `make` to run the code:
   ```bash
   make
   ```

### Firewall Monitor (`firewall_monitor.py`)

This code implements a firewall and monitoring functionality in an SDN controller using the Ryu framework. It restricts communication between specific hosts and counts the packets coming from a specific host.

#### Key Features:
- Blocks communication between specific hosts based on MAC addresses.
- Counts and logs packets coming from a specific host.
- Allows other communication and sends packets out to all ports (except the input port).

#### Commands:
- Run the Ryu application:
  ```bash
  ryu-manager ./firewall_monitor.py
  ```
- Run Mininet topology:
  ```bash
  sudo mn --custom topology.py --topo customTopology --controller remote
  ```

### Load Balancer (`load_balancer.py`)

This code implements a load balancer in an SDN controller using the Ryu framework. It balances traffic between two servers.

#### Key Features:
- Alternates traffic between two servers based on ARP requests.
- Adds flow entries to direct client traffic to the appropriate server.
- Sends ARP responses to clients with a virtual IP address mapped to the real MAC address of the chosen server.

#### Commands:
- Run the Ryu application:
  ```bash
  ryu-manager ./load_balancer.py
  ```
- Run Mininet topology:
  ```bash
  sudo mn --custom topology.py --topo customTopology --controller remote
  ```

## Report

For in-depth details about the implementation, design, and results of this project, please refer to the `report.pdf` file.

## Observations and Analysis

### Latency Values

#### Controller Type: `controller_hub`
- **h1 to h2:** avg 63.566 ms
- **h1 to h3:** avg 63.988 ms
- **h1 to h4:** avg 107.0 ms
- **h1 to h5:** avg 107.0 ms

#### Controller Type: `learning_switch`
- **h1 to h2:** avg 84.566 ms
- **h1 to h3:** avg 83.0 ms
- **h1 to h4:** avg 140.667 ms
- **h1 to h5:** avg 141.0 ms

### Throughput

#### Controller: Hub Controller
- **h1 to h5:** ~29.5 Mbits/sec
- **h5 to h1:** ~29 Mbits/sec

#### Controller: Learning Switch
- **h1 to h5:** ~35.6 Mbits/sec
- **h5 to h1:** ~35.2 Mbits/sec

### Analysis

The `learning_switch` setup generally shows lower latency and higher throughput compared to the `controller_hub` setup. This is due to the local decision-making capabilities of the learning switch, which reduces the need to involve the controller for every packet.

## Ways to Minimize Firewall Rules

1. **Implement Specific Allow Rules:** Configure specific rules to allow desired traffic between hosts.
2. **Use Wildcard Rules:** Create rules that cover multiple hosts or subnets.
3. **Apply Default Deny Policy:** Drop all traffic by default and explicitly allow only desired traffic.

## Dynamic Load Balancing

To implement dynamic load balancing without changing the provided code:
1. **Monitor Server Load:** Use metrics such as CPU usage, memory usage, or the number of active connections.
2. **Decision Logic:** Implement logic to choose the least loaded server.
3. **Periodic Load Checks:** Regularly check server loads and update decisions.
4. **Health Checks:** Ensure servers are available and responsive.
5. **Feedback Mechanism:** Gather statistics to optimize the load balancing algorithm.
6. **Configurability:** Provide options for configuring load balancing policies and thresholds.

Happy Networking! 🚀