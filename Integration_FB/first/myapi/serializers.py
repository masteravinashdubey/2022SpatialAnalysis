from rest_framework import serializers
from .models import Hero,Location
# ,Clg_score

# class HeroSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Hero
#         fields = ('name','alias')

# class LocationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Location
#         fields = ('S_No','College_Name','Address','Latitude','Longitude','District','State','Pincode','Lat','Lng')

# class Clg_scoreSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Clg_score
#         fields = ('clg_id','elsi_clg_id','college_name','state','district','robots_given','eyrtc_allowed','tbt_allowed','completed','wo_attend','lab_inaugurated','score')
