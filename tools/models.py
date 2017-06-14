from django.db import models

class Tool(models.Model):

    title = models.CharField('工具名', max_length=20)
    insturction = models.CharField('简介', max_length=50)
    image = models.ImageField('缩略图', upload_to='pic/')

    is_alive = models.BooleanField('是否正常', default=True)

    def __str__(self):
        return self.title


