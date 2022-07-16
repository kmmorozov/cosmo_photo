def write_file(dir_name, file_name, content):
    with open("{}/{}".format(dir_name, file_name), 'wb') as file:
        file.write(content)
