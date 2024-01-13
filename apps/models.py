from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, CASCADE, DateTimeField, ForeignKey, ManyToManyField, ImageField, \
    FloatField, PositiveIntegerField
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField


class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    image = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='users/images',
                              default='users/default.jpg')


class Category(Model):
    name = CharField(max_length=255)

    def count_blogs(self) -> int:
        return self.blog_set.count()


class Tag(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(CreatedBaseModel):
    name = CharField(max_length=255)
    author = ForeignKey('apps.User', CASCADE, 'blogs')
    category = ForeignKey('apps.Category', CASCADE)
    image = ImageField(default='blog/default.png', upload_to='blog/images/')
    tags = ManyToManyField('apps.Tag')
    text = CKEditor5Field(blank=True, null=True, config_name='extends')

    def count_comment(self):
        return self.comment_set.count()


class Comment(CreatedBaseModel):
    text = CharField(max_length=255)
    blog = ForeignKey('apps.Blog', CASCADE)
    author = ForeignKey('apps.User', CASCADE, 'comments')


class Product(CreatedBaseModel):
    name = CharField(max_length=255)
    price = FloatField()
    description = CKEditor5Field(blank=True, null=True, config_name='extends')
    quantity = PositiveIntegerField(default=0)


class ProductImage(Model):
    image = ImageField(upload_to='products/images/')
    product = ForeignKey('apps.Product', CASCADE)
