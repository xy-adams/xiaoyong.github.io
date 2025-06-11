import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SITE_TITLE = "小永的个人主页"
    SITE_DESCRIPTION = "欢迎来到我的个人网站"
    AUTHOR_NAME = "小永"
    AUTHOR_TITLE = "软件开发工程师"
    AUTHOR_EMAIL = "xiaoyong@example.com"
    GITHUB_URL = "https://github.com/xiaoyong"
    LINKEDIN_URL = "https://linkedin.com/in/xiaoyong"