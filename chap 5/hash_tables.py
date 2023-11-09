voted = dict()


def check_voter(name, voted):
    if voted.get('name'):
        print('kick them out!')
    else:
        voted['name'] = True
        print('let them vote!')


print(check_voter('tom', voted))
