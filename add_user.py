import requests

print("Welcome to Stan's Flight Club.\n \
We find the best flight deals and email them to you.")

SHEETY_USERS_ENDPOINT = os.environ['SHEETY_USERS']
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']

headers = {
    "Authorization": SHEETY_TOKEN
}

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()

body = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email1
    }
}

response = requests.post(url=SHEETY_USERS_ENDPOINT, json=body, headers=headers)
response.raise_for_status()

print("OK. You're in the club!")