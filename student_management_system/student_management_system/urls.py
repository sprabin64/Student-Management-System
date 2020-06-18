"""student_management_system URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from student_management_app import views, Appview
from student_management_system import settings

urlpatterns = [
    path('demo/', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('', views.showLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user),
    path('doLogin', views.doLogin),
    path('admin_homepage', Appview.admin_homepage),
    path('staff_homepage', Appview.staff_homepage),
    path('student_homepage', Appview.student_homepage),
    path('add_staff', Appview.add_staff),
    path('add_staff_save', Appview.add_staff_save),
    path('add_course', Appview.add_course),
    path('add_course_save', Appview.add_course_save),
    path('add_student', Appview.add_student),
    path('add_student_form', Appview.add_student_form),
    path('add_student_save', Appview.add_student_save),
    path('delete_student/<str:student_id>', Appview.delete_student),
    path('add_subject', Appview.add_subject),
    path('add_subject_save', Appview.add_subject_save),
    path('manage_staff', Appview.manage_staff),
    path('manage_student', Appview.manage_student),
    path('manage_course', Appview.manage_course),
    path('delete_course/<str:course_id>', Appview.delete_course),
    path('manage_subject', Appview.manage_subject),
    path('edit_staff/<str:staff_id>', Appview.edit_staff),
    path('edit_staff_save', Appview.edit_staff_save),
    path('edit_student/<str:student_id>', Appview.edit_student),
    path('edit_student_save', Appview.edit_student_save),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
