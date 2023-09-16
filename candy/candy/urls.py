from django.contrib import admin
from django.urls import path, include
from . import views  # 既にimportしている場合はこの行は不要

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),  # ここでsignup_viewを指定
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),  # この行を追加
    path('', views.welcome, name='welcome'),  # welcomeビューへのマッピング
]
