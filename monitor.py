import time
import urllib.request
import json


def check_website_status(url):
    print(f"[+] Checking status for: {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            status_code = response.getcode()
            if status_code == 200:
                print(f"[✓] ALERT: Website is ONLINE and responding normally (HTTP {status_code}).")

                # Simulating a payload notification dispatch
                log_data = {"target": url, "status": "ONLINE", "http_code": status_code}
                with open("status_log.json", "w") as log_file:
                    json.dump(log_data, log_file, indent=4)
                print("[✓] Status payload written to 'status_log.json'.")
            else:
                print(f"[!] WARNING: Unexpected response code: {status_code}")
    except Exception as e:
        print(f"[!] ERROR: Target host unreachable or down. Details: {e}")


if __name__ == "__main__":
    # Target URL to monitor
    target_site = "https://httpbin.org/status/200"
    check_website_status(target_site)