from django.db import models

#create Blog Model
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()

    def __str__(self):
        return self.blog_title
    
#create Comment Model
class Comment(models.Model):
    #create realtionship between blog and comments as each blog can have many comments
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) #if blog is deleted then comment gets deleted
    comment = models.TextField()

    def __str__(self):
        return self.comment