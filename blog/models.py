from django.db import models

class Post(models.Model):
    name = models.TextField(max_length=50)
    post_text = models.TextField(max_length=1440)
    date = models.DateTimeField(auto_now=True)
    author = models.TextField(max_length=40)
    
    def __str__(self):
        return self.name 
    
class Ip(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.TextField()

    def __str__(self):
        return self.ip + ' // ' + post.name
