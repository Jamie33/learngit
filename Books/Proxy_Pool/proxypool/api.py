from flask import Flask,g
from proxypool.db import RedisClient

__all__= ['app']
app = Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System created by Jamie</h2>'

@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()

@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """  
    conn = get_conn()
    return str(conn.count())


@app.route('/all')
def view_all():
    """
    Get all proxies
    :return: 全部代理
    """
    conn = get_conn()
    return str(conn.viewall())


if __name__ == '__main__':
    app.run()