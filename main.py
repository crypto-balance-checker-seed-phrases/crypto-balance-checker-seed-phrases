import pandas as pd
from wallets import seed_to_private_key, check_balance
from utils import load_locale

# Choose language
lang = input("Select language (en/ru): ").strip().lower()
locale = load_locale(lang)

results = []

def menu():
    while True:
        choice = input(locale["menu"])
        if choice == "1":
            seed = input(locale["enter_seed"])
            network = input(locale["select_network"]).upper()
            try:
                priv, addr = seed_to_private_key(seed, network)
                print(f"Private Key: {priv}\nAddress: {addr}")
                results.append({"seed": seed, "network": network, "private_key": priv, "address": addr})
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            for item in results:
                balance = check_balance(item["address"], item["network"])
                print(locale["balance_result"].format(network=item["network"], address=item["address"], balance=balance))
                item["balance"] = balance
        elif choice == "3":
            df = pd.DataFrame(results)
            filename = "crypto_results.xlsx"
            df.to_excel(filename, index=False)
            print(locale["export_done"].format(filename=filename))
        elif choice == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    print(locale["welcome"])
    menu()
