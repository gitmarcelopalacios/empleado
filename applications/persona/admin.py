from django.contrib import admin
from applications.persona.models import Empleado, Habilidades
from django.utils.html import format_html


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'avatar',
        'full_name',
        #'foto',
        )
    search_fields=('first_name',)
    list_filter=('departamento','job','habilidades',)
    
    filter_horizontal=('habilidades',)
    
    def full_name(self, obj):
        return obj.first_name+' '+obj.last_name
    
    def foto(self, obj):
        return format_html("<img src={{}}/>",obj.avatar.url)
        
        
    
admin.site.register(Empleado, EmpleadoAdmin)
