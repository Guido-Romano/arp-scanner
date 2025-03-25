<h1 style="color:#800080;">ARP Network Scanner v1.0</h1>

A Python script designed to scan the local network using the Address Resolution Protocol (ARP). Perfect for identifying connected devices on Class C networks.

## Features

- **ARP-Based Scanning**: Uses `scapy` to send and receive ARP packets and map active devices.
- **Class C Networks**: Automatically detects the Class C network based on the local IP address.
- **Easy to Use**: Execute the script directly to gather information about devices in your local network.

## Requirements

- **Python 3.x**
- **Scapy Library** (`scapy`)

## Installation and Usage

### Dependency Installation

#### Debian-Based Distributions (e.g., Ubuntu, Kali Linux)

1. **Update package lists**:

    ```bash
    sudo apt-get update
    ```

2. **Install Python**:

    ```bash
    sudo apt-get install python3
    ```

3. **Install Scapy**:

    ```bash
    sudo apt-get install python3-scapy
    ```

#### Arch-Based Distributions (e.g., Arch Linux, BlackArch)

1. **Update package lists**:

    ```bash
    sudo pacman -Syu
    ```

2. **Install Python**:

    ```bash
    sudo pacman -S python
    ```

3. **Install Scapy**:

    ```bash
    sudo pacman -S python-scapy
    ```

#### Red Hat-Based Distributions (e.g., CentOS, Fedora)

1. **Update package lists**:

    ```bash
    sudo dnf update
    ```

2. **Install Python**:

    ```bash
    sudo dnf install python3
    ```

3. **Install Scapy**:

    ```bash
    sudo dnf install python3-scapy
    ```

### Running the Script

1. Save the script in a file named `arp-scanner.py`.
2. Grant execution permissions to the script:

    ```bash
    chmod +x arp-scanner.py
    ```

3. Run the script:

    ```bash
    ./arp-scanner.py
    ```

### How It Works

1. **Target Network**: The script automatically determines the Class C network based on the local IP address.
2. **ARP Scanning**: Uses the `scapy` library to send ARP packets and detect active devices in the network.
3. **Output**: Displays information about detected devices.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the `scapy` library for enabling efficient implementation of network scans.
