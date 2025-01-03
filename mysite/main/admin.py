from django.contrib import admin
from .models import ToDoList, Item
from django.contrib.auth import authenticate
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)

username = "alexml"
password = "Trtploergvui1"

user = authenticate(username=username, password=password)
if user is not None and user.is_staff:
    print("Logged in as:", user)
else:
    print("Authentication failed.")
