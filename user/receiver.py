from django.dispatch import receiver
from .signal import signup_done, myname, view
from .views import SignUpView, MyUser


@receiver(signup_done, sender=SignUpView, dispatch_uid="my_unique_identifier")
def confirm_signup(sender, **kwargs):
    print('You signup successfully')
    print('sender', sender)


@receiver(myname, sender=MyUser)
def show_name(sender, instance, **kwargs):
    print(instance.username)


@receiver(view, sender=MyUser)
def show_view(sender, instance, **kwargs):
    instance.view_homepage += 1
    instance.save()
