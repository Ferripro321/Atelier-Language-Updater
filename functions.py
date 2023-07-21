# This file stores functions used on Atelier Transaltor.

import json
import re
import subprocess
import shutil
import os
import colorama
from colorama import Fore, Style
colorama.init()


def start():
    text1 = """
 ________      ___           ___  ___          ___      ___  _____     
|\   __  \    |\  \         |\  \|\  \        |\  \    /  /|/ __  \    
\ \  \|\  \   \ \  \        \ \  \\\\\  \       \ \  \  /  / /\/_|\  \   
 \ \   __  \   \ \  \        \ \  \\\\\  \       \ \  \/  / /\|/ \ \  \  
  \ \  \ \  \ __\ \  \____  __\ \  \\\\\  \       \ \    / /      \ \  \ 
   \ \__\ \__\\\\__\ \_______\\\\__\ \_______\       \ \__/ /        \ \__\\
    \|__|\|__\|__|\|_______\|__|\|_______|        \|__|/          \|__|

"""
    text2 = """
--------------------------------------------
By Ferripro & MisterGunXD
--------------------------------------------
"""
    print(Fore.RESET + text1)
    print(text2)

def get_files_with_extension(folder_path, extension):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(extension):
                file_path = os.path.join(root, file_name)
                yield file_path

def replace_hex_values(match):
    hex_value = match.group(1)
    return str(int(hex_value, 16))

def replace_decimal_values(match):
    decimal_value = match.group(1)
    return hex(int(decimal_value))

def get_subfolder_paths(folder_path):
    subfolder_paths = []
    for entry in os.listdir(folder_path):
        full_path = os.path.join(folder_path, entry)
        if os.path.isdir(full_path):
            subfolder_paths.append(full_path)
    return subfolder_paths

def get_last_folder_name(path):
    normalized_path = os.path.normpath(path)
    directories = normalized_path.split(os.sep)
    last_folder_name = directories[-1]
    
    return last_folder_name
    
def read_file_to_list(file_path):
    content_list = []
    
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                content_list.append(line.strip())

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return content_list

def remove_files_with_extension(directory_path, file_extension):
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.lower().endswith(file_extension.lower()):
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")

    except FileNotFoundError:
        print("Directory not found. Please check the directory path and try again.")
    except Exception as e:
        print(f"An error occurred while removing files: {e}")

def move_file(source, destination):
    try:
        destination_folder = os.path.dirname(destination)
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(source, destination)
        print(f"File '{source}' moved to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"File '{source}' not found.")
    except shutil.Error as e:
        print(f"An error occurred while moving the file: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
