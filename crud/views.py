from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    student = User.objects.all()
    form = StudentRegistration()
    context = {
        'form':form,
        'student':student,
    }
    return render(request, 'base.html', context)

def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid= request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if(sid == ''):
                usr = User(
                    name = name,
                    email = email,
                    password = password
                )
            else:
                usr = User(
                    id = sid,
                    name = name,
                    email = email,
                    password = password
                )

            usr.save()
            student = User.objects.values()
            student_data = list(student)
            return JsonResponse({
                'status':'Successfully save',
                'student_data':student_data
            })
        else:
            return JsonResponse({
                'status':'Error Saving Data'
            })

def delete_data(request):
    if request.method == "POST":
        id = request.POST['sid']
        stu = User.objects.get(pk=id)
        stu.delete()
        
        return JsonResponse({
                'status':'Deleted Successfully',
                
            })
    else:
            return JsonResponse({
                'status':'Error Deleted Data'
            })

def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        stu = User.objects.get(pk=id)
        student_data = {
            'id':stu.id,
            'name':stu.name,
            'email':stu.email,
            'password':stu.password
        }
        return JsonResponse(student_data);
    

