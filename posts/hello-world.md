---
title: "Hello World - 我的第一篇博客"
date: 2024-01-01
category: "日记"
tags: ["开始", "博客"]
---

# 欢迎来到我的博客

这是我的第一篇博客文章。在这里我会分享我的技术学习心得和生活感悟。

## 关于这个博客

这个博客是用Python Flask构建的，具有以下特性：

- 支持Markdown写作
- 响应式设计
- 代码高亮
- 分类和标签
- 搜索功能
- 自动部署到GitHub Pages

## 技术栈

- **后端**: Python Flask
- **前端**: HTML5, CSS3, JavaScript
- **部署**: GitHub Pages + GitHub Actions
- **写作**: Markdown

## 代码示例

```python
def hello_world():
    print("Hello, World!")
    return "欢迎来到我的博客"

hello_world()

### posts/python-tips.md
```markdown
---
title: "Python编程小技巧"
date: 2024-01-15
category: "技术"
tags: ["Python", "编程", "技巧"]
---

# Python编程小技巧

分享一些实用的Python编程技巧，帮助提高代码质量和开发效率。

## 1. 列表推导式

列表推导式是Python的强大特性之一：

```python
# 传统方法
squares = []
for i in range(10):
    squares.append(i**2)

# 列表推导式
squares = [i**2 for i in range(10)]