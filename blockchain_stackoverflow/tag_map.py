"""Build map of interesting tag ids we use to classify blockchain posts.

This will create tags.parquet that contains metadata about our tags.
"""

import pandas as pd

#: This is where you need domain specific knowledge and experience
#:
#:
#: For "too new" tags see the discussion regarding missing 
#: StackOverflow data dumps
#:
INTERESTING_TAGS = {
    "ethereum",
    "evm",
    "erc20",
    "solidity",
    # "web3",
    "vyper",
    "assemblyscript",
    "web3js",
    "ethers.js",
    "web3py",
    "web3dart",
    "web3-java",
    "go-ethereum",
    "geth",
    "web3",
    "remix",
    "foundry-rs",
    "foundry-forge",
    "cosmos",
    "cosmos-sdk",
    "tendermint",
    # "cosmwasm",  Too new
    "polkadot",
    "polkadot-js",
    "substrate",
    "elrond",
    # "polygon", Invalid because questions about polygon math
    "solana",
    "solana-cli",
    "solana-transaction-instruction",
    "solana-program-library",
    "solana-web3js",
    "anchor-solana",
    "solana-py",
    "avalanche",
    # "axelar", Too new
    "bitcoin",
    "bitcoind",
    "bitcoinj",
    "bitcoinlib",
    "nft",
    "metaplex",
    "opensea",
    "wallet-connect",
    "metamask",
    "decentralized-applications",
    "cryptocurrency",
    "hedera",
    "hedera-hashgraph",
    "cardano",
    "nearprotocol",
    "near",
    "blockchain",
    "ton",
    "binance-smart-chain",
    "bsc",
    "bep20",
    "uniswap",
    "pancakeswap",
    "chainlink",
    "thegraph",
    "gnosis-safe",
    "matic",
    "binance",
    "coinbase-api",
    "kraken.com",
    "etherscan",
    "infura",
    # "svelte",  benchmark tags
    # "sveltekit",  benchmark tags
    "hardhat",
    "truffle",
    "brownie",
    "ethers.js",
    "wagmi",
    "openzeppelin",
    "smartcontracts",
    "tron",
    "hyperledger",
    "hyperledger-fabric",
    "hyperledger-composer",
    "hyperledger-chaincode",
    "scrypto",
    "move-lang",
    "aptos",
    "sui",
    "diem",
    "xrp",
    "rippled",
    "stellar",
    "eos",
    "litecoin",
    "dogecoin-api",
    "filecoin",
    # arweave no questions
    # storj no questions
    "bigchaindb",
}

#: Unrelated technologies we use as a benchmark
OTHER_TAGS = {
    "svelte",
    "reactjs",
    "vue.js",
    "angular",
    "jquery",
    "sql",
    "mongodb",
    "firebase",
}

def main():

    df = pd.read_csv("csv/Tags.csv")

    # tag id -> tag data maps
    out_tags: list[dict] = {}

    # Use StackOverflow primary key as the tag dataframe index
    df.set_index(df["Id"])

    filtered_df: pd.DataFrame
    filtered_df = df.loc[
        df["TagName"].isin(INTERESTING_TAGS)
        ]

    print(f"We have {len(filtered_df)} tags matched")

    # Sanity check we did not misspelt any
    for our_tag in INTERESTING_TAGS:
        assert filtered_df["TagName"].str.contains(our_tag).any(), f"Does not know tag {our_tag}"
            
    filtered_df.to_parquet("tags.parquet")

    # Show top tags
    print("Top blockchain tags")
    print("-" * 80)
    for idx, row in filtered_df.sort_values("Count", ascending=False).iterrows():
        print(f"{row['TagName']} with {row['Count']} posts")

    other_tags_df: pd.DataFrame
    other_tags_df = df.loc[
        df["TagName"].isin(OTHER_TAGS)
        ]

    print(f"We have {len(other_tags_df)} tags matched")

    # Sanity check we did not misspelt any
    for our_tag in OTHER_TAGS:
        assert other_tags_df["TagName"].str.contains(our_tag).any(), f"Does not know tag {our_tag}"
            
    other_tags_df.to_parquet("other-tags.parquet")        

    # Show top tags
    print("Top other tags")
    print("-" * 80)
    for idx, row in other_tags_df.sort_values("Count", ascending=False).iterrows():
        print(f"{row['TagName']} with {row['Count']} posts")

if __name__ == "__main__":
    main()