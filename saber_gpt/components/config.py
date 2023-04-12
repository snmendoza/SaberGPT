import json
import os

# get user's home directory
home_dir = os.path.expanduser('~')

# add sabergpt folder to path
sabergpt_folder = os.path.join(home_dir, "Documents")
sabergpt_folder = os.path.join(sabergpt_folder, "SaberGPT")

# check if sabergpt folder exists, create it if it doesn't
if not os.path.exists(sabergpt_folder):
    os.makedirs(sabergpt_folder)

# define path to json file
json_path = os.path.join(sabergpt_folder, "setting.json")

# check if json file exists, create it if it doesn't
if not os.path.exists(json_path):
    # define dictionary to write to json file
    data_dict = {
        "dropdown_options": ["none"],
        "key2": "value2",
        "key3": "value3"
    }
    # write dictionary to json file
    with open(json_path, "w") as f:
        json.dump(data_dict, f)

# read data from json file
options_data = None
with open(json_path, "r") as f:
    options_data = json.load(f)



