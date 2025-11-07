from django.contrib import admin
from .models import (
    Person,
    Description,
    Achievement,
    Skill,
    Experience,
    CareerObjective,
)

class DescriptionInline(admin.TabularInline):
    model = Description
    extra = 0

class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 0

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0

class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0

class CareerObjectiveInline(admin.TabularInline):
    model = CareerObjective
    extra = 0

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    inlines = (
        DescriptionInline,
        AchievementInline,
        SkillInline,
        ExperienceInline,
        CareerObjectiveInline,
    )

admin.site.register(Description)
admin.site.register(Achievement)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(CareerObjective)