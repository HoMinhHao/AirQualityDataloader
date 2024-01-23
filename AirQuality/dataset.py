# Import necessary libraries
from urllib import request
import os
import zipfile
import pandas as pd
import tempfile  # Import the tempfile module

# Create a temporary directory for storing the ZIP file
temp_dir = tempfile.mkdtemp()


# Define the default and backup server URLs for downloading the dataset
default_server_url = "http://clouds.iec-uit.com/iot-06.test/Dataset_raw.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=LXYLPI5QK2BQ7D70ZMBZ%2F20240123%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240123T073547Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJMWFlMUEk1UUsyQlE3RDcwWk1CWiIsImV4cCI6MTcwNjAzNTA3NiwicGFyZW50IjoiaW90LTA2In0.8XcePENiJu4Ay9oM32GhG_HVXsHZ2ZCk5w2D2lcaEDrvxA2jM2kM4ILgvgpmeLx1a5vrC8C9fn3ycAaKZD2U6g&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=82d35a5b069b96233885855a6e1d702dde2c7d619d0a89a55b6656fa0383b1aa"
backup_server_url = "http://clouds.iec-uit.com/iot-06.test/Dataset_raw.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=LXYLPI5QK2BQ7D70ZMBZ%2F20240123%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240123T073547Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJMWFlMUEk1UUsyQlE3RDcwWk1CWiIsImV4cCI6MTcwNjAzNTA3NiwicGFyZW50IjoiaW90LTA2In0.8XcePENiJu4Ay9oM32GhG_HVXsHZ2ZCk5w2D2lcaEDrvxA2jM2kM4ILgvgpmeLx1a5vrC8C9fn3ycAaKZD2U6g&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=82d35a5b069b96233885855a6e1d702dde2c7d619d0a89a55b6656fa0383b1aa"

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
    return ['India_dataset_raw', 'Seoul_dataset_raw', 'Taiwan_dataset_raw']

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