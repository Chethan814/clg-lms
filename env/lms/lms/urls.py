"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from lms import settings

from account import views

urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('add_staff',views.add_staff,name="add_staff"),
    path('add_staff_save',views.add_staff_save,name="add_staff_save"),
    path('add_course', views.add_course,name="add_course"),
    path('add_course_save', views.add_course_save,name="add_course_save"),
    path('hod_add_student', views.hod_add_student,name="hod_add_student"),
    path('staff_add_student/', views.staff_add_student, name='staff_add_student'),
    path('hod_add_student_save', views.hod_add_student_save,name="hod_add_student_save"),
    path('staff_add_student_save', views.staff_add_student_save,name="staff_add_student_save"),
    path('hod_add_subject', views.hod_add_subject,name="hod_add_subject"),
    path('staff_add_subject', views.staff_add_subject,name="staff_add_subject"),
    path('add_subject_save', views.add_subject_save,name="add_subject_save"),
    path('manage_staff', views.manage_staff,name="manage_staff"),
    path('hod_manage_student', views.hod_manage_student,name="hod_manage_student"),
    path('staff_manage_student', views.staff_manage_student,name="staff_manage_student"),
    path('manage_course', views.manage_course,name="manage_course"),
    path('manage_subject', views.manage_subject,name="manage_subject"),
    path('edit_staff/<str:staff_id>', views.edit_staff,name="edit_staff"),
    path('edit_staff_save', views.edit_staff_save,name="edit_staff_save"),
    path('edit_student/<str:student_id>', views.edit_student,name="edit_student"),
    path('edit_student_save', views.edit_student_save,name="edit_student_save"),
    path('edit_subject/<str:subject_id>', views.edit_subject,name="edit_subject"),
    path('edit_subject_save', views.edit_subject_save,name="edit_subject_save"),
    path('edit_course/<str:course_id>', views.edit_course,name="edit_course"),
    path('edit_course_save', views.edit_course_save,name="edit_course_save"),
#     Staff URL Path
    path('staff_home', views.staff_home, name="staff_home"),
    path('student_home', views.student_home, name="student_home"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
