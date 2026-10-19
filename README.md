# random-quote-generator
Generate random aphorisms and quotes




# 随机名言警句生成器 📜
一个轻量、易扩展的Python随机名言生成工具，支持自定义标签筛选、手动添加名言，开箱即用。

## 功能特性
- ✨ 随机生成名言警句
- 🏷️ 支持按分类标签筛选指定类型的名言
- 📝 支持手动添加新名言并自动持久化保存
- 📦 零额外依赖，Python3.6+ 环境直接运行
- 🔌 代码结构清晰，方便二次开发接入API、网页端等场景

## 快速开始
1. 克隆项目到本地
```bash
git clone https://github.com/你的用户名/random-quote-generator.git
cd random-quote-generator
 

直接运行主程序


python quote_generator.py
 

使用示例

from quote_generator import RandomQuoteGenerator

# 初始化生成器
generator = RandomQuoteGenerator()

# 获取一条随机名言
print(generator.get_random_quote())

# 只获取励志类名言
print(generator.get_random_quote(tag="励志"))

# 添加新名言
generator.add_quote(
    content="世上无难事，只要肯登攀",
    author="毛泽东",
    tag="励志"
)
 

## 网页端使用
1. 先安装依赖
```bash
pip install -r requirements.txt
 

启动网页服务


python app.py
 

打开浏览器访问  http://127.0.0.1:5000  就可以看到网页界面啦，支持筛选标签、一键刷新名言。

部署上线
你可以用Gunicorn作为生产服务器，把这个项目部署到云服务器、Vercel或者Render等免费平台

开源协议
MIT