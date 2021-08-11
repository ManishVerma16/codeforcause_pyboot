import os
from datetime import datetime, timedelta

path = 'new1'

def file_dispenser(path, thresh, base=True):

    if os.path.isdir(path):
        for internal in os.listdir(path):
            file_dispenser(path + '/' + internal, thresh, False)
        
        if (len(os.listdir(path)) == 0) and (not base):
            os.rmdir(path)
        return

    modify_time = os.path.getmtime(path)

    if thresh > modify_time:
        print(f'this is an old file {path}')
        os.remove(path)
    else:
        print('this is a new file')

thresh = (datetime.now() - timedelta(minutes=1)).timestamp()
# print(os.path.getmtime(path))
file_dispenser(path, thresh)
# print(thresh)