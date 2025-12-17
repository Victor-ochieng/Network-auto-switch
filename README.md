# Windows Home Network Auto IP Switch

This project solves a repetitive Windows 11 networking problem.

When I leave my home network, I must switch my network adapter to DHCP.
When I return home, I must manually set a static IP address and DNS servers.
Doing this by hand every time is boring and error-prone.

This script automates that process.

## What the script does

- Detects the currently connected Wi-Fi network (SSID)
- If the SSID matches my home network:
  - Sets a specific static IPv4 address
  - Sets a specific gateway
  - Sets specific DNS servers
- If the SSID does not match:
  - Reverts the adapter to DHCP instantly

The script is run manually and makes the decision automatically.

## Platform

- Windows 11
- Python 3.x
- Uses native Windows networking commands (`netsh`)
- Requires administrator privileges

## Why this exists

Windows does not automatically switch between static IP and DHCP based on
network location. When frequently moving between home and other networks,
this becomes repetitive and annoying.

This script removes that manual work.

## How it works

1. Reads the current Wi-Fi SSID using `netsh`
2. Compares it to a configured home SSID
3. Applies network configuration to the Wi-Fi adapter:
   - Static IP + DNS at home
   - DHCP everywhere else

No registry changes are made.
No third-party tools are used.

## Configuration

Edit these values in the script:

```python
HOME_SSID = "MyHomeWiFi"
INTERFACE_NAME = "Wi-Fi"   

STATIC_IP = "192.168.0.200"
SUBNET_MASK = "255.255.255.0"
GATEWAY = "192.168.0.1"

DNS_PRIMARY = "1.1.1.1"
DNS_SECONDARY = "8.8.8.8"

