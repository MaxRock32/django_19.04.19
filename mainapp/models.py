from django.db import models


# Create model: manage.py makemigrations
# Main migrate: manage.py migrate
# Show all db migration models: manage.py showmigrations


class ProductCategory(models.Model):

    class Meta:
        verbose_name = 'Category'               # Singular
        verbose_name_plural = 'Categories'      # Plural

    name = models.CharField(
        verbose_name='Category name',           # Category name viewed in admin panel
        max_length=255,                         # 1 unit less than actual byte
        unique=True)
    description = models.TextField(
        verbose_name='Category description',    # Category name viewed in admin panel
        blank=True,                             # Leaves form blank
        null=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        verbose_name = 'Product'                    # Singular
        verbose_name_plural = 'Products'            # Plural

    category = models.ForeignKey(
        to=ProductCategory,                     # Assigning foreign key
        verbose_name='Product category',        # Category name viewed in admin panel
        on_delete=models.CASCADE)               # On category deletion, this unit is deleted
    name = models.CharField(
        verbose_name='Product name',
        max_length=128,
        unique=False)
    image = models.ImageField(
        upload_to='products_images',
        blank=True)
    short_desc = models.CharField(
        verbose_name='Product description',
        max_length=128,
        blank=True)
    description = models.TextField(
        verbose_name='Product description',
        blank=True)
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=8,
        decimal_places=2,
        default=0)
    quantity = models.PositiveIntegerField(
        verbose_name='Stock',
        default=0)

    def __str__(self):
        formatted_string = f'{self.name} ({self.category})'
        return formatted_string