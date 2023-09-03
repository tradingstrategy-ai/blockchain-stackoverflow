"""Data analysis helpers."""
from typing import Iterable
import pandas as pd


def get_posts_by_tag(df: pd.DataFrame, tags: Iterable[str]) -> pd.DataFrame:
    """Extract posts by a tag.
    
    :param df:
        StackOverflow posts data

    :return:
        DataFrame subset with only matched tags
    """

    formatted_tags = [f"<{t}>" for t in tags]
    tags_regex = "|".join(formatted_tags)
    return df.loc[df["Tags"].str.contains(tags_regex, case=False, regex=True)]
