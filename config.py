SUPPORTED_NETWORKS = [
    "BTC", "ETH", "BSC", "LTC", "SOL", "MATIC", "AVAX", "ARB", "BASE", "TRX", "XRP"
]

DEFAULT_LANGUAGE = "en"

BALANCE_API = {
    "BTC": "https://blockchain.info/balance?active={address}",
    "ETH": "https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=YourApiKeyToken",
    "BSC": "https://api.bscscan.com/api?module=account&action=balance&address={address}&tag=latest&apikey=YourApiKeyToken"
}
