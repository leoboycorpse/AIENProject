from django.shortcuts import render,redirect
from .modelscategory import Category
from .modelsproduct import Product
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    title = '商品管理'
    product = Product()
    products = product.all()
    return render(request,'product/index.html',locals())

def create(request):

    if request.method == "POST" and request.FILES["productimage"]:
        categoryid = request.POST['categoryid']
        modelnumber = request.POST['modelnumber']
        modelname = request.POST['modelname']
        unitcost = request.POST['unitcost']
        description = request.POST['description']
        
        thefile = request.FILES['productimage']
        productimage = thefile.name
        
        product = Product()
        datas = tuple([categoryid,modelnumber,modelname,unitcost,productimage,description])
        product.create(datas)

        fs = FileSystemStorage()
        fs.save(thefile.name,thefile)
        return redirect('/product')
        



    category = Category()
    datas = category.all()
    title = "商品新增"
    return render(request,'product/create.html',locals())

def update(request,id):
    if request.method == "POST" and request.FILES["productimage"]:
        categoryid = request.POST['categoryid']
        modelnumber = request.POST['modelnumber']
        modelname = request.POST['modelname']
        unitcost = request.POST['unitcost']
        description = request.POST['description']
        
        thefile = request.FILES['productimage']
        productimage = thefile.name
        
        product = Product()
        datas = tuple([categoryid,modelnumber,modelname,unitcost,productimage,description,id])
        product.update(datas)

        fs = FileSystemStorage()
        fs.save(thefile.name,thefile)
        return redirect('/product')

    title = "商品修改"
    category = Category()
    categories = category.all()

    product = Product()
    singleproduct = product.single(id)

    return render(request,'product/update.html',locals())

def delete(request,id):
    product = Product()
    product.delete(id)
    return redirect('/product')
