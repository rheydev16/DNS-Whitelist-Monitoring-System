# DNS Whitelist Monitoring System

A simple Python-based tool that monitors DNS traffic and alerts the user when a DNS request is made to a domain not included in a predefined whitelist.

---

## 📌 Project Overview

This project was created as part of my internship to demonstrate basic network monitoring using Wireshark and Python (PyShark). It helps identify unauthorized DNS requests on a local network.

---

## ⚙️ Technologies Used

- Python
- PyShark
- Wireshark / TShark


---

## 📁 File Structure
```text
dns-whitelist-monitor/
├── main.py # Main Python script to run the monitoring tool
├── whitelist.txt # Text file containing the list of allowed domains
├── README.md # Project documentation
└── logs/ # (Optional) Folder for storing alert logs
```
 ---


## 🧠 How It Works
* The script uses PyShark to capture live DNS packets on a specific network interface.

* It reads a list of allowed domains from a whitelist.txt file.

* For every DNS request captured, the script checks if the requested domain is in the whitelist.

* If the domain is not on the list, it prints an alert or logs the activity.


 ---


 ## 💻 Code Explanation
Below is a key part of the Python script that handles the whitelist checking:

```python
def load_whitelist(filename):
    with open(filename, 'r') as f:
        return [line.strip().lower() for line in f if line.strip()]


def is_whitelisted(domain, whitelist):
    domain = domain.lower()
    for allowed in whitelist:
        if domain.endswith(allowed):
            return True
    return False


if hasattr(packet.dns, 'qry_name'):
    domain = packet.dns.qry_name
    if not is_whitelisted(domain, whitelist):  # <-- WHITELIST CHECK HAPPENS HERE
```

## 🔍 What this code does:

* Load Whitelist: Reads approved domains (like facebook.com) from a file into a list

* Check Domains: For every website requested, checks if it matches or ends with any whitelisted domain

* Alert if Blocked: Prints a warning when it detects requests to non-whitelisted sites

---

 ## 📚 What I Learned

* How DNS queries work in a network.

* How to capture and analyze packets using PyShark.

* How to create simple monitoring tools with Python.

* The importance of network whitelisting and security policies.



