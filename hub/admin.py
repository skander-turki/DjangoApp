from email import message
from pyexpat import model
from turtle import title
from django.contrib import admin, messages
from .models import *

# Register your models here.

class ProjectInline(admin.StackedInline): #Stackedinline affichage verticale tabularinline affichage horizentale
    model = Project

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name'
    )
    fields = (
        ('last_name', 'first_name'),
        'email'
    )
    search_fields =['last_name']
    inlines =[ProjectInline]
@admin.register(Coach) # au lieu de  admin.site.register(Coach, CoachAdmin)   
class CoachAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name'
    )
    fields = (
        ('last_name', 'first_name'),
        'email'
    )
    search_fields =['last_name']

class ProjectDurationFilter(admin.SimpleListFilter):
    parameter_name="duree"
    title= "Durée"
    def lookups(self, request, model_admin):
        return(
            ('1 Month', 'less than 1 month'),
            ('3 Month', 'less than 3 months'),
            ('4 Month', 'greater than 3 months')
        )
    def queryset(self, request, queryset):
        if self.value() == "1 Month":
            return queryset.filter(duree__lte=30)
        if self.value() == "3 Month":
            return queryset.filter(duree__gt=30,duree__lte=90)
        if self.value() == "4 Month":
            return queryset.filter(duree__gt=90)

def set_valid(modeladmin, request, queryset):
    rows = queryset.update(isvalid= True)
    if rows == 1:
        msg = "1 project was"
    else:
        msg = f"{rows} project were"
    messages.success(request, message = f"{msg} successfully marked as valid")
     #messages pour le design des message en bootstrap
set_valid.short_description = "Validate"

    


class ProjectAdmin(admin.ModelAdmin):
    def set_invalid(modeladmin, request, queryset):
        number = queryset.filter(isvalid=False)
        if number.count() > 0:
            messages.error(request, "Project already set to not valid")
        else:
            rows = queryset.update(isvalid=False)
            messages.success(request, message= f"{rows} projects sucessfully marked as invalid")
    set_invalid.short_description = "Invalidate"

    actions = [set_valid, 'set_invalid' ]
    actions_on_bottom = True
    actions_on_top = True

    list_filter = (
        'creator',
        'isvalid',
        ProjectDurationFilter

    )
    list_display = (
        'project_name',
        'duree',
        'supervisor',
        'creator',
        'isvalid'
    )
    fieldsets = [   
        (
            'About',
            {
                'fields':(      
                    ('project_name',) ,  
                    ('description',),
                    ('creator'),
                    ('supervisor')
                    )
                
            }
        ),
        (
            None,
            {
            'fields' : ('isvalid',)
            }
        ),
        (
        'Durations',
        {
            'classes': ('collapse',),
            'fields' : (
                'duree',
                'temp_alloue'
            )
        }
        )
    ]
    #radio_fields = {'supervisor': admin.VERTICAL}
    autocomplete_fields = ['supervisor']
    #empty_value_display = '-empty-'
    #readonly_fields = ('project_name') #desactiver un champ

admin.site.register(Project,ProjectAdmin)
admin.site.register(Student, StudentAdmin)
#admin.site.register(Coach, CoachAdmin)
admin.site.register(MembreShip)