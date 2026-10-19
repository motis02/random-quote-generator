from flask import Flask, render_template, jsonify, request
from quote_generator import RandomQuoteGenerator

app = Flask(__name__)
generator = RandomQuoteGenerator()

# 首页路由，返回网页界面
@app.route('/')
def index():
    return render_template('index.html')

# API接口：获取随机名言，支持按标签筛选
@app.route('/api/random-quote')
def api_random_quote():
    tag = request.args.get('tag', None)
    try:
        quote = generator.get_random_quote(tag=tag)
        return jsonify({
            "code": 200,
            "msg": "success",
            "data": quote
        })
    except ValueError as e:
        return jsonify({
            "code": 400,
            "msg": str(e),
            "data": None
        })

# API接口：获取所有可用标签列表
@app.route('/api/tags')
def api_get_tags():
    tags = list({q['tag'] for q in generator.quotes})
    return jsonify({
        "code": 200,
        "msg": "success",
        "data": tags
    })

if __name__ == '__main__':
    # 本地调试运行，部署时可以改成0.0.0.0让局域网也能访问
    app.run(debug=True, host='127.0.0.1', port=5000)