from os.path import realpath, dirname
import json

def get_config(name):
    path = dirname(realpath(__file__) + '/configs/' + name + '.json'