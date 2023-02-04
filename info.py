import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '').split()] 
CAPTION = environ.get('CAPTION')



class temp(object):
    THUMBNAIL = environ.get("THUMBNAIL", "AgACAgUAAxkBAAIFtmPd9YCsUmKRJounDw1CCprrznL5AAKHszEb-x64Vq2TKplEh60RAAgBAAMCAAN4AAceBA")

