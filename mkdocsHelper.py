import os
import json
import yaml
import shutil

def get_category_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            if file_path.endswith('.json'):
                data = json.load(file)
            elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
                data = yaml.safe_load(file)
            else:
                return None
            return data.get('category')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def scan_folders(parent_folder):
    category_dict = {}
    parent_folder = os.path.join(parent_folder,"script")
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        if os.path.isdir(folder_path):
            cm_file_path_json = os.path.join(folder_path, '_cm.json')
            cm_file_path_yaml = os.path.join(folder_path, '_cm.yaml')
            category = None
            
            if os.path.isfile(cm_file_path_json):
                category = get_category_from_file(cm_file_path_json)
            elif os.path.isfile(cm_file_path_yaml):
                category = get_category_from_file(cm_file_path_yaml)
            
            if category:
                if category not in category_dict:
                    category_dict[category] = []
                category_dict[category].append(folder_name)
    
    return category_dict

def print_category_structure(category_dict):
    # print("  - CM Scripts:")
    for category, folders in category_dict.items():
        category_path = os.path.join("docs", category.replace("/", "-"))
        # category_path_formated = category_path.replace("/", "-")
        category_path_formated = category_path.replace(" ", "-")
        if not os.path.exists(category_path_formated):
            os.makedirs(category_path_formated)
        # print(f"    - {category}:")
        for folder in folders:
            folder_name = folder.replace("/", "-")
            source_path_folder = os.path.join("script", folder_name)
            source_file_path = os.path.join(source_path_folder, "README.md")
            target_path = os.path.join(category_path_formated, os.path.join(folder_name, "index.md"))
            if not os.path.exists(source_file_path):
                # print(f"Source file does not exist: {source_file_path}")
                continue
            if not os.path.exists(os.path.dirname(target_path)):
                os.makedirs(os.path.dirname(target_path))
            if os.path.exists(target_path):
                # print(f"Target file already exists: {target_path}")
                continue
            try:
                print(source_file_path)
                print(target_path)
                print(os.getcwd())
                shutil.copyfile(source_file_path, target_path)
                # os.symlink(source_file_path, target_path)
                # print(f"      - {folder_name}:{target_path}")
            except OSError as e:
                print(f"Failed to create symlink: {e}")
    print("  - CM Scripts:")
    for category, folders in category_dict.items():
        # category_path = os.path.join("docs", category)
        category_path_formated = category.replace("/", "-")
        category_path_formated = category_path_formated.replace(" ", "-")
        print(f"    - {category.replace("/", "-")}:")
        for folder in folders:
            folder_name = folder.replace("/", "-")
            target_path = os.path.join(category_path_formated,  os.path.join(folder_name, "index.md"))
            print(f"      - {folder_name}: {target_path}")

if __name__ == "__main__":
    parent_folder = r""  # Replace with the actual path to the parent folder
    category_dict = scan_folders(parent_folder)
    print_category_structure(category_dict)
