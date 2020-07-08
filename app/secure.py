# 配置文件1，禁止上传到git
# 数据库密码、账号、Flask的app key等机密文件
DEBUG = True
# 此为配置文件，配置文件变量必须为大写
# 生产环境应改为False

# cymysql为MySQL的驱动
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/fisher'
SECRET_KEY = '1k3m33m333mmmm'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '2501403016@qq.com'
MAIL_PASSWORD = 'puoxuyyqowheebie'
MAIL_SUBJECT_PREFIX = '[网上赠书系统]'
MAIL_SENDER = '网上赠书系统 <hello@网上赠书系统>'

