from clear import clear
class factor:
    from color import inputc, printc
    import headers
    from dm_clean import do
    cookie = ''
    def __init__(self, identifier, url, message, username, cookies, csrftoken) -> None:
        import requests
        clear()#instagram : @0xdevil
        self.printc.yellow(message)#instagram : @0xdevil
        code = self.inputc.yellow("C0DE :")
        self.data = {}#instagram : @0xdevil
        self.data['username'] = username#instagram : @0xdevil
        self.data['verificationCode'] = code
        self.data['identifier'] = identifier#instagram : @0xdevil
        post = requests.post(
            url, 
            headers=self.headers.headers(csrftoken),
            data=self.data,
            cookies=cookies)
        #instagram : @0xdevil
        if '"authenticated":true' in post.text: 
            self.printc.green("[+] Login")
            self.cookie = post.cookies
            return self.do(self.cookie)
        else: return factor(identifier, url, message, username, cookies, csrftoken)