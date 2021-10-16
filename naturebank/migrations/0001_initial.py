import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AbandonmentOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xaf\xcf\x84\xce\xbb\xce\xbf\xcf\x82 \xce\xb5\xcf\x80\xce\xb9\xcf\x80\xce\xad\xce\xb4\xce\xbf\xcf\x85 \xce\xb5\xce\xb3\xce\xba\xce\xb1\xcf\x84\xce\xac\xce\xbb\xce\xb5\xce\xb9\xcf\x88\xce\xb7\xcf\x82.",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u0395\u03c0\u03af\u03c0\u03b5\u03b4\u03bf \u03b5\u03b3\u03ba\u03b1\u03c4\u03ac\u03bb\u03b5\u03b9\u03c8\u03b7\u03c2",
                "verbose_name_plural": "\u0395\u03c0\u03af\u03c0\u03b5\u03b4\u03b1 \u03b5\u03b3\u03ba\u03b1\u03c4\u03ac\u03bb\u03b5\u03b9\u03c8\u03b7\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Biotope",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "site_code",
                    models.CharField(
                        help_text=b'\xce\x9f \xce\x9a\xcf\x89\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xcf\x80\xcf\x81\xce\xad\xcf\x80\xce\xb5\xce\xb9 \xce\xbd\xce\xb1 \xce\xad\xcf\x87\xce\xb5\xce\xb9 \xcf\x80\xcf\x81\xcf\x8c\xce\xb8\xce\xb5\xce\xbc\xce\xb1 \xce\xad\xce\xbd\xce\xb1 \xce\xb5\xce\xba \xcf\x84\xcf\x89\xce\xbd "\xce\x91\xce\xa4", "A\xce\x98", "AG", "AB" \xce\xae "GR".',
                        unique=True,
                        max_length=54,
                        verbose_name="\u039a\u03c9\u03b4\u03b9\u03ba\u03cc\u03c2 \u03a4\u03cc\u03c0\u03bf\u03c5",
                    ),
                ),
                (
                    "site_name",
                    models.CharField(
                        help_text=b"\xce\x97 \xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb1\xcf\x83\xce\xaf\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xce\xb2\xce\xb9\xcf\x8c\xcf\x84\xce\xbf\xcf\x80\xce\xbf\xcf\x85 (\xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac)",
                        max_length=1440,
                        verbose_name="\u038c\u03bd\u03bf\u03bc\u03b1 (\u0391\u03b3\u03b3\u03bb\u03b9\u03ba\u03ac)",
                        blank=True,
                    ),
                ),
                (
                    "site_name_gr",
                    models.CharField(
                        help_text=b"\xce\x97 \xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb1\xcf\x83\xce\xaf\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xce\xb2\xce\xb9\xcf\x8c\xcf\x84\xce\xbf\xcf\x80\xce\xbf\xcf\x85 (\xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac)",
                        max_length=1440,
                        verbose_name="\u038c\u03bd\u03bf\u03bc\u03b1 (\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac)",
                        blank=True,
                    ),
                ),
                (
                    "main_char_biotopos",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xce\x92\xce\xb9\xcf\x8c\xcf\x84\xce\xbf\xcf\x80\xce\xbf\xcf\x82;",
                        verbose_name="\u0392\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03c2",
                    ),
                ),
                (
                    "main_char_natural",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xce\xa6\xcf\x85\xcf\x83\xce\xb9\xce\xba\xcf\x8c \xce\xa4\xce\xbf\xcf\x80\xce\xaf\xce\xbf;",
                        verbose_name="\u03a6\u03c5\u03c3\u03b9\u03ba\u03cc \u03a4\u03bf\u03c0\u03af\u03bf",
                    ),
                ),
                (
                    "main_char_built",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xce\x94\xce\xbf\xce\xbc\xce\xb7\xce\xbc\xce\xad\xce\xbd\xce\xbf \xce\xa4\xce\xbf\xcf\x80\xce\xaf\xce\xbf;",
                        verbose_name="\u0394\u03bf\u03bc\u03b7\u03bc\u03ad\u03bd\u03bf \u03a4\u03bf\u03c0\u03af\u03bf",
                    ),
                ),
                (
                    "reg_code_1",
                    models.CharField(
                        help_text=b"\xce\x93\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xba\xcf\x89\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 1",
                        max_length=24,
                        verbose_name="\u0393\u03b5\u03c9\u03b3\u03c1\u03b1\u03c6\u03b9\u03ba\u03cc\u03c2 \u03ba\u03c9\u03b4\u03b9\u03ba\u03cc\u03c2 1",
                        blank=True,
                    ),
                ),
                (
                    "reg_code_2",
                    models.CharField(
                        help_text=b"\xce\x93\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xba\xcf\x89\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 2",
                        max_length=24,
                        verbose_name="\u0393\u03b5\u03c9\u03b3\u03c1\u03b1\u03c6\u03b9\u03ba\u03cc\u03c2 \u03ba\u03c9\u03b4\u03b9\u03ba\u03cc\u03c2 2",
                        blank=True,
                    ),
                ),
                (
                    "reg_code_3",
                    models.CharField(
                        help_text=b"\xce\x93\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xba\xcf\x89\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 3",
                        max_length=24,
                        verbose_name="\u0393\u03b5\u03c9\u03b3\u03c1\u03b1\u03c6\u03b9\u03ba\u03cc\u03c2 \u03ba\u03c9\u03b4\u03b9\u03ba\u03cc\u03c2 3",
                        blank=True,
                    ),
                ),
                (
                    "reg_code_4",
                    models.CharField(
                        help_text=b"\xce\x93\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xba\xcf\x89\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 4",
                        max_length=24,
                        verbose_name="\u0393\u03b5\u03c9\u03b3\u03c1\u03b1\u03c6\u03b9\u03ba\u03cc\u03c2 \u03ba\u03c9\u03b4\u03b9\u03ba\u03cc\u03c2 4",
                        blank=True,
                    ),
                ),
                (
                    "creation_date",
                    models.DateField(
                        help_text=b"\xce\x97\xce\xbc\xce\xb5\xcf\x81\xce\xbf\xce\xbc\xce\xb7\xce\xbd\xce\xaf\xce\xb1 \xcf\x80\xcf\x81\xcf\x8e\xcf\x84\xce\xb7\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xb1\xcf\x87\xcf\x8e\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82",
                        null=True,
                        verbose_name="\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1 \u03c0\u03c1\u03ce\u03c4\u03b7\u03c2 \u03ba\u03b1\u03c4\u03b1\u03c7\u03ce\u03c1\u03b7\u03c3\u03b7\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "update_date",
                    models.DateField(
                        help_text=b"\xce\x97\xce\xbc\xce\xb5\xcf\x81\xce\xbf\xce\xbc\xce\xb7\xce\xbd\xce\xaf\xce\xb1 \xcf\x84\xce\xb5\xce\xbb\xce\xb5\xcf\x85\xcf\x84\xce\xb1\xce\xaf\xce\xb1\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xb1\xcf\x87\xcf\x8e\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82",
                        null=True,
                        verbose_name="\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1 \u03c4\u03b5\u03bb\u03b5\u03c5\u03c4\u03b1\u03af\u03b1\u03c2 \u03ba\u03b1\u03c4\u03b1\u03c7\u03ce\u03c1\u03b7\u03c3\u03b7\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "date_old",
                    models.CharField(
                        help_text=b"\xce\x97\xce\xbc\xce\xb5\xcf\x81\xce\xbf\xce\xbc\xce\xb7\xce\xbd\xce\xaf\xce\xb1 \xce\xb4\xce\xb7\xce\xbc\xce\xb9\xce\xbf\xcf\x85\xcf\x81\xce\xb3\xce\xaf\xce\xb1\xcf\x82 \xcf\x80\xce\xb1\xce\xbb\xce\xb9\xce\xac\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xb1\xcf\x87\xcf\x8e\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82",
                        max_length=36,
                        verbose_name="\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1 \u03b4\u03b7\u03bc\u03b9\u03bf\u03c5\u03c1\u03b3\u03af\u03b1\u03c2 \u03c0\u03b1\u03bb\u03b9\u03ac\u03c2 \u03ba\u03b1\u03c4\u03b1\u03c7\u03ce\u03c1\u03b7\u03c3\u03b7\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "update_old",
                    models.CharField(
                        help_text=b"\xce\x97\xce\xbc\xce\xb5\xcf\x81\xce\xbf\xce\xbc\xce\xb7\xce\xbd\xce\xaf\xce\xb1 \xcf\x84\xce\xb5\xce\xbb\xce\xb5\xcf\x85\xcf\x84\xce\xb1\xce\xaf\xce\xb1\xcf\x82 \xce\xb1\xce\xbd\xce\xb1\xce\xbd\xce\xad\xcf\x89\xcf\x83\xce\xb7\xcf\x82 \xcf\x83\xcf\x84\xce\xb7\xce\xbd \xcf\x80\xce\xb1\xce\xbb\xce\xb9\xce\xac \xce\xba\xce\xb1\xcf\x84\xce\xb1\xcf\x87\xcf\x8e\xcf\x81\xce\xb7\xcf\x83\xce\xb7",
                        max_length=36,
                        verbose_name="\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1 \u03c4\u03b5\u03bb\u03b5\u03c5\u03c4\u03b1\u03af\u03b1\u03c2 \u03b1\u03bd\u03b1\u03bd\u03ad\u03c9\u03c3\u03b7\u03c2 \u03c3\u03c4\u03b7\u03bd \u03c0\u03b1\u03bb\u03b9\u03ac \u03b2\u03ac\u03c3\u03b7",
                        blank=True,
                    ),
                ),
                (
                    "comp_code",
                    models.CharField(
                        help_text=b"\xce\x9a\xcf\x89\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xcf\x83\xcf\x8d\xce\xbd\xce\xb8\xce\xb5\xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        max_length=54,
                        verbose_name="\u039a\u03c9\u03b4\u03b9\u03ba\u03cc\u03c2 \u03a3\u03cd\u03bd\u03b8\u03b5\u03c4\u03bf\u03c5 \u03a4\u03cc\u03c0\u03bf\u03c5",
                        blank=True,
                    ),
                ),
                (
                    "comp_name",
                    models.CharField(
                        help_text=b"\xce\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x83\xcf\x8d\xce\xbd\xce\xb8\xce\xb5\xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        max_length=1440,
                        verbose_name="\u038c\u03bd\u03bf\u03bc\u03b1 \u03a3\u03cd\u03bd\u03b8\u03b5\u03c4\u03bf\u03c5 \u03a4\u03cc\u03c0\u03bf\u03c5",
                        blank=True,
                    ),
                ),
                (
                    "dist_name",
                    models.CharField(
                        help_text=b"\xce\x86\xce\xbb\xce\xbb\xce\xb7 \xce\xb3\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xce\xae \xce\xb5\xce\xbd\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1",
                        max_length=1440,
                        verbose_name="\u0386\u03bb\u03bb\u03b7 \u03b3\u03b5\u03c9\u03b3\u03c1\u03b1\u03c6\u03b9\u03ba\u03ae \u03b5\u03bd\u03cc\u03c4\u03b7\u03c4\u03b1",
                        blank=True,
                    ),
                ),
                (
                    "reg_mun",
                    models.CharField(
                        help_text=b"\xce\x94\xce\xae\xce\xbc\xce\xbf\xcf\x82 - \xce\x9a\xce\xbf\xce\xb9\xce\xbd\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1",
                        max_length=480,
                        verbose_name="\u0394\u03ae\u03bc\u03bf\u03c2 - \u039a\u03bf\u03b9\u03bd\u03cc\u03c4\u03b7\u03c4\u03b1",
                        blank=True,
                    ),
                ),
                (
                    "area",
                    models.FloatField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xce\xbf\xce\xbb\xce\xb9\xce\xba\xce\xae \xce\xad\xce\xba\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xb2\xce\xb9\xce\xbf\xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        null=True,
                        verbose_name="\u03a3\u03c5\u03bd\u03bf\u03bb\u03b9\u03ba\u03ae \u03ad\u03ba\u03c4\u03b1\u03c3\u03b7",
                        blank=True,
                    ),
                ),
                (
                    "area_l",
                    models.FloatField(
                        help_text=b"\xce\xa7\xce\xb5\xcf\x81\xcf\x83\xce\xb1\xce\xaf\xce\xb1 \xce\xad\xce\xba\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xb2\xce\xb9\xce\xbf\xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        null=True,
                        verbose_name="\u03a7\u03b5\u03c1\u03c3\u03b1\u03af\u03b1 \u03ad\u03ba\u03c4\u03b1\u03c3\u03b7",
                        blank=True,
                    ),
                ),
                (
                    "area_s",
                    models.FloatField(
                        help_text=b"\xce\x98\xce\xb1\xce\xbb\xce\xac\xcf\x83\xcf\x83\xce\xb9\xce\xb1 \xce\xad\xce\xba\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xb2\xce\xb9\xce\xbf\xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        null=True,
                        verbose_name="\u0398\u03b1\u03bb\u03ac\u03c3\u03c3\u03b9\u03b1 \u03ad\u03ba\u03c4\u03b1\u03c3\u03b7",
                        blank=True,
                    ),
                ),
                (
                    "long_deg",
                    models.FloatField(
                        help_text=b"\xce\x9f\xce\xb9 \xce\xbc\xce\xbf\xce\xaf\xcf\x81\xce\xb5\xcf\x82 (degrees) \xcf\x84\xce\xbf\xcf\x85 longitude (\xce\xbb)",
                        null=True,
                        verbose_name="Longitude (\u03bc\u03bf\u03af\u03c1\u03b5\u03c2)",
                        blank=True,
                    ),
                ),
                (
                    "long_min",
                    models.FloatField(
                        help_text=b"\xce\xa4\xce\xb1 \xcf\x80\xcf\x81\xcf\x8e\xcf\x84\xce\xb1 \xce\xbb\xce\xb5\xcf\x80\xcf\x84\xce\xac (minutes) \xcf\x84\xce\xbf\xcf\x85 longitude (\xce\xbb)",
                        null=True,
                        verbose_name="Longitude (\u03bb\u03b5\u03c0\u03c4\u03ac)",
                        blank=True,
                    ),
                ),
                (
                    "long_sec",
                    models.FloatField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb4\xce\xb5\xcf\x8d\xcf\x84\xce\xb5\xcf\x81\xce\xb1 \xce\xbb\xce\xb5\xcf\x80\xcf\x84\xce\xac (seconds) \xcf\x84\xce\xbf\xcf\x85 longitude (\xce\xbb)",
                        null=True,
                        verbose_name="Longitude (\u03b4\u03b5\u03cd\u03c4\u03b5\u03c1\u03b1)",
                        blank=True,
                    ),
                ),
                (
                    "lat_deg",
                    models.FloatField(
                        help_text=b"\xce\x9f\xce\xb9 \xce\xbc\xce\xbf\xce\xaf\xcf\x81\xce\xb5\xcf\x82 (degrees) \xcf\x84\xce\xbf\xcf\x85 latitude.",
                        null=True,
                        verbose_name="Latitude (\u03bc\u03bf\u03af\u03c1\u03b5\u03c2)",
                        blank=True,
                    ),
                ),
                (
                    "lat_min",
                    models.FloatField(
                        help_text=b"\xce\xa4\xce\xb1 \xcf\x80\xcf\x81\xcf\x8e\xcf\x84\xce\xb1 \xce\xbb\xce\xb5\xcf\x80\xcf\x84\xce\xac (minutes) \xcf\x84\xce\xbf\xcf\x85 latitude.",
                        null=True,
                        verbose_name="Latitude (\u03bb\u03b5\u03c0\u03c4\u03ac)",
                        blank=True,
                    ),
                ),
                (
                    "lat_sec",
                    models.FloatField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb4\xce\xb5\xcf\x8d\xcf\x84\xce\xb5\xcf\x81\xce\xb1 \xce\xbb\xce\xb5\xcf\x80\xcf\x84\xce\xac (seconds) \xcf\x84\xce\xbf\xcf\x85 latitude",
                        null=True,
                        verbose_name="Latitude (\u03b4\u03b5\u03cd\u03c4\u03b5\u03c1\u03b1)",
                        blank=True,
                    ),
                ),
                (
                    "alt_mean",
                    models.FloatField(
                        help_text=b"\xce\x9c\xce\xad\xcf\x83\xce\xbf \xcf\x85\xcf\x88\xcf\x8c\xce\xbc\xce\xb5\xcf\x84\xcf\x81\xce\xbf (\xce\xb4\xce\xb5\xce\xba\xce\xb1\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xb1\xcf\x81\xce\xb9\xce\xb8\xce\xbc\xcf\x8c\xcf\x82)",
                        null=True,
                        verbose_name="\u039c\u03ad\u03c3\u03bf \u03c5\u03c8\u03cc\u03bc\u03b5\u03c4\u03c1\u03bf",
                        blank=True,
                    ),
                ),
                (
                    "alt_max",
                    models.FloatField(
                        help_text=b"\xce\x9c\xce\xad\xce\xb3\xce\xb9\xcf\x83\xcf\x84\xce\xbf \xcf\x85\xcf\x88\xcf\x8c\xce\xbc\xce\xb5\xcf\x84\xcf\x81\xce\xbf (\xce\xb4\xce\xb5\xce\xba\xce\xb1\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xb1\xcf\x81\xce\xb9\xce\xb8\xce\xbc\xcf\x8c\xcf\x82)",
                        null=True,
                        verbose_name="\u039c\u03ad\u03b3\u03b9\u03c3\u03c4\u03bf \u03c5\u03c8\u03cc\u03bc\u03b5\u03c4\u03c1\u03bf",
                        blank=True,
                    ),
                ),
                (
                    "alt_min",
                    models.FloatField(
                        help_text=b"\xce\x95\xce\xbb\xce\xac\xcf\x87\xce\xb9\xcf\x83\xcf\x84\xce\xbf \xcf\x85\xcf\x88\xcf\x8c\xce\xbc\xce\xb5\xcf\x84\xcf\x81\xce\xbf (\xce\xb4\xce\xb5\xce\xba\xce\xb1\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xb1\xcf\x81\xce\xb9\xce\xb8\xce\xbc\xcf\x8c\xcf\x82)",
                        null=True,
                        verbose_name="\u0395\u03bb\u03ac\u03c7\u03b9\u03c3\u03c4\u03bf \u03c5\u03c8\u03cc\u03bc\u03b5\u03c4\u03c1\u03bf",
                        blank=True,
                    ),
                ),
                (
                    "length_max",
                    models.FloatField(
                        help_text=b"\xce\x9c\xce\xad\xce\xb3\xce\xb9\xcf\x83\xcf\x84\xce\xbf \xce\xbc\xce\xae\xce\xba\xce\xbf\xcf\x82 (\xce\xb4\xce\xb5\xce\xba\xce\xb1\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xb1\xcf\x81\xce\xb9\xce\xb8\xce\xbc\xcf\x8c\xcf\x82)",
                        null=True,
                        verbose_name="\u039c\u03ad\u03b3\u03b9\u03c3\u03c4\u03bf \u03bc\u03ae\u03ba\u03bf\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "width_max",
                    models.FloatField(
                        help_text=b"\xce\x9c\xce\xad\xce\xb3\xce\xb9\xcf\x83\xcf\x84\xce\xbf \xcf\x80\xce\xbb\xce\xac\xcf\x84\xce\xbf\xcf\x82 (\xce\xb4\xce\xb5\xce\xba\xce\xb1\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xb1\xcf\x81\xce\xb9\xce\xb8\xce\xbc\xcf\x8c\xcf\x82)",
                        null=True,
                        verbose_name="\u039c\u03ad\u03b3\u03b9\u03c3\u03c4\u03bf \u03c0\u03bb\u03ac\u03c4\u03bf\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "respondent",
                    models.TextField(
                        help_text=b"\xce\x91\xce\xbd\xce\xb1\xce\xbb\xcf\x85\xcf\x84\xce\xb9\xce\xba\xce\xae \xcf\x80\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xcf\x89\xce\xbd \xcf\x83\xcf\x84\xce\xbf\xce\xb9\xcf\x87\xce\xb5\xce\xaf\xcf\x89\xce\xbd \xcf\x84\xce\xbf\xcf\x85 \xce\xba\xce\xb1\xcf\x84\xce\xb1\xcf\x87\xcf\x89\xcf\x81\xce\xb7\xcf\x84\xce\xae",
                        verbose_name="\u03a3\u03c4\u03bf\u03b9\u03c7\u03b5\u03af\u03b1 \u039a\u03b1\u03c4\u03b1\u03c7\u03c9\u03c1\u03b7\u03c4\u03ae",
                        blank=True,
                    ),
                ),
                (
                    "document",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb7\xce\xb3\xce\xad\xcf\x82, \xce\xb2\xce\xb9\xce\xb2\xce\xbb\xce\xb9\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xce\xba\xce\xb1\xce\xb9 \xce\xb1\xce\xbd\xce\xb1\xcf\x86\xce\xbf\xcf\x81\xce\xad\xcf\x82 \xce\xb1\xcf\x80\xcf\x8c \xcf\x8c\xcf\x80\xce\xbf\xcf\x85 \xce\xb1\xce\xbd\xcf\x84\xce\xbb\xce\xae\xce\xb8\xce\xb7\xce\xba\xce\xb1\xce\xbd \xcf\x84\xce\xb1 \xce\xb4\xce\xb5\xce\xb4\xce\xbf\xce\xbc\xce\xad\xce\xbd\xce\xb1.",
                        verbose_name="\u03a0\u03b7\u03b3\u03ad\u03c2 \u03ba\u03b1\u03b9 \u0391\u03bd\u03b1\u03c6\u03bf\u03c1\u03ad\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "trend_text",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xce\xac\xcf\x83\xce\xb7\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xce\xac\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        blank=True,
                    ),
                ),
                (
                    "threat_hunt",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xbf \xce\xba\xcf\x85\xce\xbd\xce\xae\xce\xb3\xce\xb9",
                    ),
                ),
                (
                    "threat_fish",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb1\xce\xbb\xce\xb9\xce\xb5\xce\xaf\xce\xb1",
                    ),
                ),
                (
                    "threat_coll",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x83\xcf\x85\xce\xbb\xce\xbb\xce\xbf\xce\xb3\xce\xae",
                    ),
                ),
                (
                    "threat_graz",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb2\xce\xbf\xcf\x83\xce\xba\xce\xae",
                    ),
                ),
                (
                    "threat_poll",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x81\xcf\x8d\xcf\x80\xce\xb1\xce\xbd\xcf\x83\xce\xb7",
                    ),
                ),
                (
                    "threat_cult",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xba\xce\xb1\xce\xbb\xce\xbb\xce\xb9\xce\xad\xcf\x81\xce\xb3\xce\xb5\xce\xb9\xce\xb1",
                    ),
                ),
                (
                    "threat_road",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb4\xce\xb9\xce\xac\xce\xbd\xce\xbf\xce\xb9\xce\xbe\xce\xb7 \xce\xb4\xcf\x81\xcf\x8c\xce\xbc\xcf\x89\xce\xbd",
                    ),
                ),
                (
                    "threat_buil",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb4\xcf\x8c\xce\xbc\xce\xb7\xcf\x83\xce\xb7",
                    ),
                ),
                (
                    "threat_drai",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb1\xcf\x80\xce\xbf\xce\xbe\xce\xae\xcf\x81\xce\xb1\xce\xbd\xcf\x83\xce\xb7",
                    ),
                ),
                (
                    "threat_eutr",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xbf\xce\xbd \xce\xb5\xcf\x85\xcf\x84\xcf\x81\xce\xbf\xcf\x86\xce\xb9\xcf\x83\xce\xbc\xcf\x8c\xcf\x82",
                    ),
                ),
                (
                    "threat_pest",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb1 \xcf\x86\xcf\x85\xcf\x84\xce\xbf\xcf\x86\xce\xac\xcf\x81\xce\xbc\xce\xb1\xce\xba\xce\xb1",
                    ),
                ),
                (
                    "threat_tour",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xbf\xce\xbd \xcf\x84\xce\xbf\xcf\x85\xcf\x81\xce\xb9\xcf\x83\xce\xbc\xcf\x8c",
                    ),
                ),
                (
                    "threat_fore",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x85\xce\xbb\xce\xbf\xcf\x84\xce\xbf\xce\xbc\xce\xaf\xce\xb1",
                    ),
                ),
                (
                    "threat_mini",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb5\xce\xbe\xcf\x8c\xcf\x81\xcf\x85\xce\xbe\xce\xb7",
                    ),
                ),
                (
                    "threat_other",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x86\xce\xbb\xce\xbb\xce\xb5\xcf\x82 \xce\xb1\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xad\xcf\x82/\xce\xb4\xce\xb9\xce\xb1\xcf\x84\xce\xb1\xcf\x81\xce\xb1\xcf\x87\xce\xad\xcf\x82",
                    ),
                ),
                (
                    "threat_text",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xce\xb1\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xcf\x8e\xce\xbd \xcf\x80\xce\xbf\xcf\x85 \xce\xb1\xce\xbd\xcf\x84\xce\xb9\xce\xbc\xce\xb5\xcf\x84\xcf\x89\xcf\x80\xce\xaf\xce\xb6\xce\xb5\xce\xb9 \xce\xbf \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x82",
                        verbose_name=b"\xce\xa3\xcf\x87\xcf\x8c\xce\xbb\xce\xb9\xce\xb1",
                        blank=True,
                    ),
                ),
                (
                    "measures_take",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xce\xbc\xce\xad\xcf\x84\xcf\x81\xcf\x89\xce\xbd \xcf\x80\xce\xbf\xcf\x85 \xce\xbb\xce\xb1\xce\xbc\xce\xb2\xce\xac\xce\xbd\xce\xbf\xce\xbd\xcf\x84\xce\xb1\xce\xb9 \xcf\x83\xcf\x84\xce\xbf \xce\xb2\xce\xb9\xcf\x8c\xcf\x84\xce\xbf\xcf\x80\xce\xbf",
                        verbose_name=b"\xce\x9b\xce\xb7\xcf\x86\xce\xb8\xce\xad\xce\xbd\xcf\x84\xce\xb1 \xce\x9c\xce\xad\xcf\x84\xcf\x81\xce\xb1",
                        blank=True,
                    ),
                ),
                (
                    "measures_need",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xce\xbc\xce\xad\xcf\x84\xcf\x81\xcf\x89\xce\xbd \xcf\x80\xce\xbf\xcf\x85 \xce\xb1\xcf\x80\xce\xb1\xce\xb9\xcf\x84\xce\xbf\xcf\x8d\xce\xbd\xcf\x84\xce\xb1\xce\xb9 \xcf\x83\xcf\x84\xce\xbf \xce\xb2\xce\xb9\xcf\x8c\xcf\x84\xce\xbf\xcf\x80\xce\xbf",
                        verbose_name=b"\xce\x91\xce\xbd\xce\xb1\xce\xb3\xce\xba\xce\xb1\xce\xaf\xce\xb1 \xce\x9c\xce\xad\xcf\x84\xcf\x81\xce\xb1",
                        blank=True,
                    ),
                ),
                ("fire_50", models.BooleanField(default=False, help_text=b"")),
                ("fire_3050", models.BooleanField(default=False, help_text=b"")),
                ("fire_1030", models.BooleanField(default=False, help_text=b"")),
                ("fire_10", models.BooleanField(default=False, help_text=b"")),
                (
                    "fire_text",
                    models.TextField(
                        help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xb1\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x83\xcf\x84\xce\xbf\xce\xb9\xcf\x87\xce\xb5\xce\xaf\xcf\x89\xce\xbd \xcf\x83\xcf\x87\xce\xb5\xcf\x84\xce\xb9\xce\xba\xce\xac \xce\xbc\xce\xb5 \xcf\x80\xcf\x85\xcf\x81\xce\xba\xce\xb1\xce\xb3\xce\xb9\xce\xad\xcf\x82",
                        blank=True,
                    ),
                ),
                ("restore", models.TextField(help_text=b"", blank=True)),
                (
                    "introduct",
                    models.CharField(
                        help_text=b"\xce\x9c\xce\xb9\xce\xba\xcf\x81\xcf\x8c\xcf\x82 \xcf\x84\xce\xaf\xcf\x84\xce\xbb\xce\xbf\xcf\x82",
                        max_length=24,
                        verbose_name="\u039c\u03b9\u03ba\u03c1\u03cc\u03c2 \u03a4\u03af\u03c4\u03bb\u03bf\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "intro_text",
                    models.TextField(
                        help_text=b"\xce\x95\xce\xb9\xcf\x83\xce\xb1\xce\xb3\xcf\x89\xce\xb3\xce\xb9\xce\xba\xcf\x8c \xce\xba\xce\xb5\xce\xaf\xce\xbc\xce\xb5\xce\xbd\xce\xbf",
                        verbose_name="\u0395\u03b9\u03c3\u03b1\u03b3\u03c9\u03b3\u03b9\u03ba\u03cc \u039a\u03b5\u03af\u03bc\u03b5\u03bd\u03bf",
                        blank=True,
                    ),
                ),
                (
                    "social_reaction_text",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xce\xba\xce\xbf\xce\xb9\xce\xbd\xcf\x89\xce\xbd\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbd\xcf\x84\xce\xaf\xce\xb4\xcf\x81\xce\xb1\xcf\x83\xce\xb7\xcf\x82",
                        verbose_name=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xce\xba\xce\xbf\xce\xb9\xce\xbd\xcf\x89\xce\xbd\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbd\xcf\x84\xce\xaf\xce\xb4\xcf\x81\xce\xb1\xcf\x83\xce\xb7\xcf\x82",
                        blank=True,
                    ),
                ),
                (
                    "develop",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xce\xb5\xce\xbe\xce\xad\xce\xbb\xce\xb9\xce\xbe\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name="\u03a0\u03b5\u03c1\u03b9\u03b3\u03c1\u03b1\u03c6\u03ae \u0395\u03be\u03ad\u03bb\u03b9\u03be\u03b7\u03c2 \u03a4\u03cc\u03c0\u03bf\u03c5",
                        blank=True,
                    ),
                ),
                (
                    "protection",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xce\xb7\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7\xcf\x82 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\x9a\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xa0\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82",
                        blank=True,
                    ),
                ),
                (
                    "ownership_text",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xce\xb7\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7\xcf\x82 \xce\xb9\xce\xb4\xce\xb9\xce\xbf\xce\xba\xcf\x84\xce\xb7\xcf\x83\xce\xaf\xce\xb1\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xce\x99\xce\xb4\xce\xb9\xce\xbf\xce\xba\xcf\x84\xce\xb7\xcf\x83\xce\xaf\xce\xb1\xcf\x82",
                        blank=True,
                    ),
                ),
                (
                    "geology",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xce\xb7\xcf\x82 \xce\xb3\xce\xb5\xcf\x89\xce\xbb\xce\xbf\xce\xb3\xce\xaf\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\x93\xce\xb5\xcf\x89\xce\xbb\xce\xbf\xce\xb3\xce\xaf\xce\xb1",
                        blank=True,
                    ),
                ),
                (
                    "characteristics",
                    models.TextField(
                        help_text=b"\xce\x93\xce\xb5\xce\xbd\xce\xb9\xce\xba\xce\xae \xcf\x80\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        blank=True,
                    ),
                ),
                (
                    "history",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xce\xb7\xcf\x82 \xce\xb9\xcf\x83\xcf\x84\xce\xbf\xcf\x81\xce\xaf\xce\xb1\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\x99\xcf\x83\xcf\x84\xce\xbf\xcf\x81\xce\xaf\xce\xb1 \xce\xba\xce\xb1\xce\xb9 \xce\x95\xce\xbe\xce\xad\xce\xbb\xce\xb9\xce\xbe\xce\xb7",
                        blank=True,
                    ),
                ),
                (
                    "quality",
                    models.TextField(
                        help_text=b"\xce\xa3\xcf\x87\xcf\x8c\xce\xbb\xce\xb9\xce\xb1 \xcf\x83\xcf\x87\xce\xb5\xcf\x84\xce\xb9\xce\xba\xce\xac \xce\xbc\xce\xb5 \xcf\x84\xce\xb9\xcf\x82 \xce\xb1\xce\xbe\xce\xaf\xce\xb5\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\xa3\xcf\x87\xcf\x8c\xce\xbb\xce\xb9\xce\xb1",
                        blank=True,
                    ),
                ),
                (
                    "vulnerability",
                    models.TextField(
                        help_text=b"\xce\x9a\xce\xb5\xce\xaf\xce\xbc\xce\xb5\xce\xbd\xce\xbf \xcf\x83\xcf\x87\xce\xb5\xcf\x84\xce\xb9\xce\xba\xce\xac \xce\xbc\xce\xb5 \xcf\x84\xce\xb7 \xcf\x84\xcf\x81\xcf\x89\xcf\x84\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\xa4\xcf\x81\xcf\x89\xcf\x84\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1",
                        blank=True,
                    ),
                ),
                (
                    "tourism",
                    models.TextField(
                        help_text=b"\xce\x9a\xce\xb5\xce\xaf\xce\xbc\xce\xb5\xce\xbd\xce\xbf \xce\xb3\xce\xb9\xce\xb1 \xcf\x84\xce\xb9\xcf\x82 \xce\xb4\xcf\x81\xce\xb1\xcf\x83\xcf\x84\xce\xb7\xcf\x81\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb5\xcf\x82 \xcf\x84\xce\xbf\xcf\x85\xcf\x81\xce\xb9\xcf\x83\xce\xbc\xce\xbf\xcf\x8d \xce\xba\xce\xb1\xce\xb9 \xce\xb1\xce\xbd\xce\xb1\xcf\x88\xcf\x85\xcf\x87\xce\xae\xcf\x82",
                        verbose_name=b"\xce\xa4\xce\xbf\xcf\x85\xcf\x81\xce\xb9\xcf\x83\xce\xbc\xcf\x8c\xcf\x82, \xce\xb1\xce\xbd\xce\xb1\xcf\x88\xcf\x85\xcf\x87\xce\xae",
                        blank=True,
                    ),
                ),
                (
                    "infrastructure",
                    models.TextField(
                        help_text=b"\xce\x9a\xce\xb5\xce\xaf\xce\xbc\xce\xb5\xce\xbd\xce\xbf \xcf\x83\xcf\x87\xce\xb5\xcf\x84\xce\xb9\xce\xba\xce\xac \xce\xbc\xce\xb5 \xcf\x84\xce\xb7\xce\xbd \xcf\x85\xcf\x80\xce\xbf\xce\xb4\xce\xbf\xce\xbc\xce\xae \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82/\xce\xb1\xce\xbe\xce\xb9\xce\xbf\xcf\x80\xce\xbf\xce\xaf\xce\xb7\xcf\x83\xce\xb7\xcf\x82",
                        verbose_name=b"\xce\xa5\xcf\x80\xce\xbf\xce\xb4\xce\xbf\xce\xbc\xce\xae \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82, \xce\xb1\xce\xbe\xce\xb9\xce\xbf\xcf\x80\xce\xbf\xce\xaf\xce\xb7\xcf\x83\xce\xb7\xcf\x82",
                        blank=True,
                    ),
                ),
                (
                    "view",
                    models.TextField(
                        help_text=b"\xce\x9a\xce\xb5\xce\xaf\xce\xbc\xce\xb5\xce\xbd\xce\xbf \xce\xb3\xce\xb9\xce\xb1 \xcf\x84\xce\xb1 \xcf\x83\xce\xb7\xce\xbc\xce\xb5\xce\xaf\xce\xb1 \xce\xbc\xce\xb5 \xce\xba\xce\xb1\xce\xbb\xce\xae \xce\xb8\xce\xad\xce\xb1",
                        verbose_name=b"\xce\xa3\xce\xb7\xce\xbc\xce\xb5\xce\xaf\xce\xb1 \xce\xbc\xce\xb5 \xce\xba\xce\xb1\xce\xbb\xce\xae \xce\xb8\xce\xad\xce\xb1",
                        blank=True,
                    ),
                ),
                (
                    "path",
                    models.TextField(
                        help_text=b"\xce\x9a\xce\xb5\xce\xaf\xce\xbc\xce\xb5\xce\xbd\xce\xbf \xce\xb3\xce\xb9\xce\xb1 \xcf\x84\xce\xb1 \xce\xbc\xce\xbf\xce\xbd\xce\xbf\xcf\x80\xce\xac\xcf\x84\xce\xb9\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\x9c\xce\xbf\xce\xbd\xce\xbf\xcf\x80\xce\xac\xcf\x84\xce\xb9\xce\xb1, \xcf\x80\xce\xb5\xcf\x81\xce\xaf\xcf\x80\xce\xb1\xcf\x84\xce\xbf\xce\xb9",
                        blank=True,
                    ),
                ),
                (
                    "population",
                    models.FloatField(
                        help_text=b"\xce\x9f \xcf\x80\xce\xbb\xce\xb7\xce\xb8\xcf\x85\xcf\x83\xce\xbc\xcf\x8c\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85 \xcf\x84\xce\xbf 1991",
                        null=True,
                        verbose_name=b"\xce\xa0\xce\xbb\xce\xb7\xce\xb8\xcf\x85\xcf\x83\xce\xbc\xcf\x8c\xcf\x82 1991",
                        blank=True,
                    ),
                ),
                (
                    "landvalue",
                    models.FloatField(
                        help_text=b"\xce\x97 \xce\xbc\xce\xad\xce\xb3\xce\xb9\xcf\x83\xcf\x84\xce\xb7 \xce\xb1\xce\xbe\xce\xaf\xce\xb1 \xce\xb3\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85 (\xce\x9f\xce\xb9 \xcf\x80\xce\xb1\xce\xbb\xce\xb9\xce\xad\xcf\x82 \xce\xb5\xce\xb3\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xad\xcf\x82 \xce\xb5\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xcf\x83\xce\xb5 \xce\xb4\xcf\x81\xcf\x87./\xcf\x83\xcf\x84\xcf\x81\xce\xad\xce\xbc\xce\xbc\xce\xb1)",
                        null=True,
                        verbose_name=b"\xce\x9c\xce\xad\xce\xb3\xce\xb9\xcf\x83\xcf\x84\xce\xb7 \xce\xb1\xce\xbe\xce\xaf\xce\xb1 \xce\xb3\xce\xb7\xcf\x82",
                        blank=True,
                    ),
                ),
                (
                    "species_text",
                    models.TextField(
                        help_text=b"\xce\xa3\xcf\x87\xcf\x8c\xce\xbb\xce\xb9\xce\xb1 \xce\xb3\xce\xb9\xce\xb1 \xcf\x84\xce\xb1 \xce\xb5\xce\xaf\xce\xb4\xce\xb7 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        verbose_name=b"\xce\xa3\xcf\x87\xcf\x8c\xce\xbb\xce\xb9\xce\xb1 \xce\xb3\xce\xb9\xce\xb1 \xcf\x84\xce\xb1 \xce\xb5\xce\xaf\xce\xb4\xce\xb7",
                        blank=True,
                    ),
                ),
                (
                    "gis_area",
                    models.FloatField(
                        null=True,
                        verbose_name=b"\xce\x95\xcf\x80\xce\xb9\xcf\x86\xce\xac\xce\xbd\xce\xb5\xce\xb9\xce\xb1 m\xc2\xb2",
                        blank=True,
                    ),
                ),
                (
                    "gis_perimeter",
                    models.FloatField(
                        null=True,
                        verbose_name=b"\xce\xa0\xce\xb5\xcf\x81\xce\xaf\xce\xbc\xce\xb5\xcf\x84\xcf\x81\xce\xbf\xcf\x82 m",
                        blank=True,
                    ),
                ),
                (
                    "gis_sitecode",
                    models.CharField(
                        max_length=9,
                        null=True,
                        verbose_name=b"\xce\x9a\xcf\x89\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xb1\xcf\x80\xcf\x8c GIS (sitecode)",
                        blank=True,
                    ),
                ),
                (
                    "gis_zorder",
                    models.IntegerField(
                        null=True,
                        verbose_name=b"\xce\xa3\xce\xb5\xce\xb9\xcf\x81\xce\xac \xcf\x83\xcf\x84\xcf\x81\xcf\x8e\xcf\x83\xce\xb7\xcf\x82 \xce\xba\xce\xb1\xce\xb8\xce\x84\xcf\x8d\xcf\x88\xce\xbf\xcf\x82",
                        blank=True,
                    ),
                ),
                (
                    "gis_mpoly",
                    django.contrib.gis.db.models.fields.MultiPolygonField(
                        srid=4326,
                        null=True,
                        verbose_name=b"\xce\x93\xce\xb5\xcf\x89\xce\xbc\xce\xb5\xcf\x84\xcf\x81\xce\xaf\xce\xb1 \xcf\x80\xce\xbf\xce\xbb\xcf\x85\xce\xb3\xcf\x8e\xce\xbd\xcf\x89\xce\xbd",
                        blank=True,
                    ),
                ),
                (
                    "abandon",
                    models.ForeignKey(
                        blank=True,
                        to="naturebank.AbandonmentOption",
                        help_text=b"\xce\x95\xcf\x80\xce\xaf\xcf\x80\xce\xb5\xce\xb4\xce\xb1 \xce\xb5\xce\xb3\xce\xba\xce\xb1\xcf\x84\xce\xac\xce\xbb\xce\xb5\xce\xb9\xcf\x88\xce\xb7\xcf\x82 \xce\xbf\xce\xb9\xce\xba\xce\xb9\xcf\x83\xce\xbc\xcf\x8e\xce\xbd",
                        null=True,
                        verbose_name=b"\xce\x95\xce\xb3\xce\xba\xce\xb1\xcf\x84\xce\xac\xce\xbb\xce\xb5\xce\xb9\xcf\x88\xce\xb7 \xce\xbf\xce\xb9\xce\xba\xce\xb9\xcf\x83\xce\xbc\xcf\x8e\xce\xbd",
                    ),
                ),
            ],
            options={
                "ordering": ["site_name_gr"],
                "verbose_name": "\u0392\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03c2",
                "verbose_name_plural": "\u0392\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03b9",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="BiotopeCategoryOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xce\xae \xcf\x83\xcf\x8d\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xb7 \xcf\x80\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x84\xce\xb7\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1\xcf\x82",
                        max_length=255,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1 \u03c4\u03cc\u03c0\u03bf\u03c5",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03c4\u03bf\u03c0\u03af\u03c9\u03bd",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="BiotopeImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text=b"\xce\x91\xcf\x81\xcf\x87\xce\xb5\xce\xaf\xce\xbf \xce\xb5\xce\xb9\xce\xba\xcf\x8c\xce\xbd\xce\xb1\xcf\x82",
                        upload_to=b"SitesPhotos/",
                        verbose_name="\u0395\u03b9\u03ba\u03cc\u03bd\u03b1",
                    ),
                ),
                (
                    "descr",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x8d\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xb7 \xcf\x80\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x86\xcf\x89\xcf\x84\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1\xcf\x82",
                        max_length=80,
                        verbose_name="\u03a0\u03b5\u03c1\u03b9\u03b3\u03c1\u03b1\u03c6\u03ae",
                        blank=True,
                    ),
                ),
                (
                    "order",
                    models.IntegerField(
                        help_text=b"\xce\xa3\xce\xb5\xce\xb9\xcf\x81\xce\xac \xce\xb5\xce\xbc\xcf\x86\xce\xac\xce\xbd\xce\xb9\xcf\x83\xce\xb7\xcf\x82 \xcf\x86\xcf\x89\xcf\x84\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1\xcf\x82",
                        null=True,
                        verbose_name="\u03a3\u03b5\u03b9\u03c1\u03ac",
                        blank=True,
                    ),
                ),
                (
                    "remarks",
                    models.TextField(
                        help_text=b"\xce\xa3\xcf\x87\xcf\x8c\xce\xbb\xce\xb9\xce\xb1 \xce\xb3\xce\xb9\xce\xb1 \xcf\x84\xce\xb7\xce\xbd \xce\xb5\xce\xb9\xce\xba\xcf\x8c\xce\xbd\xce\xb1",
                        verbose_name="\u03a3\u03c7\u03cc\u03bb\u03b9\u03b1",
                        blank=True,
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        help_text=b"\xce\x94\xce\xb5\xce\xaf\xce\xb3\xce\xbc\xce\xb1 (thumbnail) \xce\xb5\xce\xb9\xce\xba\xcf\x8c\xce\xbd\xce\xb1\xcf\x82",
                        verbose_name="\u0395\u03b9\u03ba\u03cc\u03bd\u03b1 \u03c0\u03c1\u03bf\u03b5\u03c0\u03b9\u03c3\u03ba\u03cc\u03c0\u03b9\u03c3\u03b7\u03c2",
                        editable=False,
                        upload_to=b"SitesPhotos/thumbs/",
                    ),
                ),
                (
                    "biotope",
                    models.ForeignKey(
                        verbose_name="\u03a4\u03cc\u03c0\u03bf\u03c2",
                        to="naturebank.Biotope",
                        help_text=b"\xce\x95\xce\xbe\xcf\x89\xcf\x84\xce\xb5\xcf\x81\xce\xb9\xce\xba\xce\xae \xce\xb1\xce\xbd\xce\xb1\xcf\x86\xce\xbf\xcf\x81\xce\xac \xcf\x83\xce\xb5 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf",
                    ),
                ),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="ClimateOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xce\xba\xce\xbb\xce\xb9\xce\xbc\xce\xb1\xcf\x84\xce\xb9\xce\xba\xce\xbf\xcf\x8d \xcf\x84\xcf\x8d\xcf\x80\xce\xbf\xcf\x85",
                        unique=True,
                        max_length=30,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8d\xcf\x80\xce\xbf\xcf\x85 \xce\xba\xce\xbb\xce\xaf\xce\xbc\xce\xb1\xcf\x84\xce\xbf\xcf\x82",
                        max_length=390,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u03a4\u03cd\u03c0\u03bf\u03c2 \u03ba\u03bb\u03af\u03bc\u03b1\u03c4\u03bf\u03c2",
                "verbose_name_plural": "\u03a4\u03cd\u03c0\u03bf\u03b9 \u03ba\u03bb\u03af\u03bc\u03b1\u03c4\u03bf\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="ConditionOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xb2\xce\xb9\xcf\x8c\xcf\x84\xce\xbf\xcf\x80\xce\xbf\xcf\x85",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03ac\u03c3\u03c4\u03b1\u03c3\u03b7 \u03b2\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03c5",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b1\u03c3\u03c4\u03ac\u03c3\u03b5\u03b9\u03c2 \u03b2\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03c5",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="ConservationOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xcf\x80\xcf\x81\xce\xbf\xcf\x84\xce\xb5\xcf\x81\xce\xb1\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1\xcf\x82 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u03a0\u03c1\u03bf\u03c4\u03b5\u03c1\u03b1\u03b9\u03cc\u03c4\u03b7\u03c4\u03b1 \u03c0\u03c1\u03bf\u03c3\u03c4\u03b1\u03c3\u03af\u03b1\u03c2",
                "verbose_name_plural": "\u03a0\u03c1\u03bf\u03c4\u03b5\u03c1\u03b1\u03b9\u03cc\u03c4\u03b7\u03c4\u03b5\u03c2 \u03c0\u03c1\u03bf\u03c3\u03c4\u03b1\u03c3\u03af\u03b1\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="CulturalValueOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xb1\xce\xb9\xcf\x83\xce\xb8\xce\xb7\xcf\x84\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbe\xce\xaf\xce\xb1\xcf\x82",
                        unique=True,
                        max_length=30,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xb1\xce\xb9\xcf\x83\xce\xb8\xce\xb7\xcf\x84\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbe\xce\xaf\xce\xb1\xcf\x82",
                        max_length=390,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u0391\u03b9\u03c3\u03b8\u03b7\u03c4\u03b9\u03ba\u03ae \u03b1\u03be\u03af\u03b1",
                "verbose_name_plural": "\u0391\u03b9\u03c3\u03b8\u03b7\u03c4\u03b9\u03ba\u03ad\u03c2 \u03b1\u03be\u03af\u03b5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="DesignationOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xce\xb4\xce\xb9\xce\xbf\xcf\x81\xce\xb9\xcf\x83\xce\xbc\xce\xbf\xcf\x8d \xce\xad\xce\xbd\xcf\x84\xce\xb1\xce\xbe\xce\xb7\xcf\x82 \xcf\x83\xce\xb5 \xce\xb8\xce\xb5\xcf\x83\xce\xbc\xce\xb9\xce\xba\xcf\x8c \xcf\x80\xce\xbb\xce\xb1\xce\xaf\xcf\x83\xce\xb9\xce\xbf",
                        unique=True,
                        max_length=30,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8d\xcf\x80\xce\xbf\xcf\x85 \xce\xad\xce\xbd\xcf\x84\xce\xb1\xce\xbe\xce\xb7\xcf\x82 \xcf\x83\xce\xb5 \xce\xb8\xce\xb5\xcf\x83\xce\xbc\xce\xb9\xce\xba\xcf\x8c \xcf\x80\xce\xbb\xce\xb1\xce\xaf\xcf\x83\xce\xb9\xce\xbf",
                        max_length=390,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1 \u03ad\u03bd\u03c4\u03b1\u03be\u03b7\u03c2",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03ad\u03bd\u03c4\u03b1\u03be\u03b7\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="EcologicalValueOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xbf\xce\xb9\xce\xba\xce\xbf\xce\xbb\xce\xbf\xce\xb3\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbe\xce\xaf\xce\xb1\xcf\x82",
                        unique=True,
                        max_length=30,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xbf\xce\xb9\xce\xba\xce\xbf\xce\xbb\xce\xbf\xce\xb3\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbe\xce\xaf\xce\xb1\xcf\x82",
                        max_length=390,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039f\u03b9\u03ba\u03bf\u03bb\u03bf\u03b3\u03b9\u03ba\u03ae \u03b1\u03be\u03af\u03b1",
                "verbose_name_plural": "\u039f\u03b9\u03ba\u03bf\u03bb\u03bf\u03b3\u03b9\u03ba\u03ad\u03c2 \u03b1\u03be\u03af\u03b5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="GeoCodeOption",
            fields=[
                (
                    "code",
                    models.CommaSeparatedIntegerField(
                        max_length=10, serialize=False, primary_key=True
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xb3\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xce\xae\xcf\x82 \xcf\x80\xce\xb5\xcf\x81\xce\xb9\xce\xbf\xcf\x87\xce\xae\xcf\x82",
                        max_length=300,
                        blank=True,
                    ),
                ),
                (
                    "name_eng",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xb3\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xce\xae\xcf\x82 \xcf\x80\xce\xb5\xcf\x81\xce\xb9\xce\xbf\xcf\x87\xce\xae\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name", "name_eng"],
                "verbose_name": "\u0393\u03b5\u03c9\u03b3\u03c1\u03b1\u03c6\u03b9\u03ba\u03ae \u03b5\u03bd\u03cc\u03c4\u03b7\u03c4\u03b1",
                "verbose_name_plural": "\u0393\u03b5\u03c9\u03b3\u03c1\u03b1\u03c6\u03b9\u03ba\u03ad\u03c2 \u03b5\u03bd\u03cc\u03c4\u03b7\u03c4\u03b5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="HabitationOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xcf\x89\xce\xbd \xcf\x87\xce\xb1\xcf\x81\xce\xb1\xce\xba\xcf\x84\xce\xb7\xcf\x81\xce\xb9\xcf\x83\xcf\x84\xce\xb9\xce\xba\xcf\x8e\xce\xbd \xce\xb5\xce\xbd\xce\xb4\xce\xb9\xce\xb1\xce\xb9\xcf\x84\xce\xb7\xce\xbc\xce\xac\xcf\x84\xcf\x89\xce\xbd",
                        unique=True,
                        max_length=30,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xbd\xce\xb4\xce\xb9\xce\xb1\xce\xb9\xcf\x84\xce\xae\xce\xbc\xce\xb1\xcf\x84\xce\xbf\xcf\x82",
                        max_length=390,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1 \u03b5\u03bd\u03b4\u03b9\u03b1\u03b9\u03c4\u03ae\u03bc\u03b1\u03c4\u03bf\u03c2",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03b5\u03bd\u03b4\u03b9\u03b1\u03b9\u03c4\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="HumanActivityOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xb1\xce\xbd\xce\xb8\xcf\x81\xcf\x8e\xcf\x80\xce\xb9\xce\xbd\xce\xb7\xcf\x82 \xce\xb4\xcf\x81\xce\xb1\xcf\x83\xcf\x84\xce\xb7\xcf\x81\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1\xcf\x82",
                        unique=True,
                        max_length=30,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xb1\xce\xbd\xce\xb8\xcf\x81\xcf\x8e\xcf\x80\xce\xb9\xce\xbd\xce\xb7\xcf\x82 \xce\xb4\xcf\x81\xce\xb1\xcf\x83\xcf\x84\xce\xb7\xcf\x81\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1\xcf\x82",
                        max_length=390,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u0391\u03bd\u03b8\u03c1\u03ce\u03c0\u03b9\u03bd\u03b7\u03c2 \u03b4\u03c1\u03b1\u03c3\u03c4\u03b7\u03c1\u03b9\u03cc\u03c4\u03b7\u03c4\u03b1\u03c2",
                "verbose_name_plural": "\u0391\u03bd\u03b8\u03c1\u03ce\u03c0\u03b9\u03bd\u03b5\u03c2 \u03b4\u03c1\u03b1\u03c3\u03c4\u03b7\u03c1\u03b9\u03cc\u03c4\u03b7\u03c4\u03b5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="KnowledgeOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xb3\xce\xbd\xcf\x8e\xcf\x83\xce\xb7\xcf\x82",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03ac\u03c3\u03c4\u03b1\u03c3\u03b7 \u03b3\u03bd\u03ce\u03c3\u03b7\u03c2 \u03b2\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03c5",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b1\u03c3\u03c4\u03ac\u03c3\u03b5\u03b9\u03c2 \u03b3\u03bd\u03ce\u03c3\u03b7\u03c2 \u03b2\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03c5",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="OwnerOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xb2\xce\xb9\xcf\x8c\xcf\x84\xce\xbf\xcf\x80\xce\xbf\xcf\x85",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1 \u03b9\u03b4\u03b9\u03bf\u03ba\u03c4\u03b7\u03c3\u03af\u03b1\u03c2 \u03c4\u03cc\u03c0\u03bf\u03c5",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03b9\u03b4\u03b9\u03bf\u03ba\u03c4\u03b7\u03c3\u03af\u03b1\u03c2 \u03c4\u03cc\u03c0\u03bf\u03c5",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Settlement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9f\xce\xbd\xce\xbf\xce\xbc\xce\xb1\xcf\x83\xce\xaf\xce\xb1 \xce\xbf\xce\xb9\xce\xba\xce\xb9\xcf\x83\xce\xbc\xce\xbf\xcf\x8d",
                        max_length=50,
                        blank=True,
                    ),
                ),
                (
                    "point",
                    django.contrib.gis.db.models.fields.PointField(
                        srid=4326, null=True, blank=True
                    ),
                ),
                (
                    "area",
                    models.FloatField(
                        null=True,
                        verbose_name=b"\xce\x95\xcf\x80\xce\xb9\xcf\x86\xce\xac\xce\xbd\xce\xb5\xce\xb9\xce\xb1 m\xc2\xb2",
                        blank=True,
                    ),
                ),
                (
                    "perimeter",
                    models.FloatField(
                        null=True,
                        verbose_name=b"\xce\xa0\xce\xb5\xcf\x81\xce\xaf\xce\xbc\xce\xb5\xcf\x84\xcf\x81\xce\xbf\xcf\x82 m",
                        blank=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "\u039f\u03b9\u03ba\u03b9\u03c3\u03bc\u03cc\u03c2",
                "verbose_name_plural": "\u039f\u03b9\u03ba\u03b9\u03c3\u03bc\u03bf\u03af",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SiteTypeOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8d\xcf\x80\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        unique=True,
                        max_length=30,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8d\xcf\x80\xce\xbf\xcf\x85",
                        max_length=390,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u03a4\u03cd\u03c0\u03bf\u03c2 \u03c4\u03cc\u03c0\u03bf\u03c5",
                "verbose_name_plural": "\u03a4\u03cd\u03c0\u03bf\u03b9 \u03c4\u03cc\u03c0\u03c9\u03bd",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SocialReactionOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xce\xba\xce\xbf\xce\xb9\xce\xbd\xcf\x89\xce\xbd\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbd\xcf\x84\xce\xaf\xce\xb4\xcf\x81\xce\xb1\xcf\x83\xce\xb7\xcf\x82",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03bf\u03b9\u03bd\u03c9\u03bd\u03b9\u03ba\u03ae \u03b1\u03bd\u03c4\u03af\u03b4\u03c1\u03b1\u03c3\u03b7",
                "verbose_name_plural": "\u039a\u03bf\u03b9\u03bd\u03c9\u03bd\u03b9\u03ba\u03ad\u03c2 \u03b1\u03bd\u03c4\u03b9\u03b4\u03c1\u03ac\u03c3\u03b5\u03b9\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SocialValueOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xba\xce\xbf\xce\xb9\xce\xbd\xcf\x89\xce\xbd\xce\xb9\xce\xba\xce\xbf\xce\xbf\xce\xb9\xce\xba\xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb9\xce\xba\xce\xae\xcf\x82/\xcf\x80\xce\xbf\xce\xbb\xce\xb9\xcf\x84\xce\xb9\xcf\x83\xcf\x84\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbe\xce\xaf\xce\xb1\xcf\x82",
                        unique=True,
                        max_length=30,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xba\xce\xbf\xce\xb9\xce\xbd\xcf\x89\xce\xbd\xce\xb9\xce\xba\xce\xbf\xce\xbf\xce\xb9\xce\xba\xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb9\xce\xba\xce\xae\xcf\x82/\xcf\x80\xce\xbf\xce\xbb\xce\xb9\xcf\x84\xce\xb9\xcf\x83\xcf\x84\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbe\xce\xaf\xce\xb1\xcf\x82",
                        max_length=390,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03bf\u03b9\u03bd/\u03c0\u03bf\u03bb\u03b9\u03c4\u03b9\u03c3\u03c4\u03b9\u03ba\u03ae \u03b1\u03be\u03af\u03b1",
                "verbose_name_plural": "\u039a\u03bf\u03b9\u03bd/\u03c0\u03bf\u03bb\u03b9\u03c4\u03b9\u03c3\u03c4\u03b9\u03ba\u03ad\u03c2 \u03b1\u03be\u03af\u03b5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Species",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "species_code",
                    models.IntegerField(
                        help_text=b"\xce\x9a\xcf\x89\xce\xb4\xce\xb9\xce\xba\xcf\x8c\xcf\x82 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                        unique=True,
                        verbose_name="\u039a\u03c9\u03b4\u03b9\u03ba\u03cc\u03c2 \u0395\u03af\u03b4\u03bf\u03c5\u03c2",
                    ),
                ),
                (
                    "species_name",
                    models.CharField(
                        help_text=b"\xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xae \xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb1\xcf\x83\xce\xaf\xce\xb1 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                        max_length=720,
                        verbose_name="\u038c\u03bd\u03bf\u03bc\u03b1 \u0395\u03af\u03b4\u03bf\u03c5\u03c2 (\u0391\u03b3\u03b3\u03bb\u03b9\u03ba\u03ac)",
                        blank=True,
                    ),
                ),
                (
                    "sub_species",
                    models.CharField(
                        help_text=b"\xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xae \xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb1\xcf\x83\xce\xaf\xce\xb1 \xcf\x85\xcf\x80\xce\xbf\xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                        max_length=720,
                        verbose_name="\u038c\u03bd\u03bf\u03bc\u03b1 \u03a5\u03c0\u03bf\u03b5\u03af\u03b4\u03bf\u03c5\u03c2 (\u0391\u03b3\u03b3\u03bb\u03b9\u03ba\u03ac)",
                        blank=True,
                    ),
                ),
                (
                    "other_names",
                    models.CharField(
                        help_text=b"\xce\x86\xce\xbb\xce\xbb\xce\xb5\xcf\x82 \xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb1\xcf\x83\xce\xaf\xce\xb5\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xaf\xce\xb4\xce\xb9\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                        max_length=960,
                        verbose_name="\u0386\u03bb\u03bb\u03b5\u03c2 \u039f\u03bd\u03bf\u03bc\u03b1\u03c3\u03af\u03b5\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "species_name_gr",
                    models.CharField(
                        help_text=b"\xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xae \xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb1\xcf\x83\xce\xaf\xce\xb1 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                        max_length=720,
                        verbose_name="\u038c\u03bd\u03bf\u03bc\u03b1 \u0395\u03af\u03b4\u03bf\u03c5\u03c2 (\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac)",
                        blank=True,
                    ),
                ),
                (
                    "habitat",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x84\xce\xbf\xce\xb9\xcf\x87\xce\xb5\xce\xaf\xce\xb1 \xcf\x83\xcf\x87\xce\xb5\xcf\x84\xce\xb9\xce\xba\xce\xac \xce\xbc\xce\xb5 \xcf\x84\xce\xb1 \xce\xb5\xce\xbd\xce\xb4\xce\xb9\xce\xb1\xce\xb9\xcf\x84\xce\xae\xce\xbc\xce\xb1\xcf\x84\xce\xb1",
                        max_length=720,
                        verbose_name="\u0395\u03bd\u03b4\u03b9\u03b1\u03b9\u03c4\u03ae\u03bc\u03b1\u03c4\u03b1",
                        blank=True,
                    ),
                ),
                (
                    "expansion",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x84\xce\xbf\xce\xb9\xcf\x87\xce\xb5\xce\xaf\xce\xb1 \xce\xb5\xce\xbe\xce\xac\xcf\x80\xce\xbb\xcf\x89\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                        max_length=960,
                        verbose_name="\u0395\u03be\u03ac\u03c0\u03bb\u03c9\u03c3\u03b7",
                        blank=True,
                    ),
                ),
                (
                    "origin",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x84\xce\xbf\xce\xb9\xcf\x87\xce\xb5\xce\xaf\xce\xb1 \xcf\x80\xcf\x81\xce\xbf\xce\xad\xce\xbb\xce\xb5\xcf\x85\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                        max_length=18,
                        verbose_name="\u03a0\u03c1\u03bf\u03ad\u03bb\u03b5\u03c5\u03c3\u03b7",
                        blank=True,
                    ),
                ),
                (
                    "creation_date",
                    models.DateField(
                        help_text=b"\xce\x97\xce\xbc\xce\xb5\xcf\x81\xce\xbf\xce\xbc\xce\xb7\xce\xbd\xce\xaf\xce\xb1 \xcf\x80\xcf\x81\xcf\x8e\xcf\x84\xce\xb7\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xb1\xcf\x87\xcf\x8e\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82",
                        null=True,
                        verbose_name="\u0397\u03bc/\u03bd\u03af\u03b1 \u03a0\u03c1\u03ce\u03c4\u03b7\u03c2 \u039a\u03b1\u03c4\u03b1\u03c7\u03ce\u03c1\u03b7\u03c3\u03b7\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "update_date",
                    models.DateField(
                        help_text=b"\xce\x97\xce\xbc\xce\xb5\xcf\x81\xce\xbf\xce\xbc\xce\xb7\xce\xbd\xce\xaf\xce\xb1 \xcf\x84\xce\xb5\xce\xbb\xce\xb5\xcf\x85\xcf\x84\xce\xb1\xce\xaf\xce\xb1\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xb1\xcf\x87\xcf\x8e\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82",
                        null=True,
                        verbose_name="\u0397\u03bc/\u03bd\u03af\u03b1 \u03a4\u03b5\u03bb\u03b5\u03c5\u03c4\u03b1\u03af\u03b1\u03c2 \u039a\u03b1\u03c4\u03b1\u03c7\u03ce\u03c1\u03b7\u03c3\u03b7\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "respondent",
                    models.TextField(
                        help_text=b"\xce\xa3\xcf\x84\xce\xbf\xce\xb9\xcf\x87\xce\xb5\xce\xaf\xce\xb1 \xce\xba\xce\xb1\xcf\x84\xce\xb1\xcf\x87\xcf\x89\xcf\x81\xce\xb7\xcf\x84\xce\xae",
                        verbose_name="\u03a3\u03c4\u03bf\u03b9\u03c7\u03b5\u03af\u03b1 \u039a\u03b1\u03c4\u03b1\u03c7\u03c9\u03c1\u03b7\u03c4\u03ae",
                        blank=True,
                    ),
                ),
                (
                    "measures_take",
                    models.TextField(
                        help_text=b"\xce\x9c\xce\xad\xcf\x84\xcf\x81\xce\xb1 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82 \xcf\x80\xce\xbf\xcf\x85 \xce\xad\xcf\x87\xce\xbf\xcf\x85\xce\xbd \xce\xbb\xce\xb7\xcf\x86\xce\xb8\xce\xb5\xce\xaf.",
                        verbose_name="\u039b\u03b7\u03c6\u03b8\u03ad\u03bd\u03c4\u03b1 \u039c\u03ad\u03c4\u03c1\u03b1",
                        blank=True,
                    ),
                ),
                (
                    "measures_need",
                    models.TextField(
                        help_text=b"\xce\x9c\xce\xad\xcf\x84\xcf\x81\xce\xb1 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82 \xcf\x80\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xce\xb1\xce\xbd\xce\xb1\xce\xb3\xce\xba\xce\xb1\xce\xaf\xce\xb1.",
                        verbose_name="\u0391\u03bd\u03b1\u03b3\u03ba\u03b1\u03af\u03b1 \u039c\u03ad\u03c4\u03c1\u03b1",
                        blank=True,
                    ),
                ),
                (
                    "threat_hunt",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xbf \xce\xba\xcf\x85\xce\xbd\xce\xae\xce\xb3\xce\xb9",
                        verbose_name="\u039a\u03c5\u03bd\u03ae\u03b3\u03b9",
                    ),
                ),
                (
                    "threat_fish",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb1\xce\xbb\xce\xb9\xce\xb5\xce\xaf\xce\xb1",
                        verbose_name="\u0391\u03bb\u03b9\u03b5\u03af\u03b1",
                    ),
                ),
                (
                    "threat_coll",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x83\xcf\x85\xce\xbb\xce\xbb\xce\xbf\xce\xb3\xce\xae",
                        verbose_name="\u03a3\u03c5\u03bb\u03bb\u03bf\u03b3\u03ae",
                    ),
                ),
                (
                    "threat_fore",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x85\xce\xbb\xce\xbf\xcf\x84\xce\xbf\xce\xbc\xce\xaf\xce\xb1",
                        verbose_name="\u03a5\u03bb\u03bf\u03c4\u03bf\u03bc\u03af\u03b1",
                    ),
                ),
                (
                    "threat_graz",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb2\xce\xbf\xcf\x83\xce\xba\xce\xae",
                        verbose_name="\u0392\u03bf\u03c3\u03ba\u03ae",
                    ),
                ),
                (
                    "threat_poll",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x81\xcf\x8d\xcf\x80\xce\xb1\xce\xbd\xcf\x83\xce\xb7",
                        verbose_name="\u03a1\u03cd\u03c0\u03b1\u03bd\u03c3\u03b7",
                    ),
                ),
                (
                    "threat_cult",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xba\xce\xb1\xce\xbb\xce\xbb\xce\xb9\xce\xad\xcf\x81\xce\xb3\xce\xb5\xce\xb9\xce\xb1",
                        verbose_name="\u039a\u03b1\u03bb\u03bb\u03b9\u03ad\u03c1\u03b3\u03b5\u03b9\u03b1",
                    ),
                ),
                (
                    "threat_tour",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xbf\xce\xbd \xcf\x84\xce\xbf\xcf\x85\xcf\x81\xce\xb9\xcf\x83\xce\xbc\xcf\x8c",
                        verbose_name="\u03a4\u03bf\u03c5\u03c1\u03b9\u03c3\u03bc\u03cc\u03c2",
                    ),
                ),
                (
                    "threat_road",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb4\xce\xb9\xce\xac\xce\xbd\xce\xbf\xce\xb9\xce\xbe\xce\xb7 \xce\xb4\xcf\x81\xcf\x8c\xce\xbc\xcf\x89\xce\xbd",
                        verbose_name="\u0394\u03b9\u03ac\u03bd\u03bf\u03b9\u03be\u03b7 \u0394\u03c1\u03cc\u03bc\u03c9\u03bd",
                    ),
                ),
                (
                    "threat_buil",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb4\xcf\x8c\xce\xbc\xce\xb7\xcf\x83\xce\xb7",
                        verbose_name="\u0394\u03cc\u03bc\u03b7\u03c3\u03b7",
                    ),
                ),
                (
                    "threat_drai",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xce\xb1\xcf\x80\xce\xbf\xce\xbe\xce\xae\xcf\x81\xce\xb1\xce\xbd\xcf\x83\xce\xb7",
                        verbose_name="\u0391\u03c0\u03bf\u03be\u03ae\u03c1\u03b1\u03bd\u03c3\u03b7",
                    ),
                ),
                (
                    "threat_eutr",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xbf\xce\xbd \xce\xb5\xcf\x85\xcf\x84\xcf\x81\xce\xbf\xcf\x86\xce\xb9\xcf\x83\xce\xbc\xcf\x8c",
                        verbose_name="\u0395\u03c5\u03c4\u03c1\u03bf\u03c6\u03b9\u03c3\u03bc\u03cc\u03c2",
                    ),
                ),
                (
                    "threat_pest",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x91\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb1 \xcf\x86\xcf\x85\xcf\x84\xce\xbf\xcf\x86\xce\xac\xcf\x81\xce\xbc\xce\xb1\xce\xba\xce\xb1",
                        verbose_name="\u03a6\u03c5\u03c4\u03bf\u03c6\u03ac\u03c1\u03bc\u03b1\u03ba\u03b1",
                    ),
                ),
                (
                    "threat_other",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x86\xce\xbb\xce\xbb\xce\xb5\xcf\x82 \xce\xb1\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xad\xcf\x82",
                        verbose_name="\u0386\u03bb\u03bb\u03b5\u03c2 \u0391\u03c0\u03b5\u03b9\u03bb\u03ad\u03c2",
                    ),
                ),
                (
                    "threat",
                    models.TextField(
                        help_text=b"\xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xae \xce\xb1\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xcf\x8e\xce\xbd \xce\xba\xce\xb1\xce\xb9 \xce\xba\xce\xb9\xce\xbd\xce\xb4\xcf\x8d\xce\xbd\xcf\x89\xce\xbd",
                        verbose_name="\u03a3\u03c7\u03cc\u03bb\u03b9\u03b1",
                        blank=True,
                    ),
                ),
                (
                    "category_ende",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xce\xb5\xce\xbd\xce\xb4\xce\xb7\xce\xbc\xce\xb9\xce\xba\xcf\x8c",
                        verbose_name="\u0395\u03bd\u03b4\u03b7\u03bc\u03b9\u03ba\u03cc",
                    ),
                ),
                (
                    "category_migr",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xce\xbc\xce\xb5\xcf\x84\xce\xb1\xce\xbd\xce\xb1\xcf\x83\xcf\x84\xce\xb5\xcf\x85\xcf\x84\xce\xb9\xce\xba\xcf\x8c",
                        verbose_name="\u039c\u03b5\u03c4\u03b1\u03bd\u03b1\u03c3\u03c4\u03b5\u03c5\u03c4\u03b9\u03ba\u03cc",
                    ),
                ),
                (
                    "category_bree",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xce\xb1\xce\xbd\xce\xb1\xcf\x80\xce\xb1\xcf\x81\xce\xb1\xce\xb3\xcf\x8c\xce\xbc\xce\xb5\xce\xbd\xce\xbf",
                        verbose_name="\u0391\u03bd\u03b1\u03c0\u03b1\u03c1\u03b1\u03b3\u03cc\u03bc\u03b5\u03bd\u03bf",
                    ),
                ),
                (
                    "category_resi",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xbf\xce\xb9\xce\xba\xce\xb5\xce\xaf \xce\xbc\xcf\x8c\xce\xbd\xce\xb9\xce\xbc\xce\xb1",
                        verbose_name="\u039c\u03cc\u03bd\u03b9\u03bc\u03bf\u03c2 \u039a\u03ac\u03c4\u03bf\u03b9\u03ba\u03bf\u03c2",
                    ),
                ),
                (
                    "category_intr",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xce\xb5\xce\xb9\xcf\x83\xce\xb1\xcf\x87\xce\xb8\xce\xad\xce\xbd",
                        verbose_name="\u0395\u03b9\u03c3\u03b1\u03c7\u03b8\u03ad\u03bd",
                    ),
                ),
                (
                    "category",
                    models.TextField(
                        help_text=b"\xce\xa3\xcf\x87\xcf\x8c\xce\xbb\xce\xb9\xce\xb1 \xce\xb3\xce\xb9\xce\xb1 \xcf\x84\xce\xb1 \xce\xb3\xce\xbd\xcf\x89\xcf\x81\xce\xaf\xcf\x83\xce\xbc\xce\xb1\xcf\x84\xce\xb1",
                        verbose_name="\u03a3\u03c7\u03cc\u03bb\u03b9\u03b1",
                        blank=True,
                    ),
                ),
                (
                    "exploit_hunt",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xba\xce\xbc\xce\xb5\xcf\x84\xce\xac\xce\xbb\xce\xbb\xce\xb5\xcf\x85\xcf\x83\xce\xb7 \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xbf \xce\xba\xcf\x85\xce\xbd\xce\xae\xce\xb3\xce\xb9",
                        verbose_name="\u039a\u03c5\u03bd\u03ae\u03b3\u03b9",
                    ),
                ),
                (
                    "exploit_fish",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xba\xce\xbc\xce\xb5\xcf\x84\xce\xac\xce\xbb\xce\xbb\xce\xb5\xcf\x85\xcf\x83\xce\xb7 \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xbf \xce\xb1\xce\xbb\xce\xb9\xce\xb5\xce\xaf\xce\xb1",
                        verbose_name="\u0391\u03bb\u03b9\u03b5\u03af\u03b1",
                    ),
                ),
                (
                    "exploit_coll",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xba\xce\xbc\xce\xb5\xcf\x84\xce\xac\xce\xbb\xce\xbb\xce\xb5\xcf\x85\xcf\x83\xce\xb7 \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7 \xcf\x83\xcf\x8d\xce\xbb\xce\xbb\xce\xbf\xce\xb3\xce\xb7",
                        verbose_name="\u03a3\u03c5\u03bb\u03bb\u03bf\u03b3\u03ae",
                    ),
                ),
                (
                    "exploit_logg",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xba\xce\xbc\xce\xb5\xcf\x84\xce\xac\xce\xbb\xce\xbb\xce\xb5\xcf\x85\xcf\x83\xce\xb7 \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7\xce\xbd \xcf\x85\xce\xbb\xce\xbf\xcf\x84\xce\xbf\xce\xbc\xce\xaf\xce\xb1",
                        verbose_name="\u03a5\u03bb\u03bf\u03c4\u03bf\u03bc\u03af\u03b1",
                    ),
                ),
                (
                    "exploit_graz",
                    models.BooleanField(
                        default=False,
                        help_text=b"\xce\x95\xce\xba\xce\xbc\xce\xb5\xcf\x84\xce\xac\xce\xbb\xce\xbb\xce\xb5\xcf\x85\xcf\x83\xce\xb7 \xce\xb1\xcf\x80\xcf\x8c \xcf\x84\xce\xb7 \xce\xb2\xce\xbf\xcf\x83\xce\xba\xce\xae",
                        verbose_name="\u0392\u03bf\u03c3\u03ba\u03ae",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        help_text=b"\xce\xa4\xce\xbf path \xcf\x80\xcf\x81\xce\xbf\xcf\x82 \xcf\x84\xce\xb7 \xcf\x86\xcf\x89\xcf\x84\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                        upload_to=b"SitesPhotos",
                        verbose_name="\u03a6\u03c9\u03c4\u03bf\u03b3\u03c1\u03b1\u03c6\u03af\u03b1",
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["species_name", "sub_species", "species_code"],
                "verbose_name_plural": "Species",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SpeciesBiotope",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abundance",
                    models.IntegerField(
                        help_text="\u0397 \u03b1\u03c6\u03b8\u03bf\u03bd\u03af\u03b1 \u03c4\u03bf\u03c5 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2 \u03c3\u03c4\u03bf \u03c3\u03c5\u03b3\u03ba\u03b5\u03ba\u03c1\u03b9\u03bc\u03ad\u03bd\u03bf \u03b2\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf",
                        null=True,
                        verbose_name="\u03a0\u03bb\u03b7\u03b8\u03c5\u03c3\u03bc\u03cc\u03c2",
                        blank=True,
                    ),
                ),
                (
                    "biotope",
                    models.ForeignKey(
                        verbose_name="\u03a4\u03cc\u03c0\u03bf\u03c2",
                        to="naturebank.Biotope",
                        help_text="\u0392\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03c2",
                    ),
                ),
                (
                    "species",
                    models.ForeignKey(
                        verbose_name="\u0395\u03af\u03b4\u03bf\u03c2",
                        to="naturebank.Species",
                        help_text="\u0395\u03af\u03b4\u03bf\u03c2 \u0396\u03ce\u03bf\u03c5/\u03a6\u03c5\u03c4\u03bf\u03cd",
                    ),
                ),
            ],
            options={
                "verbose_name": "\u03a3\u03c5\u03c3\u03c7\u03ad\u03c4\u03b9\u03c3\u03b7 \u0395\u03af\u03b4\u03bf\u03c5\u03c2 \u03bc\u03b5 \u0392\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf",
                "verbose_name_plural": "\u03a3\u03c5\u03c3\u03c7\u03b5\u03c4\u03af\u03c3\u03b5\u03b9\u03c2 \u0395\u03af\u03b4\u03bf\u03c5\u03c2 \u03bc\u03b5 \u0392\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SpeciesCategoryOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb1\xcf\x81\xcf\x87\xce\xb9\xce\xba\xce\xac \xcf\x84\xce\xb7\xcf\x82 \xcf\x83\xcf\x85\xce\xb3\xce\xba\xce\xb5\xce\xba\xcf\x81\xce\xb9\xce\xbc\xce\xad\xce\xbd\xce\xb7\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac",
                        unique=True,
                        max_length=24,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x97 \xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb1\xcf\x83\xce\xaf\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1 \u03c0\u03b1\u03bd\u03af\u03b4\u03b1\u03c2/\u03c7\u03bb\u03c9\u03c1\u03af\u03b4\u03b1\u03c2",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03c0\u03b1\u03bd\u03af\u03b4\u03b1\u03c2/\u03c7\u03bb\u03c9\u03c1\u03af\u03b4\u03b1\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SpeciesConservationOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb1\xcf\x81\xcf\x87\xce\xb9\xce\xba\xce\xac \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xcf\x80\xce\xb9\xcf\x80\xce\xad\xce\xb4\xce\xbf\xcf\x85 \xce\xb4\xce\xb9\xce\xb1\xcf\x84\xce\xae\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac",
                        unique=True,
                        max_length=24,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9f \xcf\x84\xce\xaf\xcf\x84\xce\xbb\xce\xbf\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xcf\x80\xce\xb9\xcf\x80\xce\xad\xce\xb4\xce\xbf\xcf\x85 \xce\xb4\xce\xb9\xce\xb1\xcf\x84\xce\xae\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u0395\u03c0\u03af\u03c0\u03b5\u03b4\u03bf \u03b4\u03b9\u03b1\u03c4\u03ae\u03c1\u03b7\u03c3\u03b7\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
                "verbose_name_plural": "\u0395\u03c0\u03af\u03c0\u03b5\u03b4\u03b1 \u03b4\u03b9\u03b1\u03c4\u03ae\u03c1\u03b7\u03c3\u03b7\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SpeciesConservationPriorityOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb1\xcf\x81\xcf\x87\xce\xb9\xce\xba\xce\xac \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xcf\x80\xce\xb9\xcf\x80\xce\xad\xce\xb4\xce\xbf\xcf\x85 \xcf\x80\xcf\x81\xce\xbf\xcf\x84\xce\xb5\xcf\x81\xce\xb1\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1\xcf\x82 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac",
                        unique=True,
                        max_length=24,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9f \xcf\x84\xce\xaf\xcf\x84\xce\xbb\xce\xbf\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xcf\x80\xce\xb9\xcf\x80\xce\xad\xce\xb4\xce\xbf\xcf\x85 \xcf\x80\xcf\x81\xce\xbf\xcf\x84\xce\xb5\xcf\x81\xce\xb1\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1\xcf\x82 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u03a0\u03c1\u03bf\u03c4\u03b5\u03c1\u03b1\u03b9\u03cc\u03c4\u03b7\u03c4\u03b1 \u03c0\u03c1\u03bf\u03c3\u03c4\u03b1\u03c3\u03af\u03b1\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
                "verbose_name_plural": "\u03a0\u03c1\u03bf\u03c4\u03b5\u03c1\u03b1\u03b9\u03cc\u03c4\u03b7\u03c4\u03b5\u03c2 \u03c0\u03c1\u03bf\u03c3\u03c4\u03b1\u03c3\u03af\u03b1\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SpeciesKnowledgeOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb1\xcf\x81\xcf\x87\xce\xb9\xce\xba\xce\xac \xcf\x84\xce\xbf\xcf\x85 \xcf\x83\xcf\x85\xce\xb3\xce\xba\xce\xb5\xce\xba\xcf\x81\xce\xb9\xce\xbc\xce\xad\xce\xbd\xce\xbf\xcf\x85 \xce\xb5\xcf\x80\xce\xb9\xcf\x80\xce\xad\xce\xb4\xce\xbf\xcf\x85 \xcf\x83\xcf\x84\xce\xb1 \xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac",
                        unique=True,
                        max_length=24,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9f \xcf\x84\xce\xaf\xcf\x84\xce\xbb\xce\xbf\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xcf\x80\xce\xb9\xcf\x80\xce\xad\xce\xb4\xce\xbf\xcf\x85 \xce\xb3\xce\xbd\xcf\x8e\xcf\x83\xce\xb7\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u0395\u03c0\u03af\u03c0\u03b5\u03b4\u03bf \u03b3\u03bd\u03ce\u03c3\u03b7\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
                "verbose_name_plural": "\u0395\u03c0\u03af\u03c0\u03b5\u03b4\u03b1 \u03b3\u03bd\u03ce\u03c3\u03b7\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SpeciesPlantKindOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb1\xcf\x81\xcf\x87\xce\xb9\xce\xba\xce\xac \xcf\x84\xce\xb7\xcf\x82 \xcf\x83\xcf\x85\xce\xb3\xce\xba\xce\xb5\xce\xba\xcf\x81\xce\xb9\xce\xbc\xce\xad\xce\xbd\xce\xb7\xcf\x82 \xcf\x85\xcf\x80\xce\xbf\xce\xba\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac",
                        unique=True,
                        max_length=24,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x97 \xce\xbf\xce\xbd\xce\xbf\xce\xbc\xce\xb1\xcf\x83\xce\xaf\xce\xb1 \xce\xb1\xcf\x85\xcf\x84\xce\xae\xcf\x82 \xcf\x84\xce\xb7\xcf\x82 \xce\xba\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1\xcf\x82 \xcf\x86\xcf\x85\xcf\x84\xcf\x8e\xce\xbd",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1 \u03c6\u03c5\u03c4\u03ce\u03bd",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03c6\u03c5\u03c4\u03ce\u03bd",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SpeciesProtectionOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb1\xcf\x81\xcf\x87\xce\xb9\xce\xba\xce\xac \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xcf\x80\xce\xb9\xcf\x80\xce\xad\xce\xb4\xce\xbf\xcf\x85 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac",
                        unique=True,
                        max_length=24,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9f \xcf\x84\xce\xaf\xcf\x84\xce\xbb\xce\xbf\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xcf\x80\xce\xb9\xcf\x80\xce\xad\xce\xb4\xce\xbf\xcf\x85 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u0395\u03c0\u03af\u03c0\u03b5\u03b4\u03bf \u03c0\u03c1\u03bf\u03c3\u03c4\u03b1\u03c3\u03af\u03b1\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
                "verbose_name_plural": "\u0395\u03c0\u03af\u03c0\u03b5\u03b4\u03b1 \u03c0\u03c1\u03bf\u03c3\u03c4\u03b1\u03c3\u03af\u03b1\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SpeciesRarityOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb1\xcf\x81\xcf\x87\xce\xb9\xce\xba\xce\xac \xcf\x84\xce\xbf\xcf\x85 \xce\xb2\xce\xb1\xce\xb8\xce\xbc\xce\xbf\xcf\x8d \xcf\x83\xcf\x80\xce\xb1\xce\xbd\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac",
                        unique=True,
                        max_length=24,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9f \xcf\x84\xce\xaf\xcf\x84\xce\xbb\xce\xbf\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb2\xce\xb1\xce\xb8\xce\xbc\xce\xbf\xcf\x8d \xcf\x83\xcf\x80\xce\xb1\xce\xbd\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u0392\u03b1\u03b8\u03bc\u03cc\u03c2 \u03c3\u03c0\u03b1\u03bd\u03b9\u03cc\u03c4\u03b7\u03c4\u03b1\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
                "verbose_name_plural": "\u0392\u03b1\u03b8\u03bc\u03bf\u03af \u03c3\u03c0\u03b1\u03bd\u03b9\u03cc\u03c4\u03b7\u03c4\u03b1\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="SpeciesTrendOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xb1 \xce\xb1\xcf\x81\xcf\x87\xce\xb9\xce\xba\xce\xac \xcf\x84\xce\xbf\xcf\x85 \xcf\x81\xcf\x85\xce\xb8\xce\xbc\xce\xbf\xcf\x8d \xce\xb1\xce\xbd\xce\xac\xcf\x80\xcf\x84\xcf\x85\xce\xbe\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x91\xce\xb3\xce\xb3\xce\xbb\xce\xb9\xce\xba\xce\xac",
                        unique=True,
                        max_length=24,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x9f \xcf\x84\xce\xaf\xcf\x84\xce\xbb\xce\xbf\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xcf\x81\xcf\x85\xce\xb8\xce\xbc\xce\xbf\xcf\x8d/\xcf\x84\xce\xac\xcf\x83\xce\xb7\xcf\x82 \xce\xb1\xce\xbd\xce\xac\xcf\x80\xcf\x84\xcf\x85\xce\xbe\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb1 \xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u03a1\u03c5\u03b8\u03bc\u03cc\u03c2 \u03b1\u03bd\u03ac\u03c0\u03c4\u03c5\u03be\u03b7\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
                "verbose_name_plural": "\u03a1\u03c5\u03b8\u03bc\u03bf\u03af \u03b1\u03bd\u03ac\u03c0\u03c4\u03c5\u03be\u03b7\u03c2 \u03b5\u03af\u03b4\u03bf\u03c5\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="TempDelete",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("gis_area", models.FloatField()),
                ("gis_perimeter", models.FloatField()),
                ("gis_sitecode", models.CharField(max_length=9)),
                (
                    "gis_mpoly",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
            options={
                "db_table": "temp_delete",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="ThreatOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "abbreviation",
                    models.CharField(
                        help_text=b"\xce\xa3\xcf\x85\xce\xbd\xcf\x84\xce\xbf\xce\xbc\xce\xbf\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xaf\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xb1\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae\xcf\x82",
                        unique=True,
                        max_length=30,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xbf \xcf\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xb7\xcf\x82 \xce\xb1\xcf\x80\xce\xb5\xce\xb9\xce\xbb\xce\xae\xcf\x82",
                        max_length=390,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1 \u03b1\u03c0\u03b5\u03b9\u03bb\u03ae\u03c2",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03b1\u03c0\u03b5\u03b9\u03bb\u03ce\u03bd",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="TrendOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\xa4\xce\xac\xcf\x83\xce\xb7 \xce\xba\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7\xcf\x82 \xce\xb2\xce\xb9\xcf\x8c\xcf\x84\xce\xbf\xcf\x80\xce\xbf\xcf\x85",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u03a4\u03ac\u03c3\u03b7 \u03ba\u03b1\u03c4\u03ac\u03c3\u03c4\u03b1\u03c3\u03b7\u03c2 \u03b2\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03c5",
                "verbose_name_plural": "\u03a4\u03ac\u03c3\u03b5\u03b9\u03c2 \u03ba\u03b1\u03c4\u03ac\u03c3\u03c4\u03b1\u03c3\u03b7\u03c2 \u03b2\u03b9\u03cc\u03c4\u03bf\u03c0\u03bf\u03c5",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="TrendPopOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text=b"\xce\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xcf\x84\xce\xac\xcf\x83\xce\xb7\xcf\x82 \xcf\x80\xce\xbb\xce\xb7\xce\xb8\xcf\x85\xcf\x83\xce\xbc\xce\xbf\xcf\x8d",
                        max_length=300,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1 \u03c4\u03ac\u03c3\u03b7\u03c2 \u03c0\u03bb\u03b7\u03b8\u03c5\u03c3\u03bc\u03bf\u03cd",
                "verbose_name_plural": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03c4\u03ac\u03c3\u03b7\u03c2 \u03c0\u03bb\u03b7\u03b8\u03c5\u03c3\u03bc\u03bf\u03cd",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="WideArea",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "wide_area_name",
                    models.CharField(
                        help_text=b"\xce\x8c\xce\xbd\xce\xbf\xce\xbc\xce\xb1 \xce\xb5\xcf\x85\xcf\x81\xcf\x8d\xcf\x84\xce\xb5\xcf\x81\xce\xb7\xcf\x82 \xce\xb3\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xce\xae\xcf\x82 \xcf\x80\xce\xb5\xcf\x81\xce\xb9\xce\xbf\xcf\x87\xce\xae\xcf\x82.",
                        max_length=150,
                        blank=True,
                    ),
                ),
            ],
            options={
                "ordering": ["wide_area_name"],
                "verbose_name": "\u0395\u03c5\u03c1\u03cd\u03c4\u03b5\u03c1\u03b7 \u03b3\u03b5\u03c9\u03b3\u03c1\u03b1\u03c6\u03b9\u03ba\u03ae \u03c0\u03b5\u03c1\u03b9\u03bf\u03c7\u03ae",
                "verbose_name_plural": "\u0395\u03c5\u03c1\u03cd\u03c4\u03b5\u03c1\u03b5\u03c2 \u03b3\u03b5\u03c9\u03b3\u03c1\u03b1\u03c6\u03b9\u03ba\u03ad\u03c2 \u03c0\u03b5\u03c1\u03b9\u03bf\u03c7\u03ad\u03c2",
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name="speciesbiotope",
            unique_together=set([("biotope", "species")]),
        ),
        migrations.AddField(
            model_name="species",
            name="conservation_bio",
            field=models.ForeignKey(
                related_name="species_conservation_bio_set",
                blank=True,
                to="naturebank.SpeciesConservationOption",
                help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xb4\xce\xb9\xce\xb1\xcf\x84\xce\xae\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb7\xce\xbd \xce\x92\xce\xb9\xcf\x8c\xcf\x83\xcf\x86\xce\xb1\xce\xb9\xcf\x81\xce\xb1",
                null=True,
                verbose_name="\u0392\u03b9\u03cc\u03c3\u03c6\u03b1\u03b9\u03c1\u03b1",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="conservation_eec",
            field=models.ForeignKey(
                related_name="species_conservation_eec_set",
                blank=True,
                to="naturebank.SpeciesConservationOption",
                help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xb4\xce\xb9\xce\xb1\xcf\x84\xce\xae\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb7\xce\xbd \xce\x95\xcf\x85\xcf\x81\xcf\x89\xcf\x80\xce\xb1\xce\xb9\xce\xba\xce\xae \xce\x88\xce\xbd\xcf\x89\xcf\x83\xce\xb7",
                null=True,
                verbose_name="\u0395\u03c5\u03c1\u03c9\u03c0\u03b1\u03ca\u03ba\u03ae \u0388\u03bd\u03c9\u03c3\u03b7",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="conservation_gr",
            field=models.ForeignKey(
                related_name="species_conservation_gr_set",
                blank=True,
                to="naturebank.SpeciesConservationOption",
                help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xce\xb4\xce\xb9\xce\xb1\xcf\x84\xce\xae\xcf\x81\xce\xb7\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb7\xce\xbd \xce\x95\xce\xbb\xce\xbb\xce\xac\xce\xb4\xce\xb1",
                null=True,
                verbose_name="\u0395\u03bb\u03bb\u03ac\u03b4\u03b1",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="conservation_prio",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.SpeciesConservationPriorityOption",
                help_text=b"\xce\xa0\xcf\x81\xce\xbf\xcf\x84\xce\xb5\xcf\x81\xce\xb1\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82",
                null=True,
                verbose_name="\u03a0\u03c1\u03bf\u03c4\u03b5\u03c1\u03b1\u03b9\u03cc\u03c4\u03b7\u03c4\u03b1 \u03a0\u03c1\u03bf\u03c3\u03c4\u03b1\u03c3\u03af\u03b1\u03c2",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="knowledge",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.SpeciesKnowledgeOption",
                help_text=b"\xce\xa4\xce\xbf \xce\xb5\xcf\x80\xce\xaf\xcf\x80\xce\xb5\xce\xb4\xce\xbf \xce\xb3\xce\xbd\xcf\x8e\xcf\x83\xce\xb7\xcf\x82 \xcf\x83\xcf\x84\xce\xbf \xcf\x83\xcf\x85\xce\xb3\xce\xba\xce\xb5\xce\xba\xcf\x81\xce\xb9\xce\xbc\xce\xad\xce\xbd\xce\xbf \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x82",
                null=True,
                verbose_name="\u0393\u03bd\u03ce\u03c3\u03b7",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="plant_kind",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.SpeciesPlantKindOption",
                help_text=b"\xce\xa5\xcf\x80\xce\xbf\xce\xba\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1 \xce\xb3\xce\xb9\xce\xb1 \xcf\x86\xcf\x85\xcf\x84\xcf\x8c (\xce\x91\xce\xbd \xce\xb4\xce\xb5\xce\xbd \xce\xb5\xce\xaf\xce\xbd\xce\xb1\xce\xb9 \xcf\x86\xcf\x85\xcf\x84\xcf\x8c \xcf\x80\xcf\x81\xce\xad\xcf\x80\xce\xb5\xce\xb9 \xce\xbd\xce\xb1 \xce\xb1\xcf\x86\xce\xb5\xce\xb8\xce\xb5\xce\xaf \xce\xba\xce\xb5\xce\xbd\xcf\x8c)",
                null=True,
                verbose_name=b"\xce\x9a\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1 \xce\xa6\xcf\x85\xcf\x84\xce\xbf\xcf\x8d",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="protection",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.SpeciesProtectionOption",
                help_text=b"\xce\x95\xcf\x80\xce\xaf\xcf\x80\xce\xb5\xce\xb4\xce\xbf \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                null=True,
                verbose_name="\u03a0\u03c1\u03bf\u03c3\u03c4\u03b1\u03c3\u03af\u03b1",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="rarity_bio",
            field=models.ForeignKey(
                related_name="species_rarity_bio_set",
                blank=True,
                to="naturebank.SpeciesRarityOption",
                help_text=b"\xce\xa3\xcf\x80\xce\xb1\xce\xbd\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb7\xce\xbd \xce\x92\xce\xb9\xcf\x8c\xcf\x83\xcf\x86\xce\xb1\xce\xb9\xcf\x81\xce\xb1",
                null=True,
                verbose_name="\u0392\u03b9\u03cc\u03c3\u03c6\u03b1\u03b9\u03c1\u03b1",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="rarity_eec",
            field=models.ForeignKey(
                related_name="species_rarity_eec_set",
                blank=True,
                to="naturebank.SpeciesRarityOption",
                help_text=b"\xce\xa3\xcf\x80\xce\xb1\xce\xbd\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb7\xce\xbd \xce\x95\xcf\x85\xcf\x81\xcf\x89\xcf\x80\xce\xb1\xce\xb9\xce\xba\xce\xae \xce\x88\xce\xbd\xcf\x89\xcf\x83\xce\xb7",
                null=True,
                verbose_name="\u0395\u03c5\u03c1\u03c9\u03c0\u03b1\u03ca\u03ba\u03ae \u0388\u03bd\u03c9\u03c3\u03b7",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="rarity_gr",
            field=models.ForeignKey(
                related_name="species_rarity_gr_set",
                blank=True,
                to="naturebank.SpeciesRarityOption",
                help_text=b"\xce\xa3\xcf\x80\xce\xb1\xce\xbd\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82 \xcf\x83\xcf\x84\xce\xb7\xce\xbd \xce\x95\xce\xbb\xce\xbb\xce\xac\xce\xb4\xce\xb1",
                null=True,
                verbose_name="\u0395\u03bb\u03bb\u03ac\u03b4\u03b1",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="species_category",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.SpeciesCategoryOption",
                help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1 \xcf\x87\xce\xbb\xcf\x89\xcf\x81\xce\xaf\xce\xb4\xce\xb1\xcf\x82/\xcf\x80\xce\xb1\xce\xbd\xce\xaf\xce\xb4\xce\xb1\xcf\x82 \xcf\x80\xce\xbf\xcf\x85 \xce\xb1\xce\xbd\xce\xae\xce\xba\xce\xb5\xce\xb9 \xcf\x84\xce\xbf \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x82.",
                null=True,
                verbose_name=b"\xce\x9a\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1 \xce\x95\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="species",
            name="trend",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.SpeciesTrendOption",
                help_text=b"\xce\x9f \xcf\x81\xcf\x85\xce\xb8\xce\xbc\xcf\x8c\xcf\x82 \xce\xb1\xce\xbd\xce\xac\xcf\x80\xcf\x84\xcf\x85\xce\xbe\xce\xb7\xcf\x82 \xcf\x84\xce\xbf\xcf\x85 \xce\xb5\xce\xaf\xce\xb4\xce\xbf\xcf\x85\xcf\x82",
                null=True,
                verbose_name="\u03a4\u03ac\u03c3\u03b7",
            ),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name="biotopeimage",
            unique_together=set([("biotope", "image"), ("biotope", "id")]),
        ),
        migrations.AddField(
            model_name="biotope",
            name="category",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.BiotopeCategoryOption",
                help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1 \xce\xa4\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                null=True,
                verbose_name=b"\xce\x9a\xce\xb1\xcf\x84\xce\xb7\xce\xb3\xce\xbf\xcf\x81\xce\xaf\xce\xb1 \xce\xa4\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="climate",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03ba\u03bb\u03af\u03bc\u03b1\u03c4\u03bf\u03c2.",
                to="naturebank.ClimateOption",
                null=True,
                verbose_name="\u039a\u03bb\u03af\u03bc\u03b1",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="condition",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.ConditionOption",
                help_text=b"\xce\x9a\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                null=True,
                verbose_name=b"\xce\x9a\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="conservation",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.ConservationOption",
                help_text=b"\xce\x95\xcf\x80\xce\xb9\xce\xbb\xce\xbf\xce\xb3\xce\xad\xcf\x82 \xcf\x80\xcf\x81\xce\xbf\xcf\x84\xce\xb5\xcf\x81\xce\xb1\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1\xcf\x82 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82",
                null=True,
                verbose_name=b"\xce\xa0\xcf\x81\xce\xbf\xcf\x84\xce\xb5\xcf\x81\xce\xb1\xce\xb9\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1 \xcf\x80\xcf\x81\xce\xbf\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xaf\xce\xb1\xcf\x82",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="cultural_value",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03b1\u03b9\u03c3\u03b8\u03b7\u03c4\u03b9\u03ba\u03ae\u03c2 \u03b1\u03be\u03af\u03b1\u03c2",
                to="naturebank.CulturalValueOption",
                null=True,
                verbose_name="\u0391\u03b9\u03c3\u03b8\u03b7\u03c4\u03b9\u03ba\u03ae",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="designation",
            field=models.ManyToManyField(
                help_text="\u039f\u03b9 \u03ba\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03ad\u03bd\u03c4\u03b1\u03be\u03b7\u03c2 \u03c3\u03b5 \u03b8\u03b5\u03c3\u03bc\u03b9\u03ba\u03cc \u03c0\u03bb\u03b1\u03af\u03c3\u03b9\u03bf.",
                to="naturebank.DesignationOption",
                null=True,
                verbose_name="\u0388\u03bd\u03c4\u03b1\u03be\u03b7 \u03c3\u03b5 \u0398\u03b5\u03c3\u03bc\u03b9\u03ba\u03cc \u03a0\u03bb\u03b1\u03af\u03c3\u03b9\u03bf",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="ecological_value",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03bf\u03b9\u03ba\u03bf\u03bb\u03bf\u03b3\u03b9\u03ba\u03ae\u03c2 \u03b1\u03be\u03af\u03b1\u03c2.",
                to="naturebank.EcologicalValueOption",
                null=True,
                verbose_name="\u039f\u03b9\u03ba\u03bf\u03bb\u03bf\u03b3\u03b9\u03ba\u03ae",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="geo_code",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.GeoCodeOption",
                help_text=b"\xce\x93\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xce\xae \xce\x95\xce\xbd\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1",
                null=True,
                verbose_name=b"\xce\x93\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xce\xae \xce\x95\xce\xbd\xcf\x8c\xcf\x84\xce\xb7\xcf\x84\xce\xb1",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="habitation",
            field=models.ManyToManyField(
                help_text="\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03c7\u03b1\u03c1\u03b1\u03ba\u03c4\u03b7\u03c1\u03b9\u03c3\u03c4\u03b9\u03ba\u03ce\u03bd \u03b5\u03bd\u03b4\u03b9\u03b1\u03c4\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd",
                to="naturebank.HabitationOption",
                null=True,
                verbose_name="\u03a7\u03b1\u03c1\u03b1\u03ba\u03c4\u03b7\u03c1. \u0395\u03bd\u03b4\u03b9\u03b1\u03b9\u03c4\u03ae\u03bc\u03b1\u03c4\u03b1",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="human_activity",
            field=models.ManyToManyField(
                help_text="\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03b1\u03bd\u03b8\u03c1\u03c9\u03c0\u03af\u03bd\u03c9\u03bd \u03b4\u03c1\u03b1\u03c3\u03c4\u03b7\u03c1\u03b9\u03bf\u03c4\u03ae\u03c4\u03c9\u03bd",
                to="naturebank.HumanActivityOption",
                null=True,
                verbose_name="\u0391\u03bd\u03b8\u03c1\u03ce\u03c0\u03b9\u03bd\u03b5\u03c2 \u03b4\u03c1\u03b1\u03c3\u03c4\u03b7\u03c1.",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="knowledge",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.KnowledgeOption",
                help_text=b"\xce\x93\xce\xbd\xcf\x8e\xcf\x83\xce\xb7 \xce\xb3\xce\xb9\xce\xb1 \xcf\x84\xce\xbf \xce\xb2\xce\xb9\xcf\x8c\xcf\x84\xce\xbf\xcf\x80\xce\xbf",
                null=True,
                verbose_name=b"\xce\x93\xce\xbd\xcf\x8e\xcf\x83\xce\xb7",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="owner",
            field=models.ManyToManyField(
                help_text="\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03b9\u03b4\u03b9\u03bf\u03ba\u03c4\u03b7\u03c3\u03af\u03b1\u03c2.",
                to="naturebank.OwnerOption",
                null=True,
                verbose_name="\u0399\u03b4\u03b9\u03bf\u03ba\u03c4\u03b7\u03c3\u03af\u03b1",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="reg_wide",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.WideArea",
                help_text=b"\xce\x95\xcf\x85\xcf\x81\xcf\x8d\xcf\x84\xce\xb5\xcf\x81\xce\xb7 \xce\xb3\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xce\xae \xcf\x80\xce\xb5\xcf\x81\xce\xb9\xce\xbf\xcf\x87\xce\xae",
                null=True,
                verbose_name=b"\xce\x95\xcf\x85\xcf\x81\xcf\x8d\xcf\x84\xce\xb5\xcf\x81\xce\xb7 \xce\x93\xce\xb5\xcf\x89\xce\xb3\xcf\x81\xce\xb1\xcf\x86\xce\xb9\xce\xba\xce\xae \xce\xa0\xce\xb5\xcf\x81\xce\xb9\xce\xbf\xcf\x87\xce\xae",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="site_type",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03c4\u03bf\u03c0\u03af\u03c9\u03bd.",
                to="naturebank.SiteTypeOption",
                null=True,
                verbose_name="\u03a4\u03cd\u03c0\u03bf\u03c2 \u03c4\u03bf\u03c0\u03af\u03bf\u03c5",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="social_reaction",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.SocialReactionOption",
                help_text=b"\xce\x95\xcf\x80\xce\xb9\xce\xbb\xce\xbf\xce\xb3\xce\xad\xcf\x82 \xce\xba\xce\xbf\xce\xb9\xce\xbd\xcf\x89\xce\xbd\xce\xb9\xce\xba\xce\xae\xcf\x82 \xce\xb1\xce\xbd\xcf\x84\xce\xaf\xce\xb4\xcf\x81\xce\xb1\xcf\x83\xce\xb7\xcf\x82",
                null=True,
                verbose_name=b"\xce\x9a\xce\xbf\xce\xb9\xce\xbd\xcf\x89\xce\xbd\xce\xb9\xce\xba\xce\xae \xce\xb1\xce\xbd\xcf\x84\xce\xaf\xce\xb4\xcf\x81\xce\xb1\xcf\x83\xce\xb7",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="social_value",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03ba\u03bf\u03b9\u03bd\u03c9\u03bd\u03b9\u03ba\u03bf\u03bf\u03b9\u03ba\u03bf\u03bd\u03bf\u03bc\u03b9\u03ba\u03ae\u03c2/\u03c0\u03bf\u03bb\u03b9\u03c4\u03b9\u03c3\u03c4\u03b9\u03ba\u03ae\u03c2 \u03b1\u03be\u03af\u03b1\u03c2.",
                to="naturebank.SocialValueOption",
                null=True,
                verbose_name="\u039a\u03bf\u03b9\u03bd\u03c9\u03bd\u03b9\u03ba\u03ae, \u03bf\u03b9\u03ba\u03bf\u03bd\u03bf\u03bc\u03b9\u03ba\u03ae \u03ba\u03b1\u03b9 \u03c0\u03bf\u03bb\u03b9\u03c4\u03b9\u03c3\u03c4\u03b9\u03ba\u03ae",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="species",
            field=models.ManyToManyField(
                to="naturebank.Species",
                through="naturebank.SpeciesBiotope",
                blank=True,
                help_text="\u03a4\u03b1 \u03b4\u03b9\u03ac\u03c6\u03bf\u03c1\u03b1 \u03b5\u03af\u03b4\u03b7 \u03c0\u03bf\u03c5 \u03b1\u03c0\u03b1\u03bd\u03c4\u03ce\u03bd\u03c4\u03b1\u03b9 \u03c3\u03c4\u03bf \u03c4\u03cc\u03c0\u03bf.",
                null=True,
                verbose_name="\u0395\u03af\u03b4\u03b7 \u03a4\u03cc\u03c0\u03bf\u03c5",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="threat",
            field=models.ManyToManyField(
                help_text="\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03b1\u03c0\u03b5\u03b9\u03bb\u03ce\u03bd",
                to="naturebank.ThreatOption",
                null=True,
                verbose_name="\u0391\u03c0\u03b5\u03b9\u03bb\u03ad\u03c2",
                blank=True,
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="trend",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.TrendOption",
                help_text=b"\xce\xa4\xce\xac\xcf\x83\xce\xb7 \xce\xba\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
                null=True,
                verbose_name=b"\xce\xa4\xce\xac\xcf\x83\xce\xb7 \xce\xba\xce\xb1\xcf\x84\xce\xac\xcf\x83\xcf\x84\xce\xb1\xcf\x83\xce\xb7\xcf\x82 \xcf\x84\xcf\x8c\xcf\x80\xce\xbf\xcf\x85",
            ),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="biotope",
            name="trend_pop",
            field=models.ForeignKey(
                blank=True,
                to="naturebank.TrendPopOption",
                help_text="\u03a4\u03ac\u03c3\u03b7 \u03c0\u03bb\u03b7\u03b8\u03c5\u03c3\u03bc\u03bf\u03cd",
                null=True,
                verbose_name="\u03a4\u03ac\u03c3\u03b7 \u03c0\u03bb\u03b7\u03b8\u03c5\u03c3\u03bc\u03bf\u03cd",
            ),
            preserve_default=True,
        ),
    ]
