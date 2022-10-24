def import_in_files (file, txt):
    with open(file, 'w') as data:
        data.writelines(txt)
    return