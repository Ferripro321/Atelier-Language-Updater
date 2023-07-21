from functions import *

start()
game_path = input("Please enter your game path (ex: D:\SteamLibrary\steamapps\common\Atelier Sophie 2): ")
game_path.replace("\\", "/")

main_path = os.path.dirname(os.path.abspath(__file__))
gust_pak = main_path + "/gust_pak.exe"
gust_ebm = main_path + "/gust_ebm.exe"
pack_path = game_path + "/Data/PACK01/PACK01.PAK"

move_file(game_path + "/Data/PACK01.PAK", pack_path)

subprocess.run([gust_pak, pack_path])

path = game_path + "/Data/PACK01/event/event_en"

sub_folders = get_subfolder_paths(path)

for folder in sub_folders:
    folder_name = get_last_folder_name(folder)
    ebm_folder = get_files_with_extension(folder, ".ebm")
    for file in ebm_folder:
        print(Fore.GREEN + file + Fore.RESET)
        subprocess.run([gust_ebm, file])
    remove_files_with_extension(folder, ".ebm")
    json_files = get_files_with_extension(folder, ".json")
    for json_file in json_files:
        move_file(json_file, folder + "/JSON/" + os.path.basename(json_file))
    need_translation = get_files_with_extension(folder + "/JSON", ".json")
    for js_file in need_translation:
        with open(js_file, "r", encoding="utf-8") as file:
            file_contents = file.read()
        replaced_json = re.sub(r'0x([0-9a-fA-F]+)', replace_hex_values, file_contents)
        decoded_json = json.loads(replaced_json)
        json_file_name = os.path.basename(js_file).replace(".json", ".txt") 
        translated_text = read_file_to_list(main_path + "/MOD/" + folder_name + "/" + json_file_name)
        for i, linea in enumerate(translated_text):
            decoded_json['messages'][i]['msg_string'] = linea.strip()
        with open(path + "/" + folder_name + "/JSON/" + os.path.basename(js_file), "w", encoding="utf-8") as file:
            MATCH_ALL_XYZ = r'(?<![a-zA-Z\"])(?![\"])(\b\d+)'
            file.write(re.sub(MATCH_ALL_XYZ, replace_decimal_values, json.dumps(decoded_json, ensure_ascii=False)))
        move_file(path + "/" + folder_name + "/JSON/" + os.path.basename(js_file), path + "/" + folder_name + "/" + os.path.basename(js_file))
    ebm_folder = get_files_with_extension(folder, ".json")
    for file in ebm_folder:
        print(Fore.GREEN + file + Fore.RESET)
        subprocess.run([gust_ebm, file])
    remove_files_with_extension(folder, ".json")

print(Fore.YELLOW + "Starting Repack!" + Fore.RESET)
pack_json = game_path + "/Data/PACK01/PACK01.json"
subprocess.run([gust_pak, pack_json])
move_file(pack_path, game_path + "/Data/PACK01.PAK")
move_file(game_path + "/Data/PACK01/PACK01.pak.bak", game_path + "/Data/PACK01.PAK.bak")
print(Fore.GREEN + "\nDone, enjoy :D\n" + Fore.RESET)
print(Fore.YELLOW + "If you ever wanna revert rename PACK01.PAK.bak to PACK01.PAK\n" + Fore.RESET)
exit = input("Press enter to exit.")

