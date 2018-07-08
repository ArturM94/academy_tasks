def do_continue(answer):
    """Continue function

    Gets string user answer, returns True or False depended from answer
    :param answer:
    :return: True
    :return: False
    """
    if (answer.lower() == 'y') or (answer.lower() == 'yes'):
        return True
    else:
        return False
