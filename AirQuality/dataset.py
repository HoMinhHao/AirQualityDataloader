# Import necessary libraries
from urllib import request
import os
import zipfile
import pandas as pd
import tempfile  # Import the tempfile module

# Create a temporary directory for storing the ZIP file
temp_dir = tempfile.mkdtemp()


# Define the default and backup server URLs for downloading the dataset
default_server_url = "http://clouds.iec-uit.com/haohm.airquality/Dataset_raw.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ECNV7VV1HKVVTSKCSNU5%2F20240406%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240406T142649Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJFQ05WN1ZWMUhLVlZUU0tDU05VNSIsImV4cCI6MTcxMjQ1NjYxMywicGFyZW50IjoiaGFvaG0ifQ.mCW4P4EBs0iIBXHj4QgSXXcOtA_DFSw00MfS7CeYAWw5QdHN1qN2SatPWWwGfqM70udvq7eHOO4KQ5mLI1F23g&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=9e2f30f5d737a8d6c608926cebd5542602b55da9cfe85bcc3445d74e71af9d90"
backup_server_url = "http://clouds.iec-uit.com/haohm.airquality/Dataset_raw.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ECNV7VV1HKVVTSKCSNU5%2F20240406%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240406T142649Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJFQ05WN1ZWMUhLVlZUU0tDU05VNSIsImV4cCI6MTcxMjQ1NjYxMywicGFyZW50IjoiaGFvaG0ifQ.mCW4P4EBs0iIBXHj4QgSXXcOtA_DFSw00MfS7CeYAWw5QdHN1qN2SatPWWwGfqM70udvq7eHOO4KQ5mLI1F23g&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=9e2f30f5d737a8d6c608926cebd5542602b55da9cfe85bcc3445d74e71af9d90"
# Specify the path for the downloaded ZIP file in the temporary directory
zip_file_path = os.path.join(temp_dir, "Dataset_raw.zip")
print(zip_file_path)
# Check if the ZIP file already exists, if not, attempt to download it
if not os.path.exists(zip_file_path):
    try:
        # Try to download from the default server URL
        request.urlretrieve(default_server_url, zip_file_path)
    except:
        # If the default server fails, try the backup server URL
        request.urlretrieve(backup_server_url, zip_file_path)
        

# Function to load data from the ZIP file by name
def load_data(name, train_set=True):
    """
    Load data from a specified CSV file within a ZIP archive.

    Args:
        name (str): The name of the dataset or file to be loaded.
        train_set (bool, optional): A boolean flag indicating whether to load the training set (default) or testing set.

    Returns:
        pandas.DataFrame: A DataFrame containing the loaded data.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        try:
            # Try to open and read the specified CSV file from the ZIP archive
            with zip_file.open(f'{name}.csv') as csv_file:
                return pd.read_csv(csv_file)
        except Exception as error:
            # if name == 'AndroAnalyzer':
            #     if train_set:
            #         with zip_file.open(f'MiniMalDroid2020/AndroAnalyzer/AndroAnalyzer_train.csv') as csv_file:
            #             return pd.read_csv(csv_file)
            #     else:
            #         with zip_file.open(f'MiniMalDroid2020/AndroAnalyzer/AndroAnalyzer_test.csv') as csv_file:
            #             return pd.read_csv(csv_file)
            # Handle any exceptions and print an error message
            print(error)

# Function to get SHA256 data by class name
# def get_sha256(class_name, train_set=True):
#     """
#     Retrieve SHA256 data by class name from either the training or testing set.

#     Args:
#         class_name (str): The name of the class for which SHA256 data is requested.
#         train_set (bool, optional): A boolean flag indicating whether to retrieve data from the training set (default) or testing set.

#     Returns:
#         list: A list of SHA256 strings associated with the specified class.
#     """
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
#         try:
#             if train_set:
#                 with zip_file.open(f'MiniMalDroid2020/SHA256/train_set/{class_name}') as data_file:
#                     # Read and decode the data as UTF-8 and split it into lines
#                     return data_file.read().decode('utf-8').splitlines()
#             else:
#                 with zip_file.open(f'MiniMalDroid2020/SHA256/test_set/{class_name}') as data_file:
#                     # Read and decode the data as UTF-8 and split it into lines
#                     return data_file.read().decode('utf-8').splitlines()
#         except Exception as error:
#             print(error)

# Function to get a list of dataset names
def get_list_dataset():
    """
    Get a list of dataset names available in the ZIP archive.

    Returns:
        list: A list of dataset names.
    """
    # Print and return a list of dataset names
    return ['IndiaAirQuality', 'SeoulAirQuality', 'NorthernTaiwanAirQuality', 'UCIAirQuality', 'HCMCAirQuality', 'BeijingAirQuality']

# Function to get a list of class names
# def get_classname():
#     """
#     Get a list of class names.

#     Returns:
#         list: A list of class names.
#     """
#     # Print and return a list of class names
#     return ['Adware', 'Banking', 'Benign', 'Riskware', 'SMS']

if __name__ == "__main__":
    print("Wellcome to AndroAnalyzer Dataset!!!")
    