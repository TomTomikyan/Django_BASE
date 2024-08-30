from django.db import models

# Create your models here.

class cat(models.Model):

    name = models.CharField('cat name',max_length=250)
    img = models.ImageField('cat image',upload_to='category/')

    def __str__(self) -> str:
        return self.name
    
class prod(models.Model):

    cat = models.ForeignKey(cat,on_delete=models.CASCADE,related_name='prod')
    name = models.CharField('prod name',max_length=250)
    img = models.ImageField('prod image',upload_to='product/')

    def __str__(self) -> str:
        return self.name
