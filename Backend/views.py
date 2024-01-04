from django.shortcuts import render, redirect
from Backend.models import CategoryDB, ProdcutDB, BlogDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Frontend.models import ContactDB
from django.contrib import messages

# Create your views here.
def indexpage(request):
    return render(request, 'index.html')

def addcategory(request):
    return render(request, 'AddCategory.html')

def categorysave(request):
    if request.method == 'POST':
        nm = request.POST.get('CatName')
        desc = request.POST.get('CatDesc')
        img = request.FILES['CatImage']
        obj = CategoryDB(CATNAME=nm, CATDESC=desc, CATIMAGE=img)
        obj.save()
        messages.success(request, "Category Saved Successfully")
        return redirect(addcategory)

def displaycat(request):
    category = CategoryDB.objects.all()
    return render(request, 'DisplayCategory.html', {'category':category})

def editcategory(request, catid):
    category = CategoryDB.objects.get(id=catid)
    return render(request, 'EditCategory.html', {'category':category})

def updatecategory(request, catid):
    if request.method == 'POST':
        nm = request.POST.get('CatName')
        desc = request.POST.get('CatDesc')
        try:
            img = request.FILES['CatImage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=catid).CATIMAGE
        CategoryDB.objects.filter(id=catid).update(CATNAME=nm, CATDESC=desc, CATIMAGE=file)
        messages.success(request, "Category Updated Successfully")
        return redirect(displaycat)

def deletecategory(request, catid):
    category = CategoryDB.objects.filter(id=catid)
    category.delete()
    messages.error(request, "Category is Deleted")
    return redirect(displaycat)

def addproduct(request):
    category = CategoryDB.objects.all()
    return render(request, 'AddProduct.html', {'category':category})

def productsave(request):
    if request.method == 'POST':
        cat = request.POST.get('CatName')
        pronm = request.POST.get('ProName')
        proprice = request.POST.get('ProPrice')
        prodesc = request.POST.get('ProDesc')
        proimg1 = request.FILES['ProImage1']
        proimg2 = request.FILES['ProImage2']
        obj = ProdcutDB(CATEGORY=cat, PRONAME=pronm, PROPRICE=proprice, PRODESC=prodesc, PROIMAGE=proimg1, PROIMAGE2=proimg2)
        obj.save()
        messages.success(request, "Product Saved Successfully")
        return redirect(addproduct)

def displayproduct(request):
    product = ProdcutDB.objects.all()
    return render(request, 'DisplayProduct.html', {'product':product})

def editproduct(request, proid):
    product = ProdcutDB.objects.get(id=proid)
    category = CategoryDB.objects.all()
    return render(request, 'EditProduct.html', {'product':product,'category':category})

def updateproduct(request, proid):
    if request.method == 'POST':
        catnm = request.POST.get('CatName')
        pronm = request.POST.get('ProName')
        proprice = request.POST.get('ProPrice')
        prodesc = request.POST.get('ProDesc')
        try:
            proimg1 = request.FILES['ProImage1']
            fs1 = FileSystemStorage()
            file1 = fs1.save(proimg1.name, proimg1)
        except MultiValueDictKeyError:
            file1 = ProdcutDB.objects.get(id=proid).PROIMAGE
        try:
            proimg2 = request.FILES['ProImage2']
            fs2 = FileSystemStorage()
            file2 = fs2.save(proimg2.name, proimg2)
        except MultiValueDictKeyError:
            file2 = ProdcutDB.objects.get(id=proid).PROIMAGE2
        ProdcutDB.objects.filter(id=proid).update(CATEGORY=catnm, PRONAME=pronm, PROPRICE=proprice, PRODESC=prodesc,
                                                  PROIMAGE=file1,PROIMAGE2=file2)
        messages.success(request, "Product Updated Successfully")
        return redirect(displayproduct)

def deleteproduct(request, proid):
    product = ProdcutDB.objects.filter(id=proid)
    product.delete()
    messages.error(request, "Product is Deleted")
    return redirect(displayproduct)

def AddBlog(request):
    return render(request, 'AddBlog.html')

def Blogsave(request):
    if request.method == 'POST':
        date = request.POST.get('Date')
        title = request.POST.get('Title')
        s_desc = request.POST.get('ShortDescription')
        f_desc = request.POST.get('FullDescription')
        image = request.FILES['Image']
        obj = BlogDB(DATE=date, TITLE=title, SHORTDESC=s_desc, FULLDESC=f_desc, IMAGE=image)
        obj.save()
        messages.success(request, "Blog Saved Successfully")
        return redirect(AddBlog)

def BlogDisplay(request):
    blog = BlogDB.objects.all()
    return render(request, 'BlogDisplay.html', {'blog':blog})

def editblog(request, blogid):
    blog = BlogDB.objects.get(id=blogid)
    return render(request, 'EditBlog.html', {'blog':blog})

def updateblog(request, blogid ):
    if request.method == 'POST':
        dt = request.POST.get('Date')
        title = request.POST.get('Title')
        s_desc = request.POST.get('ShortDescription')
        f_desc = request.POST.get('FullDescription')
        try:
            image = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file = BlogDB.objects.get(id=blogid).IMAGE
        BlogDB.objects.filter(id=blogid).update(DATE=dt, TITLE=title, SHORTDESC=s_desc, FULLDESC=f_desc, IMAGE=file)
        messages.success(request, "Blog Updated Successfully")
        return redirect(BlogDisplay)

def deleteblog(request, blogid):
    blog = BlogDB.objects.filter(id=blogid)
    blog.delete()
    messages.error(request, "Blog is Deleted")
    return redirect(BlogDisplay)

def adminloginpage(request):
    return render(request, 'adminloginpage.html')

def AdminLogin(request):
    if request.method == 'POST':
        unm = request.POST.get('uname')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=unm).exists():
            user = authenticate(username=unm, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = unm
                request.session['password'] = pwd
                messages.success(request, "Logged in Successfully")
                return redirect(indexpage)
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect(adminloginpage)
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect(adminloginpage)

def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "You have successfully Logged Out")
    return redirect('adminloginpage')

def UserContactDisplay(request):
    contact = ContactDB.objects.all()
    return render(request, 'UserContactDisplay.html', {'contact':contact})

def deletecontact(request, userid):
    contact = ContactDB.objects.filter(id=userid)
    contact.delete()
    messages.error(request, "Customer's Details Deleted")
    return redirect(UserContactDisplay)
