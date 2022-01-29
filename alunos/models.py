from django.db import models

# Create your models here.
class Aluno(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros')
    )
    first_name = models.CharField('Nome',max_length=50, null=False, blank=False)
    last_name = models.CharField('Sobrenome',max_length=50, null=False, blank=False)
    email = models.EmailField('E-mail', null=False, blank=False,unique=True)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
    birth_date = models.DateField('Data de nascimento', null=False, blank=False)

def  __str__(self):
    return self.first_name +" "+ self.last_name
    
