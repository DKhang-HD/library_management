from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import MyUser
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
# Create your forms


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ("username", "email", "phone_number", "date_of_birth", "password1", "password2")


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = MyUser
        fields = ("username", "email", "phone_number")

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
#
#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


class ErrorListMsg(ErrorList):
    def __unicode__(self):
        return self.as_msg()

    def as_msg(self):
        if not self:
            return u''
        return mark_safe(u'\n'.join([u'<span class="red">%s</span>' % e for e in self]))
