from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    """首页 - 个人介绍"""
    return render_template('index.html')

@app.route('/about')
def about():
    """关于页面 - 详细个人信息"""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """项目展示页面"""
    return render_template('projects.html')

@app.route('/contact')
def contact():
    """联系方式页面"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)