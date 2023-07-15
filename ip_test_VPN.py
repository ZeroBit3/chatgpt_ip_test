import subprocess
import re
from datetime import datetime

RED = "\033[0;31m"
PLAIN = "\033[0m"
GREEN = "\033[0;32m"
YELLOW = "\033[33m"
log = "unlock-chatgpt-test-result.log"

print(f"** Chat GPT ip可用性检测 ** by ZeroBit")
with open(log, "w") as log_file:
    log_file.write("Chat GPT ip可用性检测 by ZeroBit\n")
    log_file.write(f"** 系统时间: {datetime.now()}\n")

# Check if curl is installed
try:
    subprocess.check_output(["curl", "--version"])
except FileNotFoundError:
    print("curl is not installed. Please install curl manually.")
    exit(1)

def run_command(command):
    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True, universal_newlines=True
        )
        return output.strip()
    except subprocess.CalledProcessError as e:
        return e.output.strip()

def match_pattern(pattern, text):
    return re.search(pattern, text) is not None

def find_ip_address(text):
    match = re.search(r"Current IP Address: ([\d.]+)", text)
    if match:
        return match.group(1)
    return None

def UnlockChatGPTTest():
    if match_pattern(r"text/plain", run_command('curl --max-time 10 -sS https://chat.openai.com/ -I')):
        ip = find_ip_address(run_command("curl -s checkip.dyndns.org"))
        print(
            f"抱歉！本机IP：{ip} {RED}目前不支持ChatGPT IP is BLOCKED{PLAIN}"
        )
        with open(log, "a") as log_file:
            log_file.write(
                f"抱歉！本机IP：{ip} 目前不支持ChatGPT IP is BLOCKED\n"
            )
        return

    countryCode = re.search(
        r"^loc=([A-Z]+)$",
        run_command("curl --max-time 10 -sS https://chat.openai.com/cdn-cgi/trace"),
        re.MULTILINE,
    )
    if not countryCode:
        print(f"ChatGPT: {RED}Failed{PLAIN}")
        with open(log, "a") as log_file:
            log_file.write(f"ChatGPT: Failed\n")
        return

    countryCode = countryCode.group(1)
    support_countryCodes = [
        "T1", "XX", "AL", "DZ", "AD", "AO", "AG", "AR", "AM", "AU", "AT", "AZ", "BS",
        "BD", "BB", "BE", "BZ", "BJ", "BT", "BA", "BW", "BR", "BG", "BF", "CV", "CA",
        "CL", "CO", "KM", "CR", "HR", "CY", "DK", "DJ", "DM", "DO", "EC", "SV", "EE",
        "FJ", "FI", "FR", "GA", "GM", "GE", "DE", "GH", "GR", "GD", "GT", "GN", "GW",
        "GY", "HT", "HN", "HU", "IS", "IN", "ID", "IQ", "IE", "IL", "IT", "JM", "JP",
        "JO", "KZ", "KE", "KI", "KW", "KG", "LV", "LB", "LS", "LR", "LI", "LT", "LU",
        "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MR", "MU", "MX", "MC", "MN", "ME",
        "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NZ", "NI", "NE", "NG", "MK", "NO",
        "OM", "PK", "PW", "PA", "PG", "PE", "PH", "PL", "PT", "QA", "RO", "RW", "KN",
        "LC", "VC", "WS", "SM", "ST", "SN", "RS", "SC", "SL", "SG", "SK", "SI", "SB",
        "ZA", "ES", "LK", "SR", "SE", "CH", "TH", "TG", "TO", "TT", "TN", "TR", "TV",
        "UG", "AE", "US", "UY", "VU", "ZM", "BO", "BN", "CG", "CZ", "VA", "FM", "MD",
        "PS", "KR", "TW", "TZ", "TL", "GB"
    ]

    if countryCode in support_countryCodes:
        ip = find_ip_address(run_command("curl -s checkip.dyndns.org"))
        print(
            f"恭喜！本机IP:{ip} {GREEN}支持ChatGPT Yes (Region: {countryCode}){PLAIN}"
        )
        with open(log, "a") as log_file:
            log_file.write(
                f"恭喜！本机IP:{ip} 支持ChatGPT Yes (Region: {countryCode})\n"
            )
    else:
        print(f"ChatGPT: {RED}No{PLAIN}")
        with open(log, "a") as log_file:
            log_file.write(f"ChatGPT: No\n")

UnlockChatGPTTest()
