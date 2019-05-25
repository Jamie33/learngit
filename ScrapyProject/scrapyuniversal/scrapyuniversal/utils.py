from os.path import realpath, dirname
import json


def get_config(name):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'  #dirname(realpath(__file__)) 获取当前文件的上一层目录的真实路径
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
