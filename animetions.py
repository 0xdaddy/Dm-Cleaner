def load():
    from colorama import init, Fore, Style
    init()
    c   = 0
    while (20 != c):#instagram : @0xdevil
        import time
        for load in ["I", "O"]:
            print(Fore.YELLOW + Style.BRIGHT +f'[{load}]'+" Wait Please"+ Style.RESET_ALL, end="\r")
            time.sleep(0.6) 
            c +=1
            
def load2():
      c2=0#instagram : @0xdevil
      import time
      while (c2 != 8):
                for load2 in ['1', '0']:
                    from colorama import init, Fore, Back, Style
                    init()#instagram : @0xdevil
                    print(Fore.RED + Style.BRIGHT +f'[{load2}]'+" Wait Please"+ Style.RESET_ALL, end="\r")
                    time.sleep(0.5)
                    c2 +=1

def print_letterbyletter(text):
    print('\t\t\t\t\t\t', end='\r')#instagram : @0xdevil
    import time
    from colorama import init, Fore, Back, Style
    text = text
    slowprint = ''
    last_index = len(text)#instagram : @0xdevil
    for i in range(last_index): 
        slowprint += text[i]
        print(Fore.RED+ Style.BRIGHT +slowprint+ Style.RESET_ALL, end="\r")
        time.sleep(0.4)