from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from.forms import SignUpForm,AddRecordForm
from.models import Record

# Create your views here.
def home(request):
    records=Record.objects.all()
    #check to see if the user is logged in
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        #authenticate the user
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have logged in successfully")
            return redirect('home')
        else:
            messages.success(request,"There was an error in Logging it .please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {"records":records})

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        #check for record with id
        customer=Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer})
    else:
        messages.success(request,"you must have been logged in to see the record..")
        return redirect('home')
def delete_record(request,pk):
    if request.user.is_authenticated:
        customer=Record.objects.get(id=pk)
        customer.delete()
        messages.success(request,"record Deleted successfully")
        return redirect('home')
    else:
        messages.success(request,"this id does not exist")
        return render('home')
def Add_record(request):
    form=AddRecordForm(request.POST)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                add_form=form.save()
                messages.success(request,"record added successfully")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"you must be logged in")
        return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

