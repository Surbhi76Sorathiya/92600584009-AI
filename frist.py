print('=======Welcome to AI ChatBot========')
print('Type Bye to Exit')
while True:
    
    user = input('You : ').lower()
    if 'hello' in user:
        print('Bot : How are you?')
    elif 'fine' in user:
        print('Bot : Great to hear that what can i help ?')
    elif 'course ' in user:
        print('Bot : You selecterd AI course.')
    elif 'language' in user:
        print('Bot : Python Language.')
    elif 'python' in user:
        print('Bot : Python is a frist choise of AI.')
    elif 'ai' in user:
        print('Bot : AI is an artificial intelligence.')
    elif 'intelligence' in user:
        print('Bot : AI is a simulated human intelligence throgh learing and resoning.')
    elif 'processes' in user:
        print('Bot : Process language amounts of date to identify pattens.')
    elif 'learing' in user:
        print('Bot : For AI you have learn Maching Learning, Neural Network and Deep Learning.')
    elif 'essy' in user:
        print('Bot : Yes Python is use to use language.')
    elif 'bye' in user:
        print('Bot : Good Bye.....! Have a nice day......!')
        break
    else :
        print('Bot : Sorry! I dont understand your qustion.')
        break
