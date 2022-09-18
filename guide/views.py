from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from .models import Location, User
# from .forms import BookmarkForm


class PreviewList(generic.ListView):
    model = Location
    queryset = Location.objects.filter(preview=True).order_by('title')
    template_name = 'index.html'


class LocationDetails(View):

    def get(self, request, slug, *args, **kwargs): 
        queryset = Location.objects
        location = get_object_or_404(queryset, slug=slug)
        bookmarked = False
        if location.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True
        
        return render(
            request,
            "location.html",
            {
                'location': location,
                'bookmarked': bookmarked,
            }
        )


class LocationList(generic.ListView):
    model = Location
    queryset = Location.objects.order_by('country', 'title')
    template_name = 'location_directory.html'


class LocationBookmark(View):

    def post(self, request, slug):
        location = get_object_or_404(Location, slug=slug)

        if location.bookmarks.filter(id=request.user.id).exists():
            location.bookmarks.remove(request.user)
        else:
            location.bookmarks.add(request.user)
        
        return HttpResponseRedirect(reverse('location', args=[slug]))



