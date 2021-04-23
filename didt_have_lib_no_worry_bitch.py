def install():
 try:
    import os
    try:
      import requests
    except ImportError:
        os.system('pip install requests')#instagram : @0xdevil
    ##################################################
    try:
     import colorama
    except ImportError:
     os.system('pip install colorama')#instagram : @0xdevil
    ##################################################
    try:
        import json
    except ImportError:
        os.system('pip install json')#instagram : @0xdevil
    ##################################################
    try: 
        import random
    except ImportError:
        os.system('pip install random')#instagram : @0xdevil
    ##################################################
    try:
        import re
    except ImportError:
        os.system('pip install re')#instagram : @0xdevil
    ##################################################

    try:
        import time
    except ImportError:
        os.system('pip install time')#instagram : @0xdevil
    ##################################################
 except:
     print("UNKNOWN ERROR Contact the programmer On instagram -> @0xdevil.")
     input("Press Enter To exit !")
     exit()
