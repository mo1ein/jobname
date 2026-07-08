from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=255)
	about_url = models.URLField(unique=True)
	birth_date = models.DateField(null=True, blank=True)
	birth_location = models.CharField(max_length=512, null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name


class Quote(models.Model):
	text = models.TextField()
	# todo: on_delete is OK?
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="quotes")
	tags = models.ManyToManyField(Tag, related_name="quotes", blank=True)

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		# ensure idempotency at DB-level: a given author+text pair should be unique
		unique_together = ("text", "author")
		indexes = [
			models.Index(fields=["author"]),
		]

	def __str__(self):
		return f"{self.text[:80]} — {self.author.name}"
