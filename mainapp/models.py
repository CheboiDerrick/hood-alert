from django.db import models
from django.contrib.auth.models import User



# Project models

class Neighborhood(models.Model):
    '''
    Model that describes the behaviors of thr Neighborhood object
    '''
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=70)
    occupant_count = models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # create neighborhood
    def create_neigborhood(self):
        self.save()

    # delete neighborhood

    def delete_neigborhood(self):
        self.delete()

    # find a neighborhood

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        neighborhood = cls.objects.filter(pk=neigborhood_id)
        return neighborhood

    # update a neighborhood

    @classmethod
    def update_neighborhood(cls, id):
        cls.objects.filter(pk=id).update()

    # find a neighborhood occupants

    def update_occupants():
        pass

    def __str__(self):
        return self.name


class Profile(models.Model):
    '''
    Model that describes the behaviors of the User Profile object
    '''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='posts/', blank=True, null=True)
    name = models.CharField(max_length=100)
    neighborhood = models.OneToOneField(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name


class Business(models.Model):
    '''
    Model that describes the behaviors of the Business object
    '''

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True, blank=True )
    phone= models.CharField(max_length=50, null=True, blank=True)


    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.filter(id=business_id)
        return business

    @classmethod
    def update_business(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def search_business(cls, searchterm):
        businesses = cls.objects.filter(name__icontains=searchterm)
        return businesses

    def __str__(self):
        return self.name


class Post(models.Model):
    '''
    Model that describes the behaviors of the Post object
    '''
    title = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=['-posted_on']

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


class Contacts(models.Model):
    '''
    Model that describes the behaviors of thr Contact object
    '''
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(User, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='users',default=1)

    # create contact

    def create_contact(self):
        self.save()

    # delete contact
    def delete_contact(self):
        self.delete()

    # update contact
    def update_contact(self):
        self.update()

    # find contact by id
    @classmethod
    def find_contact(cls, id):
        contact = cls.objects.get(id=id)
        return contact

    def __str__(self):
        return self.name
