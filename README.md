# StackExchange blockchain data exploration scripts

This is a data research how blockchain development has changed over the years,
based on the most popular programmers' forum, StackOverflow.com data dumps.

[Read the research report](./research.ipynb).

# Prerequisites

If you want to use this notebook for your own research you need to 

- Know Python and UNIX shell basics
- Have Python 3.11 installed
- Have Poetry installed

# Get started

Check out files with `git-lfs`:

```shell
git clone ...
cd blockchain-stackoverflow
git lfs install
git lfs pull
```

Create Python environment:

```shell
poetry shell
poetry install
```

# Usage

After you have Python environment and large files set up, you can open [research.ipynb](./research.ipynb) in your notebook editor (Visual Studio Code) and point the Python interpreter to the environment created with Poetry.

Alternatively you can open the notebook using stock Jupyter and the web browser

```shell
jupyter notebook research.ipynb
```

# Recreating datasets

We supply [./blockchain-questions.parquet](./blockchain-questions.parquet)
with the Github repository. You might want to update this dataset
as soon as StackOverflow starts to re-publish their data dumps.

To re-create the dataset you need ~200 GB free disk space.
We recommend you work on a remote server using Visual Studio Code remote extensions.

We need

- Posts dataset
- Tags dataset

## Creating tag map

First we need to create tag name -> primary key mappings
we can use to navigate the StackOverflow posts dump.

Create tags CSV file we can import to Pandas:

```shell
wget https://archive.org/download/stackexchange/stackoverflow.com-Tags.7z
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
...
```

## Downloading and extracting the full posts dataset

We now need to get all StackOverflow questions to a CSV file.

Download using Bittorrent, and this way you do not die
to the old age waiting for the download to finish.

```shell
cd download
npm install
node_modules/.bin/webtorrent --select stackoverflow.com-Posts.7z stackexchange_archive.torrent 
# 658 = index for Posts.7z
node_modules/.bin/webtorrent --select 658 stackexchange_archive.torrent 
```

![Webtorrent downloading](screenshots/webtorrent.png)

And then after two hours:

```shell
7z x download/stackexchange/stackoverflow.com-Posts.7z
./converter --source-path Posts.xml --result-format csv --store-to-dir csv
rm Posts.xml  # Save 95 GB space
ipython create-reduced-dataset.ipynb  # Or run in Visual Studio Code
```

Now we have created [blockchain-posts.parquet](./blockchain-posts.parquet).

## Creating blockchain questions only reduced dataset

As the full posts dataset is too large to read in RAM,
we will use a chunked reader to create a smaller dataset
of 25k blockchain questions weighting around 25 MB.

```shell
ipython create-reduced-dataset.ipynb  # Or use Visual Studio Code
```


## Creating StackOverflow question count baseline 

Because [StackOverflow is in decline]() we need to separate
this StackOverflow's decline from the possible blockchains decline.

For this purpose, we create a time-series that contains monthly
binned question counts of all StackOverflow posts.

We do this with our notebook, which is also going to display 
a graph of the question counts:

```shell
ipython create-baseline.ipynb  # Or use Visual Studio Code
```

# Exporting Jupyter Notebook as Ghost blog post

First let's [convert the notebook to a static HTML](https://stackoverflow.com/a/77117494/315168):

```shell
jupyter nbconvert --to=html --no-input --embed-images --output-dir html-export research.ipynb
```

Then you can open `html-export/research.html` in your web browser and copy-paste content to the Ghost blog post editor.

# Useful links and background

- [Original data dumps](https://archive.org/details/stackexchange)
- [Data dump description](https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede/2678#2678)
- [Stackoverflow data dump XML to CSV data converter](https://github.com/SkobelevIgor/stackexchange-xml-converter)
- [Stackoverflow stops distributing data dumps](https://meta.stackoverflow.com/a/425121/315168)
- [The fall of StackOverlow](https://observablehq.com/@ayhanfuat/the-fall-of-stack-overflow)  
- This repo uses [git-lfs](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage)

