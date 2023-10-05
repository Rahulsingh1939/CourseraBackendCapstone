from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'restaurant'

menuitems_patterns = (
    [
        path('', views.MenuItemsView.as_view(), name = 'memu_items_list'),
        path('<int:pk>', views.SingleMenuItemView.as_view()),
    ], 'menuitems'
)

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', include(menuitems_patterns)),
    path('api-token-auth/', obtain_auth_token)
]