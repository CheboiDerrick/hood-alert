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