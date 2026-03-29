import pandas as pd


def fill_column_hierarchical(row, column_name=str, group_one_size=int, group_one_mean=float,
                             group_two_size=int, group_two_mean=float, overall_mean=float):
    """
    function to fill missing values in a column using hierarchical imputation:
    1. If the platform-genre group has more than 10 valid values, use the mean critic score of that group.
    2. If the platform group has more than 10 valid values, use the mean critic score of that platform.
    3. If neither condition is met, use the overall mean critic score.

    This approach ensures that we use the most specific available information for imputation while maintaining reliability
    by requiring a minimum sample size.
    """

    # if no missing value, returns the original value
    if not pd.isna(row[column_name]):
        return row[column_name]

    # If missing, applies the hierarchical logic
    platform = row['platform']
    genre = row['genre']

    # checking if platform-genre group has more than 10 valid values
    if group_one_size.get((platform, genre), 0) > 10:
        return group_one_mean.get((platform, genre))

    # checking if platform group has more than 10 valid values
    elif group_two_size.get(platform, 0) > 10:
        return group_two_mean.get(platform)

    # applying overall mean if no other condition is met
    else:
        return overall_mean
