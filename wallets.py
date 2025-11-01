from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from web3 import Web3
import requests

# Generate private key from seed
def seed_to_private_key(seed_phrase, network="ETH"):
    seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
    if network == "BTC":
        bip_obj = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
    elif network == "ETH" or network == "BASE":
        bip_obj = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    elif network == "BSC":
        bip_obj = Bip44.FromSeed(seed_bytes, Bip44Coins.BINANCE_SMART_CHAIN)
    else:
        raise ValueError(f"Network {network} not supported")
    
    acct = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    return acct.PrivateKey().ToHex(), acct.PublicKey().ToAddress()

# Check balance (simplified)
def check_balance(address, network="ETH"):
    if network == "ETH" or network == "BASE":
        w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_KEY"))
        balance = w3.eth.get_balance(address)
        return Web3.fromWei(balance, "ether")
    elif network == "BTC":
        url = f"https://blockchain.info/balance?active={address}"
        r = requests.get(url).json()
        return r[address]["final_balance"] / 1e8
    elif network == "BSC":
        url = f"https://api.bscscan.com/api?module=account&action=balance&address={address}&tag=latest&apikey=YourApiKeyToken"
        r = requests.get(url).json()
        if r["status"] == "1":
            return int(r["result"]) / 1e18
        return 0
    else:
        return 0
