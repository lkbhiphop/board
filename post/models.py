from django.db import models

# Create your models here.
class Post(models.Model):
    # Post라는 모델을 models.Model을 상속받는다
    title  = models.Charfield(max_length =50) 
    content = models.Charfield(max_length = 100)
    
    def __str__(self):
    # object에 대해 출력하면 title을 출력할수잇도록 꺼내준다.
        return self.title