def do_continue():
    # Если пользователь ответил утвердительно, вызывается инициализатор,
    # иначе программа завершается с выводом соответвующего уведомления
    print('Do you want to continue? [y / yes]')
    answer = str(input())
    if (answer.lower() == 'y') or (answer.lower() == 'yes'):
        return True
    else:
        return False
