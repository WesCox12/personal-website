from django.shortcuts import render

tasks = [
    {"title": "Finish Week 1", "done": True},
    {"title": "Get an Oil Change", "done": True},
    {"title": "Respond to Emails", "done": False},
    {"title": "Pay Rent", "done": True},
    {"title": "Buy a Lamborghini", "done": False},
]
# Create your views here.
def home(request):
    return render(request, "home.html", {"tasks": tasks})
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
