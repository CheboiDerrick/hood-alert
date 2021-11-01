from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=70)
    occupant_count=models.IntegerField()

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()
    
    @classmethod
    def find_neigborhood(cls,neigborhood_id):
        neighborhood=cls.objects.filter(pk=neigborhood_id)
        return neighborhood

    @classmethod
    def update_neighborhood(cls,id):
        cls.objects.filter(pk=id).update()

    def update_occupants():
        pass

    def __str__(self):
        return self.name


class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    neighborhood= models.OneToOneField(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Business(models.Model):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email=models.EmailField(unique=True)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business=cls.objects.filter(id=business_id)
        return business

    @classmethod
    def update_business(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def search_business(cls,searchterm):
        businesses=cls.objects.filter(name__icontains=searchterm)
        return businesses


    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    # image=CloudinaryField('image', blank=True, null=True)
    image=models.ImageField(upload_to='posts/', blank=True, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    posted_on=models.DateTimeField()

        # create post
    def create_post(self):
        self.save()

    # delete post
    def delete_post(self):
        self.delete()

    # update post
    def update_post(self):
        self.update()


    def __str__(self):
        return self.title

