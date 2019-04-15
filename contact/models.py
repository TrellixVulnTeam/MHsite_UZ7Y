from django.db import models

# Create your models here.

class contact(models.Model):
	primeiro_nome = models.CharField(max_length=20)
	segundo_nome = models.CharField(max_length=20)
	email = models.EmailField()
	mensagem = models.CharField(max_length= 550)

	def __str__(self):
		return f'{self.first_name} {self.second_name}'