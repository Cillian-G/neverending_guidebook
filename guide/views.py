from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Location, User, Region, Patron
from .forms import RegionForm, LocationForm


# This view generates the list of preview posts on the homepage
class PreviewList(generic.ListView):
    model = Location
    queryset = Location.objects.filter(preview=True).order_by('title')
    template_name = 'index.html'


# This view generates the guidebook listings for individual locations
class LocationDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Location.objects
        location = get_object_or_404(queryset, slug=slug)
        bookmarked = False
        if location.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True
        return render(request, "location.html", {
                'location': location,
                'bookmarked': bookmarked,
            }
        )


# This view creates the index of locations covered by the guidebook
class LocationList(generic.ListView):
    model = Location
    queryset = Location.objects.order_by('country', 'title')
    template_name = 'location_directory.html'


# This view allows superusers to add new regions in the front end
@login_required
def add_region(request):
    if not request.user.is_superuser:
        messages.error(
            request,
            'Only memebers of the Neverending Guidebook staff can do that'
            )
        return redirect(reverse('home'))
    region_form = RegionForm(request.POST or None)
    if request.method == 'POST':
        if region_form.is_valid():
            region_form.save()
            return redirect('directory')
    context = {
        'region_form': region_form
    }
    return render(request, 'add_region.html', context)


# This view allows superusers to add new location listings in the front end
@login_required
def add_location(request):
    if not request.user.is_superuser:
        messages.error(
            request,
            'Only memebers of the Neverending Guidebook staff can do that'
            )
        return redirect(reverse('home'))
    location_form = LocationForm(request.POST, request.FILES)
    if request.method == 'POST':
        if location_form.is_valid():
            location_form.save()
            return redirect('directory')
    context = {
        'location_form': location_form
    }
    return render(request, 'add_location.html', context)


# This view allows users to edit location listing details in the front end
@login_required
def edit_location(request, location_id):
    if not request.user.is_superuser:
        messages.error(
            request,
            'Only memebers of the Neverending Guidebook staff can do that'
            )
        return redirect(reverse('home'))
    location = get_object_or_404(Location, id=location_id)
    location_form = LocationForm(
        request.POST or None, request.FILES or None, instance=location
        )
    if request.method == 'POST':
        if location_form.is_valid():
            location_form.save()
            return redirect('directory')
    context = {
        'location': location,
        'location_form': location_form
    }
    return render(request, 'edit_location.html', context)


# This view allows superusers to delete locations from the front end
@login_required
def delete_location(request, location_id):
    if not request.user.is_superuser:
        messages.error(
            request,
            'Only memebers of the Neverending Guidebook staff can do that'
            )
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        location.delete()
        return redirect('directory')
    context = {
        'location': location
    }
    return render(request, 'delete_location.html', context)


# This view allows superusers to delete region from the front end
@login_required
def delete_region(request, item_id):
    if not request.user.is_superuser:
        messages.error(
            request,
            'Only memebers of the Neverending Guidebook staff can do that'
            )
    region = get_object_or_404(Region, id=item_id)
    if request.method == 'POST':
        region.delete()
        return redirect('directory')
    context = {
        'region': region
    }
    return render(request, 'delete_region.html', context)


# This view allows superusers to edit region titles from the front end
@login_required
def edit_region(request, item_id):
    if not request.user.is_superuser:
        messages.error(
            request,
            'Only memebers of the Neverending Guidebook staff can do that'
            )
        return redirect(reverse('home'))
    region = get_object_or_404(Region, id=item_id)
    region_form = RegionForm(request.POST or None, instance=region)
    if request.method == 'POST':
        if region_form.is_valid():
            region = region_form.save(commit=False)
            region.save()
            return redirect('directory')
    context = {
        'region_form': region_form,
        'region': region
    }
    return render(request, 'edit_region.html', context)


# This view allows users to bookmark locations from within the front end
class LocationBookmark(View):

    def post(self, request, slug):
        location = get_object_or_404(Location, slug=slug)

        if location.bookmarks.filter(id=request.user.id).exists():
            location.bookmarks.remove(request.user)
        else:
            location.bookmarks.add(request.user)
        return HttpResponseRedirect(reverse('location', args=[slug]))


# This view allows signed-in users to view their patron status and bookmarks
@login_required
def my_account(request):
    user = get_object_or_404(User, username=request.user)
    is_patron = get_object_or_404(Patron, user=request.user)
    locations = Location.objects.filter(bookmarks=user).order_by(
        'country', 'title')
    template = 'my_account.html'
    context = {
        'user': user,
        'is_patron': is_patron,
        'locations': locations,
    }
    return render(request, template, context)
