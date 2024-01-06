from django.contrib import admin
from .models import Producer
from .models import Transporters
from .models import Owner
from .models import Wood
# Register your models here.
admin.site.register(Producer)
admin.site.register(Transporters)
admin.site.register(Owner)
admin.site.register(Wood)