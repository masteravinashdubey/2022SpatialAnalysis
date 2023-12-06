from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)
# router.register(r'locations', views.LocationViewSet)
# router.register(r'clg_score', views.Clg_scoreViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^first',views.first),
    url(r'^scoring_values',views.scoring_values),
    url(r'^get_score_college_wise',views.get_score_college_wise),
    url(r'^get_score_district_wise',views.get_score_district_wise),
    url(r'^get_score_state_wise',views.get_score_state_wise),
    url(r'^work_sugg',views.work_sugg),
]