def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    have_middle_name = False
    have_middle_name = input("\nDo you have a middle name: " \
                             "enter 'y' for yes and 'n' for no)")

    if have_middle_name == 'y':
        have_middle_name = True
        m_name = input("Middle name: ")
        if m_name == 'q':
            break
        formatted_name = get_formatted_name(f_name, l_name, m_name)
    else:
        formatted_name = get_formatted_name(f_name, l_name)

    print("\nHello, " + formatted_name + "!")

