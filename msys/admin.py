from django.contrib import admin
from .models import DataEntrycc1, DataEntrycc2, DataEntryacl
#from django.contrib.auth import get_user_model
#from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import CustomUser

'''class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
'''
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('System_No', 'Model_No', 'Date',)
    list_filter = ('Date',)

# admin.site.register(Post)
admin.site.register(DataEntrycc1, SnippetAdmin)
admin.site.register(DataEntrycc2, SnippetAdmin)
admin.site.register(DataEntryacl, SnippetAdmin)
