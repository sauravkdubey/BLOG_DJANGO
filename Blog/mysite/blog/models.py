#######################################################################################################################################
###########################             AUTHOR : SAURAV DUBEY           ###############################################################
###########################                DATE: 09/01/2019             ###############################################################


from django.db import models
from django.utils import timezone

class Author(models.Model):

	'''
	Define Author for User
	'''
    name = models.CharField(max_length = 20)
    email = models.EmailField(verbose_name = 'e-mail')
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):

         '''
	Define Post for User
	'''
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=80)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def __str__(self):
        return self.author.name
    
    
class Comment(models.Model):

        '''
	Define Post for User
	'''
    author = models.OneToOneField(Author)
    post = models.ForeignKey(Post)
    text = models.TextField()
    post_date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.author + "commented"
    
    
    
    
  
