from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    def update_rating(self):
        self.rating_author = 0
        for post_ in Post.objects.all():
            if post_.author_id == self.id:
                self.rating_author += post_.rating_post * 3
            for comments_to_post in Comment.objects.filter(post=post_.id):
                if comments_to_post.user_id == self.id:
                    self.rating_author += comments_to_post.rating_comment
        for comment_author in Comment.objects.all():
            if comment_author.user_id == self.id:
                self.rating_author += comment_author.rating_comment
        self.save()


class Category(models.Model):
    name_category = models.CharField(unique=True, max_length=255)


article = "AR"
news = "NE"

TYPE_POST = [
    (article, "Статья"),
    (news, "Новость")
]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_post = models.CharField(max_length=2, choices=TYPE_POST)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating_post = models.IntegerField(default=0)
    post_category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text_comment = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()