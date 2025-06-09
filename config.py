import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    BLOG_TITLE = "我的个人博客"
    BLOG_DESCRIPTION = "分享技术与生活"
    AUTHOR_NAME = "Your Name"
    POSTS_PER_PAGE = 5