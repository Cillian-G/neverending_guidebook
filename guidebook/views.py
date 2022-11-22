from django.shortcuts import render


# This function handles 404 errors
def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)
