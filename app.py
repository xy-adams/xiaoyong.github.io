from flask import Flask, render_template, request, abort
import frontmatter
import markdown
import os
from datetime import datetime
import glob
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_posts():
    """获取所有博文"""
    posts = []
    post_files = glob.glob('posts/*.md')
    
    for file_path in post_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            post_data = {
                'title': post.metadata.get('title', '无标题'),
                'date': post.metadata.get('date', datetime.now()),
                'category': post.metadata.get('category', '未分类'),
                'tags': post.metadata.get('tags', []),
                'slug': os.path.splitext(os.path.basename(file_path))[0],
                'content': markdown.markdown(post.content, extensions=['codehilite', 'fenced_code']),
                'excerpt': post.content[:200] + '...' if len(post.content) > 200 else post.content
            }
            posts.append(post_data)
    
    # 按日期排序
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

@app.route('/')
def index():
    """首页"""
    page = request.args.get('page', 1, type=int)
    posts = get_posts()
    
    # 分页
    per_page = app.config['POSTS_PER_PAGE']
    start = (page - 1) * per_page
    end = start + per_page
    posts_page = posts[start:end]
    
    # 计算分页信息
    total_pages = (len(posts) + per_page - 1) // per_page
    has_prev = page > 1
    has_next = page < total_pages
    
    return render_template('index.html', 
                         posts=posts_page,
                         page=page,
                         total_pages=total_pages,
                         has_prev=has_prev,
                         has_next=has_next)

@app.route('/post/<slug>')
def post(slug):
    """博文详情页"""
    file_path = f'posts/{slug}.md'
    if not os.path.exists(file_path):
        abort(404)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
        post_data = {
            'title': post.metadata.get('title', '无标题'),
            'date': post.metadata.get('date', datetime.now()),
            'category': post.metadata.get('category', '未分类'),
            'tags': post.metadata.get('tags', []),
            'content': markdown.markdown(post.content, extensions=['codehilite', 'fenced_code', 'toc'])
        }
    
    return render_template('post.html', post=post_data)

@app.route('/category/<category>')
def category(category):
    """分类页面"""
    posts = get_posts()
    filtered_posts = [post for post in posts if post['category'] == category]
    return render_template('index.html', posts=filtered_posts, category=category)

@app.route('/search')
def search():
    """搜索功能"""
    query = request.args.get('q', '')
    if not query:
        return render_template('index.html', posts=[])
    
    posts = get_posts()
    filtered_posts = []
    
    for post in posts:
        if (query.lower() in post['title'].lower() or 
            query.lower() in post['content'].lower() or
            any(query.lower() in tag.lower() for tag in post['tags'])):
            filtered_posts.append(post)
    
    return render_template('index.html', posts=filtered_posts, search_query=query)

@app.route('/about')
def about():
    """关于页面"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)