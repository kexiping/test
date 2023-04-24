def get_fomatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f'{first_name} {last_name}'
    return full_name.title()

while True:
    print('\nPlease tell me your name:')
    print("\nenter")
    f_name = input('First name:')
    l_name = input('Last name:')
    
    formatted_name = get_fomatted_name(f_name, l_name)
    print(f'\nHello, {formatted_name}!')