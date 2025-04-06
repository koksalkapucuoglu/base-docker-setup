from django.apps import AppConfig


class NewappConfig(AppConfig):
    name = 'newapp'
    default_auto_field = "django_mongodb_backend.fields.ObjectIdAutoField"
