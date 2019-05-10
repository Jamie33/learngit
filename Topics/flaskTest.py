from flask import Flask  # 导入包

app = Flask(__name__)  # 创建一个Web应用


@app.route('/')  # 定义路由(Views)，可以理解为定义页面的URL
def index():
    return "这是用Python + Flask 搞出来的。"  # 渲染页面


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)  # 运行，指定监听地址为 127.0.0.1:8080