from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, authenticate, logout
from auction.forms import RegistrationForm, AccountAuthenticationForm
import json
from .models import *
from datetime import date
from datetime import datetime
from django.core.mail import send_mail
from typing import Union, Optional
# Create your views here.

#Note : 1. get_object_or_404 will mean 404 will happen if an object can't be found with its ID
#       2. Need to check if Username passwords are automatically hashed by abstract user or if they want us to do it, they're already hashed from looking at the admin page
#       3. Add/Change stuff in Post/Put to make inputs work (sometimes dates/time recieved needs to be formatted before database accepts it)


def users_api(request : HttpRequest) ->Union[JsonResponse,HttpResponse]:
    """API handling all users. GET request returns JSON of all objects. POST request adds new user record and returns it."""
    if request.method == 'GET':
        return JsonResponse({
            'user': [
                user.to_dict()
                for user in User.objects.all()
            ]
        })

    elif request.method == 'POST':
        body = json.loads(request.body)
        data = body["data"]
        username = data["username"]
        password = data["password"]
        email = data["email"]
        fname = data["fname"]
        sname = data["sname"]
        city=data["city"]
        dob=data["dob"]
    # Create a model instance and set the value of the image field
        user = User.objects.create(username=username, password=password, email=email, fname=fname, sname=sname,city=city,dob=dob)
        user.picture.name="default.png"
        user.save()
        return JsonResponse(user.to_dict())

    return HttpResponse("")

def user_api(request : HttpRequest, userID : int)->Union[JsonResponse,HttpResponse]:
    """API handling an individual User, an integer ID of the User must be passed. GET returns User with ID specified. DELETE removes User with ID specified. PUT updates User with ID specified."""
    user = get_object_or_404(User, id=userID)

    if request.method == "GET":
        return JsonResponse({
            'user': user.to_dict()
        })
    elif request.method == "DELETE":
        user.delete()
        return HttpResponse("")

    elif request.method == "PUT":
        #Data is retrieved from request body
        body = json.loads(request.body)
        data = body["data"]
        username = data["username"]
        #password = data["password"]
        email = data["email"]
        fname = data["fname"]
        sname = data["sname"]
        dob = data["dob"]
        city = data["city"]


        #Data of user object is reassigned to passed values
        user.username = username
        #user.password = password
        user.email = email
        user.first_name = fname 
        user.last_name = sname 
        user.dob = dob
        user.city = city
        user.save()

        return JsonResponse({
            'User': user.to_dict()
        })

    return HttpResponse("")


def sessionUser(request: HttpRequest)->Union[JsonResponse,HttpResponse]:
    """Returns the JSON of the User the session corresponds to. None if no session exists"""
    
    if request.method == 'GET':
        userId = request.session.get('_auth_user_id')
        try:
            sessionUser = User.objects.filter(id=userId)[0]
        except IndexError:
            return JsonResponse({
                'User': "None"
            })
        
        return JsonResponse({
            'User':
                sessionUser.to_dict()
        })

    return HttpResponse("")

def items_api(request : HttpRequest)->Union[JsonResponse,HttpResponse]:
    """API handling all items. GET request returns JSON of all objects. POST request adds new item record and returns it."""
    if request.method == 'GET':
        return JsonResponse({
            'items': [
                item.to_dict()
                for item in Item.objects.all()
            ]
        })

    elif request.method == 'POST':
        name = request.POST["name"]
        description = request.POST["description"]
        condition = request.POST["condition"]
        price = request.POST["price"]
        start = request.POST["startDate"]
        end = request.POST["endDate"]
        userId = request.session.get('_auth_user_id')
        owner = get_object_or_404(User, id=userId)

        item = Item.objects.create(name=name, description=description, condition=condition, price=price, start=start, end=end, owner=owner)

        uploaded_file = request.FILES['myFile']
        item.picture=uploaded_file
        item.save()

        return JsonResponse({
            'item': [
                item.to_dict()
            ]
        })

    return HttpResponse("")

def emailWinners(request:HttpRequest)->HttpResponse:
    #Retrieve items that end today
    today = datetime.now().strftime('%Y-%m-%d')
    items = Item.objects.filter(end=today)

    #
    for item in items:
        latest_bid = Bid.objects.filter(item=item).order_by('-time').first()
        if latest_bid != None:
            print(latest_bid)
            winner = latest_bid.bidder
            send_mail(
                'Auction Winner',
                'Congratulations, You have won the auction for "{}"'.format(item.name),
                'group7auction@gmail.com',
                [winner.email],
                fail_silently=False,
            )

    return HttpResponse("Finished")



def item_api(request : HttpRequest, itemID : int)->Union[JsonResponse,HttpResponse]:
    """API handling individual item, an integer ID of the item must be passed. GET returns item with ID specified. DELETE removes item with ID specified. PUT updates item with ID specified."""
    item = get_object_or_404(Item, id=itemID)

    if request.method == "GET":
        return JsonResponse({
            'item': item.to_dict()
        })
    elif request.method == "DELETE":
        item.delete()
        return HttpResponse("")

    elif request.method == "PUT":
        #Data is retrieved from request body
        data = json.loads(request.body)
        name = data["name"]
        description = data["description"]
        condition = data["condition"]
        price = data["price"]
        start = data["start"]
        end = data["end"]
        picture = data["picture"]
        sold = data["sold"]
        userId = request.session.get('_auth_user_id')
        owner = get_object_or_404(User, id=userId)

        #Data of item object is reassigned to passed values
        item.name = name
        item.description = description
        item.condition = condition
        item.price = price
        item.start = start
        item.end = end
        item.picture = picture
        item.sold = sold
        item.owner = owner
        item.save()

        return JsonResponse({
            'item': item.to_dict()
        })

    return HttpResponse("")

def available_items(request:HttpRequest, query:str="")->Union[JsonResponse]:

    today = date.today()
    available = Item.objects.filter(start__lte=today).filter(end__gte=today).filter(sold=False)
    if query != "":
        available = available.filter(name__contains=query) | available.filter(description__contains=query)

    return JsonResponse({
        'items': [
            item.to_dict()
            for item in available
        ]
    })



def bids_api(request: HttpRequest)->Union[JsonResponse,HttpResponse]:
    """API handling all bids. GET request returns JSON of all objects. POST request adds new bid record and returns it."""
    if request.method == 'GET':
        return JsonResponse({
            'bids': [
                bid.to_dict()
                for bid in Bid.objects.all()
            ]
        })

    elif request.method == 'POST':
        data = json.loads(request.body)
        time = datetime.now()
        amount = data["amount"]
        itemID = data["itemId"]

        userId = request.session.get('_auth_user_id')
        bidder = get_object_or_404(User, id=userId)
        item = get_object_or_404(Item, id=itemID)
        item.price = amount
        item.save()
        bid = Bid.objects.create(bidder=bidder, item=item, time=time, amount=amount)

        return JsonResponse(bid.to_dict())

    return HttpResponse("")

def bid_api(request:HttpRequest, bidID:int)->Union[JsonResponse,HttpResponse]:
    """API handling individual bid, an integer ID of the bid must be passed. GET returns bid with ID specified. DELETE removes bid with ID specified. PUT updates bid with ID specified."""
    bid = get_object_or_404(Bid, id=bidID)

    if request.method == "GET":
        return JsonResponse({
            'bid': bid.to_dict()
        })
    elif request.method == "DELETE":
        bid.delete()
        return HttpResponse("")

    elif request.method == "PUT":
        #Data is retrieved from request body
        body = json.loads(request.body)
        data = body["data"]
        time = data["time"]
        amount = data["amount"]
        userId = request.session.get('_auth_user_id')
        itemID = data["item"]

        bidder = get_object_or_404(User, id=userId)
        item = get_object_or_404(Item, id=itemID)

        #Data of bid object is reassigned to passed values
        bid.bidder = bidder
        bid.item = item
        bid.time = time
        bid.amount = amount
        bid.save()

        return JsonResponse({
            'bid': bid.to_dict()
        })

    return HttpResponse("")


def questions_api(request:HttpRequest)->Union[JsonResponse,HttpResponse]:
    """API handling all questions. GET request returns JSON of all objects. POST request adds new question record and returns it."""
    if request.method == 'GET':
        return JsonResponse({
            'questions': [
                question.to_dict()
                for question in Bid.objects.all()
            ]
        })

    elif request.method == 'POST':
        data=json.loads(request.body)
        title = data["title"]
        description = data["description"]
        response = data["response"]
        itemID = data["item"]
        userId = request.session.get('_auth_user_id')
        
        item = get_object_or_404(Item, id=itemID)
        questioner = get_object_or_404(User, id=userId)

        question = Question.objects.create(title=title, description=description,response=response,item=item,questioner=questioner)
        return JsonResponse(question.to_dict())

    return HttpResponse("")


def item_questions_api(request:HttpRequest, itemID:int)->Union[JsonResponse,HttpResponse]:
    """API returning questions for the ID of the given item."""
    if request.method == 'GET':
        givenItem = get_object_or_404(Item, id=itemID)
        return JsonResponse({
            'questions': [
                question.to_dict()
                for question in Question.objects.filter(item=givenItem)
            ]
        })
    
    return HttpResponse("")

def item_bids_api(request:HttpRequest, itemID:int)->Union[JsonResponse,HttpResponse]:
    """API returning bids for the ID of the given item"""
    if request.method == 'GET':
        givenItem = get_object_or_404(Item, id=itemID)
        
        return JsonResponse({
          'bids': [
            bid.to_dict()
            for bid in Bid.objects.filter(item=givenItem).order_by('-time')
          ]  
        })

    return HttpResponse("")

def question_api(request:HttpRequest, questionID:int)->Union[JsonResponse,HttpResponse]:
    """API handling individual question, an integer ID of the question must be passed. GET returns question with ID specified. DELETE removes question with ID specified. PUT updates question with ID specified."""
    question = get_object_or_404(Question, id=questionID)

    if request.method == "GET":
        return JsonResponse({
            'question': question.to_dict()
        })
    elif request.method == "DELETE":
        question.delete()
        return HttpResponse("")

    elif request.method == "PUT":
        #Data is retrieved from request body
        data = json.loads(request.body)
        title = data["title"]
        description = data["description"]
        response = data["response"]
        itemID = data["item"]
        userId = request.session.get('_auth_user_id')

        item = get_object_or_404(Item, id=itemID)
        questioner = get_object_or_404(User, id=userId)

        #Data of question object is reassigned to passed values
        question.title = title
        question.description = description
        question.response = response
        question.item = item
        question.questioner = questioner
        question.save()

        return JsonResponse({
            'question': question.to_dict()
        })

    return HttpResponse("")


def profileImage_api(request: HttpRequest, userID : int)->Union[JsonResponse,HttpResponse]:        
    """API handling of profile picture."""
    user = get_object_or_404(User, id=userID)
    if request.method == 'POST':
        uploaded_file = request.FILES['myFile']
        user.picture=uploaded_file
        user.save()

        return JsonResponse({
            'filename' : uploaded_file.name,

        })

    return HttpResponse("")
    
def registerPage(request:HttpRequest)->Union[HttpResponseRedirect,HttpResponse]:
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            account = form.save()
            email1 = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            #account = authenticate(email=email1, password=raw_password)
            login(request, account)
            response = redirect('http://127.0.0.1:5173/')          
            return response
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)

def loginPage(request:HttpRequest)->Union[HttpResponse, HttpResponseRedirect]:

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            response = redirect('http://127.0.0.1:5173/')          
            return response
            # response = HttpResponse()
            # response.headers['userID']= request.session.get('_auth_user_id')
            # return response
            
        
    return render(request, 'accounts/login.html', {})

def logout_view(request:HttpRequest)->HttpResponseRedirect:
    logout(request)
    return redirect('login')

