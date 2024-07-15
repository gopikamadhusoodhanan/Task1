from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .views import BlogPost
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'user_type', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register(BlogPost)