from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from .forms import MyUserCreationForm, MyUserChangeForm

# Register your models here.


# Display the custom field and make them editable through admin

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ["username", "email", "phone_number", "date_of_birth"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ("phone_number", "date_of_birth", "address")}),)


admin.site.register(MyUser, MyUserAdmin)
