from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins
from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey

# EDIT THESE WITH THE COSMOS PREFIX
PREFIX="sent"
PREFIX_NODE="sentnode"

def generate_cosmos_wallet(mnemonic, prefix):
    """
    Generate a Cosmos wallet using a BIP39 mnemonic.

    Args:
        mnemonic (str): The BIP39 mnemonic.
        prefix (str): The wallet prefix.

    Returns:
        LocalWallet: The generated Cosmos wallet.
    """
    try:
        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Create a Cosmos BIP44 wallet
        bip44_def_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.COSMOS).DeriveDefaultPath()

        # Create a local wallet with the private key
        private_key = PrivateKey(bip44_def_ctx.PrivateKey().Raw().ToBytes())
        wallet = LocalWallet(private_key, prefix=prefix)

        return wallet
    except Exception as e:
        print(f"Error while generating Cosmos wallet: {e}")
        return None

def main():
    while True:
        mnemonic = input("Enter mnemonic (Ctrl+C to quit): ")  # Replace with your actual mnemonic
    
        wallet = generate_cosmos_wallet(mnemonic, PREFIX)
        nodeaddr = generate_cosmos_wallet(mnemonic, PREFIX_NODE)
        if wallet and nodeaddr:
            address = wallet.address()
            node_addr = nodeaddr.address()
            print(f"Operator: {address}")
            print(f"Node: {node_addr}")
        else:
            print("Failed to generate Cosmos wallet.")

if __name__ == "__main__":
    main()
