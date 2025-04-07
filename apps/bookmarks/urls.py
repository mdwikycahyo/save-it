from django.urls import path

from apps.bookmarks.views import Bookmarks, FormBookmarks, EditBookmark, delete_bookmark

urlpatterns = [
    path("bookmarks/", Bookmarks.as_view(), name="bookmarks"),
    path("bookmarks/add/", FormBookmarks.as_view(), name="add-bookmark"),
    path("bookmarks/edit/<str:id>/", EditBookmark.as_view(), name='edit-bookmark'),
    path("bookmarks/delete/<str:id>/", delete_bookmark, name='delete-bookmark')
]
