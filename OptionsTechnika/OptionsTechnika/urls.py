"""OptionsTechnika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from OptionsTechnikaApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index1'),
    path('courses/',views.courses),
    path('about/',views.about),
    path('contact/',views.contact),
    path('walloffame/',views.wallof),
    path('alumini/',views.alumini),
    path('register/',views.register,name="register"),
    path('login/',views.login,name='login1'),
    path('enquiry/',views.enquiry),
    path('team/',views.team),
    path('ibm/',views.ibm),
    path('software/',views.software),
    path('solution/',views.solution),
    path('logout/',views.logout,name='logout'),
    path('details/',views.details),
    path('profile/<username>',views.coun_profile),
    path('counsellor/<username>',views.counsellor,name="counsellor"),
    path('editenquiry/<username>/<email>',views.editenquiry,name="editenquiry"),
    path('faculty/<username>/<actn>',views.faculty),
    path('prof/<username>/<actn>',views.fac_profile),
    path('student/<username>',views.student,name="student"),
    path('stu_pro/<username>',views.stu_profile),
    path('addalumini/',views.addalumini),
    path('error/',views.error,name="error"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
