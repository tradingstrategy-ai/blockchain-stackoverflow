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
    "solidity",
    "vyper",
    "web3js",
    "web3py",
    "web3",
    "foundry-rs",
    "foundry-forge",
    "cosmos",
    "cosmos-sdk",
    # "cosmwasm",  Too new
    "elrond",
    # "polygon", Invalid because questions about polygon math
    "solana",
    "anchor-solana",
    "avalanche",
    # "axelar", Too new
    "bitcoin",
    "nft",
    "cryptocurrency",
    "bitcoin",
    "hedera-hashgraph",
    "cardano",
    "nearprotocol",
    "near",
    "blockchain",
    "ton",
    "binance-smart-chain",
    "uniswap",
    "chainlink",
    "matic",
    "binance",
    # "svelte",  benchmark tags
    # "sveltekit",  benchmark tags
    "hardhat",
    "truffle",
    "brownie",
    "ethers.js",
    "openzeppelin",
    "smartcontracts",
    "tron",
    "hyperledger",
}

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
for idx, row in filtered_df.sort_values("Count", ascending=False).iterrows():
    print(f"{row['TagName']} with {row['Count']} posts")