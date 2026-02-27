# app.py - 项目根目录下的核心入口文件
from flask import Flask

# 这里的 "app" 必须和启动命令里第二个 "app" 对应
app = Flask(__name__)

# 测试路由，验证服务能启动
@app.route('/')
def hello():
    return "部署成功！", 200

# 生产环境启动适配
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
