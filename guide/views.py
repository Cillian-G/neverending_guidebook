from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Location   


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
