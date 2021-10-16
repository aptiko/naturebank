from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("naturebank", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="biotope",
            name="climate",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03ba\u03bb\u03af\u03bc\u03b1\u03c4\u03bf\u03c2.",
                to="naturebank.ClimateOption",
                verbose_name="\u039a\u03bb\u03af\u03bc\u03b1",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="cultural_value",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03b1\u03b9\u03c3\u03b8\u03b7\u03c4\u03b9\u03ba\u03ae\u03c2 \u03b1\u03be\u03af\u03b1\u03c2",
                to="naturebank.CulturalValueOption",
                verbose_name="\u0391\u03b9\u03c3\u03b8\u03b7\u03c4\u03b9\u03ba\u03ae",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="designation",
            field=models.ManyToManyField(
                help_text="\u039f\u03b9 \u03ba\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03ad\u03bd\u03c4\u03b1\u03be\u03b7\u03c2 \u03c3\u03b5 \u03b8\u03b5\u03c3\u03bc\u03b9\u03ba\u03cc \u03c0\u03bb\u03b1\u03af\u03c3\u03b9\u03bf.",
                to="naturebank.DesignationOption",
                verbose_name="\u0388\u03bd\u03c4\u03b1\u03be\u03b7 \u03c3\u03b5 \u0398\u03b5\u03c3\u03bc\u03b9\u03ba\u03cc \u03a0\u03bb\u03b1\u03af\u03c3\u03b9\u03bf",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="ecological_value",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03bf\u03b9\u03ba\u03bf\u03bb\u03bf\u03b3\u03b9\u03ba\u03ae\u03c2 \u03b1\u03be\u03af\u03b1\u03c2.",
                to="naturebank.EcologicalValueOption",
                verbose_name="\u039f\u03b9\u03ba\u03bf\u03bb\u03bf\u03b3\u03b9\u03ba\u03ae",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="habitation",
            field=models.ManyToManyField(
                help_text="\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03c7\u03b1\u03c1\u03b1\u03ba\u03c4\u03b7\u03c1\u03b9\u03c3\u03c4\u03b9\u03ba\u03ce\u03bd \u03b5\u03bd\u03b4\u03b9\u03b1\u03c4\u03b7\u03bc\u03ac\u03c4\u03c9\u03bd",
                to="naturebank.HabitationOption",
                verbose_name="\u03a7\u03b1\u03c1\u03b1\u03ba\u03c4\u03b7\u03c1. \u0395\u03bd\u03b4\u03b9\u03b1\u03b9\u03c4\u03ae\u03bc\u03b1\u03c4\u03b1",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="human_activity",
            field=models.ManyToManyField(
                help_text="\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03b1\u03bd\u03b8\u03c1\u03c9\u03c0\u03af\u03bd\u03c9\u03bd \u03b4\u03c1\u03b1\u03c3\u03c4\u03b7\u03c1\u03b9\u03bf\u03c4\u03ae\u03c4\u03c9\u03bd",
                to="naturebank.HumanActivityOption",
                verbose_name="\u0391\u03bd\u03b8\u03c1\u03ce\u03c0\u03b9\u03bd\u03b5\u03c2 \u03b4\u03c1\u03b1\u03c3\u03c4\u03b7\u03c1.",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="owner",
            field=models.ManyToManyField(
                help_text="\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03b9\u03b4\u03b9\u03bf\u03ba\u03c4\u03b7\u03c3\u03af\u03b1\u03c2.",
                to="naturebank.OwnerOption",
                verbose_name="\u0399\u03b4\u03b9\u03bf\u03ba\u03c4\u03b7\u03c3\u03af\u03b1",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="site_type",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03c4\u03bf\u03c0\u03af\u03c9\u03bd.",
                to="naturebank.SiteTypeOption",
                verbose_name="\u03a4\u03cd\u03c0\u03bf\u03c2 \u03c4\u03bf\u03c0\u03af\u03bf\u03c5",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="social_value",
            field=models.ManyToManyField(
                help_text="\u03a4\u03cd\u03c0\u03bf\u03b9 \u03ba\u03bf\u03b9\u03bd\u03c9\u03bd\u03b9\u03ba\u03bf\u03bf\u03b9\u03ba\u03bf\u03bd\u03bf\u03bc\u03b9\u03ba\u03ae\u03c2/\u03c0\u03bf\u03bb\u03b9\u03c4\u03b9\u03c3\u03c4\u03b9\u03ba\u03ae\u03c2 \u03b1\u03be\u03af\u03b1\u03c2.",
                to="naturebank.SocialValueOption",
                verbose_name="\u039a\u03bf\u03b9\u03bd\u03c9\u03bd\u03b9\u03ba\u03ae, \u03bf\u03b9\u03ba\u03bf\u03bd\u03bf\u03bc\u03b9\u03ba\u03ae \u03ba\u03b1\u03b9 \u03c0\u03bf\u03bb\u03b9\u03c4\u03b9\u03c3\u03c4\u03b9\u03ba\u03ae",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="species",
            field=models.ManyToManyField(
                help_text="\u03a4\u03b1 \u03b4\u03b9\u03ac\u03c6\u03bf\u03c1\u03b1 \u03b5\u03af\u03b4\u03b7 \u03c0\u03bf\u03c5 \u03b1\u03c0\u03b1\u03bd\u03c4\u03ce\u03bd\u03c4\u03b1\u03b9 \u03c3\u03c4\u03bf \u03c4\u03cc\u03c0\u03bf.",
                to="naturebank.Species",
                verbose_name="\u0395\u03af\u03b4\u03b7 \u03a4\u03cc\u03c0\u03bf\u03c5",
                through="naturebank.SpeciesBiotope",
            ),
        ),
        migrations.AlterField(
            model_name="biotope",
            name="threat",
            field=models.ManyToManyField(
                help_text="\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b5\u03c2 \u03b1\u03c0\u03b5\u03b9\u03bb\u03ce\u03bd",
                to="naturebank.ThreatOption",
                verbose_name="\u0391\u03c0\u03b5\u03b9\u03bb\u03ad\u03c2",
            ),
        ),
    ]
