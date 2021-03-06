# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify,
#   and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Abonne(models.Model):
    # Field name made lowercase.
    abonneid = models.AutoField(db_column='AbonneID', primary_key=True)
    # Field name made lowercase.
    categorieid = models.ForeignKey('Categorie', db_column='CategorieID')
    # Field name made lowercase.
    abonne = models.CharField(
        db_column='Abonne', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    bibliotheque = models.CharField(db_column='Bibliotheque', max_length=200)
    # Field name made lowercase.
    consortiumid = models.IntegerField(db_column='ConsortiumID')
    # Field name made lowercase.
    activer = models.IntegerField(db_column='Activer')
    # Field name made lowercase.
    service = models.CharField(db_column='Service', max_length=75)
    # Field name made lowercase.
    exclure = models.IntegerField(db_column='Exclure')
    # Field name made lowercase.
    abonnefact = models.CharField(db_column='AbonneFact', max_length=200)
    # Field name made lowercase.
    bibliothequefact = models.CharField(
        db_column='BibliothequeFact', max_length=200)
    # Field name made lowercase.
    servicefact = models.CharField(db_column='ServiceFact', max_length=75)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.
    # Field name made lowercase.
    agence = models.IntegerField(db_column='Agence')
    icone = models.CharField(max_length=75)
    # Field name made lowercase.
    requesterid = models.CharField(
        db_column='requesterID', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abonne'
        app_label = 'legacy'

    def __str__(self):
        return '{} [type: {}] {}'.format(self.abonneid, self.categorieid, self.abonne)


class Abonneaccess(models.Model):
    # Field name made lowercase.
    abonneaccessid = models.AutoField(
        db_column='AbonneAccessID', primary_key=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    mot_de_passe = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID', blank=True, null=True)
    # Field name made lowercase.
    exclure = models.IntegerField(db_column='Exclure')
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'abonneaccess'
        app_label = 'legacy'


class Abonneindividus(models.Model):
    # Field name made lowercase.
    abonneindividusid = models.AutoField(
        db_column='abonneIndividusID', primary_key=True)
    password = models.CharField(max_length=50)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    courriel = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abonneindividus'
        app_label = 'legacy'


class Abonnement(models.Model):
    # Field name made lowercase.
    abonnementid = models.AutoField(db_column='AbonnementID', primary_key=True)
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID', blank=True, null=True)
    # Field name made lowercase.
    prixtotalabonnement = models.DecimalField(
        db_column='PrixTotalAbonnement', max_digits=20, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    typeabonnementid = models.IntegerField(
        db_column='TypeAbonnementID', blank=True, null=True)
    # Field name made lowercase.
    categorieid = models.IntegerField(
        db_column='CategorieID', blank=True, null=True)
    # Field name made lowercase.
    typedocumentid = models.IntegerField(
        db_column='TypeDocumentID', blank=True, null=True)
    # Field name made lowercase.
    modeaccessid = models.IntegerField(
        db_column='ModeAccessID', blank=True, null=True)
    # Field name made lowercase.
    individuid = models.IntegerField(
        db_column='IndividuID', blank=True, null=True)
    # Field name made lowercase.
    consortiumid = models.IntegerField(
        db_column='ConsortiumID', blank=True, null=True)
    # Field name made lowercase.
    debutabonnement = models.DateTimeField(
        db_column='DebutAbonnement', blank=True, null=True)
    # Field name made lowercase.
    finabonnement = models.DateTimeField(
        db_column='FinAbonnement', blank=True, null=True)
    # Field name made lowercase.
    papier = models.IntegerField(db_column='Papier', blank=True, null=True)
    # Field name made lowercase.
    commentaires = models.TextField(
        db_column='Commentaires', blank=True, null=True)
    gratuit = models.IntegerField(blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'abonnement'
        app_label = 'legacy'


class Abonnepanier(models.Model):
    # Field name made lowercase.
    abonnepanierid = models.AutoField(
        db_column='AbonnePanierID', primary_key=True)
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID')
    # Field name made lowercase.
    panierid = models.IntegerField(db_column='PanierID')

    class Meta:
        managed = False
        db_table = 'abonnepanier'
        app_label = 'legacy'


class Adresse(models.Model):
    # Field name made lowercase.
    adresseid = models.AutoField(db_column='AdresseID', primary_key=True)
    # Field name made lowercase.
    typeadresseid = models.IntegerField(
        db_column='TypeAdresseID', blank=True, null=True)
    # Field name made lowercase.
    adresse1 = models.CharField(
        db_column='Adresse1', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    contactid = models.IntegerField(
        db_column='ContactID', blank=True, null=True)
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID')
    # Field name made lowercase.
    paysid = models.IntegerField(db_column='PaysID')
    # Field name made lowercase.
    provinceetatid = models.IntegerField(db_column='ProvinceEtatID')
    # Field name made lowercase.
    codepostal = models.CharField(
        db_column='CodePostal', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    autreprovince = models.CharField(db_column='AutreProvince', max_length=55)
    # Field name made lowercase.
    ville = models.CharField(db_column='Ville', max_length=50)
    # Field name made lowercase.
    adresse2 = models.CharField(
        db_column='Adresse2', max_length=70, blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.
    # Field name made lowercase.
    localisationid = models.IntegerField(db_column='LocalisationID')

    class Meta:
        managed = False
        db_table = 'adresse'
        app_label = 'legacy'


class Adressesip(models.Model):
    # Field name made lowercase.
    adresseipid = models.BigIntegerField(
        db_column='adresseIPID', primary_key=True)
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID', blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adressesip'
        app_label = 'legacy'


class Categorie(models.Model):
    # Field name made lowercase.
    categorieid = models.AutoField(db_column='CategorieID', primary_key=True)
    # Field name made lowercase.
    categorie = models.CharField(
        db_column='Categorie', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    categorieanglais = models.CharField(
        db_column='CategorieAnglais', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    pourcentage = models.CharField(
        db_column='Pourcentage', max_length=50, blank=True, null=True)
    langue = models.CharField(max_length=2)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.
    idunique = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categorie'
        app_label = 'legacy'

    def __str__(self):
        return '{} {}'.format(self.categorieid, self.categorie)


class Commande(models.Model):
    commandeid = models.AutoField(primary_key=True)
    nocommande = models.CharField(max_length=45)
    daterecu = models.DateField()
    heurerecu = models.TimeField(blank=True, null=True)
    abonneid = models.IntegerField()
    # Field name made lowercase. This field type is a guess.
    anneeabonnement = models.TextField(db_column='AnneeAbonnement')
    # Field name made lowercase.
    noboncommande = models.CharField(db_column='NoBonCommande', max_length=45)
    panier = models.IntegerField()
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.
    # Field name made lowercase.
    prorata = models.IntegerField(db_column='Prorata')
    # Field name made lowercase.
    periode = models.CharField(db_column='Periode', max_length=45)
    trimestrepayable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commande'
        app_label = 'legacy'


class Consortium(models.Model):
    # Field name made lowercase.
    consortiumid = models.AutoField(db_column='ConsortiumID', primary_key=True)
    # Field name made lowercase.
    consortium = models.CharField(
        db_column='Consortium', max_length=100, blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consortium'
        app_label = 'legacy'


class Contact(models.Model):
    # Field name made lowercase.
    contactid = models.AutoField(db_column='ContactID', primary_key=True)
    # Field name made lowercase.
    typecontactid = models.ForeignKey(
        'Typecontact', db_column='TypeContactID', blank=True, null=True)
    # Field name made lowercase.
    nomfamille = models.CharField(
        db_column='NomFamille', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    prenom = models.CharField(
        db_column='Prenom', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    courriel = models.CharField(
        db_column='Courriel', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID', blank=True, null=True)
    # Field name made lowercase.
    telephone = models.CharField(
        db_column='Telephone', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    telecopieur = models.CharField(db_column='Telecopieur', max_length=25)
    # Field name made lowercase.
    exclure = models.IntegerField(db_column='Exclure')
    # Field name made lowercase.
    motdepasse = models.CharField(
        db_column='MotDePasse', unique=True, max_length=45)
    # Field name made lowercase.
    nomfamillefact = models.CharField(
        db_column='NomFamilleFact', max_length=50)
    # Field name made lowercase.
    prenomfact = models.CharField(db_column='PrenomFact', max_length=50)
    # Field name made lowercase.
    courrielfact = models.CharField(db_column='CourrielFact', max_length=50)
    groupe = models.CharField(max_length=6)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact'
        app_label = 'legacy'


class Devise(models.Model):
    # Field name made lowercase.
    deviseid = models.AutoField(db_column='DeviseID', primary_key=True)
    # Field name made lowercase.
    devise = models.CharField(
        db_column='Devise', max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devise'
        app_label = 'legacy'


class Editeur(models.Model):
    # Field name made lowercase.
    editeurid = models.IntegerField(db_column='EditeurID', primary_key=True)
    # Field name made lowercase.
    revueid = models.ForeignKey('Revue', db_column='RevueID')
    # Field name made lowercase.
    editeur = models.CharField(db_column='Editeur', max_length=200)

    class Meta:
        managed = False
        db_table = 'editeur'
        app_label = 'legacy'


class Facture(models.Model):
    # Field name made lowercase.
    factureid = models.AutoField(db_column='FactureID', primary_key=True)
    nofacture = models.CharField(max_length=45)
    # Field name made lowercase.
    prixavanttaxe = models.DecimalField(
        db_column='PrixAvantTaxe', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    prixaprestaxe = models.DecimalField(
        db_column='PrixAprestaxe', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID')
    commandeid = models.IntegerField()
    # Field name made lowercase.
    datefacturation = models.DateField(db_column='DateFacturation')
    # Field name made lowercase.
    sommerecue = models.DecimalField(
        db_column='SommeRecue', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    solde = models.DecimalField(
        db_column='Solde', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    nocheque = models.CharField(
        db_column='NoCheque', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    regle = models.IntegerField(db_column='Regle')
    # Field name made lowercase.
    datemaj = models.DateTimeField(db_column='DateMAJ')
    # Field name made lowercase.
    notes = models.CharField(
        db_column='Notes', max_length=120, blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.
    # Field name made lowercase.
    deviseid = models.IntegerField(db_column='DeviseID')
    # Field name made lowercase.
    prorate = models.IntegerField(db_column='Prorate')
    # Field name made lowercase.
    gratuit = models.IntegerField(db_column='Gratuit')
    # Field name made lowercase.
    tpsexclure = models.IntegerField(db_column='TPSExclure')
    # Field name made lowercase.
    tvqexclure = models.IntegerField(db_column='TVQExclure')
    # Field name made lowercase.
    tauxtaxeid = models.IntegerField(
        db_column='TauxTaxeID', blank=True, null=True)
    # Field name made lowercase.
    datedepot = models.DateField(db_column='DateDepot', blank=True, null=True)
    # Field name made lowercase.
    tps = models.FloatField(db_column='TPS', blank=True, null=True)
    # Field name made lowercase.
    tvq = models.FloatField(db_column='TVQ', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facture'
        app_label = 'legacy'


class Historique(models.Model):
    # Field name made lowercase.
    historiqueid = models.AutoField(db_column='HistoriqueID', primary_key=True)
    # Field name made lowercase.
    historiquedescription = models.CharField(
        db_column='HistoriqueDescription', max_length=100)

    class Meta:
        managed = False
        db_table = 'historique'
        app_label = 'legacy'


class Historiquerevue(models.Model):
    # Field name made lowercase.
    historiqueid = models.ForeignKey(Historique, db_column='HistoriqueID')
    # Field name made lowercase.
    revueid = models.ForeignKey('Revue', db_column='RevueID')
    # Field name made lowercase.
    ordre = models.SmallIntegerField(db_column='Ordre')

    class Meta:
        managed = False
        db_table = 'historiquerevue'
        unique_together = (('historiqueid', 'revueid'),)
        app_label = 'legacy'


class Individu(models.Model):
    # Field name made lowercase.
    individuid = models.AutoField(db_column='IndividuID', primary_key=True)
    # Field name made lowercase.
    nomfamille = models.CharField(
        db_column='NomFamille', max_length=75, blank=True, null=True)
    # Field name made lowercase.
    prenom = models.CharField(
        db_column='Prenom', max_length=50, blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'individu'
        app_label = 'legacy'


class Intip(models.Model):
    # Field name made lowercase.
    intipid = models.AutoField(db_column='intipID', primary_key=True)
    debutint = models.CharField(max_length=15)
    finint = models.CharField(max_length=15)
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID')
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'intip'
        app_label = 'legacy'


class Ls(models.Model):
    # Field name made lowercase.
    ls_revueabonneid = models.AutoField(
        db_column='LS_RevueAbonneID', primary_key=True)
    # Field name made lowercase.
    ls_revueid = models.IntegerField(
        db_column='LS_RevueID', blank=True, null=True)
    # Field name made lowercase.
    ls_abonneid = models.IntegerField(
        db_column='LS_AbonneID', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    ls_annneeabonnement = models.TextField(
        db_column='LS_AnnneeAbonnement', blank=True, null=True)
    # Field name made lowercase.
    ls_commandeid = models.IntegerField(
        db_column='LS_CommandeID', blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ls'
        app_label = 'legacy'


class Paiement(models.Model):
    # Field name made lowercase.
    paiementid = models.AutoField(db_column='PaiementID', primary_key=True)
    # Field name made lowercase.
    abonneid = models.ForeignKey(
        Abonne, db_column='AbonneID', blank=True, null=True)
    # Field name made lowercase.
    commandeid = models.IntegerField(
        db_column='CommandeID', blank=True, null=True)
    # Field name made lowercase.
    anneeabonnement = models.CharField(
        db_column='AnneeAbonnement', max_length=4)
    # Field name made lowercase.
    daterecue = models.DateField(db_column='DateRecue')
    # Field name made lowercase.
    paiementfait = models.IntegerField(db_column='PaiementFait')

    class Meta:
        managed = False
        db_table = 'paiement'
        app_label = 'legacy'


class Panier(models.Model):
    # Field name made lowercase.
    panierid = models.AutoField(db_column='PanierID', primary_key=True)
    # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=75)
    # Field name made lowercase.
    dateapplication = models.DateTimeField(db_column='DateApplication')
    consortium = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'panier'
        app_label = 'legacy'


class Panierrevue(models.Model):
    # Field name made lowercase.
    panierrevueid = models.AutoField(
        db_column='PanierRevueID', primary_key=True)
    # Field name made lowercase.
    panierid = models.IntegerField(db_column='PanierID', blank=True, null=True)
    # Field name made lowercase.
    revueid = models.IntegerField(db_column='RevueID')

    class Meta:
        managed = False
        db_table = 'panierrevue'
        app_label = 'legacy'


class Pays(models.Model):
    # Field name made lowercase.
    paysid = models.AutoField(db_column='PaysID', primary_key=True)
    # Field name made lowercase.
    pays = models.CharField(
        db_column='Pays', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    code = models.CharField(
        db_column='Code', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    langue = models.CharField(
        db_column='Langue', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    devise = models.CharField(db_column='Devise', max_length=6)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.
    # Field name made lowercase.
    paysanglais = models.CharField(
        db_column='PaysAnglais', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pays'
        app_label = 'legacy'


class Prixrevue(models.Model):
    # Field name made lowercase.
    prixpanierid = models.AutoField(db_column='prixpanierID', primary_key=True)
    revueid = models.IntegerField()
    prix = models.DecimalField(
        max_digits=19, decimal_places=2, blank=True, null=True)
    panierid = models.IntegerField()
    reglecalcul = models.IntegerField()
    annee = models.TextField()  # This field type is a guess.
    consortiumid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prixrevue'
        app_label = 'legacy'


class Provetetat(models.Model):
    # Field name made lowercase.
    provetatid = models.AutoField(db_column='ProvEtatID', primary_key=True)
    # Field name made lowercase.
    provetat = models.CharField(
        db_column='ProvEtat', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    codealpha = models.CharField(
        db_column='CodeAlpha', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    abreviation = models.CharField(
        db_column='Abreviation', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    code = models.IntegerField(db_column='Code', blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provetetat'
        app_label = 'legacy'


class Rapport2007(models.Model):
    # Field name made lowercase.
    rapport2007id = models.AutoField(
        db_column='Rapport2007ID', primary_key=True)
    # Field name made lowercase.
    abonne = models.CharField(db_column='Abonne', max_length=145)
    # Field name made lowercase.
    daterecue = models.DateTimeField(db_column='DateRecue')
    # Field name made lowercase.
    typeabonnement = models.CharField(
        db_column='TypeAbonnement', max_length=15)
    # Field name made lowercase.
    prorata = models.IntegerField(db_column='Prorata')
    # Field name made lowercase.
    prixitem = models.DecimalField(
        db_column='PrixItem', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    tarifprorata = models.DecimalField(
        db_column='TarifProrata', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    escompte = models.IntegerField(db_column='Escompte')
    # Field name made lowercase.
    prixpaye = models.DecimalField(
        db_column='PrixPaye', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    revue = models.CharField(db_column='Revue', max_length=175)
    # Field name made lowercase.
    periode = models.CharField(db_column='Periode', max_length=75)
    # Field name made lowercase.
    anneeabonnement = models.IntegerField(db_column='AnneeAbonnement')
    # Field name made lowercase.
    revueid = models.IntegerField(db_column='RevueID')
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID')
    # Field name made lowercase.
    commandeid = models.IntegerField(db_column='CommandeID')
    # Field name made lowercase.
    deviseid = models.IntegerField(db_column='DeviseID')

    class Meta:
        managed = False
        db_table = 'rapport2007'
        app_label = 'legacy'


class Rapport2008(models.Model):
    # Field name made lowercase.
    rapport2008id = models.AutoField(
        db_column='Rapport2008ID', primary_key=True)
    # Field name made lowercase.
    abonne = models.CharField(db_column='Abonne', max_length=145)
    # Field name made lowercase.
    daterecue = models.DateTimeField(db_column='DateRecue')
    # Field name made lowercase.
    typeabonnement = models.CharField(
        db_column='TypeAbonnement', max_length=15)
    # Field name made lowercase.
    prorata = models.IntegerField(db_column='Prorata')
    # Field name made lowercase.
    prixitem = models.DecimalField(
        db_column='PrixItem', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    tarifprorata = models.DecimalField(
        db_column='TarifProrata', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    escompte = models.IntegerField(db_column='Escompte')
    # Field name made lowercase.
    prixpaye = models.DecimalField(
        db_column='PrixPaye', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    revue = models.CharField(db_column='Revue', max_length=175)
    # Field name made lowercase.
    periode = models.CharField(db_column='Periode', max_length=75)
    # Field name made lowercase.
    anneeabonnement = models.IntegerField(
        db_column='AnneeAbonnement', blank=True, null=True)
    # Field name made lowercase.
    revueid = models.IntegerField(db_column='RevueID')
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID')
    # Field name made lowercase.
    commandeid = models.IntegerField(db_column='CommandeID')
    # Field name made lowercase.
    deviseid = models.IntegerField(db_column='DeviseID')
    # Field name made lowercase.
    prixcan = models.DecimalField(
        db_column='PrixCan', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    tauxchange = models.DecimalField(
        db_column='TauxChange', max_digits=19, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'rapport2008'
        app_label = 'legacy'


class Rapport2009(models.Model):
    # Field name made lowercase.
    rapport2009id = models.AutoField(
        db_column='Rapport2009ID', primary_key=True)
    # Field name made lowercase.
    abonne = models.CharField(db_column='Abonne', max_length=145)
    # Field name made lowercase.
    daterecue = models.DateTimeField(db_column='DateRecue')
    # Field name made lowercase.
    typeabonnement = models.CharField(
        db_column='TypeAbonnement', max_length=15)
    # Field name made lowercase.
    prorata = models.IntegerField(db_column='Prorata')
    # Field name made lowercase.
    prixitem = models.DecimalField(
        db_column='PrixItem', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    tarifprorata = models.DecimalField(
        db_column='TarifProrata', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    escompte = models.IntegerField(db_column='Escompte')
    # Field name made lowercase.
    prixpaye = models.DecimalField(
        db_column='PrixPaye', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    revue = models.CharField(db_column='Revue', max_length=175)
    # Field name made lowercase.
    periode = models.CharField(db_column='Periode', max_length=75)
    # Field name made lowercase.
    anneeabonnement = models.IntegerField(
        db_column='AnneeAbonnement', blank=True, null=True)
    # Field name made lowercase.
    revueid = models.IntegerField(db_column='RevueID')
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID')
    # Field name made lowercase.
    commandeid = models.IntegerField(db_column='CommandeID')
    # Field name made lowercase.
    deviseid = models.IntegerField(db_column='DeviseID')
    # Field name made lowercase.
    prixcan = models.DecimalField(
        db_column='PrixCan', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    tauxchange = models.DecimalField(
        db_column='TauxChange', max_digits=19, decimal_places=8)
    # Field name made lowercase.
    prixpayefacture = models.DecimalField(
        db_column='PrixPayeFacture', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    transfere = models.IntegerField(db_column='Transfere')
    # Field name made lowercase.
    paiementfait = models.IntegerField(
        db_column='PaiementFait', blank=True, null=True)
    # Field name made lowercase.
    consortiumid = models.IntegerField(db_column='ConsortiumID')
    # Field name made lowercase.
    escompteconsortium = models.IntegerField(db_column='EscompteConsortium')

    class Meta:
        managed = False
        db_table = 'rapport2009'
        app_label = 'legacy'


class Rapport2010(models.Model):
    # Field name made lowercase.
    rapport2010id = models.AutoField(
        db_column='Rapport2010ID', primary_key=True)
    # Field name made lowercase.
    abonne = models.CharField(db_column='Abonne', max_length=145)
    # Field name made lowercase.
    daterecue = models.DateTimeField(db_column='DateRecue')
    # Field name made lowercase.
    typeabonnement = models.CharField(
        db_column='TypeAbonnement', max_length=15)
    # Field name made lowercase.
    prorata = models.IntegerField(db_column='Prorata')
    # Field name made lowercase.
    prixitem = models.DecimalField(
        db_column='PrixItem', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    tarifprorata = models.DecimalField(
        db_column='TarifProrata', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    escompte = models.IntegerField(db_column='Escompte')
    # Field name made lowercase.
    prixpaye = models.DecimalField(
        db_column='PrixPaye', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    revue = models.CharField(db_column='Revue', max_length=175)
    # Field name made lowercase.
    periode = models.CharField(db_column='Periode', max_length=75)
    # Field name made lowercase.
    anneeabonnement = models.IntegerField(
        db_column='AnneeAbonnement', blank=True, null=True)
    # Field name made lowercase.
    revueid = models.IntegerField(db_column='RevueID')
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID')
    # Field name made lowercase.
    commandeid = models.IntegerField(db_column='CommandeID')
    # Field name made lowercase.
    deviseid = models.IntegerField(db_column='DeviseID')
    # Field name made lowercase.
    prixcan = models.DecimalField(
        db_column='PrixCan', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    tauxchange = models.DecimalField(
        db_column='TauxChange', max_digits=19, decimal_places=8)
    # Field name made lowercase.
    prixpayefacture = models.DecimalField(
        db_column='PrixPayeFacture', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    transfere = models.IntegerField(db_column='Transfere')
    # Field name made lowercase.
    paiementfait = models.IntegerField(
        db_column='PaiementFait', blank=True, null=True)
    # Field name made lowercase.
    consortiumid = models.IntegerField(db_column='ConsortiumID')
    # Field name made lowercase.
    escompteconsortium = models.IntegerField(db_column='EscompteConsortium')
    # Field name made lowercase.
    quantite = models.IntegerField(db_column='Quantite')

    class Meta:
        managed = False
        db_table = 'rapport2010'
        app_label = 'legacy'


class Rapport2011(models.Model):
    # Field name made lowercase.
    rapport2011id = models.AutoField(
        db_column='Rapport2011ID', primary_key=True)
    # Field name made lowercase.
    abonne = models.CharField(db_column='Abonne', max_length=145)
    # Field name made lowercase.
    daterecue = models.DateTimeField(db_column='DateRecue')
    # Field name made lowercase.
    typeabonnement = models.CharField(
        db_column='TypeAbonnement', max_length=15)
    # Field name made lowercase.
    prorata = models.IntegerField(db_column='Prorata')
    # Field name made lowercase.
    prixitem = models.DecimalField(
        db_column='PrixItem', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    tarifprorata = models.DecimalField(
        db_column='TarifProrata', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    escompte = models.IntegerField(db_column='Escompte')
    # Field name made lowercase.
    prixpaye = models.DecimalField(
        db_column='PrixPaye', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    revue = models.CharField(db_column='Revue', max_length=175)
    # Field name made lowercase.
    periode = models.CharField(db_column='Periode', max_length=75)
    # Field name made lowercase.
    anneeabonnement = models.IntegerField(
        db_column='AnneeAbonnement', blank=True, null=True)
    # Field name made lowercase.
    revueid = models.IntegerField(db_column='RevueID')
    # Field name made lowercase.
    abonneid = models.IntegerField(db_column='AbonneID')
    # Field name made lowercase.
    commandeid = models.IntegerField(db_column='CommandeID')
    # Field name made lowercase.
    deviseid = models.IntegerField(db_column='DeviseID')
    # Field name made lowercase.
    prixcan = models.DecimalField(
        db_column='PrixCan', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    tauxchange = models.DecimalField(
        db_column='TauxChange', max_digits=19, decimal_places=8)
    # Field name made lowercase.
    prixpayefacture = models.DecimalField(
        db_column='PrixPayeFacture', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    transfere = models.IntegerField(db_column='Transfere')
    # Field name made lowercase.
    paiementfait = models.IntegerField(
        db_column='PaiementFait', blank=True, null=True)
    # Field name made lowercase.
    consortiumid = models.IntegerField(db_column='ConsortiumID')
    # Field name made lowercase.
    escompteconsortium = models.IntegerField(db_column='EscompteConsortium')
    # Field name made lowercase.
    quantite = models.IntegerField(db_column='Quantite')

    class Meta:
        managed = False
        db_table = 'rapport2011'
        app_label = 'legacy'


class Rapportconsolide(models.Model):
    # Field name made lowercase.
    rapportconsolideid = models.AutoField(
        db_column='RapportConsolideID', primary_key=True)
    abonne = models.CharField(max_length=145)
    titrerev = models.CharField(max_length=145)
    daterecue = models.DateTimeField()
    panier = models.IntegerField()
    prorata = models.IntegerField()
    pourcentage = models.IntegerField()
    prixitem = models.DecimalField(max_digits=19, decimal_places=2)
    reglecalcul = models.IntegerField()
    revueid = models.IntegerField()
    clerapport = models.CharField(max_length=45)
    motpasse = models.CharField(max_length=30)
    abonneid = models.IntegerField()
    prixpaye = models.DecimalField(max_digits=19, decimal_places=2)
    anneeabonnement = models.IntegerField()
    regle = models.IntegerField()
    gratuit = models.IntegerField()
    commandeid = models.IntegerField()
    deviseid = models.IntegerField()
    tauxchange = models.DecimalField(max_digits=19, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'rapportconsolide'
        app_label = 'legacy'


class Rapportjuinseptembre2008(models.Model):
    # Field name made lowercase.
    rapportjuinseptembre2008id = models.AutoField(
        db_column='RapportJuinSeptembre2008ID', primary_key=True)
    # Field name made lowercase.
    abonne = models.CharField(db_column='Abonne', max_length=145)
    # Field name made lowercase.
    daterecue = models.DateTimeField(db_column='DateRecue')
    # Field name made lowercase.
    typeabonnement = models.IntegerField(db_column='TypeAbonnement')
    # Field name made lowercase.
    prorata = models.IntegerField(db_column='Prorata')
    # Field name made lowercase.
    prix = models.DecimalField(
        db_column='Prix', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    prixitem = models.DecimalField(
        db_column='PrixItem', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    pourcentage = models.IntegerField(db_column='Pourcentage')
    # Field name made lowercase.
    prixpaye = models.DecimalField(
        db_column='PrixPaye', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    reglecalcul = models.IntegerField(db_column='RegleCalcul')
    # Field name made lowercase.
    titrerev = models.CharField(db_column='Titrerev', max_length=145)
    # Field name made lowercase.
    consortiumid = models.IntegerField(db_column='ConsortiumID')
    # Field name made lowercase.
    anneeabonnement = models.IntegerField(db_column='AnneeAbonnement')
    # Field name made lowercase.
    revueid = models.IntegerField(db_column='RevueID')
    # Field name made lowercase.
    commandeid = models.IntegerField(db_column='CommandeID')
    # Field name made lowercase.
    tauxchange = models.DecimalField(
        db_column='TauxChange', max_digits=19, decimal_places=8)
    # Field name made lowercase.
    deviseid = models.IntegerField(db_column='DeviseID')
    # Field name made lowercase.
    prixprorata = models.DecimalField(
        db_column='Prixprorata', max_digits=19, decimal_places=2)
    # Field name made lowercase.
    notes = models.CharField(
        db_column='Notes', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    escompteconsortium = models.IntegerField(db_column='EscompteConsortium')
    # Field name made lowercase.
    region = models.IntegerField(db_column='Region')
    # Field name made lowercase.
    clerapport = models.CharField(db_column='CleRapport', max_length=45)

    class Meta:
        managed = False
        db_table = 'rapportjuinseptembre2008'
        app_label = 'legacy'


class Revenus(models.Model):
    revueid = models.IntegerField()
    abonneid = models.IntegerField()
    pourcentage = models.IntegerField()
    prorata = models.IntegerField()
    tarifprorata = models.DecimalField(max_digits=19, decimal_places=4)
    prixpaye = models.DecimalField(max_digits=19, decimal_places=2)
    tauxchange = models.DecimalField(max_digits=19, decimal_places=8)
    devise = models.IntegerField()
    commandeid = models.IntegerField()
    revueabonneid = models.IntegerField()
    trimestre = models.IntegerField()
    revenusid = models.AutoField(primary_key=True)
    service = models.DecimalField(max_digits=19, decimal_places=4)
    typeabonnement = models.CharField(max_length=10)
    regle = models.IntegerField()
    dateabonnement = models.DateField()
    mois = models.IntegerField()
    nonregleavant = models.IntegerField()
    anneeabonnement = models.TextField()  # This field type is a guess.
    anneepaiement = models.TextField()  # This field type is a guess.
    # Field name made lowercase.
    consortiumid = models.IntegerField(db_column='ConsortiumID')
    complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'revenus'
        app_label = 'legacy'


class Revenus2008(models.Model):
    # Field name made lowercase.
    revenus2008id = models.AutoField(
        db_column='Revenus2008ID', primary_key=True)
    abonneid = models.IntegerField(blank=True, null=True)
    commandeid = models.IntegerField()
    revueid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'revenus2008'
        app_label = 'legacy'


class Revue(models.Model):
    # Field name made lowercase.
    revueid = models.AutoField(db_column='RevueID', primary_key=True)
    titrerev = models.CharField(max_length=150, blank=True, null=True)
    # Field name made lowercase.
    periodiciteid = models.IntegerField(
        db_column='PeriodiciteID', blank=True, null=True)
    # Field name made lowercase.
    nombrenoannuel = models.IntegerField(
        db_column='NombreNoAnnuel', blank=True, null=True)
    # Field name made lowercase.
    prix = models.DecimalField(
        db_column='Prix', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    debutanneerestricti = models.IntegerField(
        db_column='DebutAnneeRestricti', blank=True, null=True)
    # Field name made lowercase.
    finanneerestriction = models.IntegerField(
        db_column='FinAnneeRestriction', blank=True, null=True)
    titrerevabr = models.CharField(max_length=50, blank=True, null=True)
    gratuit = models.IntegerField(blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.
    # Field name made lowercase.
    exclure = models.IntegerField(db_column='Exclure')
    # Field name made lowercase.
    clerapport = models.CharField(db_column='cleRapport', max_length=45)
    # Field name made lowercase.
    prixsuivante = models.DecimalField(
        db_column='PrixSuivante', max_digits=19, decimal_places=4)
    # Field name made lowercase.
    retire = models.IntegerField(db_column='Retire')
    # Field name made lowercase.
    aparaitre = models.IntegerField(db_column='Aparaitre')
    motpasse = models.CharField(max_length=30)
    lettre = models.CharField(max_length=1)
    logo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'revue'
        app_label = 'legacy'

    def __str__(self):
        return '{} {}'.format(self.revueid, self.titrerev)


class Revueabonne(models.Model):
    # Field name made lowercase.
    revueabonneid = models.AutoField(
        db_column='RevueAbonneID', primary_key=True)
    # Field name made lowercase.
    revueid = models.ForeignKey(
        Revue, db_column='RevueID', blank=True, null=True)
    # Field name made lowercase.
    abonneid = models.ForeignKey(
        Abonne, db_column='AbonneID', blank=True, null=True)
    # Field name made lowercase. This field type is a guess.
    anneeabonnement = models.TextField(db_column='AnneeAbonnement')
    commandeid = models.IntegerField()
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.
    # Field name made lowercase.
    exclure = models.IntegerField(db_column='Exclure')
    # Field name made lowercase.
    prixitem = models.DecimalField(
        db_column='PrixItem', max_digits=19, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    reglecalcul = models.IntegerField(db_column='RegleCalcul')
    # Field name made lowercase.
    quantite = models.IntegerField(db_column='Quantite')

    class Meta:
        managed = False
        db_table = 'revueabonne'
        app_label = 'legacy'


class Revuefiltre(models.Model):
    # Field name made lowercase.
    revuefiltreid = models.AutoField(
        db_column='revuefiltreID', primary_key=True)
    nomabrege = models.CharField(max_length=20)
    volume = models.IntegerField(blank=True, null=True)
    nonumero = models.IntegerField()
    nonumerodouble = models.IntegerField(blank=True, null=True)
    annee = models.TextField()  # This field type is a guess.
    exceptionnonumerodouble = models.CharField(max_length=45)
    # Field name made lowercase.
    filtre = models.IntegerField(db_column='Filtre')
    revueid = models.IntegerField()
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'revuefiltre'
        app_label = 'legacy'


class Revueindividus(models.Model):
    # Field name made lowercase.
    abonneindividusid = models.ForeignKey(
        'Abonneindividus', db_column='abonneIndividusID')
    # Field name made lowercase.
    revueid = models.ForeignKey('Revue', db_column='revueID')

    class Meta:
        managed = False
        db_table = 'revueindividus'
        unique_together = (('abonneindividusid', 'revueid'),)
        app_label = 'legacy'


class Tauxchange(models.Model):
    tauxchangeid = models.AutoField(primary_key=True)
    taux = models.DecimalField(max_digits=19, decimal_places=8)
    devise = models.IntegerField()
    mois = models.IntegerField()
    annee = models.IntegerField()
    trimestre = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tauxchange'
        app_label = 'legacy'


class Tauxtaxe(models.Model):
    # Field name made lowercase.
    tauxtaxeid = models.AutoField(db_column='TauxTaxeID', primary_key=True)
    # Field name made lowercase.
    tps = models.DecimalField(db_column='TPS', max_digits=10, decimal_places=5)
    # Field name made lowercase.
    tvq = models.DecimalField(db_column='TVQ', max_digits=10, decimal_places=5)
    # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)

    class Meta:
        managed = False
        db_table = 'tauxtaxe'
        app_label = 'legacy'


class Tauxtaxeequisoft(models.Model):
    # Field name made lowercase.
    tauxtaxeidequisoft = models.AutoField(
        db_column='TauxTaxeIDEquisoft', primary_key=True)
    # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45)
    # Field name made lowercase.
    tauxtps = models.FloatField(db_column='TauxTPS')
    # Field name made lowercase.
    tauxtvq = models.FloatField(db_column='TauxTVQ')

    class Meta:
        managed = False
        db_table = 'tauxtaxeequisoft'
        app_label = 'legacy'


class Telephone(models.Model):
    # Field name made lowercase.
    telephoneid = models.AutoField(db_column='TelephoneID', primary_key=True)
    # Field name made lowercase.
    telephone = models.CharField(
        db_column='Telephone', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    typetelephoneid = models.IntegerField(
        db_column='TypeTelephoneID', blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telephone'
        app_label = 'legacy'


class Typeabonnement(models.Model):
    # Field name made lowercase.
    typeabonnementid = models.AutoField(
        db_column='TypeAbonnementID', primary_key=True)
    # Field name made lowercase.
    typeabonnement = models.CharField(
        db_column='TypeAbonnement', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    prix = models.DecimalField(
        db_column='Prix', max_digits=20, decimal_places=4, blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typeabonnement'
        app_label = 'legacy'


class Typeadresse(models.Model):
    # Field name made lowercase.
    typeadresseid = models.AutoField(
        db_column='TypeAdresseID', primary_key=True)
    # Field name made lowercase.
    typeadresse = models.CharField(
        db_column='TypeAdresse', max_length=50, blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typeadresse'
        app_label = 'legacy'


class Typecontact(models.Model):
    # Field name made lowercase.
    typecontactid = models.AutoField(
        db_column='TypeContactID', primary_key=True)
    # Field name made lowercase.
    typecontact = models.CharField(
        db_column='TypeContact', max_length=50, blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typecontact'
        app_label = 'legacy'


class Typetelephone(models.Model):
    # Field name made lowercase.
    typetelephoneid = models.AutoField(
        db_column='TypeTelephoneID', primary_key=True)
    # Field name made lowercase.
    typetelephone = models.CharField(
        db_column='TypeTelephone', max_length=50, blank=True, null=True)
    maj = models.DateTimeField(db_column='MAJ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typetelephone'
        app_label = 'legacy'


class Urlrapportrevenus(models.Model):
    # Field name made lowercase.
    urlrapportrevenusid = models.AutoField(
        db_column='urlrapportrevenusID', primary_key=True)
    revueid = models.IntegerField()
    clerapport = models.CharField(max_length=45)
    trimestre = models.CharField(max_length=4)
    devise = models.CharField(max_length=5)
    mimetype = models.CharField(max_length=5)
    annee = models.CharField(max_length=4)
    disponible = models.IntegerField()
    # Field name made lowercase.
    trimestretexte = models.CharField(
        db_column='trimestreTexte', max_length=45)

    class Meta:
        managed = False
        db_table = 'urlrapportrevenus'
        app_label = 'legacy'


class Valeurdefaut(models.Model):
    # Field name made lowercase.
    valeurdefautid = models.AutoField(
        db_column='ValeurDefautID', primary_key=True)
    # Field name made lowercase. This field type is a guess.
    anneeabonnement = models.TextField(db_column='AnneeAbonnement')
    # Field name made lowercase.
    tps = models.DecimalField(db_column='TPS', max_digits=6, decimal_places=1)
    # Field name made lowercase.
    tvq = models.DecimalField(db_column='TVQ', max_digits=6, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'valeurdefaut'
        app_label = 'legacy'
