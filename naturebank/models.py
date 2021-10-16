# -*- coding: utf-8 -*-
# UTF8 Encoded

from django.contrib.gis.db import models
from django.core.validators import validate_comma_separated_integer_list

#Forward declaration
class Image:
    pass

class Biotope(models.Model):
    # TODO : Add the ownership field and find the appropriate table to relate it.
    """Core Class-Model which corresponds to the biotopes entities of Greece.

     There are 5 different types of Biotopes according to their sitecode
    identifier. Beginning with "AT" are the "TIFK", "A0" are the CORINE
    biotopes, "AG" are other biotopes from CORINE project, "AB" corresponds
    to "Alloi Biotopoi" and "GR" to NATURA biotopes.
     Some information refers only to CORINE biotopes and they are blank for
    all the other biotope types.

    """
    # Core fields.
    site_code = models.CharField(max_length=54, unique=True,
        verbose_name="Κωδικός Τόπου",
        help_text=("Ο Κωδικός πρέπει να έχει πρόθεμα ένα εκ των \"ΑΤ\", "
                   "\"AΘ\", \"AG\", \"AB\" ή \"GR\"."))
    site_name = models.CharField(max_length=1440, blank=True,
        verbose_name="Όνομα (Αγγλικά)",
        help_text="Η ονομασία του βιότοπου (Αγγλικά)")
    site_name_gr = models.CharField(max_length=1440, blank=True,
        verbose_name="Όνομα (Ελληνικά)",
        help_text="Η ονομασία του βιότοπου (Ελληνικά)")

    # Category (Corine etc.)
    category = models.ForeignKey('BiotopeCategoryOption',null=True, blank=True,
        verbose_name="Κατηγορία Τόπου",
        help_text="Κατηγορία Τόπου")

    # Species relation through intermediate table.
    species = models.ManyToManyField('Species', through='SpeciesBiotope',
        verbose_name="Είδη Τόπου",
        help_text="Τα διάφορα είδη που απαντώνται στο τόπο.")

    # Designation relation through intermediate table.
    designation = models.ManyToManyField('DesignationOption',
        verbose_name="Ένταξη σε Θεσμικό Πλαίσιο",
        help_text="Οι κατηγορίες ένταξης σε θεσμικό πλαίσιο.")

    # Ownership relation through intermediate table.
    owner = models.ManyToManyField('OwnerOption',
        verbose_name="Ιδιοκτησία",
        help_text="Κατηγορίες ιδιοκτησίας.")

    # Sitetype relation through intermediate table.
    site_type = models.ManyToManyField('SiteTypeOption',
        verbose_name="Τύπος τοπίου",
        help_text="Τύποι τοπίων.")

    # Climate relation through intermediate table.
    climate = models.ManyToManyField('ClimateOption',
        verbose_name="Κλίμα",
        help_text="Τύποι κλίματος.")

    # Ecological value relation through intermediate table.
    ecological_value = models.ManyToManyField('EcologicalValueOption',
        verbose_name="Οικολογική",
        help_text="Τύποι οικολογικής αξίας.")

    # Social value relation through intermediate table.
    social_value = models.ManyToManyField('SocialValueOption',
        verbose_name="Κοινωνική, οικονομική και πολιτιστική",
        help_text="Τύποι κοινωνικοοικονομικής/πολιτιστικής αξίας.")

    # Cultural value relation through intermediate table.
    cultural_value = models.ManyToManyField('CulturalValueOption',
        verbose_name="Αισθητική",
        help_text="Τύποι αισθητικής αξίας")

    # Threat relation through intermediate table.
    threat = models.ManyToManyField('ThreatOption',
        verbose_name="Απειλές",
        help_text="Κατηγορίες απειλών")

    # Human activity m2m
    human_activity = models.ManyToManyField('HumanActivityOption',
        verbose_name="Ανθρώπινες δραστηρ.",
        help_text="Κατηγορίες ανθρωπίνων δραστηριοτήτων")

    # Habitation m2m
    habitation = models.ManyToManyField('HabitationOption',
        verbose_name="Χαρακτηρ. Ενδιαιτήματα",
        help_text="Κατηγορίες χαρακτηριστικών ενδιατημάτων")

    # Population trend field
    trend_pop = models.ForeignKey('TrendPopOption',null=True, blank=True,
        verbose_name="Τάση πληθυσμού",
        help_text="Τάση πληθυσμού")

    # Main Character (BIOTOPOS - FYSIKO TOPIO - DOMHMENO TOPIO)
    main_char_biotopos = models.BooleanField(default=False,
        verbose_name="Βιότοπος",
        help_text="Είναι Βιότοπος;")
    main_char_natural = models.BooleanField(default=False,
        verbose_name="Φυσικό Τοπίο",
        help_text="Είναι Φυσικό Τοπίο;")
    main_char_built = models.BooleanField(default=False,
        verbose_name="Δομημένο Τοπίο",
        help_text="Είναι Δομημένο Τοπίο;")

    # Geographical fields (BIOLOCATION).
    geo_code = models.ForeignKey('GeoCodeOption',null=True, blank=True,
        verbose_name="Γεωγραφική Ενότητα",
        help_text="Γεωγραφική Ενότητα")

    # Geographical Region Codes.
    reg_code_1 = models.CharField(max_length=24, blank=True,
        verbose_name="Γεωγραφικός κωδικός 1",
        help_text="Γεωγραφικός κωδικός 1")
    reg_code_2 = models.CharField(max_length=24, blank=True,
        verbose_name="Γεωγραφικός κωδικός 2",
        help_text="Γεωγραφικός κωδικός 2")
    reg_code_3 = models.CharField(max_length=24, blank=True,
        verbose_name="Γεωγραφικός κωδικός 3",
        help_text="Γεωγραφικός κωδικός 3")
    reg_code_4 = models.CharField(max_length=24, blank=True,
        verbose_name="Γεωγραφικός κωδικός 4",
        help_text="Γεωγραφικός κωδικός 4")

    # Wide Area Code.
    reg_wide = models.ForeignKey('WideArea', null=True, blank=True,
        verbose_name="Ευρύτερη Γεωγραφική Περιοχή",
        help_text="Ευρύτερη γεωγραφική περιοχή")

    # Date fields.
    creation_date = models.DateField(null=True, blank=True,
        verbose_name="Ημερομηνία πρώτης καταχώρησης",
        help_text="Ημερομηνία πρώτης καταχώρησης")
    update_date = models.DateField(null=True, blank=True,
        verbose_name="Ημερομηνία τελευταίας καταχώρησης",
        help_text="Ημερομηνία τελευταίας καταχώρησης")
    date_old = models.CharField(max_length=36, blank=True,
        verbose_name="Ημερομηνία δημιουργίας παλιάς καταχώρησης",
        help_text="Ημερομηνία δημιουργίας παλιάς καταχώρησης")
    update_old = models.CharField(max_length=36, blank=True,
        verbose_name="Ημερομηνία τελευταίας ανανέωσης στην παλιά βάση",
        help_text="Ημερομηνία τελευταίας ανανέωσης στην παλιά καταχώρηση")

    # Abandonment
    abandon = models.ForeignKey('AbandonmentOption', null=True, blank=True,
        verbose_name="Εγκατάλειψη οικισμών",
        help_text="Επίπεδα εγκατάλειψης οικισμών")

     # Composite Code.
    comp_code = models.CharField(max_length=54, blank=True,
        verbose_name="Κωδικός Σύνθετου Τόπου",
        help_text="Κωδικός σύνθετου τόπου")
    comp_name = models.CharField(max_length=1440, blank=True,
        verbose_name="Όνομα Σύνθετου Τόπου",
        help_text="Όνομα σύνθετου τόπου")

    # Region, Municipality names
    dist_name = models.CharField(max_length=1440, blank=True,
        verbose_name="Άλλη γεωγραφική ενότητα",
        help_text="Άλλη γεωγραφική ενότητα")
    reg_mun = models.CharField(max_length=480, blank=True,
        verbose_name="Δήμος - Κοινότητα",
        help_text="Δήμος - Κοινότητα")

    # Size of area.
    area = models.FloatField(null=True, blank=True,
        verbose_name="Συνολική έκταση",
        help_text="Συνολική έκταση βιοτόπου")
    area_l = models.FloatField(null=True, blank=True,
        verbose_name="Χερσαία έκταση",
        help_text="Χερσαία έκταση βιοτόπου")
    area_s = models.FloatField(null=True, blank=True,
        verbose_name="Θαλάσσια έκταση",
        help_text="Θαλάσσια έκταση βιοτόπου")

    # GeoCode Lon/Lat
    long_deg = models.FloatField(null=True, blank=True,
        verbose_name="Longitude (μοίρες)",
        help_text="Οι μοίρες (degrees) του longitude (λ)")
    long_min = models.FloatField(null=True, blank=True,
        verbose_name="Longitude (λεπτά)",
        help_text="Τα πρώτα λεπτά (minutes) του longitude (λ)")
    long_sec = models.FloatField(null=True, blank=True,
        verbose_name="Longitude (δεύτερα)",
        help_text="Τα δεύτερα λεπτά (seconds) του longitude (λ)")
    lat_deg = models.FloatField(null=True, blank=True,
        verbose_name="Latitude (μοίρες)",
        help_text="Οι μοίρες (degrees) του latitude.")
    lat_min = models.FloatField(null=True, blank=True,
        verbose_name="Latitude (λεπτά)",
        help_text="Τα πρώτα λεπτά (minutes) του latitude.")
    lat_sec = models.FloatField(null=True, blank=True,
        verbose_name="Latitude (δεύτερα)",
        help_text="Τα δεύτερα λεπτά (seconds) του latitude")

    # Altitude, Length, Width
    alt_mean = models.FloatField(null=True, blank=True,
        verbose_name="Μέσο υψόμετρο",
        help_text="Μέσο υψόμετρο (δεκαδικός αριθμός)")
    alt_max = models.FloatField(null=True, blank=True,
        verbose_name="Μέγιστο υψόμετρο",
        help_text="Μέγιστο υψόμετρο (δεκαδικός αριθμός)")
    alt_min = models.FloatField(null=True, blank=True,
        verbose_name="Ελάχιστο υψόμετρο",
        help_text="Ελάχιστο υψόμετρο (δεκαδικός αριθμός)")
    length_max = models.FloatField(null=True, blank=True,
        verbose_name="Μέγιστο μήκος",
        help_text="Μέγιστο μήκος (δεκαδικός αριθμός)")
    width_max = models.FloatField(null=True, blank=True,
        verbose_name="Μέγιστο πλάτος",
        help_text="Μέγιστο πλάτος (δεκαδικός αριθμός)")

    # Text
    respondent = models.TextField(blank=True,
        verbose_name="Στοιχεία Καταχωρητή",
        help_text="Αναλυτική περιγραφή των στοιχείων του καταχωρητή")
    document = models.TextField(blank=True,
                                verbose_name="Πηγές και Αναφορές",
                                help_text=("Πηγές, βιβλιογραφία και αναφορές "
                                           "από όπου αντλήθηκαν τα δεδομένα."))

    #### BIOSUPPL Fields ####

    # Condition (Foreign Key Relation)
    condition = models.ForeignKey('ConditionOption', null=True, blank=True,
        verbose_name="Κατάσταση τόπου",
        help_text="Κατάσταση τόπου")

    # Trend (Foreign Key Relation)
    trend = models.ForeignKey('TrendOption', null=True, blank=True,
        verbose_name="Τάση κατάστασης τόπου",
        help_text="Τάση κατάστασης τόπου")
    trend_text = models.TextField(blank=True,
        verbose_name="Περιγραφή τάσης τόπου",
        help_text=("Περιγραφή τάσης κατάστασης τόπου"))

    # Threats (Boolean)
    threat_hunt = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από το κυνήγι")
    threat_fish = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την αλιεία")
    threat_coll = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την συλλογή")
    threat_graz = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την βοσκή")
    threat_poll = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την ρύπανση")
    threat_cult = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την καλλιέργεια")
    threat_road = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την διάνοιξη δρόμων")
    threat_buil = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την δόμηση")
    threat_drai = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την αποξήρανση")
    threat_eutr = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από τον ευτροφισμός")
    threat_pest = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από τα φυτοφάρμακα")
    threat_tour = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από τον τουρισμό")
    threat_fore = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την υλοτομία")
    threat_mini = models.BooleanField(blank=True, default=False,
        help_text="Απειλή από την εξόρυξη")
    threat_other = models.BooleanField(blank=True, default=False,
        help_text="Άλλες απειλές/διαταραχές")
    threat_text = models.TextField(blank=True,
        verbose_name="Σχόλια",
        help_text=("Περιγραφή απειλών που αντιμετωπίζει ο τόπος"))

    # Knowledge (Foreign Key Relation)
    knowledge = models.ForeignKey('KnowledgeOption', blank=True, null=True,
        verbose_name="Γνώση",
        help_text="Γνώση για το βιότοπο")

    # Measures (Text)
    measures_take = models.TextField(blank=True,
        verbose_name="Ληφθέντα Μέτρα",
        help_text=("Περιγραφή μέτρων που λαμβάνονται στο βιότοπο"))
    measures_need = models.TextField(blank=True,
        verbose_name="Αναγκαία Μέτρα",
        help_text=("Περιγραφή μέτρων που απαιτούνται στο βιότοπο"))

    # Fire (Boolean)
    fire_50 = models.BooleanField(blank=True, default=False, help_text="")
    fire_3050 = models.BooleanField(blank=True,default=False,  help_text="")
    fire_1030 = models.BooleanField(blank=True,default=False,  help_text="")
    fire_10 = models.BooleanField(blank=True,default=False,  help_text="")
    fire_text = models.TextField(blank=True, help_text=("Καταγραφή στοιχείων "
        "σχετικά με πυρκαγιές"))

    # Restore (Text)
    restore = models.TextField(blank=True, help_text="")

    # Introduction (Short Text/ Text)
    introduct = models.CharField(max_length=24, blank=True,
        verbose_name="Μικρός Τίτλος",
        help_text="Μικρός τίτλος")
    intro_text = models.TextField(blank=True,
        verbose_name="Εισαγωγικό Κείμενο",
        help_text="Εισαγωγικό κείμενο")

    # Social Reaction
    social_reaction = models.ForeignKey('SocialReactionOption', null=True,
        blank=True, verbose_name="Κοινωνική αντίδραση",
        help_text="Επιλογές κοινωνικής αντίδρασης")
    social_reaction_text = models.TextField(blank=True,
        verbose_name="Περιγραφή κοινωνικής αντίδρασης",
        help_text=("Περιγραφή κοινωνικής αντίδρασης"))

    # Development (Text)
    develop = models.TextField(blank=True,
        verbose_name="Περιγραφή Εξέλιξης Τόπου",
        help_text="Περιγραφή εξέλιξης του τόπου")

    # Conservation (Foreign Key Relation)
    conservation = models.ForeignKey('ConservationOption', blank=True,
        verbose_name="Προτεραιότητα προστασίας",
        null=True, help_text="Επιλογές προτεραιότητας προστασίας")

    protection = models.TextField(blank=True,
        verbose_name="Κατάσταση Προστασίας",
        help_text="Περιγραφή της κατάστασης προστασίας του τόπου")

    ownership_text = models.TextField(blank=True,
        verbose_name="Περιγραφή Ιδιοκτησίας",
        help_text="Περιγραφή της κατάστασης ιδιοκτησίας του τόπου")

    geology = models.TextField(blank=True,
        verbose_name="Γεωλογία",
        help_text="Περιγραφή της γεωλογία του τόπου")

    characteristics = models.TextField(blank=True,
        verbose_name="Περιγραφή τόπου",
        help_text="Γενική περιγραφή του τόπου")

    history = models.TextField(blank=True,
        verbose_name="Ιστορία και Εξέλιξη",
        help_text="Περιγραφή της ιστορίας του τόπου")

    quality = models.TextField(blank=True,
        verbose_name="Σχόλια",
        help_text="Σχόλια σχετικά με τις αξίες του τόπου")

    vulnerability = models.TextField(blank=True,
        verbose_name="Τρωτότητα",
        help_text="Κείμενο σχετικά με τη τρωτότητα του τόπου")

    tourism = models.TextField(blank=True,
        verbose_name="Τουρισμός, αναψυχή",
        help_text="Κείμενο για τις δραστηριότητες τουρισμού και αναψυχής")

    infrastructure = models.TextField(blank=True,
        verbose_name="Υποδομή προστασίας, αξιοποίησης",
        help_text="Κείμενο σχετικά με την υποδομή προστασίας/αξιοποίησης")

    view = models.TextField(blank=True,
        verbose_name="Σημεία με καλή θέα",
        help_text="Κείμενο για τα σημεία με καλή θέα")

    path = models.TextField(blank=True,
        verbose_name="Μονοπάτια, περίπατοι",
        help_text="Κείμενο για τα μονοπάτια του τόπου")

    population = models.FloatField(null=True, blank=True,
        verbose_name="Πληθυσμός 1991",
        help_text="Ο πληθυσμός του τόπου το 1991")

    landvalue = models.FloatField(null=True, blank=True,
        verbose_name="Μέγιστη αξία γης",
        help_text=("Η μέγιστη αξία γης του τόπου (Οι παλιές εγγραφές είναι σε"
        " δρχ./στρέμμα)"))

    species_text = models.TextField(blank=True,
        verbose_name="Σχόλια για τα είδη",
        help_text="Σχόλια για τα είδη του τόπου")

#    @property
#    def photo_url(self):
#        return "site_media/images/foo/%s.png" % self.site_code or 'noimage'

#    Spatial fields
    gis_area = models.FloatField(null=True, blank=True, verbose_name="Επιφάνεια m²")
    gis_perimeter = models.FloatField(null=True, blank=True, verbose_name="Περίμετρος m")
    gis_sitecode = models.CharField(null=True, blank=True, max_length=9,
                                    verbose_name="Κωδικός από GIS (sitecode)")
    gis_zorder = models.IntegerField(null=True, blank=True,
                                    verbose_name="Σειρά στρώσης καθ΄ύψος")

    gis_mpoly = models.MultiPolygonField(null=True, blank=True, verbose_name="Γεωμετρία πολυγώνων")
    objects = models.GeoManager()

    def total_gis_area_ha(self):
        result = None
        if self.gis_area:
            result = '%5.2f'%(self.gis_area/10000)
        else:
            if self.area:
                result = '%5.2f'%self.area
        return result
    def gis_perimeter_km(self):
        result = None
        if self.gis_perimeter:
            result = '%3.1f'%(self.gis_perimeter/1000)
        return result
    def has_mpoly(self):
        result = False
        if self.category.id!=5:
            if self.gis_mpoly:
                result = True
        else:
            asite_code = self.site_code
            asite_code = asite_code.replace("AE", "A0")
            aobj = Biotope.objects.filter(site_code=asite_code)
            if aobj is not None and len(aobj)>0:
                if aobj[0].gis_mpoly:
                    result = True
        return result
    def hasphotos(self):
        return len(BiotopeImage.objects.all().filter(work__id=self.id))>0

    class Meta:
        verbose_name="Βιότοπος"
        verbose_name_plural="Βιότοποι"
        ordering = ["site_name_gr"]

    def __str__(self):
        if self.site_name_gr: return "%s" % self.site_name_gr
        else: return "%s | N/A" % (self.site_code,)

# The class bellow is used to import GIS data from shapefiles

class TempDelete(models.Model):
    gis_area = models.FloatField()
    gis_perimeter = models.FloatField()
    gis_sitecode = models.CharField(max_length=9)

    gis_mpoly = models.MultiPolygonField()
    gis_objects = models.GeoManager()

    class Meta:
            db_table = 'temp_delete'

#Biotope images

class BiotopeImage(models.Model):
    biotope = models.ForeignKey(Biotope,
                                verbose_name="Τόπος", help_text="Εξωτερική αναφορά σε τόπο")
    image = models.ImageField(upload_to='SitesPhotos/',
                                verbose_name="Εικόνα", help_text="Αρχείο εικόνας")
    descr = models.CharField(max_length=80,
                                verbose_name="Περιγραφή", help_text="Σύντομη περιγραφή φωτογραφίας",
                                blank=True)
    order = models.IntegerField(blank=True, null=True,
                                verbose_name="Σειρά", help_text="Σειρά εμφάνισης φωτογραφίας")
    remarks = models.TextField(blank=True,
                                verbose_name="Σχόλια", help_text="Σχόλια για την εικόνα")
    thumbnail = models.ImageField(upload_to="SitesPhotos/thumbs/", editable=False,
                                verbose_name="Εικόνα προεπισκόπισης", help_text="Δείγμα (thumbnail) εικόνας")
    def save(self):
        if True: #not self.thumbnail:
            from PIL import Image as ImageClass
            from io import StringIO
            from django.core.files.uploadedfile import SimpleUploadedFile
            import os
            THUMBNAIL_SIZE = (160, 160)
            aimage = ImageClass.open(self.image)
            if aimage.mode not in ('L', 'RGB'):
                aimage = aimage.convert('RGB')
            aimage.thumbnail(THUMBNAIL_SIZE, ImageClass.ANTIALIAS)
            temp_handle = StringIO()
            aimage.save(temp_handle, 'png')
            temp_handle.seek(0)
            suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                    temp_handle.read(), content_type='image/png')
            self.thumbnail.save(suf.name+'.png', suf, save=False)
#Comment the following line in the case of interactive run, e.g.
#when importing images
        super(BiotopeImage, self).save()
    class Admin:
        pass
    def __str__(self):
        return self.descr
    class Meta:
        unique_together = (("biotope", "image"),
                           ("biotope", "id"))

#### #### #### SECONDARY BIOTOPE-RELATED OPTION TABLES #### #### ####

class HabitationOption(models.Model):
    """List all the habitation options for a biotope"""

    abbreviation = models.CharField(max_length=30, blank=False, unique=True,
        help_text="Συντομογραφία των χαρακτηριστικών ενδιαιτημάτων")
    name = models.CharField(max_length=390, blank=True,
        help_text="Το όνομα του ενδιαιτήματος")

    class Meta:
        verbose_name="Κατηγορία ενδιαιτήματος"
        verbose_name_plural="Κατηγορίες ενδιαιτημάτων"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)

class TrendPopOption(models.Model):
    """Options for population trends of biotope"""

    # Core Fields
    name = models.CharField(max_length=300, blank=True,
        help_text="Όνομα τάσης πληθυσμού")

    class Meta:
        verbose_name="Κατηγορία τάσης πληθυσμού"
        verbose_name_plural="Κατηγορίες τάσης πληθυσμού"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.id,)

class HumanActivityOption(models.Model):
    """List all the human acivity options for a biotope"""

    abbreviation = models.CharField(max_length=30, blank=False, unique=True,
        help_text="Συντομογραφία της ανθρώπινης δραστηριότητας")
    name = models.CharField(max_length=390, blank=True,
        help_text="Το όνομα της ανθρώπινης δραστηριότητας")

    class Meta:
        verbose_name="Ανθρώπινης δραστηριότητας"
        verbose_name_plural="Ανθρώπινες δραστηριότητες"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)

class ThreatOption(models.Model):
    """List all the threat options for a biotope"""

    abbreviation = models.CharField(max_length=30, blank=False, unique=True,
        help_text="Συντομογραφία της απειλής")
    name = models.CharField(max_length=390, blank=True,
        help_text="Το όνομα της απειλής")

    class Meta:
        verbose_name="Κατηγορία απειλής"
        verbose_name_plural="Κατηγορίες απειλών"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)

class CulturalValueOption(models.Model):
    """List with all the options of cultural values"""

    abbreviation = models.CharField(max_length=30, blank=False, unique=True,
        help_text="Συντομογραφία της αισθητικής αξίας")
    name = models.CharField(max_length=390, blank=True,
        help_text="Το όνομα της αισθητικής αξίας")

    class Meta:
        verbose_name="Αισθητική αξία"
        verbose_name_plural="Αισθητικές αξίες"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)

class SocialValueOption(models.Model):
    """List with all the options of social/economical/cultural values"""

    abbreviation = models.CharField(max_length=30, blank=False, unique=True,
        help_text="Συντομογραφία της κοινωνικοοικονομικής/πολιτιστικής αξίας")
    name = models.CharField(max_length=390, blank=True,
        help_text="Το όνομα της κοινωνικοοικονομικής/πολιτιστικής αξίας")

    class Meta:
        verbose_name="Κοιν/πολιτιστική αξία"
        verbose_name_plural="Κοιν/πολιτιστικές αξίες"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)

class EcologicalValueOption(models.Model):
    """List with all the options of ecological values"""

    abbreviation = models.CharField(max_length=30, blank=False, unique=True,
        help_text="Συντομογραφία της οικολογικής αξίας")
    name = models.CharField(max_length=390, blank=True,
        help_text="Το όνομα της οικολογικής αξίας")

    class Meta:
        verbose_name="Οικολογική αξία"
        verbose_name_plural="Οικολογικές αξίες"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)

class ClimateOption(models.Model):
    """List with all the climate types"""

    abbreviation = models.CharField(max_length=30, blank=False, unique=True,
        help_text="Συντομογραφία του κλιματικού τύπου")
    name = models.CharField(max_length=390, blank=True,
        help_text="Το όνομα του τύπου κλίματος")

    class Meta:
        verbose_name="Τύπος κλίματος"
        verbose_name_plural="Τύποι κλίματος"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)

class SiteTypeOption(models.Model):
    """List with all the types of a biotope"""

    abbreviation = models.CharField(max_length=30, blank=False, unique=True,
        help_text="Συντομογραφία του τύπου τόπου")
    name = models.CharField(max_length=390, blank=True,
        help_text="Το όνομα του τύπου")

    class Meta:
        verbose_name="Τύπος τόπου"
        verbose_name_plural="Τύποι τόπων"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)

class OwnerOption(models.Model):
    """Values/options of the ownership of a biotope."""

    # Core Fields
    name = models.CharField(max_length=300, blank=True,
        help_text="Κατάσταση βιότοπου")

    class Meta:
        verbose_name="Κατηγορία ιδιοκτησίας τόπου"
        verbose_name_plural="Κατηγορίες ιδιοκτησίας τόπου"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.id,)

class DesignationOption(models.Model):
    """List with all the designation options for a given biotope"""

    abbreviation = models.CharField(max_length=30, blank=False, unique=True,
        help_text="Συντομογραφία του προσδιορισμού ένταξης σε θεσμικό πλαίσιο")
    name = models.CharField(max_length=390, blank=True,
        help_text="Το όνομα του τύπου ένταξης σε θεσμικό πλαίσιο")

    class Meta:
        verbose_name="Κατηγορία ένταξης"
        verbose_name_plural="Κατηγορίες ένταξης"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)


class BiotopeCategoryOption(models.Model):
    """Categories of Biotopes obtained by the program which provides the data"""

    name = models.CharField(max_length=255, blank=True,
        help_text="Το όνομα ή σύντομη περιγραφή της κατηγορίας")

    class Meta:
        verbose_name="Κατηγορία τόπου"
        verbose_name_plural="Κατηγορίες τοπίων"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.id,)


class GeoCodeOption(models.Model):
    """ A mapping of level 1,2,3 geocodes to the region names."""

    code = models.CharField(
        max_length=10,
        primary_key=True,
        validators=[validate_comma_separated_integer_list],
    )
    name = models.CharField(max_length=300, blank=True,
        help_text="Το όνομα της γεωγραφικής περιοχής")
    name_eng = models.CharField(max_length=300, blank=True,
        help_text="Το όνομα της γεωγραφικής περιοχής στα Αγγλικά")

    class Meta:
        verbose_name="Γεωγραφική ενότητα"
        verbose_name_plural="Γεωγραφικές ενότητες"
        ordering = ["name","name_eng"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.code,)


class ConditionOption(models.Model):
    """Options for biotope conditions

    Biosuppls depends on this table. This table enumerates the options for
    biotope conditions.

    """

    # Core Fields
    name = models.CharField(max_length=300, blank=True,
        help_text="Κατάσταση βιότοπου")

    class Meta:
        verbose_name="Κατάσταση βιότοπου"
        verbose_name_plural="Καταστάσεις βιότοπου"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.id,)


class TrendOption(models.Model):
    """Options for biotope trends

    Biosuppls depends on this table. This table enumerates the options for
    biotope trends on the biotope conditions. For example, how quick the biotope
    growth is increased/decreased.

    """

    # Core Fields
    name = models.CharField(max_length=300, blank=True,
        help_text="Τάση κατάστασης βιότοπου")

    class Meta:
        verbose_name="Τάση κατάστασης βιότοπου"
        verbose_name_plural="Τάσεις κατάστασης βιότοπου"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.id,)


class KnowledgeOption(models.Model):
    """Options for biotope knowledge levels

    Biosuppls depends on this table. This table enumerates the options for
    biotope knowledge levels.

    """

    # Core Fields
    name = models.CharField(max_length=300, blank=True,
        help_text="Κατάσταση γνώσης")

    class Meta:
        verbose_name="Κατάσταση γνώσης βιότοπου"
        verbose_name_plural="Καταστάσεις γνώσης βιότοπου"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.id,)


class SocialReactionOption(models.Model):
    """Options for social reaction about biotope

    Biosuppls depends on this table. This table enumerates the options for
    social reaction about biotope.

    """

    # Core Fields
    name = models.CharField(max_length=300, blank=True,
        help_text="Περιγραφή κοινωνικής αντίδρασης")

    class Meta:
        verbose_name="Κοινωνική αντίδραση"
        verbose_name_plural="Κοινωνικές αντιδράσεις"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.id,)


class ConservationOption(models.Model):
    """Options for conservation levels given as priorities high - low"""

    # Core Fields
    name = models.CharField(max_length=300, blank=True,
        help_text="Περιγραφή προτεραιότητας προστασίας")

    class Meta:
        verbose_name="Προτεραιότητα προστασίας"
        verbose_name_plural="Προτεραιότητες προστασίας"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.id,)


class WideArea(models.Model):
    """Stores the wide areas' codes and names

    This table contains the codes and strings of geographical regions of Greece
    such as "Sterea Ellada".

    """

    # Core Fields
    wide_area_name = models.CharField(max_length=150, blank=True,
        help_text="Όνομα ευρύτερης γεωγραφικής περιοχής.")

    class Meta:
        verbose_name = "Ευρύτερη γεωγραφική περιοχή"
        verbose_name_plural = "Ευρύτερες γεωγραφικές περιοχές"
        ordering = ["wide_area_name"]

    def __str__(self):
        if self.wide_area_name: return "%s" % self.wide_area_name
        else: return "%s | N/A" % (self.id,)


class AbandonmentOption(models.Model):
    """Stores the code values for the abandonment levels.

    Biotopes depends on this table.

    """

    # Core Fields
    name = models.CharField(max_length=300, blank=True,
        help_text="Τίτλος επιπέδου εγκατάλειψης.")

    class Meta:
        verbose_name="Επίπεδο εγκατάλειψης"
        verbose_name_plural="Επίπεδα εγκατάλειψης"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.id,)


class Species(models.Model):
    #FIXME: Find the foreign key relations. Every attribute with combobox should
    #       have a related table.
    """Store species.

    Species, are animals or plants uniquely defined by their species_code.
    Many to many relation with Biotope through the SpeciesBiotope model.

    """

    # Core fields
    species_code = models.IntegerField(null=False, unique=True,
        verbose_name="Κωδικός Είδους",
        help_text="Κωδικός είδους")
    species_name = models.CharField(max_length=720, blank=True,
        verbose_name="Όνομα Είδους (Αγγλικά)",
        help_text="Αγγλική ονομασία είδους")
    sub_species = models.CharField(max_length=720, blank=True,
        verbose_name="Όνομα Υποείδους (Αγγλικά)",
        help_text="Αγγλική ονομασία υποείδους")
    species_category = models.ForeignKey('SpeciesCategoryOption', null=True,
        verbose_name="Κατηγορία Είδους",
        blank=True, help_text="Κατηγορία χλωρίδας/πανίδας που ανήκει το είδος.")
    other_names = models.CharField(max_length=960, blank=True,
        verbose_name="Άλλες Ονομασίες",
        help_text="Άλλες ονομασίες του ίδιου είδους")
    species_name_gr = models.CharField(max_length=720, blank=True,
        verbose_name="Όνομα Είδους (Ελληνικά)",
        help_text="Ελληνική ονομασία είδους")
    plant_kind = models.ForeignKey('SpeciesPlantKindOption', null=True,
        verbose_name="Κατηγορία Φυτού",blank=True,
        help_text=("Υποκατηγορία για φυτό (Αν δεν είναι φυτό πρέπει"
        " να αφεθεί κενό)"))
    knowledge = models.ForeignKey('SpeciesKnowledgeOption', null=True,
        blank=True, verbose_name="Γνώση",
        help_text="Το επίπεδο γνώσης στο συγκεκριμένο είδος")
    habitat = models.CharField(max_length=720, blank=True,
        verbose_name="Ενδιαιτήματα",
        help_text="Στοιχεία σχετικά με τα ενδιαιτήματα")
    expansion = models.CharField(max_length=960, blank=True,
        verbose_name="Εξάπλωση",
        help_text="Στοιχεία εξάπλωσης του είδους")
    origin = models.CharField(max_length=18, blank=True,
        verbose_name="Προέλευση",
        help_text="Στοιχεία προέλευσης του είδους")

    # Date fields.and Respondent
    creation_date = models.DateField(null=True, blank=True,
        verbose_name="Ημ/νία Πρώτης Καταχώρησης",
        help_text="Ημερομηνία πρώτης καταχώρησης")
    update_date = models.DateField(null=True, blank=True,
        verbose_name="Ημ/νία Τελευταίας Καταχώρησης",
        help_text="Ημερομηνία τελευταίας καταχώρησης")
    respondent = models.TextField(blank=True,
        verbose_name="Στοιχεία Καταχωρητή",
        help_text="Στοιχεία καταχωρητή")

    # Protection and Growth
    protection = models.ForeignKey('SpeciesProtectionOption', null=True,
        verbose_name="Προστασία",
        blank=True, help_text="Επίπεδο προστασίας του είδους")
    conservation_prio = models.ForeignKey('SpeciesConservationPriorityOption',
        verbose_name="Προτεραιότητα Προστασίας",
        null=True, blank=True, help_text="Προτεραιότητα προστασίας")
    trend = models.ForeignKey('SpeciesTrendOption', null=True,
        verbose_name="Τάση",
        blank=True, help_text="Ο ρυθμός ανάπτυξης του είδους")
    measures_take = models.TextField(blank=True,
        verbose_name="Ληφθέντα Μέτρα",
        help_text="Μέτρα προστασίας που έχουν ληφθεί.")
    measures_need = models.TextField(blank=True,
        verbose_name="Αναγκαία Μέτρα",
        help_text="Μέτρα προστασίας που είναι αναγκαία.")

    # Conservation
    conservation_gr = models.ForeignKey('SpeciesConservationOption', null=True,
        verbose_name="Ελλάδα",
        related_name="species_conservation_gr_set", blank=True,
        help_text="Κατάσταση διατήρησης του είδους στην Ελλάδα")
    conservation_eec = models.ForeignKey('SpeciesConservationOption', null=True,
        verbose_name="Ευρωπαϊκή Ένωση",
        related_name="species_conservation_eec_set", blank=True,
        help_text="Κατάσταση διατήρησης του είδους στην Ευρωπαική Ένωση")
    conservation_bio = models.ForeignKey('SpeciesConservationOption', null=True,
        verbose_name="Βιόσφαιρα",
        related_name="species_conservation_bio_set", blank=True,
        help_text="Κατάσταση διατήρησης του είδους στην Βιόσφαιρα")

    # Rarity
    rarity_gr = models.ForeignKey('SpeciesRarityOption', null=True,
        verbose_name="Ελλάδα",
        related_name="species_rarity_gr_set", blank=True,
        help_text="Σπανιότητα του είδους στην Ελλάδα")
    rarity_eec = models.ForeignKey('SpeciesRarityOption', null=True,
        verbose_name="Ευρωπαϊκή Ένωση",
        related_name="species_rarity_eec_set", blank=True,
        help_text="Σπανιότητα του είδους στην Ευρωπαική Ένωση")
    rarity_bio = models.ForeignKey('SpeciesRarityOption', null=True,
        verbose_name="Βιόσφαιρα",
        related_name="species_rarity_bio_set", blank=True,
        help_text="Σπανιότητα του είδους στην Βιόσφαιρα")

    # Threats (Boolean)
    threat_hunt = models.BooleanField(blank=True, default=False,
        verbose_name="Κυνήγι",
        help_text="Απειλή από το κυνήγι")
    threat_fish = models.BooleanField(blank=True, default=False,
        verbose_name="Αλιεία",
        help_text="Απειλή από την αλιεία")
    threat_coll = models.BooleanField(blank=True, default=False,
        verbose_name="Συλλογή",
        help_text="Απειλή από την συλλογή")
    threat_fore = models.BooleanField(blank=True, default=False,
        verbose_name="Υλοτομία",
        help_text="Απειλή από την υλοτομία")
    threat_graz = models.BooleanField(blank=True, default=False,
        verbose_name="Βοσκή",
        help_text="Απειλή από την βοσκή")
    threat_poll = models.BooleanField(blank=True, default=False,
        verbose_name="Ρύπανση",
        help_text="Απειλή από την ρύπανση")
    threat_cult = models.BooleanField(blank=True, default=False,
        verbose_name="Καλλιέργεια",
        help_text="Απειλή από την καλλιέργεια")
    threat_tour = models.BooleanField(blank=True, default=False,
        verbose_name="Τουρισμός",
        help_text="Απειλή από τον τουρισμό")
    threat_road = models.BooleanField(blank=True, default=False,
        verbose_name="Διάνοιξη Δρόμων",
        help_text="Απειλή από την διάνοιξη δρόμων")
    threat_buil = models.BooleanField(blank=True, default=False,
        verbose_name="Δόμηση",
        help_text="Απειλή από την δόμηση")
    threat_drai = models.BooleanField(blank=True, default=False,
        verbose_name="Αποξήρανση",
        help_text="Απειλή από την αποξήρανση")
    threat_eutr = models.BooleanField(blank=True, default=False,
        verbose_name="Ευτροφισμός",
        help_text="Απειλή από τον ευτροφισμό")
    threat_pest = models.BooleanField(blank=True, default=False,
        verbose_name="Φυτοφάρμακα",
        help_text="Απειλή από τα φυτοφάρμακα")
    threat_other = models.BooleanField(blank=True, default=False,
        verbose_name="Άλλες Απειλές",
        help_text="Άλλες απειλές")
    threat = models.TextField(blank=True,
        verbose_name="Σχόλια",
        help_text="Περιγραφή απειλών και κινδύνων")

    # Attributes (Boolean)
    category_ende = models.BooleanField(blank=True, default=False,
        verbose_name="Ενδημικό",
        help_text="Είναι ενδημικό")
    category_migr = models.BooleanField(blank=True, default=False,
        verbose_name="Μεταναστευτικό",
        help_text="Είναι μεταναστευτικό")
    category_bree = models.BooleanField(blank=True, default=False,
        verbose_name="Αναπαραγόμενο",
        help_text="Είναι αναπαραγόμενο")
    category_resi = models.BooleanField(blank=True, default=False,
        verbose_name="Μόνιμος Κάτοικος",
        help_text="Κατοικεί μόνιμα")
    category_intr = models.BooleanField(blank=True, default=False,
        verbose_name="Εισαχθέν",
        help_text="Είναι εισαχθέν")
    category = models.TextField(blank=True,
        verbose_name="Σχόλια",
        help_text="Σχόλια για τα γνωρίσματα")

    # Exploitation (Boolean)
    exploit_hunt = models.BooleanField(blank=True, default=False,
        verbose_name="Κυνήγι",
        help_text="Εκμετάλλευση από το κυνήγι")
    exploit_fish = models.BooleanField(blank=True, default=False,
        verbose_name="Αλιεία",
        help_text="Εκμετάλλευση από το αλιεία")
    exploit_coll = models.BooleanField(blank=True, default=False,
        verbose_name="Συλλογή",
        help_text="Εκμετάλλευση από τη σύλλογη")
    exploit_logg = models.BooleanField(blank=True, default=False,
        verbose_name="Υλοτομία",
        help_text="Εκμετάλλευση από την υλοτομία")
    exploit_graz = models.BooleanField(blank=True, default=False,
        verbose_name="Βοσκή",
        help_text="Εκμετάλλευση από τη βοσκή")

    # Photo Field
    photo = models.ImageField(upload_to="SitesPhotos", blank=True,
        verbose_name="Φωτογραφία",
        help_text="Το path προς τη φωτογραφία του τόπου")

    class Meta:
        verbose_name_plural="Species"
        ordering = ["species_name", "sub_species", "species_code"]

    def __str__(self):
        #to_return = unicode(self.species_code)
        to_return = ""
        if self.species_name:
            to_return += "%s" % self.species_name
        else:
            to_return += "N/A"
        if self.sub_species:
            to_return += " | %s" % self.sub_species
        else:
            to_return += " | N/A"
        return to_return


class SpeciesBiotope(models.Model):
    """Intermediate table between Biotopes and Species

    Denotes the Many to many relation between them.
    Contains two foreign keys for the two fields.
    In admin this should be taken into account.

    """

    # Core fields
    species = models.ForeignKey('Species',
        verbose_name="Είδος",
        help_text="Είδος Ζώου/Φυτού")
    biotope = models.ForeignKey('Biotope',
        verbose_name="Τόπος",
        help_text="Βιότοπος")
    abundance = models.IntegerField(null=True, blank=True,
        verbose_name="Πληθυσμός",
        help_text="Η αφθονία του είδους στο συγκεκριμένο βιότοπο")

    class Meta:
        verbose_name="Συσχέτιση Είδους με Βιότοπο"
        verbose_name_plural="Συσχετίσεις Είδους με Βιότοπο"
        unique_together = (('biotope', 'species'),)

    def __str__(self):
        to_return = ""
        if self.species:
            to_return += " %s" % (str(self.species),)
        else:
            to_return += " N/A"
        if self.biotope:
            to_return += " -- %s" % (str(self.biotope),)
        else:
            to_return += " -- N/A"
        return to_return

#### #### #### SECONDARY SPECIES-RELATED TABLES #### #### ####


class SpeciesCategoryOption(models.Model):
    """Lists the options on species categories. """

    # Core fields
    abbreviation = models.CharField(max_length=24, unique=True,
        help_text="Τα αρχικά της συγκεκριμένης κατηγορίας στα Αγγλικά")
    name = models.CharField(max_length=300, blank=True,
        help_text="Η ονομασία του είδους")

    class Meta:
        verbose_name="Κατηγορία πανίδας/χλωρίδας"
        verbose_name_plural="Κατηγορίες πανίδας/χλωρίδας"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)


class SpeciesPlantKindOption(models.Model):
    """Lists the options on plant kinds. """

    # Core fields
    abbreviation = models.CharField(max_length=24, unique=True,
        help_text="Τα αρχικά της συγκεκριμένης υποκατηγορίας στα Αγγλικά")
    name = models.CharField(max_length=300, blank=True,
        help_text="Η ονομασία αυτής της κατηγορίας φυτών")

    class Meta:
        verbose_name="Κατηγορία φυτών"
        verbose_name_plural="Κατηγορίες φυτών"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)


class SpeciesKnowledgeOption(models.Model):
    """Lists the options on knowledge levels """

    # Core fields
    abbreviation = models.CharField(max_length=24, unique=True,
        help_text="Τα αρχικά του συγκεκριμένου επιπέδου στα Αγγλικά")
    name = models.CharField(max_length=300, blank=True,
        help_text="Ο τίτλος του επιπέδου γνώσης στα Ελληνικά")

    class Meta:
        verbose_name="Επίπεδο γνώσης είδους"
        verbose_name_plural="Επίπεδα γνώσης είδους"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)


class SpeciesProtectionOption(models.Model):
    """Lists the options on protection levels """

    # Core fields
    abbreviation = models.CharField(max_length=24, unique=True,
        help_text="Τα αρχικά του επιπέδου προστασίας στα Αγγλικά")
    name = models.CharField(max_length=300, blank=True,
        help_text="Ο τίτλος του επιπέδου προστασίας στα Ελληνικά")

    class Meta:
        verbose_name="Επίπεδο προστασίας είδους"
        verbose_name_plural="Επίπεδα προστασίας είδους"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)


class SpeciesConservationPriorityOption(models.Model):
    """Lists the options on conservation priority """

    # Core fields
    abbreviation = models.CharField(max_length=24, unique=True,
        help_text="Τα αρχικά του επιπέδου προτεραιότητας προστασίας στα Αγγλικά")
    name = models.CharField(max_length=300, blank=True,
        help_text="Ο τίτλος του επιπέδου προτεραιότητας προστασίας στα Ελληνικά")

    class Meta:
        verbose_name="Προτεραιότητα προστασίας είδους"
        verbose_name_plural="Προτεραιότητες προστασίας είδους"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)


class SpeciesTrendOption(models.Model):
    """Lists the options on trend levels (growth rate) """

    # Core fields
    abbreviation = models.CharField(max_length=24, unique=True,
        help_text="Τα αρχικά του ρυθμού ανάπτυξης του είδους στα Αγγλικά")
    name = models.CharField(max_length=300, blank=True,
        help_text="Ο τίτλος του ρυθμού/τάσης ανάπτυξης του είδους στα Ελληνικά")

    class Meta:
        verbose_name="Ρυθμός ανάπτυξης είδους"
        verbose_name_plural="Ρυθμοί ανάπτυξης είδους"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" %  self.name
        else: return "%s | N/A" % (self.abbreviation,)


class SpeciesConservationOption(models.Model):
    """Lists the options on conservation levels """

    # Core fields
    abbreviation = models.CharField(max_length=24, unique=True,
        help_text="Τα αρχικά του επιπέδου διατήρησης του είδους στα Αγγλικά")
    name = models.CharField(max_length=300, blank=True,
        help_text="Ο τίτλος του επιπέδου διατήρησης του είδους στα Ελληνικά")

    class Meta:
        verbose_name="Επίπεδο διατήρησης είδους"
        verbose_name_plural="Επίπεδα διατήρησης είδους"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)


class SpeciesRarityOption(models.Model):
    """Lists the options on rarity levels """

    # Core fields
    abbreviation = models.CharField(max_length=24, unique=True,
        help_text="Τα αρχικά του βαθμού σπανιότητας του είδους στα Αγγλικά")
    name = models.CharField(max_length=300, blank=True,
        help_text="Ο τίτλος του βαθμού σπανιότητας του είδους στα Ελληνικά")

    class Meta:
        verbose_name="Βαθμός σπανιότητας είδους"
        verbose_name_plural="Βαθμοί σπανιότητας είδους"
        ordering = ["name"]

    def __str__(self):
        if self.name: return "%s" % self.name
        else: return "%s | N/A" % (self.abbreviation,)

class Settlement(models.Model):
    """Settlements list """
    name = models.CharField(max_length=50, blank=True,
        help_text="Ονομασία οικισμού")
    point = models.PointField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True, verbose_name="Επιφάνεια m²")
    perimeter = models.FloatField(null=True, blank=True, verbose_name="Περίμετρος m")
    objects = models.GeoManager()

    class Meta:
        verbose_name="Οικισμός"
        verbose_name_plural="Οικισμοί"

    def __str__(self):
        return self.name
