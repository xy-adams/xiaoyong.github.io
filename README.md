# 小永的个人主页

这是一个基于Flask构建的现代化个人介绍网站，部署在GitHub Pages上。

## 功能特点

- 📱 响应式设计，支持各种设备
- 🎨 现代化UI界面
- ⚡ 快速加载和流畅动画
- 📧 联系表单
- 🔍 项目展示和过滤
- 🌙 准备支持深色主题

## 技术栈

- **后端**: Flask + Python
- **前端**: HTML5 + CSS3 + JavaScript
- **构建**: Frozen-Flask (生成静态文件)
- **部署**: GitHub Pages
- **样式**: 现代CSS变量和Flexbox/Grid
- **图标**: Font Awesome

## 快速开始

1. 克隆仓库
```bash
git clone https://github.com/xiaoyong/xiaoyong.github.io.git
cd xiaoyong.github.io
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行开发服务器
```bash
python app.py
```

4. 生成静态网站
```bash
python build.py
```

## 自定义配置

编辑 `config.py` 文件来修改个人信息：

- `SITE_TITLE`: 网站标题
- `AUTHOR_NAME`: 个人姓名
- `AUTHOR_EMAIL`: 联系邮箱
- `GITHUB_URL`: GitHub链接
- `LINKEDIN_URL`: LinkedIn链接

## 部署

网站会自动生成到 `docs` 文件夹，可以直接部署到GitHub Pages。

## 许可证

MIT License

## 联系方式

- 邮箱: xiaoyong@example.com
- GitHub: https://github.com/xiaoyong
