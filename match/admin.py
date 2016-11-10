from django.contrib import admin

from .models import Team
from .models import Player
from .models import Tournament

# Registered models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Tournament)