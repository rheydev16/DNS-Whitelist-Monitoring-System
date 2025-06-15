import pyshark
from datetime import datetime

def load_whitelist(filename):
    with open(filename, 'r') as f:
        return [line.strip().lower() for line in f if line.strip()]
    

def is_whitelisted(domain, whitelist):
    domain = domain.lower()
    for allowed in whitelist:
        if domain.endswith(allowed):
            return True
        
    return False



def monitor_dns(interface, whitelist_file):
    whitelist = load_whitelist(whitelist_file)
    print(f"Loaded whitelist: {whitelist}")

    capture = pyshark.LiveCapture(
        interface=interface,
        display_filter='dns.qry.name and udp.port == 53'
    )

    print("Starting DNS monitoring....")

    for packet in capture.sniff_continuously():
        try: 
            if hasattr(packet.dns, 'qry_name'):
                domain = packet.dns.qry_name
                if not is_whitelisted(domain, whitelist):
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    alert_msg = f"[{timestamp}] ALERT: Non-whitelisted DNS query: {domain}"
                    print(alert_msg)

                    with open("dns_alerts.log", "a") as log_file:
                        log_file.write(alert_msg + "\n")

        except AttributeError:
            pass


if __name__ == "__main__":
    # Change these as needed
    NETWORK_INTERFACE = "Wi-Fi 2"  # "Ethernet" for wired, or check your system
    WHITELIST_FILE = "whitelist.txt"
    
    monitor_dns(NETWORK_INTERFACE, WHITELIST_FILE)