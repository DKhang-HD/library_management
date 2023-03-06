from django.db import models
from django.contrib.auth.models import AbstractUser


class AddressField(models.Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'VARCHAR(255)'

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None

        street, city, country = value.split(', ')
        return {'street': street, 'city': city, 'country': country}

    def to_python(self, value):
        if isinstance(value, dict):
            return value

        if value is None:
            return None

        street, city, country = value.split(', ')
        return {'street': street, 'city': city, 'country': country}

    def get_prep_value(self, value):
        if value is None:
            return None

        return f"{value['street']}, {value['city']}, {value['country']}"


class MyUser(AbstractUser):
    email = models.EmailField(max_length=50)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=10, unique=True, null=True)
    address = AddressField(null=True)
    view_homepage = models.IntegerField(default=0)

