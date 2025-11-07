from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    linkedin_profile = models.URLField(blank=True, null=True)

    def fullName(self):
        return f"{self.first_name} {self.last_name}"

class Description(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='description')
    text = models.TextField()

class Achievement(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='achievements')
    description = models.TextField()

class Skill(models.Model):
    choicesList = {
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    }
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(choices=choicesList)

    def getProficiencyLabel(self):
        return dict(self.choicesList).get(self.proficiency, 'Unknown')

class Experience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()

    def getResponsibilitiesList(self):
        return self.responsibilities.splitlines()

class CareerObjective(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='careerobjectives')
    text = models.TextField()