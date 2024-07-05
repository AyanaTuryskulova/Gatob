from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='photos/', null=False, blank=False)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)

    def __str__(self):
        return self.title if self.title else 'Photo without title'

class Comment(models.Model):
    photo = models.ForeignKey(Photo, related_name='comments', on_delete=models.CASCADE)
    news = models.ForeignKey('News', related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.photo:
            return f'Comment on {self.photo.title if self.photo.title else "untitled photo"}'
        elif self.news:
            return f'Comment on {self.news.title}'
        else:
            return 'Comment'

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
