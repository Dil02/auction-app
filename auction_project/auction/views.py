from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, authenticate, logout
from auction.forms import RegistrationForm, AccountAuthenticationForm
import json
from .models import *
from datetime import date
# Create your views here.

#Note : 1. get_object_or_404 will mean 404 will happen if an object can't be found with its ID
#       2. Need to check if Username passwords are automatically hashed by abstract user or if they want us to do it, they're already hashed from looking at the admin page
#       3. Add/Change stuff in Post/Put to make inputs work (sometimes dates/time recieved needs to be formatted before database accepts it)

@csrf_exempt
def users_api(request : HttpRequest) ->JsonResponse:
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
        user = User.objects.create(username=username, password=password, email=email, fname=fname, sname=sname)
        return JsonResponse(user.to_dict())

@csrf_exempt
def user_api(request : HttpRequest, userID : int)->JsonResponse:
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


@csrf_exempt
def items_api(request : HttpRequest) ->JsonResponse:
    """API handling all items. GET request returns JSON of all objects. POST request adds new item record and returns it."""
    if request.method == 'GET':
        return JsonResponse({
            'items': [
                item.to_dict()
                for item in Item.objects.all()
            ]
        })

    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data["name"]
        description = data["description"]
        condition = data["condition"]
        price = data["price"]
        start = data["start"]
        end = data["end"]
        picture = data["picture"]
        sold = data["sold"]
        #ownerID = data["owner"]
        #owner = get_object_or_404(User, id=ownerID)
        owner = User.objects.first()        
        item = Item.objects.create(name=name, description=description, condition=condition, price=price, start=start, end=end, picture=picture, sold=sold, owner=owner)
        return JsonResponse(item.to_dict())

@csrf_exempt
def item_api(request : HttpRequest, itemID : int)->JsonResponse:
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
        #ownerID = data["owner"]

        #owner = get_object_or_404(User, id=ownerID)
        owner = User.objects.first()

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

@csrf_exempt
def available_items(request:HttpRequest, query:str="")->JsonResponse:

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


@csrf_exempt
def bids_api(request: HttpRequest)->JsonResponse:
    """API handling all bids. GET request returns JSON of all objects. POST request adds new bid record and returns it."""
    if request.method == 'GET':
        return JsonResponse({
            'bids': [
                bid.to_dict()
                for bid in Bid.objects.all()
            ]
        })

    elif request.method == 'POST':
        body = json.loads(request.body)
        data = body["data"]
        time = data["time"]
        amount = data["amount"]
        bidderID = data["bidder"]
        itemID = data["item"]

        bidder = get_object_or_404(User, id=bidderID)
        item = get_object_or_404(Item, id=itemID)

        bid = Bid.objects.create(bidder=bidder, item=item, time=time, amount=amount)
        return JsonResponse(bid.to_dict())

@csrf_exempt
def bid_api(request:HttpRequest, bidID:int)->JsonResponse:
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
        bidderID = data["bidder"]
        itemID = data["item"]

        bidder = get_object_or_404(User, id=bidderID)
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

@csrf_exempt
def questions_api(request:HttpRequest)->JsonResponse:
    """API handling all questions. GET request returns JSON of all objects. POST request adds new question record and returns it."""
    if request.method == 'GET':
        return JsonResponse({
            'questions': [
                question.to_dict()
                for question in Bid.objects.all()
            ]
        })

    elif request.method == 'POST':
        body = json.loads(request.body)
        data = body["data"]
        title = data["title"]
        description = data["description"]
        response = data["response"]
        itemID = data["item"]
        questionerID = data["questioner"]

        item = get_object_or_404(Item, id=itemID)
        questioner = get_object_or_404(User, id=questionerID)

        question = Question.objects.create(title=title, description=description,response=response,item=item,questioner=questioner)
        return JsonResponse(question.to_dict())

@csrf_exempt
def item_questions_api(request:HttpRequest, itemID:int)->JsonResponse:
    """API returning questions for the ID of an item."""
    if request.method == 'GET':
        givenItem = get_object_or_404(Item, id=itemID)
        return JsonResponse({
            'questions': [
                question.to_dict()
                for question in Question.objects.filter(item=givenItem)
            ]
        })
    

@csrf_exempt
def question_api(request:HttpRequest, questionID:int)->JsonResponse:
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
        body = json.loads(request.body)
        data = body["data"]
        title = data["title"]
        description = data["description"]
        response = data["response"]
        itemID = data["item"]
        questionerID = data["questioner"]

        item = get_object_or_404(Item, id=itemID)
        questioner = get_object_or_404(User, id=questionerID)

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

@csrf_exempt
def profileImage_api(request: HttpRequest, userID : int)->JsonResponse:        
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
    
def registerPage(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            account = form.save()
            email1 = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            #account = authenticate(email=email1, password=raw_password)
            login(request, account)
            return redirect('register')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)

@csrf_exempt
def loginPage(request):
    context = {}
    
    # user = request.user
    # if user.is_authenticated:
    #     return redirect('register')
    
    # if request.POST:
    #     form = AccountAuthenticationForm(request.POST)
    #     if form.is_valid():
    #         email = request.POST['email']
    #         password = request.POST['password']
    #         user = authenticate(request, email=email, password=password)
            
    #         if user:
    #             login(request, user)
    #             return redirect('register')
    # else:
    #     form = AccountAuthenticationForm()
        
    # context['login_form'] = form
    # return render(request, 'accounts/login.html', context)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('register')
        
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('register')
