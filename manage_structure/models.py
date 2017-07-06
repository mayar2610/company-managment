from mptt.managers import TreeManager
from mptt.models import MPTTOptions
import mptt
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Company(MPTTModel):
	name = models.CharField(unique=True, max_length=30)
	earnings = models.IntegerField()
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		return self.name
"""
class Migration(DataMigration):

	def forwards(self, orm):
		Company = orm['models.Company']
		Company.add_to_class('tree', TreeManager())
		Company.add_to_class('_mptt_meta', MPTTOptions())
		Company.tree.init_from_model(Place)
		Company.tree.rebuild()
"""