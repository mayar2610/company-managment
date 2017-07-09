from mptt.managers import TreeManager
from mptt.models import MPTTOptions
import mptt
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Company(MPTTModel):
	name = models.CharField(unique=True, max_length=30)
	earnings = models.IntegerField()
	total = models.IntegerField(null=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		return self.name
