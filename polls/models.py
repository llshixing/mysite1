from django.db import models

# Create your models here.


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=200)

    def __str__(self):  # 重写直接输出类的方法
        return "<Question:{id=%s,text=%s}>" \
            % (self.id, self.text)
