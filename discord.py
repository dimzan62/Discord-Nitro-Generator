import requests
import random
import string
import time


WEBHOOK_URL = "Your Webhook URL Here"


def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=18))

def check_code(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code == 200

def send_to_webhook(code):
    data = {"content": f"Valid Nitro Code Found: https://discord.gift/{code}"}
    requests.post(WEBHOOK_URL, json=data)
    print(f"Sent valid code to webhook: {code}")

def main():
    while True:
        code = generate_code()
        print(f"Checking code: {code}")

        if check_code(code):
            send_to_webhook(code)
        time.sleep(1)

if __name__ == "__main__":
    main()
