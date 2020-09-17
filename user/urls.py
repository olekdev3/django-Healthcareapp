from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', user_views.dashboard, name='dashboard'),
    path('about/',user_views.about, name='about'),
    path('profile/',user_views.profile, name='profile'),
    # path('newpatient/', user_views.newPatient, name='newp'),
    path('newpatient/', user_views.addPatient.as_view(), name='newp'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('doctors/', user_views.DoctorsList.as_view(),name='doctors'),
    path('patients/', user_views.PatientList.as_view(),name='patients'),
    path('history/', user_views.HistoryList.as_view(),name='history'),
    path('report/', user_views.report,name='report'),
    path('newcase/', user_views.addCase.as_view(),name='addCase'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),

]