from unipath import Path

#################
#   Variables   #
#################
PROJECT_PATH = Path(__file__).ancestor(2)
_STATIC_ROOT = PROJECT_PATH.child('assets').child('static')
_MEDIA_ROOT = PROJECT_PATH.child('assets').child('uploads')

LIB_DIR = PROJECT_PATH.child('_lib')
LOG_DIR = PROJECT_PATH.child('_logs')
