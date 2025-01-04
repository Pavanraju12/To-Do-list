from django.shortcuts import render,redirect


from django.contrib.auth.decorators import login_required

# Create your views here.
 
from .models import ToDoItem

@login_required(login_url="login")

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        
        ToDoItem.objects.create(name=name, description=description,user=request.user)
        print("success")
        return redirect('todolist')
    
    return render(request, 'home.html')

def todolist(request):
    items = ToDoItem.objects.filter(reviewed=False,user=request.user)
    details = None 
    if request.method == 'POST' and 'name' in request.POST:
        account_no = request.POST['name']
        
        # Try to fetch the bank account details by account number
        try:
            items = ToDoItem.objects.filter(name=account_no)
        except ToDoItem.DoesNotExist:
            items = None 
    return render(request, 'todolist.html', {'items': items,'search_visible': True})

def history(request):
    items = ToDoItem.objects.filter(reviewed=True)
    return render(request, 'history.html', {'items': items})
def contact(request):
     return render(request, 'contact.html')

def mark_as_reviewed(request, pk):
    item = ToDoItem.objects.get(pk=pk)
    item.reviewed = True
    item.save()
    return redirect('todolist')

def delete_item(request, pk):
    item = ToDoItem.objects.get(pk=pk)
    item.delete()
    return redirect('history')
