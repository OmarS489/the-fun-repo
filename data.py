import pandas as pd

url_1 = "https://raw.githubusercontent.com/OmarS489/the-fun-repo/the-lol-branch/data/CAPITALCOM_DXY%2C%201D_7d6db.csv"
url_2 = "https://raw.githubusercontent.com/OmarS489/the-fun-repo/the-lol-branch/data/CRYPTOCAP_TOTAL%2C%201D_5f95d.csv"
url_3 = "https://raw.githubusercontent.com/OmarS489/the-fun-repo/the-lol-branch/data/CRYPTOCAP_TOTAL2%2C%201D_2a8e1.csv"
url_4 = "https://raw.githubusercontent.com/OmarS489/the-fun-repo/the-lol-branch/data/CRYPTOCAP_TOTAL3%2C%201D_c180b.csv"

# Modified function to load and clean data from a URL
def remove_nan_columns_from_url(url, save=False):
    """
    Loads a dataset from a URL, removes columns with any NaN values, and returns the cleaned dataset.
    Optionally saves the cleaned dataset to a file.

    :param url: URL of the dataset file.
    :param save: Boolean, if True, the cleaned dataset is saved to a file.
    :return: Cleaned DataFrame.
    """
    # Load the dataset from the URL
    data = pd.read_csv(url)

    # Remove columns with any NaN values
    cleaned_data = data.dropna(axis=1)

    # Optionally save the cleaned dataset
    if save:
        # Create a new file name based on the URL
        new_file_name = url.split('/')[-1].split('.csv')[0] + '_cleaned.csv'
        cleaned_data.to_csv(new_file_name, index=False)
        return cleaned_data, new_file_name

    return cleaned_data


dxy = remove_nan_columns_from_url(url_1)
total1 = remove_nan_columns_from_url(url_2)
total2 = remove_nan_columns_from_url(url_3)
total3 = remove_nan_columns_from_url(url_4)

# Show the data
print(dxy)
print(total1)
print(total2)
print(total3)
