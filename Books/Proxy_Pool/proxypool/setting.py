# Redis数据库地址
Redis_host = 'localhost'

# Redis端口
Redis_port = 6379

# Redis密码，如无填None
Redis_password = None

Redis_key = 'proxies'

# 代理分数
Max_score = 100
Min_score = 0
Initial_score = 10

VALID_STATUS_CODES = [200]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 10000


# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://www.lazada.vn'

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True


# 最大批测试量
BATCH_TEST_SIZE = 100