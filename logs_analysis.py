import json
from pathlib import Path
from typing import Set


def count_requests_by_ip(filename):
    path = Path(filename)
    ip_counts = {}

    with path.open(mode="r", encoding="utf-8") as log_file:
        for line in log_file:
            try:
                log_entry = json.loads(line)
                remote_ip = log_entry["remote_ip"]
                ip_counts[remote_ip] = ip_counts.get(remote_ip, 0) + 1
            except json.JSONDecodeError:
                print("Error decoding JSON from line", line)
                continue
    return ip_counts


def count_response_codes(filename):
    path = Path(filename)
    response_codes = {}

    with path.open(mode="r", encoding="utf-8") as log_file:
        for line in log_file:
            try:
                log_entry = json.loads(line)
                response_code = log_entry["response"]
                response_codes[response_code] = response_codes.get(response_code, 0) + 1
            except json.JSONDecodeError:
                print("Error decoding JSON from line", line)
                continue
    return response_codes


def unique_ips(filename: str) -> Set[str]:
    path = Path(filename)
    unique_ips = set()
    with path.open(mode="r", encoding="utf-8") as log_file:
        for line in log_file:
            try:
                log_entry = json.loads(line)
                remote_ip = log_entry["remote_ip"]
                unique_ips.add(remote_ip)
            except json.JSONDecodeError:
                print("Error decoding JSON from line", line)
                continue
    return unique_ips


filename = "files/nginx_json_logs"
response_code_stats = count_response_codes(filename)
for resp_code in sorted(response_code_stats.keys()):
    print(f"{resp_code}: {response_code_stats[resp_code]}")

# ip_counts = count_requests_by_ip("files/nginx_json_logs")
# for ip, count in ip_counts.items():
#     print(f"{ip}: {count}")

unique_ip_adrs = unique_ips(filename)
print(f"IP adresses accesing your server: {unique_ip_adrs}")
