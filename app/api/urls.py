from django.urls import include, path


app_name = 'api'
urlpatterns = [
    path('v1/orders/', include('api.orders.urls'), name="v1_orders"),
]
