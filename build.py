from frozen_flask import Freezer
from app import app
import os
import shutil

# 创建Freezer实例
freezer = Freezer(app)

@freezer.register_generator
def post():
    """为每个博文生成URL"""
    import glob
    post_files = glob.glob('posts/*.md')
    for file_path in post_files:
        slug = os.path.splitext(os.path.basename(file_path))[0]
        yield {'slug': slug}

@freezer.register_generator
def category():
    """为每个分类生成URL"""
    from app import get_posts
    posts = get_posts()
    categories = set(post['category'] for post in posts)
    for cat in categories:
        yield {'category': cat}

if __name__ == '__main__':
    # 清理构建目录
    if os.path.exists('docs'):
        shutil.rmtree('docs')
    
    # 设置构建目录为docs（GitHub Pages要求）
    app.config['FREEZER_DESTINATION'] = 'docs'
    
    # 生成静态文件
    freezer.freeze()
    
    # 创建.nojekyll文件（禁用Jekyll处理）
    with open('docs/.nojekyll', 'w') as f:
        f.write('')
    
    print("静态站点生成完成！")