def moscow_counter(f):

    count_moscow = 0

    for line in f:
        # Преобразование str в int
        line = list(line[:6])
        line = [int(i) for i in line]

        # Срезы двух половин номера билета
        first_half = line[:3]
        last_half = line[3:6]

        # print(first_half, last_half)
        # print(sum(first_half), sum(last_half))

        if sum(first_half) == sum(last_half):
            count_moscow += 1

    return count_moscow


def petersburg_counter(f):

    count_petersburg = 0

    for line in f:
        # Преобразование str в int
        line = list(line[:6])
        line = [int(i) for i in line]

        # Генерация списков с четными и нечетными цифрами билетов
        even_line = [i for i in line if i % 2 == 0]
        odd_line = [i for i in line if i % 2 != 0]

        # print(even_line, odd_line)
        # print(sum(even_line), sum(odd_line))

        if sum(even_line) == sum(odd_line):
            count_petersburg += 1

    return count_petersburg


def main():
    # C:\Users\Artur\Desktop\tickets.txt
    file_dir = input('Input directory:\n')
    with open(fr'{file_dir}', 'r') as file:
        mc = moscow_counter(file)
        print(f'Moscow lucky tickets: {mc}')

    with open(fr'{file_dir}', 'r') as file:
        pc = petersburg_counter(file)
        print(f'Petersburg lucky tickets: {pc}')


if __name__ == '__main__':
    main()
