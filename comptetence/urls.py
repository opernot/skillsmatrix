#from django.views.generic import DetailView, ListView
from django.conf.urls import patterns, url, include
from django.views.generic import list_detail
from comptetence.models import Competence

competence_info = {
    "queryset" : Competence.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'comptetence.views.index'),
    (r'^candidats/$', 'comptetence.views.candidats'),
    (r'^candidats/(?P<candidat_id>\d+)/$', 'comptetence.views.candidatDetail'),
    (r'^candidats/search/$', 'comptetence.views.candidatsAvecCriteres'),
    (r'^candidats/search/validate/$', 'comptetence.views.searchCandidats'),
    (r'^competence/$', list_detail.object_list, competence_info)
)
