from comptetence.models import Candidat, Entretient, Technologie, Def_Niveau, Employe, Def_Site, Def_Projet, Competence
from django.contrib import admin

admin.site.register(Candidat)
admin.site.register(Employe)
admin.site.register(Competence)
admin.site.register(Technologie)
admin.site.register(Entretient)
admin.site.register(Def_Niveau)
admin.site.register(Def_Projet)
admin.site.register(Def_Site)
