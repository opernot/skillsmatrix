from django.db import models

# Definition du modele pour les competences du centre
class Def_Niveau(models.Model):
    nom = models.CharField(max_length=200)
    valeur = models.IntegerField(null=True)
    def __unicode__(self):
        return self.nom    

class Def_Site(models.Model):
    nom = models.CharField(max_length=200)
    localisation = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nom    

class Def_Projet(models.Model):
    nom = models.CharField(max_length=200)
    localisation = models.ManyToManyField("Def_Site",blank=True, null=True)
    def __unicode__(self):
        return self.nom

class Technologie(models.Model):
    nom = models.CharField(max_length=200)
    domain = models.CharField(max_length=200, null=True)
    def __unicode__(self):
        return self.nom

class Competence(models.Model):
    tecno = models.ForeignKey(Technologie)
    niveau = models.ForeignKey(Def_Niveau)
    experience = models.IntegerField(null=True)
    observation = models.CharField(max_length=200, null=True)
    def __unicode__(self):
        return "Competence " + self.tecno.nom

class Candidat(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    statut = models.CharField(max_length=200, null=True, help_text="Please specify the statut of the candidat.")
    tecnos = models.ManyToManyField("Technologie",blank=True, null=True)
    def __unicode__(self):
        return self.prenom + " " + self.nom  

class Employe(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    fonction = models.CharField(max_length=200, null=True)
    projet = models.ForeignKey("Candidat", null=True)
    statut = models.CharField(max_length=200, null=True)
    competence = models.ManyToManyField("Competence",blank=True, null=True)
    projet = models.ManyToManyField("Def_Projet",blank=True, null=True)
    photo = models.ImageField(upload_to='img/photo', null=True)
    def __unicode__(self):
        return self.prenom + " " + self.nom  

class Entretient(models.Model):
    candidat = models.ForeignKey(Candidat)
    observation_technique = models.CharField(max_length=200, null=True)
    observation = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return "entretient(" + self.candidat.nom + ")"
