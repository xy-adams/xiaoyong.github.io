from flask_frozen import Freezer
from app import app
import os
import shutil

# 创建Freezer实例
freezer = Freezer(app)

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