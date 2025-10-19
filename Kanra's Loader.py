import requests
from getpass import getpass  # this will hide input when users input / paste their key
import sys

# this dot art will appear above the login. you can remove it or add your own dot art. (https://emojicombos.com/dot-art)
print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⣆⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⣼⣿⡗⠀⠀⠀⠀
⠀⠀⠀⣠⠟⠀⠘⠷⠶⠶⠶⠾⠉⢳⡄⠀⠀⠀⠀⠀⣧⣿⠀⠀⠀⠀⠀
⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣤⣤⣤⣤⣤⣿⢿⣄⠀⠀⠀⠀
⠀⠀⡇⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠙⣷⡴⠶⣦
⠀⠀⢱⡀⠀⠉⠉⠀⠀⠀⠀⠛⠃⠀⢠⡟⠂⠀⠀⢀⣀⣠⣤⠿⠞⠛⠋
⣠⠾⠋⠙⣶⣤⣤⣤⣤⣤⣀⣠⣤⣾⣿⠴⠶⠚⠋⠉⠁⠀⠀⠀⠀⠀⠀
⠛⠒⠛⠉⠉⠀⠀⠀⣴⠟⣣⡴⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

# navigate to (https://keyauth.cc/app/?page=manage-apps) and paste each of the following.
app_name = "nameofapp"
owner_id = "oWnErId"
version = "1.0"
seller_key = "your_own_sellerkey"  # for this you must navigate to (https:\/\/keyauth.cc\/app\/?page=seller-settings)
# DISCLAIMER: IF YOU DO NOT HAVE THE SELLER TIER YOU CAN'T DO ANY OF THIS. (https://keyauth.cc//app//?page=upgrade)
# the key feature needed for this is "Seller API", if in the future they decide to open this up to free accounts or a lower tier than get that!

# this will prompt your users to login, each time the login fails, it will loop again so they can retry!
while True:
    username = input("Username: ")

    try:
        key = getpass("Key: ")  # prefer hidden input
    except Exception:
        key = input("Key: ")  # fallback if getpass fails

    # KeyAuth API v1.3 endpoint
    url = "https://keyauth.com/api/seller/"
    params = {
        "type": "verify",
        "user": username,
        "key": key,
        "name": app_name,
        "ownerid": owner_id,
        "sellerkey": seller_key
    }

    try:
        response = requests.get(url, params=params, timeout=8)
        data = response.json()
    except Exception as e:
        print("( ꩜ ᯅ ꩜;)⁭ Error connecting to KeyAuth API:", e) # this message will appear if it fails to connect to KeyAuth, you can customize it.
        continue

    if data.get("success"):
        print("\nAccess granted! ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧ Welcome,", username) # this message appears when access is granted, you can customize it.
        break 
    else:
        print("\nInvalid username or key. ( ˶°ㅁ°) !! Try again.\n") # this message appears if username or key is invalud, you can customize it.

# down below you can paste your script, whatever it is you wish to have locked behind KeyAuth.
# paste it directly below the prompted area.

def code_main():
    # --- BEGIN CODE ---
    print("code activated!")

# insert code here

    # --- END CODE ---
# that's all, enjoy! @cigarfumes on discord.

code_main()

