from django.db import models
from django.utils.text import slugify


class Party(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    leader = models.CharField(max_length=100, blank=True, default="")
    founded = models.CharField(max_length=50, blank=True, default="")

    ideology = models.CharField(max_length=150, blank=True, default="")
    political_position = models.CharField(max_length=100, blank=True, default="")

    short_explainer = models.TextField(blank=True, default="")
    historical_context = models.TextField(blank=True, default="")
    political_identity = models.TextField(blank=True, default="")
    society_vision = models.TextField(blank=True, default="")
    economic_approach = models.TextField(blank=True, default="")
    equality_view = models.TextField(blank=True, default="")
    immigration_view = models.TextField(blank=True, default="")
    crime_view = models.TextField(blank=True, default="")
    social_approach = models.TextField(blank=True, default="")
    governance_style = models.TextField(blank=True, default="")
    youth_relevance = models.TextField(blank=True, default="")
    major_support_base = models.TextField(blank=True, default="")
    common_criticisms = models.TextField(blank=True, default="")
    yoh_commentary = models.TextField(blank=True, default="")

    youth_appeal = models.IntegerField(default=5)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.abbreviation or self.name)
            slug = base_slug
            counter = 1

            while Party.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                counter += 1
                slug = f"{base_slug}-{counter}"

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ManifestoPolicy(models.Model):
    party = models.ForeignKey(
        Party,
        on_delete=models.CASCADE,
        related_name="manifesto_policies"
    )

    category = models.CharField(max_length=100)
    policy_title = models.CharField(max_length=200)

    manifesto_position = models.TextField()
    simplified_explanation = models.TextField()
    possible_advantages = models.TextField()
    possible_concerns = models.TextField()
    affected_groups = models.TextField()
    yoh_analysis = models.TextField()

    def __str__(self):
        return f"{self.party.abbreviation} - {self.category}"


class CommentaryArticle(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    summary = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    CATEGORY_CHOICES = [
        ("economy", "Economy"),
        ("land", "Land"),
        ("education", "Education"),
        ("governance", "Governance"),
        ("crime", "Crime"),
        ("social", "Social"),
    ]

    question = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    left_score = models.IntegerField(default=0)
    right_score = models.IntegerField(default=0)

    def __str__(self):
        return self.question
