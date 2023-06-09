from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView,
)

from . import views
from .views import LogoutAPIView, UpdateUsersAPIView, DeleteUsersAPIView, CreateRoleView, RoleUpdateView, \
    RoleDeleteView, GetRoleAPIView, CustomerCreateView, GetCustomerAPIView, UpdateCustomerAPIView, \
    DeleteCustomerAPIView, AddVariantCreateView, GetVariantAPIView, UpdateVariantAPIView, DeleteVariantAPIView, \
    Attachment_Sensor_CreateView
# UpdateSensorAPIView, GetSensorAPIView, DeleteSensorAPIView, \
# GetAttachmentAPIView, UpdateAttachmentAPIView, DeleteAttachmentAPIView

urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register"),
    path('login', views.LoginAPIView.as_view(), name="login"),
    path('get_users', views.GetUsersAPIView.as_view(), name="logout"),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutAPIView.as_view(), name='logout_token'),
    path('update_user/<int:pk>', UpdateUsersAPIView.as_view(), name='update_user'),
    path('delete_user/<int:pk>', DeleteUsersAPIView.as_view(), name='delete_user'),
    path('add_role', CreateRoleView.as_view(), name='add_role'),
    path('get_role', GetRoleAPIView.as_view(), name='role-list'),
    path('update_role/<int:role_id>', RoleUpdateView.as_view(), name='update_role'),
    path('delete_role/<int:role_id>', RoleDeleteView.as_view(), name='role-delete'),
    path('addcustomer', CustomerCreateView.as_view(), name='customer-create'),
    path('getcustomer', GetCustomerAPIView.as_view(), name='customer-get'),
    path('updatecustomer/<int:id>', UpdateCustomerAPIView.as_view(), name='customer-update'),
    path('deletecustomer/<int:id>', DeleteCustomerAPIView.as_view(), name='customer-delete'),
    # path('addsensor', SensorCreateView.as_view(), name='add-sensor'),
    # path('updatesensor/<int:sensor_id>', UpdateSensorAPIView.as_view(), name='update-sensor'),
    # path('getsensor', GetSensorAPIView.as_view(), name='getsensor'),
    # path('deletesensor/<int:sensor_id>', DeleteSensorAPIView.as_view(), name='delete-sensor'),
    path('addattachment_or_sensor', Attachment_Sensor_CreateView.as_view(), name='add-attachment'),
    # path('updateattachment/<attachment_id>', UpdateAttachmentAPIView.as_view(), name='update-attachment'),
    # path('getattachment', GetAttachmentAPIView.as_view(), name='get-attachment'),
    # path('deleteattachment/<attachment_id>', DeleteAttachmentAPIView.as_view(), name='delete-attachment'),
    path('addvariant', AddVariantCreateView.as_view(), name='addvariant'),
    path('getvariant', GetVariantAPIView.as_view(), name='variant-get'),
    path('updatevariant/<int:variant_id>', UpdateVariantAPIView.as_view(), name='variant-update'),
    path('deletevariant/<int:variant_id>', DeleteVariantAPIView.as_view(), name='variant-delete'),

]
