from django.contrib import admin
from .models import NumberPair
from .tasks import add

@admin.action(description="Run Celery Task: Add")
def run_add_task(modeladmin, request, queryset):
    """
    This function is called when the admin action is triggered.
    It will run the add task for each selected NumberPair object.
    The add task will calculate the sum of number1 and number2 and store it in result.
    """
    for obj in queryset:
        add.delay(str(obj.id))

@admin.register(NumberPair)
class NumberPairAdmin(admin.ModelAdmin):
    list_display = ('number1', 'number2', 'result')
    actions = [run_add_task]
