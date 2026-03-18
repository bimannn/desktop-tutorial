# create_list_dirs.py
import os

os.makedirs("Practice6/test_dir/sub_dir", exist_ok=True)
print(os.listdir("Practice6/test_dir"))