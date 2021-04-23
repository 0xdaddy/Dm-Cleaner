def url_login():
    return 'https://www.instagram.com/accounts/login/ajax/'#instagram : @0xdevil
def url_send_sms_message():
    return 'https://www.instagram.com/accounts/send_two_factor_login_sms/'#instagram : @0xdevil
def url_two_factor():
    return 'https://www.instagram.com/accounts/login/ajax/two_factor/'#instagram : @0xdevil
def url_set_private():
    return 'https://www.instagram.com/accounts/set_private/'#instagram : @0xdevil
def url_get_requests():
    return 'https://www.instagram.com/accounts/activity/?__a=1'#instagram : @0xdevil
def url_accept_follower(id):
    return f'https://www.instagram.com/web/friendships/{id}/approve/'#instagram : @0xdevil
def url_ignore_follower(id):
    return f'https://www.instagram.com/web/friendships/{id}/ignore/'#instagram : @0xdevil
def url_users(user):
    return f"https://www.instagram.com/{user}"#instagram : @0xdevil
def url_follow(id):
    return f'https://www.instagram.com/web/friendships/{id}/follow/'#instagram : @0xdevil
def url_block(id):
    return f'https://www.instagram.com/web/friendships/{id}/block/'#instagram : @0xdevil