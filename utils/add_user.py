# coding=utf-8
# auth: zhangyiling
# time: 2019/3/16 下午11:01
# description: 引用django环境变量  # 批量创建用户

import os, sys, django
from django.contrib.auth import get_user_model

User = get_user_model()

# 当前脚本目录: /Users/mac/venv/Adaops/utils/add_user.py
print(os.path.realpath(__file__))

# /Users/mac/venv/Adaops
project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(project_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Adaops.settings')

django.setup()  # 接下来和写 django 项目一样 # 引用 django


def ger_user():
    """获取用户."""
    for user in User.objects.all():
        print(user.username)


if __name__ == '__main__':
    ger_user()
