def headers(csrftoken):#instagram : @0xdevil
  headers = {}#instagram : @0xdevil
  headers['accept']          = '*/*'#instagram : @0xdevil
  headers['user-agent']      = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
  headers['x-csrftoken']     = f'{csrftoken}'#instagram : @0xdevil
  headers['x-requested-with']= 'XMLHttpRequest' #instagram : @0xdevil
  return headers