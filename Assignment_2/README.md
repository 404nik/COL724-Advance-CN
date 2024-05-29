# Total Order Multicasting

Total Order Multicasting is a communication system that guarantees the delivery of messages to all participating nodes in the same order. This project is an implementation of such a system, designed to ensure that messages are received and processed by all nodes consistently.

## Getting Started

These instructions will help you set up and run the Total Order Multicasting system on your local machine.

### Prerequisites

To run this project, you'll need the following software:

- Python (3.x recommended)
- ZeroMQ (ØMQ) library
- `make` (optional, for convenience)

### Installation

1. **Python**: If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/).

2. **ZeroMQ**: You can install ZeroMQ via Python's package manager `pip`. Use the following command:
   ```bash
   pip install pyzmq
   ```

## Usage

- The main functionality of this system is to ensure that all nodes receive and process messages in the same order.
- Clients can specify the messages they want to send by creating a command file, and the system will handle the multicasting and total ordering.
- The results of this multicasting can be found in the `result` folder.
- Use the command `make` to run the code:
   ```bash
   make
   ```

## Report

For in-depth details about the implementation, design, and results of this Total Order Multicasting project, please refer to the `report.pdf` file.