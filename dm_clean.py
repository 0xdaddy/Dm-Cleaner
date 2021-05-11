import requests
from time import sleep, time
from colorama import Fore
from clear import clear

class do:
    cok = None
    c = 0
    def __init__(self, cok) -> None:
        self.cok = cok
        self.dm_clean()
    def dm_clean(self):
        clear()
        while True:
            try:
                base_url = "https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging=true&folder=&limit=20&thread_message_limit=10"
                headers = {}
                headers['user-agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
                res       = requests.get(base_url,headers=headers,cookies=self.cok)
                csrftoken = res.cookies.get_dict()['csrftoken']
                thread_info = res.json()
                thread_id = thread_info['inbox']['threads']
                for threads_ids in thread_id:
                    sleep(5)
                    thread = threads_ids['thread_id']
                    title = threads_ids['thread_title']
                    headers['accept']          = '*/*'#instagram : @0xdevil
                    headers['x-csrftoken'] = csrftoken
                    headers['x-requested-with']= 'XMLHttpRequest' #instagram : @0xdevil
                    headers['x-ig-app-id'] = '1217981644879628'
                    headers['x-ig-www-claim']       = 'hmac.AR0HivqsJm2KwPGKqFLzly2C-vud0G6K9-3E0WbLFdpElpuF'
                    headers['x-instagram-ajax'] = '2f5a8c09a5f5'
                    hide = requests.post(
                        f'https://i.instagram.com/api/v1/direct_v2/threads/{thread}/hide/',
                        headers=headers
                    ,cookies=self.cok)
    
                    if hide.json()['status'] == 'ok':
                        self.c += 1
                        clear()
                        print(Fore.GREEN + f'[-] Done Hide => {title}\n [-] thread num => {thread}\n [-] count => {self.c}')
                    else:
                        print(hide.text)
            except:
                clear()
                input(Fore.GREEN+f"[-] Done Clean {self.c} thread!")

                exit(0)

