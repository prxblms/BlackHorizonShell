import os, glob
from src.functions import *

# load config.json.
with open('src\config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

config_lang = config['lang']

_lang_ = translator()

pinger_list = [
    'prxblms',
    'sss',
    'ssss'
]

command_list = [
    'clear',
    'exit',
    'help',
    'commands',
    'ls',
    'clear temp files',
    'ip pinger',
]

def setLanguage(arg):
        if config_lang == arg:
            delayPrint(f'\n  {arg} {_lang_("this language has already been defined")} \n')
        else:
            config['lang'] = arg
            with open('src\config.json', 'w', encoding='utf-8') as config_file:
                json.dump(config, config_file, ensure_ascii=False, indent=4)

def ipPingers(arg):
    if arg in pinger_list:
        os.chdir('./bin/ippingers')
        os.system(f'start py {arg}.py')
        os.chdir('../..')
    else:
        delayPrint(f'\n  {arg} {_lang_("this ip pinger does not exist")} \n')

def deleteTempFiles():
    temp_1 = 'C:\\Windows\\Temp'
    temp_2 = f'C:\\Users\\{username}\\AppData\\Local\\Temp'
    prefetch = 'C:\\Windows\\Prefetch'
    recent = f'C:\\Users\\{username}\\Recent'

    count = 1
    while count <= 4:
        if count == 1:
            temp_dir = temp_1

        elif count == 2:
            temp_dir = temp_2
        
        elif count == 3:
            temp_dir = prefetch

        else:
            temp_dir = recent

        for file_path in glob.glob(os.path.join(temp_dir, '*')):
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as error:
                # print('A file does not deleted...')
                pass

        count += 1
        print(f' [{temp_dir}] {_lang_("all files were deleted successfully...")}')

    print('\n Cleaning finished!')