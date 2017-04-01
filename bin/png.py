import os
import sys
from png_2 import run

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

data=()
def parameter(auth_type):
    def auth(func):
        def wrapped(args):
            if auth_type == 'png':
                for i,k in enumerate(args):
                    run(args)
                    # print(i,k,args[k])
            return func(args)
        return wrapped
    return auth