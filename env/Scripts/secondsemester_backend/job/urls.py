from django.urls import path, re_path
from . import views

# for mongoDb
from job import views

urlpatterns = [
    path('notification/', views.notificationView.as_view()),
    path('newest/', views.NewestHistoryView.as_view()),
    path('<int:pk>/', views.DashboardView.as_view()),
    # added
    path('total/', views.totalSlots_View.as_view()),
    path('available/', views.availableSlots_View.as_view()),
    path('parking/', views.parkingSlots_View.as_view()),


    # (updated) mongoDB
    re_path(r'^department$', views.departmentApi),
    re_path(r'^department/([0-9]+)$', views.departmentApi),

    # for example (notifiaction api to front end)
    re_path(r'^notification$', views.departmentApi),

    # for dashboard api
    re_path(r'^total$', views.totalSlotsApi),
    re_path(r'^available$', views.availableApi),
    re_path(r'^parking$', views.parkingApi),
    
    # for jairo's db
    re_path(r'^track$', views.realTimeApi),

    re_path(r'^history$', views.historyApi),
    re_path(r'^sse$', views.sse, name='sse'),
    re_path(r'^count_documents$', views.count_documents, name='count_documents'),
    re_path(r'^decrement_documents$', views.decrement_documents, name='decrement_documents'),

    # for getting user documents to be printed in history tab
    re_path(r'^documents$', views.get_documents),

    re_path(r'pasok$', views.UserLoginAPIView.as_view()),
    re_path(r'^registration$', views.UserRegistrationView.as_view(), name='user-registration'),

    re_path(r'^register/$', views.UserRegistrationView.as_view(), name='user-registration'),
    re_path(r'^login/$', views.UserLoginAPIView.as_view(), name='user-login'),
    # re_path(r'^profile/$', views.UserProfileDetail.as_view(), name='user-profile'),
    # 
    # this is original (woprking)
    re_path(r'^update/(?P<pk>[0-9a-f]{24})/$', views.UpdateDocumentView.as_view(), name='update_document'),
    re_path(r'^getdocuments/(?P<id>.+)/$', views.get, name='get_document'),  # Capture any characters
    re_path(r'^getus$', views.get_user),


]