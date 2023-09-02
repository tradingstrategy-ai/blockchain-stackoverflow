# StackExchange blockchain data exploration scripts

Scripts to explore and plot out data for blockchain developer communities.

- [Original data dumps](https://archive.org/download/stackexchange)
- [Stackoverflow data dump XML to CSV data converter](https://github.com/SkobelevIgor/stackexchange-xml-converter)
- [Stackoverflow stops distributing data dumps](https://meta.stackoverflow.com/a/425121/315168)
  and 

Dataset size is ~40 GB.

# Usage

First download the data from the archive.

We need

- Posts dataset
- Tags dataset

```shell
wget https://archive.org/download/stackexchange/stackoverflow.com-PostHistory.7z
wget https://archive.org/download/stackexchange/stackoverflow.com-Tags.7z
```

## Tags

First we need to create tag name -> primary key mappings
we can use to navigate the StackOverflow posts dump.

Create tags CSV file we can import to Pandas:

```shell
7z x stackoverflow.com-Tags.7z
./converter --source-path Tags.xml --result-format csv --store-to-dir csv
```

Then we create `tags.json` using our script:

```shell
python blockchain_stackoverflow/tag_map.py 
```

This will create `tags.parquet` and also output post counts for our tags:

```
ethereum with 6681 posts
blockchain with 6637 posts
solidity with 6534 posts
svelte with 4932 posts
hyperledger with 3938 posts
smartcontracts with 2989 posts
web3js with 2333 posts
sveltekit with 1969 posts
bitcoin with 1753 posts
solana with 1211 posts
truffle with 1088 posts
binance with 990 posts
cryptocurrency with 944 posts
ethers.js with 741 posts
nft with 717 posts
hardhat with 665 posts
nearprotocol with 626 posts
web3py with 565 posts
chainlink with 486 posts
uniswap with 238 posts
openzeppelin with 238 posts
binance-smart-chain with 237 posts
brownie with 236 posts
anchor-solana with 193 posts
tron with 175 posts
cosmos with 138 posts
hedera-hashgraph with 109 posts
near with 102 posts
elrond with 94 posts
cardano with 80 posts
cosmos-sdk with 51 posts
matic with 42 posts
avalanche with 32 posts
vyper with 22 posts
ton with 10 posts
web3 with 3 posts
foundry-forge with 2 posts
foundry-rs with 1 posts
```

