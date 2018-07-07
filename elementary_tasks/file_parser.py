def read_file(f_dir, string):
    with open(fr'{f_dir}', 'r') as file:
        counter = 0
        for line in file:
            if line[:len(string)] == string:
                counter += 1
    return counter


def replace_line(f_dir, str_search, str_replace):
    with open(fr'{f_dir}', 'r') as f:
        strings = f.readlines()

    length = len(str_search)
    for line in strings:
        index = strings.index(line)
        # Обрезка строки исключает символ \n
        line = str(line[:length])
        if line == str_search:
            strings[index] = str_replace + '\n'

    with open(fr'{f_dir}', 'w') as f:
        f.writelines(strings)


try:
    while True:
        mode = input('[1] - Count of string occurrences in a text file.\n'
                     '[2] - Replacement of one string for another in a text '
                     'file.\n'
                     'Select the mode. [1 / 2]\n')
        # C:\Users\Artur\Desktop\parsing1.txt
        # 402795
        if mode == '1':
            file_dir = input('File directory:\n')
            string_for_counting = input('String for counting:\n')
            count = read_file(file_dir, string_for_counting)
            print(count)
        # C:\Users\Artur\Desktop\parsing2.txt
        # Самым известным «рыбным» текстом является знаменитый Lorem ipsum.
        elif mode == '2':
            file_dir = input('File directory:\n')
            string_for_searching = str(input('String for searching:\n'))
            string_for_replacing = str(input('String for changing:\n'))
            replace_line(file_dir, string_for_searching, string_for_replacing)
        elif not mode:
            print('FILE PARSER\n'
                  '1. Enter the mode of the file parser.\n'
                  '2. Enter the requested data\n'
                  '    for mode 1:\n'
                  '    - file directory\n'
                  '    - string for counting\n'
                  '    for mode 2:\n'
                  '    - file directory\n'
                  '    - string for counting\n'
                  '    - string for replacing\n')
        else:
            print('Incorrect input. Enter must contain number of mode.\n')
except FileNotFoundError:
    print('Not found file or directory.')
