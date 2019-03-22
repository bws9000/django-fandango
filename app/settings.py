import os
import sys

"""
IS_PRODUCTION = os.environ.get('IS_PRODUCTION')
"""
IS_PRODUCTION = (sys.argv[1] != 'runserver')

if IS_PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *
