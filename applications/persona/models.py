from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField(max_length=50)
    
    
    # class Meta:
        # verbose_name='Mi departamento'
        # verbose_name_plural='Areas de la empresa'

    def __str__(self):
        return str(self.id)+'-'+self.habilidad    
            
class Empleado(models.Model):
    JOB_CHOICES=(
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='fotos', blank=True, null=True)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida= RichTextField() 
    
    class Meta:
        # verbose_name='Mi departamento'
        # verbose_name_plural='Areas de la empresa'
        ordering=['first_name','last_name']
        # unique_together=('name','shor_name')
    
    def __str__(self):
        return str(self.id)+'-'+self.first_name+'-'+self.last_name
    