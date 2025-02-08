from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins
from mnemonic import Mnemonic
from web3 import Web3

def check_passphrase(mnemonic):
    # Generate the seed from the mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

    # Derive the Ethereum private key using BIP-44
    bip44 = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
    private_key = bip44.PrivateKey().Raw().ToHex()

    # Derive public key and address using Web3
    account = Web3().eth.account.from_key(private_key)
    eth_address = account.address

    return private_key, eth_address

# Load the English BIP-39 wordlist
mnem = Mnemonic("english")
seed_words = mnem.wordlist

hits = []
for sw in seed_words:
    phrase = ' '.join(24*[sw])
    try:
        pk, addr = check_passphrase(phrase)
        print(sw.ljust(10), pk, addr)
        hits.append(addr)
    except Exception as e:
        # invalid, ignoring
        continue