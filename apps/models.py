from django.db.models import Model, TextField, CharField, CASCADE, DateTimeField, IntegerField, ForeignKey, \
    ManyToManyField


class Category(Model):
    name = CharField(max_length=255)


class Tag(Model):
    name = CharField(max_length=255)


class Blog(Model):
    name = CharField(max_length=255)
    author = ForeignKey('auth.User', CASCADE, 'blogs')
    category = ForeignKey('apps.Category', on_delete=CASCADE)
    tags = ManyToManyField('apps.Tag')
    text = TextField(blank=True, null=True)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    def count_comment(self):
        return self.comment_set.count()


class Comment(Model):
    text = CharField(max_length=255)
    blog = ForeignKey('apps.Blog', CASCADE)
    author = ForeignKey('auth.User', CASCADE, 'comments')
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)
