from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context = {}, status=202)

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consumed by javascript/android/ios/etc...
    return JSON data
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consumed by javascript/android/ios/etc...
    return JSON data
    """

    data = {
        "id": tweet_id,
    }
    status = 200
    try: 
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except: 
        data['message'] = "Not found"
        status = 404 
    
    return JsonResponse(data, status=status)