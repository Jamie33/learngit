from proxypool.setting import *
import redis
from random import choice

"""
定义一个类来操作数据库的有序集合，定义一些方法来实现分数的设置，代理的获取等。

"""

class RedisClient(object):
    
    def __init__(self,host=Redis_host,port=Redis_port,db=Redis_db,password=Redis_password):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis 密码
        """
        self.db = redis.StrictRedis(host=host,port=port,db=db,password=password) # 声明了一个StrictRedis 对象
        
    def add(self,proxy,score=Initial_score):
        """
        如果代理不存在，添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return 添加结果
        zscore(name, value) 返回key为name的zset中value元素的分数 
        zadd(name, args, *kwargs) 向key为name的zset中添加元素member，score用于排序。如果该元素存在，则更新其顺序
        """
        if not self.db.zscore(Redis_key,proxy):  
            return self.db.zadd(Redis_key,score,proxy) 
            
    def random(self):
        """
         随机获取有效代理，首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取，否者异常
         :return 随机代理
         zrangebyscore(name, min, max, start=None, num=None, withscores=False) 返回key为name的zset中score在给定区间的元素
         zrevrange(name, start, end, withscores=False) 返回key为name的zset（按score从大到小排序）中的index从start到end的所有元素
        """
        result = self.db.zrangebyscore(Redis_key,Max_score,Max_score)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(Redis_key,0,100)
            if len(result):
                return choice(result)
            else:
                raise 'PoolEmptyError(have not defined yet)'
    
    def decrease(self,proxy):
        """
        代理值减一分，分数小于最小值，则代理删除
        :param proxy: 代理
        :return: 修改后的代理分数
        zscore(name, value) 返回key为name的zset中value元素的分数 
        zincrby(name, value, amount=1) 如果在key为name的zset中已经存在元素value，则该元素的score增加amount，否则向该集合中添加该元素，其score的值为amount
        zrem(name, *values)  删除key为name的zset中的元素
        """
        score = self.db.zscore(Redis_key,proxy)
        if score and score > Min_score:
            print('代理{}当前分数{}减1'.format(proxy,score))
            return self.db.zincrby(Redis_key,score,-1)
        else:
            print('代理{}当前分数{}移除'.format(proxy,score))
            return self.db.zrem(Redis_key,proxy)
    
    def exists(self,proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        zscore(name, value) 返回key为name的zset中value元素的分数
        zadd(name, args, *kwargs) 向key为name的zset中添加元素member，score用于排序。如果该元素存在，则更新其顺序
        """
        return not self.db.zscore(Redis_key,proxy) == None
    
    def setmax(self,proxy):
        """
        将代理设置为 Max_score
        :param proxy: 代理
        :return: 设置结果
        """
        print('代理{}可用，设置为{}'.format(proxy,Max_score))
        return self.db.zadd(Redis_key,Max_score,proxy)
    
    def count(self):
        """
        获取数量
        :return: 数量
        """
        return self.db.zcard(Redis_key)
    
    def viewall(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        return self.db.zrangebyscore(Redis_key,Min_score,Max_score)