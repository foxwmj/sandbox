import logging
import os

log = logging.getLogger('werkzeug')

def init(log_file_path):
    FORMAT = "[%(asctime)s | %(filename)-20s:%(lineno)3s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(format=FORMAT)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG) #INFO #WARNING 
    #logging.basicConfig(format='%(asctime)s %(message)s')
    handler = logging.FileHandler(os.path.join(log_file_path, 'access.log'))
    log.addHandler(handler)
    return log

