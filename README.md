# StackExchange blockchain data exploration scripts

Scripts to explore and plot out data for blockchain developer communities.

- [Original data dumps](https://archive.org/download/stackexchange)
- [XML to CSV data converter](https://github.com/SkobelevIgor/stackexchange-xml-converter)

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

Create CSV file we can import to Pandas:

```shell
7z x stackoverflow.com-Tags.7z
./converter
```