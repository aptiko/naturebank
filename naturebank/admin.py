from django.contrib.gis import admin

from naturebank import models


class SpeciesBiotopeInline(admin.TabularInline):
    model = models.SpeciesBiotope
    extra = 3
    raw_id_fields = ("species",)


class BiotopeSupplInline(admin.StackedInline):
    model = models.Biotope
    extra = 1


class SpeciesBiotopeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SpeciesBiotope._meta.fields]
    fieldsets = (
        (
            None,
            {
                "fields": ("species", "biotope", "abundance"),
            },
        ),
    )


admin.site.register(models.SpeciesBiotope, SpeciesBiotopeAdmin)


class BiotopeImageInline(admin.TabularInline):
    classes = ["collapse"]
    extra = 1
    model = models.BiotopeImage


class BiotopeAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.display_srid = 4326
        admin.ModelAdmin.__init__(self, model, admin_site)

    list_display = (
        "site_code",
        "site_name_gr",
        "geo_code",
        "category",
        "creation_date",
        "update_date",
    )
    list_filter = (
        "category",
        "update_date",
        "knowledge",
        "conservation",
        "social_reaction",
        "condition",
    )
    search_fields = ("site_code", "site_name_gr", "geo_code__name", "category__name")
    ordering = ("site_name_gr",)
    list_display_links = ("site_code", "site_name_gr")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "site_code",
                    ("site_name", "site_name_gr"),
                    "category",
                    ("creation_date", "update_date"),
                    ("main_char_biotopos", "main_char_natural", "main_char_built"),
                    "reg_wide",
                    ("comp_code", "comp_name"),
                    "respondent",
                ),
            },
        ),
        (
            "GIS",
            {
                "classes": ("collapse",),
                "fields": ("gis_sitecode", "gis_area", "gis_perimeter"),
            },
        ),
        (
            "Γεωγραφική Τοποθέτηση",
            {
                "classes": ("collapse",),
                "fields": (
                    "geo_code",
                    "dist_name",
                    "reg_mun",
                    "area",
                    "area_l",
                    "area_s",
                    "long_deg",
                    "long_min",
                    "long_sec",
                    "lat_deg",
                    "lat_min",
                    "lat_sec",
                    "length_max",
                    "width_max",
                    "alt_mean",
                    "alt_max",
                    "alt_min",
                ),
            },
        ),
        (
            "Γνώση",
            {
                "classes": ("collapse",),
                "fields": ("knowledge", "designation"),
            },
        ),
        (
            "Προστασία",
            {
                "classes": ("collapse",),
                "fields": (
                    "protection",
                    ("measures_take", "measures_need"),
                    "social_reaction",
                    "social_reaction_text",
                    "conservation",
                    "owner",
                    "ownership_text",
                ),
            },
        ),
        (
            "Χαρακτηριστικά",
            {
                "classes": ("collapse",),
                "fields": (
                    "site_type",
                    "climate",
                    "condition",
                    "trend",
                    "trend_text",
                    "abandon",
                    "geology",
                    "characteristics",
                    "history",
                ),
            },
        ),
        (
            "Αξίες",
            {
                "classes": ("collapse",),
                "fields": (
                    "ecological_value",
                    "social_value",
                    "cultural_value",
                    "quality",
                ),
            },
        ),
        (
            "Κίνδυνοι",
            {
                "classes": ("collapse",),
                "fields": (
                    "threat",
                    "threat_text",
                    "vulnerability",
                ),
            },
        ),
        (
            "Ανθρώπινη Παρουσία",
            {
                "classes": ("collapse",),
                "fields": (
                    "population",
                    "landvalue",
                    "trend_pop",
                    "human_activity",
                    "tourism",
                    "infrastructure",
                    "view",
                    "path",
                ),
            },
        ),
        (
            "Πανίδα και Χλωρίδα",
            {
                "classes": ("collapse",),
                "fields": (
                    "habitation",
                    "species_text",
                ),
            },
        ),
        (
            "Τεκμηρίωση",
            {
                "classes": ("collapse",),
                "fields": ("document",),
            },
        ),
    )
    filter_horizontal = (
        "designation",
        "owner",
        "site_type",
        "climate",
        "ecological_value",
        "social_value",
        "cultural_value",
        "threat",
        "human_activity",
        "habitation",
    )

    inlines = (
        BiotopeImageInline,
        SpeciesBiotopeInline,
    )


admin.site.register(models.Biotope, BiotopeAdmin)


class DesignationOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.DesignationOption._meta.fields]


admin.site.register(models.DesignationOption, DesignationOptionAdmin)


class BiotopeCategoryOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.BiotopeCategoryOption._meta.fields]


admin.site.register(models.BiotopeCategoryOption, BiotopeCategoryOptionAdmin)


class GeoCodeOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.GeoCodeOption._meta.fields]


admin.site.register(models.GeoCodeOption, GeoCodeOptionAdmin)


class WideAreaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.WideArea._meta.fields]


admin.site.register(models.WideArea, WideAreaAdmin)


class AbandonmentOptionAdmin(admin.ModelAdmin):
    list_dsiplay = [f.name for f in models.AbandonmentOption._meta.fields]


admin.site.register(models.AbandonmentOption, AbandonmentOptionAdmin)


class ConditionOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.ConditionOption._meta.fields]


admin.site.register(models.ConditionOption, ConditionOptionAdmin)


class TrendOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.TrendOption._meta.fields]


admin.site.register(models.TrendOption, TrendOptionAdmin)


class KnowledgeOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.KnowledgeOption._meta.fields]


admin.site.register(models.KnowledgeOption, KnowledgeOptionAdmin)


class SocialReactionOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SocialReactionOption._meta.fields]


admin.site.register(models.SocialReactionOption, SocialReactionOptionAdmin)


class ConservationOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.ConservationOption._meta.fields]


admin.site.register(models.ConservationOption, ConservationOptionAdmin)


class SocialValueOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SocialValueOption._meta.fields]


admin.site.register(models.SocialValueOption, SocialValueOptionAdmin)


class CulturalValueOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.CulturalValueOption._meta.fields]


admin.site.register(models.CulturalValueOption, CulturalValueOptionAdmin)


class EcologicalValueOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.EcologicalValueOption._meta.fields]


admin.site.register(models.EcologicalValueOption, EcologicalValueOptionAdmin)


class HabitationOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.HabitationOption._meta.fields]


admin.site.register(models.HabitationOption, HabitationOptionAdmin)


class SiteTypeOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SiteTypeOption._meta.fields]


admin.site.register(models.SiteTypeOption, SiteTypeOptionAdmin)


class ClimateOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.ClimateOption._meta.fields]


admin.site.register(models.ClimateOption, ClimateOptionAdmin)


class HumanActivityOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.HumanActivityOption._meta.fields]


admin.site.register(models.HumanActivityOption, HumanActivityOptionAdmin)


class TrendPopOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.TrendPopOption._meta.fields]


admin.site.register(models.TrendPopOption, TrendPopOptionAdmin)


class ThreatOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.ThreatOption._meta.fields]


admin.site.register(models.ThreatOption, ThreatOptionAdmin)

###############################################################################


class SpeciesAdmin(admin.ModelAdmin):
    list_display = (
        "species_code",
        "species_name",
        "sub_species",
        "species_category",
        "plant_kind",
        "creation_date",
        "update_date",
    )
    list_filter = ("species_category", "plant_kind", "update_date")
    search_fields = (
        "species_code",
        "species_name",
        "sub_species",
        "species_category__name",
        "plant_kind__name",
    )
    ordering = ("species_name",)
    list_display_links = ("species_code", "species_name")
    fieldsets = (
        (
            "Γενικά Στοιχεία",
            {
                "fields": (
                    "species_code",
                    "species_name",
                    "sub_species",
                    ("creation_date", "update_date"),
                    "species_category",
                    "other_names",
                    "species_name_gr",
                    "plant_kind",
                    "knowledge",
                    "habitat",
                    "expansion",
                    "origin",
                    "respondent",
                    "photo",
                ),
            },
        ),
        (
            "Γνωρίσματα",
            {
                "classes": ("collapse",),
                "fields": (
                    "category_ende",
                    "category_migr",
                    "category_bree",
                    "category_resi",
                    "category_intr",
                    "category",
                ),
            },
        ),
        (
            "Στοιχεία Προστασίας και Ανάπτυξης",
            {
                "classes": ("collapse",),
                "fields": (
                    "protection",
                    "conservation_prio",
                    "trend",
                    "measures_take",
                    "measures_need",
                ),
            },
        ),
        (
            "Κατάσταση Διατήρησης",
            {
                "classes": ("collapse",),
                "fields": ("conservation_gr", "conservation_eec", "conservation_bio"),
            },
        ),
        (
            "Σπανιότητα",
            {
                "classes": ("collapse",),
                "fields": ("rarity_gr", "rarity_eec", "rarity_bio"),
            },
        ),
        (
            "Απειλές",
            {
                "classes": ("collapse",),
                "fields": (
                    "threat_hunt",
                    "threat_fish",
                    "threat_coll",
                    "threat_fore",
                    "threat_graz",
                    "threat_poll",
                    "threat_cult",
                    "threat_tour",
                    "threat_road",
                    "threat_buil",
                    "threat_drai",
                    "threat_eutr",
                    "threat_pest",
                    "threat_other",
                    "threat",
                ),
            },
        ),
        (
            "Εκμετάλλευση",
            {
                "classes": ("collapse",),
                "fields": (
                    "exploit_hunt",
                    "exploit_fish",
                    "exploit_coll",
                    "exploit_logg",
                    "exploit_graz",
                ),
            },
        ),
    )


admin.site.register(models.Species, SpeciesAdmin)


class SpeciesCategoryOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SpeciesCategoryOption._meta.fields]


admin.site.register(models.SpeciesCategoryOption, SpeciesCategoryOptionAdmin)


class SpeciesPlantKindOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SpeciesPlantKindOption._meta.fields]


admin.site.register(models.SpeciesPlantKindOption, SpeciesPlantKindOptionAdmin)


class SpeciesKnowledgeOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SpeciesKnowledgeOption._meta.fields]


admin.site.register(models.SpeciesKnowledgeOption, SpeciesKnowledgeOptionAdmin)


class SpeciesProtectionOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SpeciesProtectionOption._meta.fields]


admin.site.register(models.SpeciesProtectionOption, SpeciesProtectionOptionAdmin)


class SpeciesConservationPriorityOptionAdmin(admin.ModelAdmin):
    list_display = [
        f.name for f in models.SpeciesConservationPriorityOption._meta.fields
    ]


admin.site.register(
    models.SpeciesConservationPriorityOption, SpeciesConservationPriorityOptionAdmin
)


class SpeciesTrendOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SpeciesTrendOption._meta.fields]


admin.site.register(models.SpeciesTrendOption, SpeciesTrendOptionAdmin)


class SpeciesConservationOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SpeciesConservationOption._meta.fields]


admin.site.register(models.SpeciesConservationOption, SpeciesConservationOptionAdmin)


class SpeciesRarityOptionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.SpeciesCategoryOption._meta.fields]


admin.site.register(models.SpeciesRarityOption, SpeciesRarityOptionAdmin)
