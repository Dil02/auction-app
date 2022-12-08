from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
import json
from auction.models import Item

from django.http import HttpResponse, HttpRequest, JsonResponse

# Create your views here.

@csrf_exempt
def items_api(request):
    if request.method == "POST":
        # gets the json data from the frontend
        data = json.loads(request.body)
        # Creates new object and adds it to the existing object
        Item.objects.create(
            condition=data['Type'],
            name=data['name'],
            description=data['description'],
            start=data['start'],
            price=data['price'],
            end=data['end'],
            picture=data['picture']
        )
    return JsonResponse({
        'Item': [
            # Gives the data for the object
            Item.to_dict()
            # Transportation.object.all() gets all the transportation objects
            for Item in Item.objects.all()

        ]
    })