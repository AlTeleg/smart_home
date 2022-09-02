from django.urls import path

from measurement.views import SensorView, MeasurementView, SensorsView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/<pk>/', SensorView.as_view(), name='sensors'),
    path('sensors/', SensorsView.as_view(), name='sensors'),
    path('measurements/', MeasurementView.as_view(), name='measurements'),
]
