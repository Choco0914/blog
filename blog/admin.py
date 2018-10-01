from django.contrib import admin
from . models import Post, Comment
# settings.py 에서 LANGUAGE_CODE = 'en-us'를 'ko'로 바꿔 한국어로 변경했다
admin.site.register(Post)
# 관리자 사이트에서 Post모델을 보려고 위의 코드로 모델을 등록했다
admin.site.register(Comment)
"""
django 관리자 사이트를 이용하기 위해서는 superuser라는 계정을 만들어야 한다
터미널 창에서 python3 manage.py createsuperuser를 입력하면 계정이 생성된다
"""
