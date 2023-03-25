from django.urls import path
from . import views

app_name   = 'pages'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('sermons', views.SermonView.as_view(), name='sermons'),
    path('giving', views.GivingView.as_view(), name='giving'),
    path('outreach', views.OutreachView.as_view(), name='outreach'),
    path('branches', views.BranchesView.as_view(), name='branches'),
    path('store', views.StoreView.as_view(), name='store'),
    path('store/order', views.OrderView.as_view(), name='order'),
]

