import subprocess
import re
import sys


HOME_SSID = "SSID-name"          # your home Wi-Fi name
INTERFACE_NAME = "Wi-Fi"          # Windows adapter name

STATIC_IP = "192.168.0.200"
SUBNET_MASK = "255.255.255.0"
GATEWAY = "192.168.0.1"

DNS_PRIMARY = "8.8.8.8"
DNS_SECONDARY = "1.1.1.1"


def run(cmd):
    return subprocess.check_output(
        cmd, shell=True, text=True, stderr=subprocess.DEVNULL
    )


def get_current_ssid():
    try:
        output = run("netsh wlan show interfaces")
        match = re.search(r"SSID\s+:\s(.+)", output)
        return match.group(1).strip() if match else None
    except subprocess.CalledProcessError:
        return None


def set_static_ip():
    print("[+] Home network detected → STATIC IP")
    run(
        f'netsh interface ip set address name="{INTERFACE_NAME}" '
        f'static {STATIC_IP} {SUBNET_MASK} {GATEWAY}'
    )
    run(
        f'netsh interface ip set dns name="{INTERFACE_NAME}" static {DNS_PRIMARY}'
    )
    run(
        f'netsh interface ip add dns name="{INTERFACE_NAME}" {DNS_SECONDARY} index=2'
    )


def set_dhcp():
    print("[+] Away from home → DHCP")
    run(f'netsh interface ip set address name="{INTERFACE_NAME}" dhcp')
    run(f'netsh interface ip set dns name="{INTERFACE_NAME}" dhcp')


def main():
    ssid = get_current_ssid()

    if not ssid:
        print("[-] No Wi-Fi connection detected")
        sys.exit(1)

    print(f"[i] Connected SSID: {ssid}")

    if ssid == HOME_SSID:
        set_static_ip()
    else:
        set_dhcp()


if __name__ == "__main__":
    main()

