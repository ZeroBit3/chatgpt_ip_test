#!/bin/bash

RED='\033[0;31m'
PLAIN='\033[0m'
GREEN='\033[0;32m'
Yellow="\033[33m"
log="unlock-chatgpt-test-result.log"

echo -e "${GREEN}** Chat GPT ip可用性检测${PLAIN} ${Yellow}by ZeroBit${PLAIN}"
echo -e "Chat GPT ip可用性检测 by ZeroBit" > "$log"
echo -e "** 系统时间: $(date)" >> "$log"

if ! command -v curl &> /dev/null; then
  echo "curl is not installed. Installing curl..."
  if command -v apt &> /dev/null; then
    sudo apt install curl -y
  elif command -v dnf &> /dev/null; then
    sudo dnf install curl -y
  else
    echo "Your system package manager is not supported. Please install curl manually."
    exit 1
  fi
fi

if ! command -v grep &> /dev/null; then
  echo "grep is not installed. Installing grep..."
  if command -v apt &> /dev/null; then
    sudo apt install grep -y
  elif command -v dnf &> /dev/null; then
    sudo dnf install grep -y
  else
    echo "Your system package manager is not supported. Please install grep manually."
    exit 1
  fi
fi

function UnlockChatGPTTest() {
    if [[ $(curl --max-time 10 -sS https://chat.openai.com/ -I | grep "text/plain") != "" ]]; then
        local ip="$(dig +short myip.opendns.com @resolver1.opendns.com)"
        echo -e " 抱歉！本机IP：${ip} ${RED}目前不支持ChatGPT IP is BLOCKED${PLAIN}" >> "$log"
        return
    fi

    local countryCode="$(curl --max-time 10 -sS https://chat.openai.com/cdn-cgi/trace | awk -F= '/^loc/{print $2}')"
    if [ -z "$countryCode" ]; then
        echo -e " ChatGPT: ${RED}Failed${PLAIN}" >> "$log"
        return
    fi

    support_countryCodes=("T1" "XX" "AL" "DZ" "AD" "AO" "AG" "AR" "AM" "AU" "AT" "AZ" "BS" "BD" "BB" "BE" "BZ" "BJ" "BT" "BA" "BW" "BR" "BG" "BF" "CV" "CA" "CL" "CO" "KM" "CR" "HR" "CY" "DK" "DJ" "DM" "DO" "EC" "SV" "EE" "FJ" "FI" "FR" "GA" "GM" "GE" "DE" "GH" "GR" "GD" "GT" "GN" "GW" "GY" "HT" "HN" "HU" "IS" "IN" "ID" "IQ" "IE" "IL" "IT" "JM" "JP" "JO" "KZ" "KE" "KI" "KW" "KG" "LV" "LB" "LS" "LR" "LI" "LT" "LU" "MG" "MW" "MY" "MV" "ML" "MT" "MH" "MR" "MU" "MX" "MC" "MN" "ME" "MA" "MZ" "MM" "NA" "NR" "NP" "NL" "NZ" "NI" "NE" "NG" "MK" "NO" "OM" "PK" "PW" "PA" "PG" "PE" "PH" "PL" "PT" "QA" "RO" "RW" "KN" "LC" "VC" "WS" "SM" "ST" "SN" "RS" "SC" "SL" "SG" "SK" "SI" "SB" "ZA" "ES" "LK" "SR" "SE" "CH" "TH" "TG" "TO" "TT" "TN" "TR" "TV" "UG" "AE" "US" "UY" "VU" "ZM" "BO" "BN" "CG" "CZ" "VA" "FM" "MD" "PS" "KR" "TW" "TZ" "TL" "GB")

    if [[ " ${support_countryCodes[@]} " =~ " ${countryCode} " ]]; then
        local ip="$(dig +short myip.opendns.com @resolver1.opendns.com)"
        echo -e " 恭喜！本机IP:${ip} ${GREEN}支持ChatGPT Yes (Region: ${countryCode})${PLAIN}" >> "$log"
    else
        echo -e " ChatGPT: ${RED}No${PLAIN}" >> "$log"
    fi
}

UnlockChatGPTTest
