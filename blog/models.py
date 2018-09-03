from django.db import models
from django.utils import timezone

class Post(models.Model):
    # models는 Post가 django model임을 의미한다 이 코드로 인해 django는
    # Post가 데이터베이스에 저장되어야 한다고 알게 된다
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # models.ForeignKey 다른 모델에 대한 링크를 의미한다
    title = models.CharField(max_length=200)
    # models.ChariField 글자 수가 제한된 텍스트를 정의할 때 사용한다
    text = models.TextField()
    # models.TextField  글자 수에 제한이 없는 긴 텍스트를 위한 속성이다
    created_date = models.DateTimeField(
            default = timezone.now)
    published_date = models.DateTimeField(
                blank = True, null = True)
    # models.DateTimeField는 날짜와 시간을 의미한다
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
