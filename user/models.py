from django.db import models
# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    registerTime = models.DateTimeField(auto_now_add=True,null=True)
    role_id = models.ForeignKey('Role', to_field='roleId', default=1, on_delete=models.CASCADE)

    def __str__(self):  # 重写直接输出类的方法
        return "<User:{id=%s,userName=%s,password=%s}>" \
            % (self.id, self.password, self.password)


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    roleValue = models.CharField(max_length=20)
    roleId = models.IntegerField(unique=True)
