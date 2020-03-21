from django.db import models

from django.db.models.signals import pre_save, post_save


from project.utils import unique_slug_generator



class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    text = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-published_at',)

    def __str__(self):
        return self.title


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Post)