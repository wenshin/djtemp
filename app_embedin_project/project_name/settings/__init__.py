from common import *

if DEBUG:
    try:
        from dev import *
        from test import *
    except:
        pass
else:
    try:
        from prod import *
    except:
        pass
