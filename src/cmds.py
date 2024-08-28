import os, glob

username = os.getlogin()

def DeleteTempFiles():
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
        print(f" [{temp_dir}] all files were deleted successfully...")

    print('\n Cleaning finished!')