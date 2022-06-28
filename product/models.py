from django.db.models.lookups import BuiltinLookup
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields.related import ForeignKey

from PIL import Image




# Create your models here.

class Brand(models.Model):
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='brand/', null=True, blank=True)

	is_featured_brand = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		ordering = ('-id', )


	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		self.name = self.name.title()
		super().save(*args, **kwargs)




class Category(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	icon = models.FileField(upload_to="category/", blank=True, null=True)
	image = models.ImageField(upload_to="category/", blank=True, null=True)

	parent = ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	is_active = models.BooleanField(default=True)

	is_top_category = models.BooleanField(default=False)
	show_on_homepage = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-id',]
		verbose_name_plural = 'Categories'
	
	def save(self, *args, **kwargs):
		self.name = self.name.title()
		super().save(*args, **kwargs)




class Product(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	short_desc = models.TextField(blank=True, null=True)
	full_desc = models.TextField(blank=True, null=True)
	sku = models.CharField(max_length=255, null=True, blank=True)
	gtin = models.CharField(max_length=50, null=True, blank=True)
	barcode = models.PositiveBigIntegerField(null=True, blank=True)

	brand = models.ForeignKey(Brand, on_delete= models.SET_NULL, null=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

	old_price = models.DecimalField(default=0, max_digits=20, decimal_places=2, null=True, blank=True)
	unit_price = models.DecimalField(default=0, max_digits=20, decimal_places=2)

	condition = models.CharField(max_length=255, null=True, blank=True)

	is_published = models.BooleanField(default=True)
	is_disabled = models.BooleanField(default=False)
	is_popular = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)
	is_flash_deal = models.BooleanField(default=False)
	is_new_arrival = models.BooleanField(default=False)
	is_under_discount = models.BooleanField(default=False)
	is_available_for_preorder = models.BooleanField(default=False)
	
	mark_as_new = models.BooleanField(default=False)
	show_on_homepage = models.BooleanField(default=False)
	disable_wishlist_button = models.BooleanField(default=False)
	disable_buy_button = models.BooleanField(default=False)

	is_verified = models.BooleanField(default=False)

	thumbnail = models.ImageField(upload_to="product/", null=True, blank=True)

	rating = models.DecimalField(max_digits=7, decimal_places=1, null=True, blank=True)
	num_reviews = models.PositiveIntegerField(default=0, null=True, blank=True)

	display_order = models.PositiveIntegerField(default=1, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)])

	expire_info = models.TextField(blank=True, null=True)
	admin_comment = models.TextField(blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	verified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		self.name = self.name.title()
		super().save(*args, **kwargs)




class Discount(models.Model):
	product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_discount', null=True, blank=True)

	discount_percent = models.IntegerField(default=0, null=True, blank=True)

	start_date = models.DateTimeField(null=True, blank=True)
	end_date = models.DateTimeField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		ordering = ('-id', )

	def __str__(self):
		return str(self.product)




class ProductTag(models.Model):
	name = models.CharField(max_length=255)
	product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		verbose_name_plural = 'ProductTags'
		ordering = ('-id', )

	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		self.name = self.name.title()
		super().save(*args, **kwargs)




class Color(models.Model):
	name = models.CharField(max_length=255)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		ordering = ('-id', )

	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super().save(*args, **kwargs)




class ProductColor(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
	color = models.ManyToManyField(Color, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		verbose_name_plural = 'ProductColors'
		ordering = ('-id',)

	def __str__(self):
		return str(self.id)




class Size(models.Model):
	name = models.CharField(max_length=255)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		ordering = ('-id',)

	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super().save(*args, **kwargs)




class ProductSize(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
	size = models.ManyToManyField(Size, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		verbose_name_plural = 'ProductSizes'
		ordering = ('id',)

	def __str__(self):
		return str(self.id)




class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete= models.CASCADE, null=True, blank=True)
	image = models.ImageField(upload_to="productImage/", null=True, blank=True)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, related_name="+", null=True, blank=True)

	class Meta:
		verbose_name_plural = 'ProductImages'
		ordering = ('-id', )



