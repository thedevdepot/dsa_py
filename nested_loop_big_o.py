first_names = ['bill', 'Ted', 'Jack', 'Robert']
last_names = ['Jackson', 'Smith', 'Torvalds', 'Gates']

def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if f'{first_name} {last_name}' == full_name:
                return True
    return False

def main():
    '''
        checks to see if the full name exists in the list of names
    '''
    full_name = 'ked Smith'
    if does_name_exist(first_names, last_names, full_name) == False:
        full_name = '  ***Name not present***'
    print(f'If the full name is in the list it will print here: {full_name}')

if __name__ == '__main__':
    main()
