from django.contrib import admin
from .models import personal,paciente,solicitud_turno
# SUPER USER:   User: eveLPP
#               email: e.pignattagarcia@gmail.com
#               password: ramo123567
admin.site.register(personal)

admin.site.register(paciente)

admin.site.register(solicitud_turno)