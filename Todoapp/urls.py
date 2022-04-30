from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    # path('classhome',views.tasklist.as_view(),name="classhome"),
    # path("classdetail/<int:pk>/",views.taskdetail.as_view(),name="classdetail"),
    path("classupdate/<int:pk>/",views.taskupdate.as_view(),name="classupdate"),
    path("classdelete/<int:pk>/", views.taskdelete.as_view(), name="classdelete"),

    # path('delete/<int:taskid>/',views.delete,name="delete"),
    # path('update/<int:id>/',views.update,name="update"),

]
