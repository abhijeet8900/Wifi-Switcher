def log(message):
    if (type(message) == list):
        print(f'Wifi-Switcher Log : ')
        for index, i in enumerate(message):
            print(f'{index} {i}')
            print("\n")
    elif (type(message) == dict):
        print(f'Wifi-Switcher Log : ')
        keys = message.keys()
        for i in keys:
            print(f'{i} : {message[i]}')
    else:
        print(f'Wifi-Switcher Log : {message}')
