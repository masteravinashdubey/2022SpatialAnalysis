from math import radians, cos, sin, asin, sqrt
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# Create your views here.
from rest_framework import viewsets
# from .serializers import HeroSerializer
from .models import clg_score, scoring_district_wise, scoring_state_wise

# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     print('Hero')
#     serializer_class = HeroSerializer

@api_view(['POST'])
def first(request):
    temp = JSONParser().parse(request)
    body = temp.get('name')
    # print(body)
    return JsonResponse({'dbs': 'data'})

@api_view(['POST'])
def scoring_values(request):
    temp = JSONParser().parse(request)
    EYRTC_Score = float(temp.get('EYRTC_Score'))
    TBT_Allowed = float(temp.get('TBT_Allowed'))
    TBT_Completed = float(temp.get('TBT_Completed'))
    Wo_Attend = float(temp.get('Wo_Attend'))
    Lab_InAug = float(temp.get('Lab_InAug'))
    # print(EYRTC_Score)
    # print(TBT_Allowed)
    # print(TBT_Completed)
    # print(Wo_Attend)
    # print(Lab_InAug)

    count = clg_score.objects.all().count()
    # print(count)

    for i in range(1, count+1):
        data = clg_score.objects.filter(id=i)
        up_score = ((EYRTC_Score*float(data[0].eyrtc_score))+(TBT_Allowed*float(data[0].tbt_allowed))
                    + (TBT_Completed*float(data[0].completed)
                       )+(Wo_Attend*float(data[0].wo_attend))
                    + (Lab_InAug*float(data[0].lab_inaugurated)))
        clg_score.objects.filter(id=i).update(score=up_score)
        print(data[0].college_name)
    # c=1
    # while c!=count:
    #     data=clg_score.objects.filter(id=c)
    #     up_score=((EYRTC_Score*float(data[0].eyrtc_score))+(TBT_Allowed*float(data[0].tbt_allowed))
    #     +(TBT_Completed*float(data[0].completed))+(Wo_Attend*float(data[0].wo_attend))
    #     +(Lab_InAug*float(data[0].lab_inaugurated)))
    #     clg_score.objects.filter(id=c).update(score=up_score)
    #     print(data[0].college_name)
    #     c+=1
    
    dist_data_count = scoring_district_wise.objects.all().count()
    for i in range(1, dist_data_count+1):
        district_data = scoring_district_wise.objects.filter(id=i)
        # print(district_data[0].district)
        dist_cnt = clg_score.objects.filter(
            district=district_data[0].district).count()
        dist_data = clg_score.objects.filter(
            district=district_data[0].district)
        # print(dist_data)
        # print(district_data[0].district)
        # print(dist_cnt)
        temp_score = 0.0
        for j in range(0, dist_cnt):
            print(dist_data[j].score)
            temp_score += dist_data[j].score
        # print(temp_score)
        scoring_district_wise.objects.filter(
            district=district_data[0].district).update(score=temp_score)
        # print(type(temp_score))
    # print(dist_data_count)
    
    state_data_count = scoring_state_wise.objects.all().count()
    for i in range(1, state_data_count+1):
        state_data = scoring_state_wise.objects.filter(id=i)
        # print(state_data[0].state)
        sta_cnt = clg_score.objects.filter(state=state_data[0].state).count()
        sta_data = clg_score.objects.filter(state=state_data[0].state)
        # print(sta_data)
        # print(state_data[0].state)
        # print(sta_cnt)
        temp_score = 0.0
        for j in range(0, sta_cnt):
            # print(sta_data[j].score)
            temp_score += sta_data[j].score
        # print(temp_score)
        scoring_state_wise.objects.filter(
            state=state_data[0].state).update(score=temp_score)
    return JsonResponse({'success': 'fail'})

@api_view(['POST'])
def get_score_college_wise(request):
    temp = JSONParser().parse(request)
    tmp = temp.get('GET')
    count = clg_score.objects.all().count()
    # data=clg_score.objects.all()
    frnt_data = dict()
    # print(frnt_data)
    for i in range(1, count+1):
        data = clg_score.objects.filter(id=i)
        temp_data = list()
        temp_data.append(data[0].college_name)
        temp_data.append(data[0].state)
        temp_data.append(data[0].district)
        temp_data.append(data[0].score)
        frnt_data[i] = temp_data
        del temp_data
    # print(frnt_data)
    # print(tmp)
    return JsonResponse({'data': frnt_data})

@api_view(['POST'])
def get_score_district_wise(request):
    temp = JSONParser().parse(request)
    tmp = temp.get('GET')
    count = scoring_district_wise.objects.all().count()
    # dist_data = scoring_district_wise.objects.all()
    # print(count)
    # print(dist_data)
    frnt_data = dict()
    for i in range(1, count+1):
        data = scoring_district_wise.objects.filter(id=i)
        temp_data = list()
        temp_data.append(data[0].district)
        temp_data.append(data[0].score)
        frnt_data[i] = temp_data
        del temp_data
    # print(frnt_data)
    return JsonResponse({'data': frnt_data})

@api_view(['POST'])
def get_score_state_wise(request):
    temp = JSONParser().parse(request)
    tmp = temp.get('GET')
    count = scoring_state_wise.objects.all().count()
    frnt_data = dict()
    for i in range(1, count+1):
        data = scoring_state_wise.objects.filter(id=i)
        temp_data = list()
        temp_data.append(data[0].state)
        temp_data.append(data[0].score)
        frnt_data[i] = temp_data
        del temp_data
    # print(frnt_data)
    return JsonResponse({'data': frnt_data})

@api_view(['POST'])
def work_sugg(request):
    temp = JSONParser().parse(request)
    tmp = temp.get('GET')
    latlong = temp['long_lat']
    latlong = latlong.translate({ord('('): None},)
    latlong = latlong.translate({ord(')'): None})
    latlong = latlong.translate({ord(','): None})
    latlong = latlong.split()
    latitude = float(latlong[0])
    longitude = float(latlong[1])
    # print("Mouse clicked location :")
    # print(latitude)
    # print(longitude)

    count = clg_score.objects.all().count()
    frnt_data=dict()
    j=0
    for i in range(1,count+1):        
        valid_clg=list()
        data = clg_score.objects.filter(id=i)
        # driver code
        # print("college location")
        # print(data[0].latitude)
        # print(data[0].longitude)
        lat1 = latitude
        lon1 = longitude
        lat2 = data[0].latitude
        lon2 = data[0].longitude
        cal_dist = distance(lat1, lat2, lon1, lon2)
        # print(str(cal_dist)+ " K.M")
        if cal_dist<100:
            j+=1
            print("College VALID")
            valid_clg.append(data[0].elsi_clg_id)
            valid_clg.append(data[0].clg_code)
            valid_clg.append(data[0].college_name)
            valid_clg.append(data[0].address)
            valid_clg.append(data[0].state)
            valid_clg.append(data[0].district)
            valid_clg.append(data[0].score)
            frnt_data[j]=valid_clg
            del valid_clg
        # else:
        #     print("NOT VALID")        
    # print(frnt_data)
    return JsonResponse({'data': frnt_data})

# Python 3 program to calculate Distance Between Two Points on Earth
def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
    # calculate the result
    return(c * r)