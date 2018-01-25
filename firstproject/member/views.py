from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Member

# Create your views here.
def index(request):  
    
    title = "會員管理"

    #todo 讀取會員資料傳給index.html
    members = Member.objects.all()
    # print(members)
    return render(request,'member/index.html',locals())

def create(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        useremail = request.POST["useremail"]
        userbirth = request.POST["userbirth"]

        #todo 接收到的會員資料寫進資料庫
        Member.objects.create(username=username,password=password,useremail=useremail,userbirth=userbirth)
        
        #todo 新增完成後轉到http://localhost:8000/member
        return redirect("/member")
       
    title = "會員新增" 
    return render(request,'member/create.html',locals())

def addmember(request):
    if request.method == 'POST':
        Models = request.POST["Models"]
        Rates  = request.POST["Rates"]
        Dates  = request.POST["Dates"]
        


def update(request,id):
    if request.method == 'POST':        
        username = request.POST["username"]      
        useremail = request.POST["useremail"]
        userbirth = request.POST["userbirth"]

        #todo 修改資料庫中的會員資料
        member = Member.objects.get(id=int(id))
        member.username = username
        member.useremail = useremail
        member.userbirth = userbirth
        member.save()
        #todo 修改完成後轉到http://localhost:8000/member
        return redirect("/member")

    title = "會員修改"
    #todo 根據會員編號取得會員資料傳給update.html
    member = Member.objects.get(id=int(id))

    return render(request,'member/update.html',locals())

def delete(request,id):
    #todo 根據會員編號刪除會員資料
    member = Member.objects.get(id=int(id))
    member.delete()

    #todo 刪除完成後轉到http://localhost:8000/member
    return redirect('/member')

def login(request):  
    if request.method == "POST":
        email = request.POST['useremail']
        pwd = request.POST['userpassword']
        member = Member.objects.filter(useremail=email,password=pwd).values('username')
        
        if member:

            themember = member[0]
            respone = HttpResponse("<script>alert('成功');location.href='/member/'</script>")
            if 'rememberme' in request.POST.keys() and request.POST['rememberme']:
                expiresdate = datetime.datetime.now() + datetime.timedelta(days=7)
                respone.set_cookie("name",themember['username'],expires=expiresdate)
            else:
                respone.set.set_cookie("name",themember['username'])
            return respone            
        else:
            return HttpResponse("<script>alert('帳號或密碼錯誤');location.href='/member/login'</script>")

    title = "會員登入"
    return render(request,'member/login.html',locals())

def logout(request):
    respone = HttpResponse("<script>alert('登出');location.href='/member/login'</script>")
    respone.delete_cookie('name')
    return HttpResponse("登出")
