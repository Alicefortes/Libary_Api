from django.db import models
from uuid import uuid4
# Create your models here.
class Books(models.Model):
    id_book= models.UUIDField(primary_key=True, default=uuid4,editable=False)
    title= models.CharField(max_length=255)
    autor= models.CharField(max_length=255)
    ano_lançamento=models.IntegerField()
    estado= models.CharField(max_length=50)
    paginas= models.IntegerField()
    editora =models.CharField(max_length=255)
    criacao=models.DateField(auto_now_add=True)