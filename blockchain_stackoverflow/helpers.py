"""Data analysis helpers."""
from typing import Iterable, TypeAlias
import matplotlib
import pandas as pd


#: Associate one or more StackOverflow tags with a label 
#:
#:
LabelledTagMap = dict[str, Iterable[str]]



def get_posts_by_tags(df: pd.DataFrame, tags: Iterable[str]) -> pd.DataFrame:
    """Extract posts by a tag.
    
    :param df:
        StackOverflow posts data

    :return:
        DataFrame subset with only matched tags
    """

    formatted_tags = [f"<{t}>" for t in tags]
    tags_regex = "|".join(formatted_tags)
    return df.loc[df["Tags"].str.contains(tags_regex, case=False, regex=True)]


def bin_to_time(
    df: pd.DataFrame,
    frequency=pd.offsets.QuarterBegin(),        
) -> pd.Series:
    """Bin So posts to a certain time bucket.
    
    :param frequency:
        groupby(freq).

        ``QS`` for quarter start.

        ``MS`` for month start.

    :return:
        Series (period start timestamp, post count)
    """
    
    post_counts_month_df = pd.DataFrame()
    grouped_df = df.groupby([pd.Grouper(key='CreationDate', freq=frequency)])
    
    post_counts_month_df["post_count"] = grouped_df['CreationDate'].count()
    # post_counts_month_df = post_counts_month_df.set_index("CreationDate")
    return post_counts_month_df["post_count"]


def create_binned_df_by_tags(
        df: pd.DataFrame, 
        tag_map: LabelledTagMap,
        frequency=pd.offsets.QuarterBegin(),      
) -> pd.DataFrame:
    """Draw post created charts.

    :param df:
        StackOveflow posts

    :return:
        DataFrame where index is time series and each column is post count per timestamp.
    """

    subjects = pd.DataFrame()
    for label, tags in tag_map.items():
        post_data = get_posts_by_tags(df, tags)
        post_data = get_posts_by_tags(df, tags)
        subjects[label] = bin_to_time(post_data, frequency)
    return subjects


def clip_to_data_available_period(
    df: pd.DataFrame,
    end=pd.Timestamp("2023-08-31")
):
    """Make sure we have data clipped correctly.
    
    - StackOverflow data ends 2023-06
    - Don't display anything beyond 2023-05-31
    """
    return df.loc[df["CreationDate"] < end]


def bin_to_time_with_answers(
    df: pd.DataFrame,
    frequency=pd.offsets.QuarterBegin(),        
) -> pd.DataFrame:
    """Bin So posts to a certain time bucket.
    
    :param frequency:
        groupby(freq).

        ``QS`` for quarter start.

        ``MS`` for month start.

    :return:
        Series (period start timestamp, post count)
    """
    
    post_counts_month_df = pd.DataFrame()
    grouped_df = df.groupby([pd.Grouper(key='CreationDate', freq=frequency)])
    
    post_counts_month_df["post_count"] = grouped_df['CreationDate'].count()
    post_counts_month_df["answer_count"] = grouped_df['AnswerCount'].sum()
    post_counts_month_df["answer_to_posts_ratio"] = post_counts_month_df["answer_count"] / post_counts_month_df["post_count"]
    # post_counts_month_df = post_counts_month_df.set_index("CreationDate")
    return post_counts_month_df

#: See https://stackoverflow.com/a/51734441/315168
#:
#:
axis_formatter_with_separator = matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ','))