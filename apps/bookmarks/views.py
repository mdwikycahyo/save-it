from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import SavedBookmarks
from .tasks import simulate_long_process

class Bookmarks(ListView):
    model = SavedBookmarks
    template_name = "bookmarks.html"
    context_object_name = "bookmarks"

    def get(self, request):
        bookmarks = SavedBookmarks.objects.all()
        return render(request, "bookmarks.html", {"bookmarks": bookmarks})

def delete_bookmark(request, id):
    SavedBookmarks.objects.filter(id=id).delete()
    return redirect('bookmarks')

class FormBookmarks(View):
    def get(self, request):
        return render(request, "add-bookmark.html")

    def post(self, request):
        url = request.POST.get("url")
        description = request.POST.get("description")
        source = request.POST.get("source")
        simulate_long_process()
        SavedBookmarks.objects.create(url=url, description=description, source=source)
        return redirect("bookmarks")
    
class EditBookmark(View):
    def get(self, request, id):
        selected_bookmark =  SavedBookmarks.objects.get(id=id)
        print('hole',id, selected_bookmark)
        return render(request, "edit-bookmark.html", {"bookmark": selected_bookmark})

    def post(self, request, id):
        bookmark = SavedBookmarks.objects.get(id=id)
        bookmark.url = request.POST.get("url")
        bookmark.description = request.POST.get("description")
        bookmark.source = request.POST.get("source")
        simulate_long_process()
        bookmark.save()
        return redirect("bookmarks")
