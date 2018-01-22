from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage
from django.db import connection

# Create your views here.
def index(request):
    # return HttpResponse('<h2>Hello!! How are you<h2>')
    users = [{'Name':'Jack','Age':36,'email':'Jack@gmail.com'},
             {'Name':'Annie','Age':20,'email':'Annie@gmail.com'},
             {'Name':'Chen','Age':64,'email':'Chen@gmail.com'}]

    return render(request,'home/main.html',{'title':'首頁','users':users,'Name':'Jack'})
    # return render(request,'home/main.html',{'title':'首頁','users':users})


def about(request):
    if request.method == 'POST':
        email = request.POST['email']
        Name = request.POST['namee']
    
    title = '關於我們'
    return render(request,'home/about.html',locals())
def contact(request):
    title = '聯絡我們'
    return render(request,'home/contact.html',locals())
def test(request):
    return render(request,'home/test.html')
def test2(request):
    title = '車款介紹'
    return render(request,'home/test2.html')

def contact1(request,name):
    
    title = '聯絡' + name
    return render(request,'home/contact1.html',locals())

def upload(request):
    if request.method == "POST" and request.FILES["myfile"]:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save(myfile.name,myfile)

    title = '檔案上傳'
    return render(request,'home/upload.html',locals())

def Pagehome(request):
    return render(request,'home/Pagehome.html', locals())


def model(request):
    return render(request,'home/model.html', locals())
def price(request):
    return render(request,'home/price.html', locals())
def service(request):
    return render(request,'home/service.html', locals())
def area(request):
    return render(request,'home/area.html', locals())
def logins(request):
    return render(request,'home/logins.html')
def signup(request):
    return render(request,'home/signup.html')

def signupcheck(request):
    # 接收參數
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        address = request.POST["address"]
        phone = request.POST["phone"]

        # 處理過程
        member = selectSingle("select * from carmember where email=%s",(email,))
        if not member:
            insert("""INSERT INTO carmember(name,password,
                            email,address,phone)
                                VALUES(%s,%s,%s,%s,%s)""",(name,password,email,address,phone))
        # Member.objects.create(name=Name,password=password,useremail=useremail,userbirth=userbirth)
            return redirect("/logins")
        
        else:
            return HttpResponse("<script>alert('此Email已註冊');location.href='/signup'</script>")
       
       # 回復結果
    # title = "會員新增" 
    # return render(request,'lo',locals())


def loginscheck(request):
    # 接收參數
    if request.method == "POST":
        email = request.POST['email']
        pwrd = request.POST['password']

        # 處理過程
        member = selectSingle("select * from carmember where email=%s and password=%s",(email,pwrd))
        result = True

        if member:
            name = member[1]
        else:
            result = False

        # 回復結果
        # location.href='/price'
            
        if result:
            response = HttpResponse("<script>alert('login success');location.href='/Pagehome'</script>")
            if 'rememberme' in request.POST.keys() and request.POST['rememberme']:
                expiresdate = datetime.datetime.now() + datetime.timedelta(days=7)
                response.set_cookie("name", name, expires=expiresdate)
                response.set_cookie("email", email, expires=expiresdate)
            else:
                response.set_cookie("name", name)
                response.set_cookie("email", email)
                
            return response
        else :   
            return HttpResponse("<script>alert('login failed');location.href='/logins'</script>")
    else :
        return HttpResponse("<script>alert('method error');location.href='/logins'</script>")

def logouts(request):
    response = HttpResponse("<script>alert('登出');location.href='/Pagehome'</script>")
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response

def checkorder(request):

    # 接收參數
    if request.method == "POST":
        model = request.POST['model']
        days = int(request.POST['days'])
        area = request.POST['area']
        returnarea = request.POST['returnarea']

    # 處理過程
    
    if 'email' in request.COOKIES:
        email = request.COOKIES['email']
        member = selectSingle("select * from carmember where email=%s",(email,))
        
        if member:
            insert("""INSERT INTO carorder(model,days,area,returnarea,email) VALUES (%s,%s,%s,%s,%s)""", tuple([model,days,area,returnarea,email]))    
            # 回復結果
            responseString = "已接收訂單，會有專人與您聯絡, model:%s, days:%s , area:%s, returnarea:%s, email:%s" % (model,days,area,returnarea,email)
            return HttpResponse("<script>alert('"+ responseString +"');location.href='/Pagehome'</script>")
        
    responseString = "請先加入會員"
    return HttpResponse("<script>alert('"+ responseString +"');location.href='/signup'</script>")

def selectAll(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        datas = cursor.fetchall()
    return datas

def selectSingle(sql, data):
    with connection.cursor() as cursor:
        cursor.execute(sql, data)
        data = cursor.fetchone()
    return data

def insert(sql, data):
    with connection.cursor() as cursor:
        # sql = """INSERT INTO product(CategoryID,ModelNumber,ModelName,UnitCost,ProductImage,Description)
        #             VALUES(%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, data)

def update(sql, data):
    with connection.cursor() as cursor:
        # sql = """UPDATE product set CategoryID=%s,ModelNumber=%s,ModelName=%s,UnitCost=%s,ProductImage=%s,Description=%s
        #             where productid=%s"""
        cursor.execute(sql, data)

def delete(sql, data):
    with connection.cursor() as cursor:
        # sql = "delete from product where productid=%s"
        cursor.execute(sql, data)