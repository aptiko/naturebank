from __future__ import unicode_literals

import re

import django.contrib.gis.db.models.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("naturebank", "0003_comma_separated_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="abandonmentoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Τίτλος επιπέδου εγκατάλειψης.", max_length=300
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="abandon",
            field=models.ForeignKey(
                blank=True,
                help_text="Επίπεδα εγκατάλειψης οικισμών",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.AbandonmentOption",
                verbose_name="Εγκατάλειψη οικισμών",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="alt_max",
            field=models.FloatField(
                blank=True,
                help_text="Μέγιστο υψόμετρο (δεκαδικός αριθμός)",
                null=True,
                verbose_name="Μέγιστο υψόμετρο",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="alt_mean",
            field=models.FloatField(
                blank=True,
                help_text="Μέσο υψόμετρο (δεκαδικός αριθμός)",
                null=True,
                verbose_name="Μέσο υψόμετρο",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="alt_min",
            field=models.FloatField(
                blank=True,
                help_text="Ελάχιστο υψόμετρο (δεκαδικός αριθμός)",
                null=True,
                verbose_name="Ελάχιστο υψόμετρο",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="area",
            field=models.FloatField(
                blank=True,
                help_text="Συνολική έκταση βιοτόπου",
                null=True,
                verbose_name="Συνολική έκταση",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="area_l",
            field=models.FloatField(
                blank=True,
                help_text="Χερσαία έκταση βιοτόπου",
                null=True,
                verbose_name="Χερσαία έκταση",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="area_s",
            field=models.FloatField(
                blank=True,
                help_text="Θαλάσσια έκταση βιοτόπου",
                null=True,
                verbose_name="Θαλάσσια έκταση",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="category",
            field=models.ForeignKey(
                blank=True,
                help_text="Κατηγορία Τόπου",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.BiotopeCategoryOption",
                verbose_name="Κατηγορία Τόπου",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="characteristics",
            field=models.TextField(
                blank=True,
                help_text="Γενική περιγραφή του τόπου",
                verbose_name="Περιγραφή τόπου",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="comp_code",
            field=models.CharField(
                blank=True,
                help_text="Κωδικός σύνθετου τόπου",
                max_length=54,
                verbose_name="Κωδικός Σύνθετου Τόπου",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="comp_name",
            field=models.CharField(
                blank=True,
                help_text="Όνομα σύνθετου τόπου",
                max_length=1440,
                verbose_name="Όνομα Σύνθετου Τόπου",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="condition",
            field=models.ForeignKey(
                blank=True,
                help_text="Κατάσταση τόπου",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.ConditionOption",
                verbose_name="Κατάσταση τόπου",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="conservation",
            field=models.ForeignKey(
                blank=True,
                help_text="Επιλογές προτεραιότητας προστασίας",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.ConservationOption",
                verbose_name="Προτεραιότητα προστασίας",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="creation_date",
            field=models.DateField(
                blank=True,
                help_text="Ημερομηνία πρώτης καταχώρησης",
                null=True,
                verbose_name="Ημερομηνία πρώτης καταχώρησης",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="date_old",
            field=models.CharField(
                blank=True,
                help_text="Ημερομηνία δημιουργίας παλιάς καταχώρησης",
                max_length=36,
                verbose_name="Ημερομηνία δημιουργίας παλιάς καταχώρησης",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="develop",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή εξέλιξης του τόπου",
                verbose_name="Περιγραφή Εξέλιξης Τόπου",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="dist_name",
            field=models.CharField(
                blank=True,
                help_text="Άλλη γεωγραφική ενότητα",
                max_length=1440,
                verbose_name="Άλλη γεωγραφική ενότητα",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="document",
            field=models.TextField(
                blank=True,
                help_text="Πηγές, βιβλιογραφία και αναφορές από όπου αντλήθηκαν τα δεδομένα.",
                verbose_name="Πηγές και Αναφορές",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="fire_10",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="fire_1030",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="fire_3050",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="fire_50",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="fire_text",
            field=models.TextField(
                blank=True, help_text="Καταγραφή στοιχείων σχετικά με πυρκαγιές"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="geo_code",
            field=models.ForeignKey(
                blank=True,
                help_text="Γεωγραφική Ενότητα",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.GeoCodeOption",
                verbose_name="Γεωγραφική Ενότητα",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="geology",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή της γεωλογία του τόπου",
                verbose_name="Γεωλογία",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="gis_area",
            field=models.FloatField(blank=True, null=True, verbose_name="Επιφάνεια m²"),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="gis_mpoly",
            field=django.contrib.gis.db.models.fields.MultiPolygonField(
                blank=True, null=True, srid=4326, verbose_name="Γεωμετρία πολυγώνων"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="gis_perimeter",
            field=models.FloatField(blank=True, null=True, verbose_name="Περίμετρος m"),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="gis_sitecode",
            field=models.CharField(
                blank=True,
                max_length=9,
                null=True,
                verbose_name="Κωδικός από GIS (sitecode)",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="gis_zorder",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Σειρά στρώσης καθ΄ύψος"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="history",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή της ιστορίας του τόπου",
                verbose_name="Ιστορία και Εξέλιξη",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="infrastructure",
            field=models.TextField(
                blank=True,
                help_text="Κείμενο σχετικά με την υποδομή προστασίας/αξιοποίησης",
                verbose_name="Υποδομή προστασίας, αξιοποίησης",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="intro_text",
            field=models.TextField(
                blank=True,
                help_text="Εισαγωγικό κείμενο",
                verbose_name="Εισαγωγικό Κείμενο",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="introduct",
            field=models.CharField(
                blank=True,
                help_text="Μικρός τίτλος",
                max_length=24,
                verbose_name="Μικρός Τίτλος",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="knowledge",
            field=models.ForeignKey(
                blank=True,
                help_text="Γνώση για το βιότοπο",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.KnowledgeOption",
                verbose_name="Γνώση",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="landvalue",
            field=models.FloatField(
                blank=True,
                help_text="Η μέγιστη αξία γης του τόπου (Οι παλιές εγγραφές είναι σε δρχ./στρέμμα)",
                null=True,
                verbose_name="Μέγιστη αξία γης",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="lat_deg",
            field=models.FloatField(
                blank=True,
                help_text="Οι μοίρες (degrees) του latitude.",
                null=True,
                verbose_name="Latitude (μοίρες)",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="lat_min",
            field=models.FloatField(
                blank=True,
                help_text="Τα πρώτα λεπτά (minutes) του latitude.",
                null=True,
                verbose_name="Latitude (λεπτά)",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="lat_sec",
            field=models.FloatField(
                blank=True,
                help_text="Τα δεύτερα λεπτά (seconds) του latitude",
                null=True,
                verbose_name="Latitude (δεύτερα)",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="length_max",
            field=models.FloatField(
                blank=True,
                help_text="Μέγιστο μήκος (δεκαδικός αριθμός)",
                null=True,
                verbose_name="Μέγιστο μήκος",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="long_deg",
            field=models.FloatField(
                blank=True,
                help_text="Οι μοίρες (degrees) του longitude (λ)",
                null=True,
                verbose_name="Longitude (μοίρες)",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="long_min",
            field=models.FloatField(
                blank=True,
                help_text="Τα πρώτα λεπτά (minutes) του longitude (λ)",
                null=True,
                verbose_name="Longitude (λεπτά)",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="long_sec",
            field=models.FloatField(
                blank=True,
                help_text="Τα δεύτερα λεπτά (seconds) του longitude (λ)",
                null=True,
                verbose_name="Longitude (δεύτερα)",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="main_char_biotopos",
            field=models.BooleanField(
                default=False, help_text="Είναι Βιότοπος;", verbose_name="Βιότοπος"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="main_char_built",
            field=models.BooleanField(
                default=False,
                help_text="Είναι Δομημένο Τοπίο;",
                verbose_name="Δομημένο Τοπίο",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="main_char_natural",
            field=models.BooleanField(
                default=False,
                help_text="Είναι Φυσικό Τοπίο;",
                verbose_name="Φυσικό Τοπίο",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="measures_need",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή μέτρων που απαιτούνται στο βιότοπο",
                verbose_name="Αναγκαία Μέτρα",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="measures_take",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή μέτρων που λαμβάνονται στο βιότοπο",
                verbose_name="Ληφθέντα Μέτρα",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="ownership_text",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή της κατάστασης ιδιοκτησίας του τόπου",
                verbose_name="Περιγραφή Ιδιοκτησίας",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="path",
            field=models.TextField(
                blank=True,
                help_text="Κείμενο για τα μονοπάτια του τόπου",
                verbose_name="Μονοπάτια, περίπατοι",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="population",
            field=models.FloatField(
                blank=True,
                help_text="Ο πληθυσμός του τόπου το 1991",
                null=True,
                verbose_name="Πληθυσμός 1991",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="protection",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή της κατάστασης προστασίας του τόπου",
                verbose_name="Κατάσταση Προστασίας",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="quality",
            field=models.TextField(
                blank=True,
                help_text="Σχόλια σχετικά με τις αξίες του τόπου",
                verbose_name="Σχόλια",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="reg_code_1",
            field=models.CharField(
                blank=True,
                help_text="Γεωγραφικός κωδικός 1",
                max_length=24,
                verbose_name="Γεωγραφικός κωδικός 1",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="reg_code_2",
            field=models.CharField(
                blank=True,
                help_text="Γεωγραφικός κωδικός 2",
                max_length=24,
                verbose_name="Γεωγραφικός κωδικός 2",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="reg_code_3",
            field=models.CharField(
                blank=True,
                help_text="Γεωγραφικός κωδικός 3",
                max_length=24,
                verbose_name="Γεωγραφικός κωδικός 3",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="reg_code_4",
            field=models.CharField(
                blank=True,
                help_text="Γεωγραφικός κωδικός 4",
                max_length=24,
                verbose_name="Γεωγραφικός κωδικός 4",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="reg_mun",
            field=models.CharField(
                blank=True,
                help_text="Δήμος - Κοινότητα",
                max_length=480,
                verbose_name="Δήμος - Κοινότητα",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="reg_wide",
            field=models.ForeignKey(
                blank=True,
                help_text="Ευρύτερη γεωγραφική περιοχή",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.WideArea",
                verbose_name="Ευρύτερη Γεωγραφική Περιοχή",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="respondent",
            field=models.TextField(
                blank=True,
                help_text="Αναλυτική περιγραφή των στοιχείων του καταχωρητή",
                verbose_name="Στοιχεία Καταχωρητή",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="restore",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="site_code",
            field=models.CharField(
                help_text='Ο Κωδικός πρέπει να έχει πρόθεμα ένα εκ των "ΑΤ", "AΘ", "AG", "AB" ή "GR".',
                max_length=54,
                unique=True,
                verbose_name="Κωδικός Τόπου",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="site_name",
            field=models.CharField(
                blank=True,
                help_text="Η ονομασία του βιότοπου (Αγγλικά)",
                max_length=1440,
                verbose_name="Όνομα (Αγγλικά)",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="site_name_gr",
            field=models.CharField(
                blank=True,
                help_text="Η ονομασία του βιότοπου (Ελληνικά)",
                max_length=1440,
                verbose_name="Όνομα (Ελληνικά)",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="social_reaction",
            field=models.ForeignKey(
                blank=True,
                help_text="Επιλογές κοινωνικής αντίδρασης",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.SocialReactionOption",
                verbose_name="Κοινωνική αντίδραση",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="social_reaction_text",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή κοινωνικής αντίδρασης",
                verbose_name="Περιγραφή κοινωνικής αντίδρασης",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="species_text",
            field=models.TextField(
                blank=True,
                help_text="Σχόλια για τα είδη του τόπου",
                verbose_name="Σχόλια για τα είδη",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_buil",
            field=models.BooleanField(default=False, help_text="Απειλή από την δόμηση"),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_coll",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την συλλογή"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_cult",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την καλλιέργεια"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_drai",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την αποξήρανση"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_eutr",
            field=models.BooleanField(
                default=False, help_text="Απειλή από τον ευτροφισμός"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_fish",
            field=models.BooleanField(default=False, help_text="Απειλή από την αλιεία"),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_fore",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την υλοτομία"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_graz",
            field=models.BooleanField(default=False, help_text="Απειλή από την βοσκή"),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_hunt",
            field=models.BooleanField(default=False, help_text="Απειλή από το κυνήγι"),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_mini",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την εξόρυξη"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_other",
            field=models.BooleanField(
                default=False, help_text="Άλλες απειλές/διαταραχές"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_pest",
            field=models.BooleanField(
                default=False, help_text="Απειλή από τα φυτοφάρμακα"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_poll",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την ρύπανση"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_road",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την διάνοιξη δρόμων"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_text",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή απειλών που αντιμετωπίζει ο τόπος",
                verbose_name="Σχόλια",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat_tour",
            field=models.BooleanField(
                default=False, help_text="Απειλή από τον τουρισμό"
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="tourism",
            field=models.TextField(
                blank=True,
                help_text="Κείμενο για τις δραστηριότητες τουρισμού και αναψυχής",
                verbose_name="Τουρισμός, αναψυχή",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="trend",
            field=models.ForeignKey(
                blank=True,
                help_text="Τάση κατάστασης τόπου",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.TrendOption",
                verbose_name="Τάση κατάστασης τόπου",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="trend_text",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή τάσης κατάστασης τόπου",
                verbose_name="Περιγραφή τάσης τόπου",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="update_date",
            field=models.DateField(
                blank=True,
                help_text="Ημερομηνία τελευταίας καταχώρησης",
                null=True,
                verbose_name="Ημερομηνία τελευταίας καταχώρησης",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="update_old",
            field=models.CharField(
                blank=True,
                help_text="Ημερομηνία τελευταίας ανανέωσης στην παλιά καταχώρηση",
                max_length=36,
                verbose_name="Ημερομηνία τελευταίας ανανέωσης στην παλιά βάση",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="view",
            field=models.TextField(
                blank=True,
                help_text="Κείμενο για τα σημεία με καλή θέα",
                verbose_name="Σημεία με καλή θέα",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="vulnerability",
            field=models.TextField(
                blank=True,
                help_text="Κείμενο σχετικά με τη τρωτότητα του τόπου",
                verbose_name="Τρωτότητα",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="width_max",
            field=models.FloatField(
                blank=True,
                help_text="Μέγιστο πλάτος (δεκαδικός αριθμός)",
                null=True,
                verbose_name="Μέγιστο πλάτος",
            ),
        ),
        migrations.AlterField(
            model_name="biotopecategoryoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Το όνομα ή σύντομη περιγραφή της κατηγορίας",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="biotopeimage",
            name="biotope",
            field=models.ForeignKey(
                help_text="Εξωτερική αναφορά σε τόπο",
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.Biotope",
                verbose_name="Τόπος",
            ),
        ),
        migrations.AlterField(
            model_name="biotopeimage",
            name="descr",
            field=models.CharField(
                blank=True,
                help_text="Σύντομη περιγραφή φωτογραφίας",
                max_length=80,
                verbose_name="Περιγραφή",
            ),
        ),
        migrations.AlterField(
            model_name="biotopeimage",
            name="image",
            field=models.ImageField(
                help_text="Αρχείο εικόνας",
                upload_to="SitesPhotos/",
                verbose_name="Εικόνα",
            ),
        ),
        migrations.AlterField(
            model_name="biotopeimage",
            name="order",
            field=models.IntegerField(
                blank=True,
                help_text="Σειρά εμφάνισης φωτογραφίας",
                null=True,
                verbose_name="Σειρά",
            ),
        ),
        migrations.AlterField(
            model_name="biotopeimage",
            name="remarks",
            field=models.TextField(
                blank=True, help_text="Σχόλια για την εικόνα", verbose_name="Σχόλια"
            ),
        ),
        migrations.AlterField(
            model_name="biotopeimage",
            name="thumbnail",
            field=models.ImageField(
                editable=False,
                help_text="Δείγμα (thumbnail) εικόνας",
                upload_to="SitesPhotos/thumbs/",
                verbose_name="Εικόνα προεπισκόπισης",
            ),
        ),
        migrations.AlterField(
            model_name="climateoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Συντομογραφία του κλιματικού τύπου",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="climateoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Το όνομα του τύπου κλίματος", max_length=390
            ),
        ),
        migrations.AlterField(
            model_name="conditionoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Κατάσταση βιότοπου", max_length=300
            ),
        ),
        migrations.AlterField(
            model_name="conservationoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Περιγραφή προτεραιότητας προστασίας",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="culturalvalueoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Συντομογραφία της αισθητικής αξίας",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="culturalvalueoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Το όνομα της αισθητικής αξίας", max_length=390
            ),
        ),
        migrations.AlterField(
            model_name="designationoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Συντομογραφία του προσδιορισμού ένταξης σε θεσμικό πλαίσιο",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="designationoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Το όνομα του τύπου ένταξης σε θεσμικό πλαίσιο",
                max_length=390,
            ),
        ),
        migrations.AlterField(
            model_name="ecologicalvalueoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Συντομογραφία της οικολογικής αξίας",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="ecologicalvalueoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Το όνομα της οικολογικής αξίας", max_length=390
            ),
        ),
        migrations.AlterField(
            model_name="geocodeoption",
            name="code",
            field=models.CharField(
                max_length=10,
                primary_key=True,
                serialize=False,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^\\d+(?:,\\d+)*\\Z", 32),
                        code="invalid",
                        message="Enter only digits separated by commas.",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="geocodeoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Το όνομα της γεωγραφικής περιοχής",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="geocodeoption",
            name="name_eng",
            field=models.CharField(
                blank=True,
                help_text="Το όνομα της γεωγραφικής περιοχής στα Αγγλικά",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="habitationoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Συντομογραφία των χαρακτηριστικών ενδιαιτημάτων",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="habitationoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Το όνομα του ενδιαιτήματος", max_length=390
            ),
        ),
        migrations.AlterField(
            model_name="humanactivityoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Συντομογραφία της ανθρώπινης δραστηριότητας",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="humanactivityoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Το όνομα της ανθρώπινης δραστηριότητας",
                max_length=390,
            ),
        ),
        migrations.AlterField(
            model_name="knowledgeoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Κατάσταση γνώσης", max_length=300
            ),
        ),
        migrations.AlterField(
            model_name="owneroption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Κατάσταση βιότοπου", max_length=300
            ),
        ),
        migrations.AlterField(
            model_name="settlement",
            name="area",
            field=models.FloatField(blank=True, null=True, verbose_name="Επιφάνεια m²"),
        ),
        migrations.AlterField(
            model_name="settlement",
            name="name",
            field=models.CharField(
                blank=True, help_text="Ονομασία οικισμού", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="settlement",
            name="perimeter",
            field=models.FloatField(blank=True, null=True, verbose_name="Περίμετρος m"),
        ),
        migrations.AlterField(
            model_name="sitetypeoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Συντομογραφία του τύπου τόπου", max_length=30, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="sitetypeoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Το όνομα του τύπου", max_length=390
            ),
        ),
        migrations.AlterField(
            model_name="socialreactionoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Περιγραφή κοινωνικής αντίδρασης", max_length=300
            ),
        ),
        migrations.AlterField(
            model_name="socialvalueoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Συντομογραφία της κοινωνικοοικονομικής/πολιτιστικής αξίας",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="socialvalueoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Το όνομα της κοινωνικοοικονομικής/πολιτιστικής αξίας",
                max_length=390,
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="category",
            field=models.TextField(
                blank=True, help_text="Σχόλια για τα γνωρίσματα", verbose_name="Σχόλια"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="category_bree",
            field=models.BooleanField(
                default=False,
                help_text="Είναι αναπαραγόμενο",
                verbose_name="Αναπαραγόμενο",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="category_ende",
            field=models.BooleanField(
                default=False, help_text="Είναι ενδημικό", verbose_name="Ενδημικό"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="category_intr",
            field=models.BooleanField(
                default=False, help_text="Είναι εισαχθέν", verbose_name="Εισαχθέν"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="category_migr",
            field=models.BooleanField(
                default=False,
                help_text="Είναι μεταναστευτικό",
                verbose_name="Μεταναστευτικό",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="category_resi",
            field=models.BooleanField(
                default=False,
                help_text="Κατοικεί μόνιμα",
                verbose_name="Μόνιμος Κάτοικος",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="conservation_bio",
            field=models.ForeignKey(
                blank=True,
                help_text="Κατάσταση διατήρησης του είδους στην Βιόσφαιρα",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="species_conservation_bio_set",
                to="naturebank.SpeciesConservationOption",
                verbose_name="Βιόσφαιρα",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="conservation_eec",
            field=models.ForeignKey(
                blank=True,
                help_text="Κατάσταση διατήρησης του είδους στην Ευρωπαική Ένωση",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="species_conservation_eec_set",
                to="naturebank.SpeciesConservationOption",
                verbose_name="Ευρωπαϊκή Ένωση",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="conservation_gr",
            field=models.ForeignKey(
                blank=True,
                help_text="Κατάσταση διατήρησης του είδους στην Ελλάδα",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="species_conservation_gr_set",
                to="naturebank.SpeciesConservationOption",
                verbose_name="Ελλάδα",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="conservation_prio",
            field=models.ForeignKey(
                blank=True,
                help_text="Προτεραιότητα προστασίας",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.SpeciesConservationPriorityOption",
                verbose_name="Προτεραιότητα Προστασίας",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="creation_date",
            field=models.DateField(
                blank=True,
                help_text="Ημερομηνία πρώτης καταχώρησης",
                null=True,
                verbose_name="Ημ/νία Πρώτης Καταχώρησης",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="expansion",
            field=models.CharField(
                blank=True,
                help_text="Στοιχεία εξάπλωσης του είδους",
                max_length=960,
                verbose_name="Εξάπλωση",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="exploit_coll",
            field=models.BooleanField(
                default=False,
                help_text="Εκμετάλλευση από τη σύλλογη",
                verbose_name="Συλλογή",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="exploit_fish",
            field=models.BooleanField(
                default=False,
                help_text="Εκμετάλλευση από το αλιεία",
                verbose_name="Αλιεία",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="exploit_graz",
            field=models.BooleanField(
                default=False,
                help_text="Εκμετάλλευση από τη βοσκή",
                verbose_name="Βοσκή",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="exploit_hunt",
            field=models.BooleanField(
                default=False,
                help_text="Εκμετάλλευση από το κυνήγι",
                verbose_name="Κυνήγι",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="exploit_logg",
            field=models.BooleanField(
                default=False,
                help_text="Εκμετάλλευση από την υλοτομία",
                verbose_name="Υλοτομία",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="habitat",
            field=models.CharField(
                blank=True,
                help_text="Στοιχεία σχετικά με τα ενδιαιτήματα",
                max_length=720,
                verbose_name="Ενδιαιτήματα",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="knowledge",
            field=models.ForeignKey(
                blank=True,
                help_text="Το επίπεδο γνώσης στο συγκεκριμένο είδος",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.SpeciesKnowledgeOption",
                verbose_name="Γνώση",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="measures_need",
            field=models.TextField(
                blank=True,
                help_text="Μέτρα προστασίας που είναι αναγκαία.",
                verbose_name="Αναγκαία Μέτρα",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="measures_take",
            field=models.TextField(
                blank=True,
                help_text="Μέτρα προστασίας που έχουν ληφθεί.",
                verbose_name="Ληφθέντα Μέτρα",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="origin",
            field=models.CharField(
                blank=True,
                help_text="Στοιχεία προέλευσης του είδους",
                max_length=18,
                verbose_name="Προέλευση",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="other_names",
            field=models.CharField(
                blank=True,
                help_text="Άλλες ονομασίες του ίδιου είδους",
                max_length=960,
                verbose_name="Άλλες Ονομασίες",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="Το path προς τη φωτογραφία του τόπου",
                upload_to="SitesPhotos",
                verbose_name="Φωτογραφία",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="plant_kind",
            field=models.ForeignKey(
                blank=True,
                help_text="Υποκατηγορία για φυτό (Αν δεν είναι φυτό πρέπει να αφεθεί κενό)",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.SpeciesPlantKindOption",
                verbose_name="Κατηγορία Φυτού",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="protection",
            field=models.ForeignKey(
                blank=True,
                help_text="Επίπεδο προστασίας του είδους",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.SpeciesProtectionOption",
                verbose_name="Προστασία",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="rarity_bio",
            field=models.ForeignKey(
                blank=True,
                help_text="Σπανιότητα του είδους στην Βιόσφαιρα",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="species_rarity_bio_set",
                to="naturebank.SpeciesRarityOption",
                verbose_name="Βιόσφαιρα",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="rarity_eec",
            field=models.ForeignKey(
                blank=True,
                help_text="Σπανιότητα του είδους στην Ευρωπαική Ένωση",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="species_rarity_eec_set",
                to="naturebank.SpeciesRarityOption",
                verbose_name="Ευρωπαϊκή Ένωση",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="rarity_gr",
            field=models.ForeignKey(
                blank=True,
                help_text="Σπανιότητα του είδους στην Ελλάδα",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="species_rarity_gr_set",
                to="naturebank.SpeciesRarityOption",
                verbose_name="Ελλάδα",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="respondent",
            field=models.TextField(
                blank=True,
                help_text="Στοιχεία καταχωρητή",
                verbose_name="Στοιχεία Καταχωρητή",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="species_category",
            field=models.ForeignKey(
                blank=True,
                help_text="Κατηγορία χλωρίδας/πανίδας που ανήκει το είδος.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.SpeciesCategoryOption",
                verbose_name="Κατηγορία Είδους",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="species_code",
            field=models.IntegerField(
                help_text="Κωδικός είδους", unique=True, verbose_name="Κωδικός Είδους"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="species_name",
            field=models.CharField(
                blank=True,
                help_text="Αγγλική ονομασία είδους",
                max_length=720,
                verbose_name="Όνομα Είδους (Αγγλικά)",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="species_name_gr",
            field=models.CharField(
                blank=True,
                help_text="Ελληνική ονομασία είδους",
                max_length=720,
                verbose_name="Όνομα Είδους (Ελληνικά)",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="sub_species",
            field=models.CharField(
                blank=True,
                help_text="Αγγλική ονομασία υποείδους",
                max_length=720,
                verbose_name="Όνομα Υποείδους (Αγγλικά)",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat",
            field=models.TextField(
                blank=True,
                help_text="Περιγραφή απειλών και κινδύνων",
                verbose_name="Σχόλια",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_buil",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την δόμηση", verbose_name="Δόμηση"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_coll",
            field=models.BooleanField(
                default=False,
                help_text="Απειλή από την συλλογή",
                verbose_name="Συλλογή",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_cult",
            field=models.BooleanField(
                default=False,
                help_text="Απειλή από την καλλιέργεια",
                verbose_name="Καλλιέργεια",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_drai",
            field=models.BooleanField(
                default=False,
                help_text="Απειλή από την αποξήρανση",
                verbose_name="Αποξήρανση",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_eutr",
            field=models.BooleanField(
                default=False,
                help_text="Απειλή από τον ευτροφισμό",
                verbose_name="Ευτροφισμός",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_fish",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την αλιεία", verbose_name="Αλιεία"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_fore",
            field=models.BooleanField(
                default=False,
                help_text="Απειλή από την υλοτομία",
                verbose_name="Υλοτομία",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_graz",
            field=models.BooleanField(
                default=False, help_text="Απειλή από την βοσκή", verbose_name="Βοσκή"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_hunt",
            field=models.BooleanField(
                default=False, help_text="Απειλή από το κυνήγι", verbose_name="Κυνήγι"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_other",
            field=models.BooleanField(
                default=False, help_text="Άλλες απειλές", verbose_name="Άλλες Απειλές"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_pest",
            field=models.BooleanField(
                default=False,
                help_text="Απειλή από τα φυτοφάρμακα",
                verbose_name="Φυτοφάρμακα",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_poll",
            field=models.BooleanField(
                default=False,
                help_text="Απειλή από την ρύπανση",
                verbose_name="Ρύπανση",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_road",
            field=models.BooleanField(
                default=False,
                help_text="Απειλή από την διάνοιξη δρόμων",
                verbose_name="Διάνοιξη Δρόμων",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="threat_tour",
            field=models.BooleanField(
                default=False,
                help_text="Απειλή από τον τουρισμό",
                verbose_name="Τουρισμός",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="trend",
            field=models.ForeignKey(
                blank=True,
                help_text="Ο ρυθμός ανάπτυξης του είδους",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="naturebank.SpeciesTrendOption",
                verbose_name="Τάση",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="update_date",
            field=models.DateField(
                blank=True,
                help_text="Ημερομηνία τελευταίας καταχώρησης",
                null=True,
                verbose_name="Ημ/νία Τελευταίας Καταχώρησης",
            ),
        ),
        migrations.AlterField(
            model_name="speciescategoryoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Τα αρχικά της συγκεκριμένης κατηγορίας στα Αγγλικά",
                max_length=24,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="speciescategoryoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Η ονομασία του είδους", max_length=300
            ),
        ),
        migrations.AlterField(
            model_name="speciesconservationoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Τα αρχικά του επιπέδου διατήρησης του είδους στα Αγγλικά",
                max_length=24,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="speciesconservationoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Ο τίτλος του επιπέδου διατήρησης του είδους στα Ελληνικά",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="speciesconservationpriorityoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Τα αρχικά του επιπέδου προτεραιότητας προστασίας στα Αγγλικά",
                max_length=24,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="speciesconservationpriorityoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Ο τίτλος του επιπέδου προτεραιότητας προστασίας στα Ελληνικά",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="speciesknowledgeoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Τα αρχικά του συγκεκριμένου επιπέδου στα Αγγλικά",
                max_length=24,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="speciesknowledgeoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Ο τίτλος του επιπέδου γνώσης στα Ελληνικά",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="speciesplantkindoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Τα αρχικά της συγκεκριμένης υποκατηγορίας στα Αγγλικά",
                max_length=24,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="speciesplantkindoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Η ονομασία αυτής της κατηγορίας φυτών",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="speciesprotectionoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Τα αρχικά του επιπέδου προστασίας στα Αγγλικά",
                max_length=24,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="speciesprotectionoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Ο τίτλος του επιπέδου προστασίας στα Ελληνικά",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="speciesrarityoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Τα αρχικά του βαθμού σπανιότητας του είδους στα Αγγλικά",
                max_length=24,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="speciesrarityoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Ο τίτλος του βαθμού σπανιότητας του είδους στα Ελληνικά",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="speciestrendoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Τα αρχικά του ρυθμού ανάπτυξης του είδους στα Αγγλικά",
                max_length=24,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="speciestrendoption",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Ο τίτλος του ρυθμού/τάσης ανάπτυξης του είδους στα Ελληνικά",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="threatoption",
            name="abbreviation",
            field=models.CharField(
                help_text="Συντομογραφία της απειλής", max_length=30, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="threatoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Το όνομα της απειλής", max_length=390
            ),
        ),
        migrations.AlterField(
            model_name="trendoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Τάση κατάστασης βιότοπου", max_length=300
            ),
        ),
        migrations.AlterField(
            model_name="trendpopoption",
            name="name",
            field=models.CharField(
                blank=True, help_text="Όνομα τάσης πληθυσμού", max_length=300
            ),
        ),
        migrations.AlterField(
            model_name="widearea",
            name="wide_area_name",
            field=models.CharField(
                blank=True,
                help_text="Όνομα ευρύτερης γεωγραφικής περιοχής.",
                max_length=150,
            ),
        ),
    ]
