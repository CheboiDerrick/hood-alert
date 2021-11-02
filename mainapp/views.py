from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mainapp.models import *


#Home view
@login_required(login_url='/accounts/login/')
def  home(request):
    current_user = request.user
    profile=Profile.objects.filter(user_id=current_user.id).first()
    if profile is None:
        profile=Profile.objects.filter(user_id=current_user.id).first()
        posts=Profile.objects.filter(user_id=current_user.id )
        neighborhood=Neighborhood.objects.all()
        businesses=Business.objects.filter(user_id=current_user.id)
        contacts=Contacts.objects.filter(user_id=current_user.id)
        return render(request, 'profile.html', {'message':'Kindly select a neighborhood before accessing this route', 'neighborhood':neighborhood, 'businesses':businesses, 'contacts':contacts, 'posts':posts})
    else:
        neighborhood=profile.neighborhood
        posts=Post.objects.filter(neighborhood=neighborhood)
        return render(request, 'home.html', {'posts':posts})

# profile view
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(
        user_id=current_user.id).first()  # get profile
    posts = Post.objects.filter(user_id=current_user.id)
    # get all locations
    neighbourhood = Neighborhood.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    contacts = Contacts.objects.filter(user_id=current_user.id)
    return render(request, 'profile.html', {'profile': profile, 'posts': posts, 'neighbourhood': neighbourhood,'businesses': businesses, 'contacts': contacts})


@login_required(login_url="/accounts/login/")
def update_profile(request):
    if request.method == "POST":

        current_user = request.user

        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        neighbourhood = request.POST["neighbourhood"]
        location = request.POST["location"]

        # check if its an instance of neighbourhood
        if neighbourhood == "":
            neighbourhood = None
        else:
            neighbourhood = Neighborhood.objects.get(name=neighbourhood)

        profile_image = request.FILES["profile_photo"]

        user = User.objects.get(id=current_user.id)

        # check if user exists in profile table and if not create a new profile
        if Profile.objects.filter(user_id=current_user.id).exists():

            profile = Profile.objects.get(user_id=current_user.id)
            profile.photo = profile_image
            profile.neighbourhood = neighbourhood
            profile.location = location
            profile.save()
        else:
            profile = Profile(
                user_id=current_user.id,
                name=name,
                profile_photo=profile_image,
                neighbourhood=neighbourhood,
                location=location,
            )

            profile.save_profile()

        user.username = username
        user.email = email

        user.save()

        return redirect("/profile", {"success": "Profile Updated Successfully"})

        # return render(request, 'profile.html', {'success': 'Profile Updated Successfully'})
    else:
        return render(request, "profile.html", {"danger": "Profile Update Failed"})


    # create post
@login_required(login_url="/accounts/login/")
def create_post(request):
    if request.method == "POST":
        current_user = request.user
        title = request.POST["title"]
        content = request.POST["content"]
        # neighbourhood = request.POST["neighbourhood"]

        # get current user neighbourhood
        profile = Profile.objects.filter(user_id=current_user.id).first()
        # check if user has neighbourhood
        if profile is None:
            profile = Profile.objects.filter(
                user_id=current_user.id).first()  # get profile
            posts = Post.objects.filter(user_id=current_user.id)
            neighbourhood = Neighborhood.objects.all()
            contacts = Contacts.objects.filter(user_id=current_user.id)
            businesses=Business.objects.filter(user_id=current_user.id)
        
            return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!",  "neighbourhood": neighbourhood, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            neighbourhood = profile.neighbourhood

        # check if there is a post with image
        if request.FILES:
            image = request.FILES["image"]
            post = Post(
                user_id=current_user.id,
                title=title,
                content=content,
                image=image,
                neighbourhood=neighbourhood,
            )
            post.create_post()

            return redirect("/profile", {"success": "Post Created Successfully"})
        else:
            post = Post(
                user_id=current_user.id,
                title=title,
                content=content,
                neighbourhood=neighbourhood,
            )
            post.create_post()
            return redirect("/profile", {"success": "Post Created Successfully"})

    else:
        return render(request, "profile.html", {"danger": "Post Creation Failed"})

# create business
@login_required(login_url="/accounts/login/")
def create_business(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]

        # get current user neighbourhood
        profile = Profile.objects.filter(user_id=current_user.id).first()
        # check if user has neighbourhood
        if profile is None:
            profile = Profile.objects.filter(
                user_id=current_user.id).first()  # get profile
            posts = Post.objects.filter(user_id=current_user.id)
            # get all locations
            neighbourhood = Neighborhood.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contacts.objects.filter(user_id=current_user.id)
            # redirect to profile with error message
            return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "neighbourhood": neighbourhood, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            neighbourhood = profile.neighbourhood

        # check if its an instance of neighbourhood
        if neighbourhood == "":
            neighbourhood = None
        else:
            neighbourhood = Neighborhood.objects.get(name=neighbourhood)

        business = Business(
            user_id=current_user.id,
            name=name,
            email=email,
            phone=phone,
            neighbourhood=neighbourhood,
        )
        business.create_business()

        return redirect("/profile", {"success": "Business Created Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Business Creation Failed"})

# create contact
@login_required(login_url="/accounts/login/")
def create_contact(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST["name"]
        phone = request.POST["phone"]
        
        profile = Profile.objects.filter(user_id=current_user.id).first()
        # check if user has neighbourhood
        if profile is None:
            profile = Profile.objects.filter(
                user_id=current_user.id).first()  # get profile
            posts = Post.objects.filter(user_id=current_user.id)
            # get all locations
            neighbourhood = Neighborhood.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contacts.objects.filter(user_id=current_user.id)
            
            return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "neighbourhood": neighbourhood,"businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            neighbourhood = profile.neighbourhood

        # check if its an instance of neighbourhood
        if neighbourhood == "":
            neighbourhood = None
        else:
            neighbourhood = Neighborhood.objects.get(name=neighbourhood)

        contact = Contacts(
            user_id=current_user.id,
            name=name,
            phone=phone,
            neighbourhood=neighbourhood,
        )
        contact.create_contact()

        return redirect("/profile", {"success": "Contact Created Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Contact Creation Failed"})

@login_required(login_url="/accounts/login/")
# posts page
def posts(request):
    current_user = request.user
    # get current user neighbourhood
    profile = Profile.objects.filter(user_id=current_user.id).first()
    # check if user has neighbourhood
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()  # get profile
        posts = Post.objects.filter(user_id=current_user.id)
        # get all locations
        neighbourhood = Neighborhood.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contacts.objects.filter(user_id=current_user.id)
        # redirect to profile with error message
        return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "neighbourhood": neighbourhood, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        neighbourhood = profile.neighbourhood
        # get all posts in the neighbourhood of the user ordered by date
        posts = Post.objects.filter(neighbourhood=neighbourhood)
        return render(request, "posts.html", {"posts": posts})