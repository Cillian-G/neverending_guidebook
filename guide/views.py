from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from .models import Location, User, Region
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


def delete_region(request, item_id):
    region = get_object_or_404(Region, id=item_id)
    id = region.id
    if request.method == 'POST':
        region.delete()
        return redirect('directory')
    context = {
        'region': region
    }
    return render(request, 'delete_region.html', context)

class LocationBookmark(View):

    def post(self, request, slug):
        location = get_object_or_404(Location, slug=slug)

        if location.bookmarks.filter(id=request.user.id).exists():
            location.bookmarks.remove(request.user)
        else:
            location.bookmarks.add(request.user)
        
        return HttpResponseRedirect(reverse('location', args=[slug]))


# class BookmarkList(generic.ListView):
#     model = Location
#     queryset = Location.objects.bookmarks.filter(id=request.user.id).order_by('country', 'title')
#     template_name = 'my_account.html'


# class UserBookmarks(View):

#     def get(self, request, slug, *args, **kwargs): 
#         queryset = Location.objects
#         location = get_object_or_404(queryset, slug=slug)
#         bookmarked = False
#         if location.bookmarks.filter(id=self.request.user.id).exists():
#             bookmarked = True
        
#         return render(
#             request,
#             "location.html",
#             {
#                 'location': location,
#                 'bookmarked': bookmarked,
#             }
#         )



# class BookmarkedLocations(View):

#     def get(self, request):
#         queryset = Location
#         bookmarks = Location.bookmarks
#         bookmarked_locations = Location.filter(
#             id=self.request.user.id
#             ).order_by(
#                 "region", "country", "title"
#                 )
#         return render(
#             request,
#             "my_account.html",
#             {
#                 bookmarked_locations: "locations"
#             }
#          )
