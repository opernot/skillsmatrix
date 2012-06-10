# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from comptetence.models import Candidat

def index(request):
    return render_to_response('comptetence/index.html', context_instance=RequestContext(request))

def candidats(request):
    candidats=Candidat.objects.all()
    return render_to_response('comptetence/candidat_list.html', {'listeCandidats':candidats} ,context_instance=RequestContext(request))

def candidatsAvecCriteres(request):
    return render_to_response('comptetence/candidat_rechercher.html',context_instance=RequestContext(request))

def candidatDetail(request, candidat_id):
    p = get_object_or_404(Candidat, pk=candidat_id)
    return render_to_response('comptetence/candidat_detail.html', {'candidat': p})

def searchCandidats(request):
    listeResultat = Candidat.objects.filter(nom__contains=request.POST['nameSearched'])
    return render_to_response('comptetence/candidat_list.html', {'listeCandidats':listeResultat} ,context_instance=RequestContext(request))

