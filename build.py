from flask_frozen import Freezer
from app import app
import os
import shutil

# 创建Freezer实例
freezer = Freezer(app)

# 配置Flask-Frozen
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_BASE_URL'] = 'https://xiaoyong.github.io/'
app.config['FREEZER_RELATIVE_URLS'] = True

@freezer.register_generator
def static_files():
    """生成静态文件URL"""
    # 确保静态文件目录存在的文件都被包含
    static_dir = os.path.join(app.root_path, 'static')
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            # 计算相对于static目录的路径
            rel_path = os.path.relpath(os.path.join(root, file), static_dir).replace('\\', '/')
            yield 'static', {'filename': rel_path}

if __name__ == '__main__':
    # 清理构建目录
    if os.path.exists('docs'):
        shutil.rmtree('docs')
    
    try:
        # 生成静态文件
        freezer.freeze()
        
        # 创建.nojekyll文件（禁用Jekyll处理）
        with open('docs/.nojekyll', 'w') as f:
            f.write('')
        
        print("静态站点生成完成！")
        
    except Exception as e:
        print(f"生成过程中出现错误: {e}")
        print("这通常是因为缺少静态文件，让我们继续处理...")