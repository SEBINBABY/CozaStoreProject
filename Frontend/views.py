from django.shortcuts import render, redirect
from Backend.models import ProdcutDB, CategoryDB, BlogDB
from Frontend.models import ContactDB, UserRegistrationDB, cartdbsave, CheckoutDB
from django.contrib import messages

# Create your views here.

def HomePage(request):
    products = ProdcutDB.objects.all()
    categories = CategoryDB.objects.all()
    cart = cartdbsave.objects.filter(usrname=request.session['NAME'])
    return render(request, 'HomePage.html', {'products':products, 'categories':categories, 'cart':cart})

def ProductsPage(request, catname):
    cart = cartdbsave.objects.filter(usrname=request.session['NAME'])
    products = ProdcutDB.objects.filter(CATEGORY=catname)
    categories = CategoryDB.objects.all()
    return render(request, 'ShopProducts.html', {'products':products,'cart':cart, 'categories':categories})

def ContactPage(request):
    cart = cartdbsave.objects.filter(usrname=request.session['NAME'])
    categories = CategoryDB.objects.all()
    return render(request, 'ContactPage.html', {'cart':cart, 'categories':categories})

def ContactPageSave(request):
    if request.method == 'POST':
        nm = request.POST.get('Name')
        email = request.POST.get('Email')
        msg = request.POST.get('Message')
        obj = ContactDB(NAME=nm, EMAIL=email, MESSAGE=msg)
        obj.save()
        return redirect(ContactPage)

def AboutPage(request):
    cart = cartdbsave.objects.filter(usrname=request.session['NAME'])
    categories = CategoryDB.objects.all()
    return render(request, 'AboutPage.html', {'cart':cart, 'categories':categories})

def SingleProduct(request, proid):
    cart = cartdbsave.objects.filter(usrname=request.session['NAME'])
    product = ProdcutDB.objects.get(id=proid)
    categories = CategoryDB.objects.all()
    return render(request, 'SingleProduct.html', {'product':product,'cart':cart,  'categories':categories})

def LoginSignUp(request):
    return render(request, 'User_Login.html')

def UserRegistrationDBsave(request):
    if request.method == "POST":
        nm = request.POST.get('UserName')
        email = request.POST.get('Email')
        pwd = request.POST.get('Password')
        obj = UserRegistrationDB(NAME=nm, EMAIL=email, PASSWORD=pwd)
        obj.save()
        return redirect(LoginSignUp)

def UserLogin(request):
    if request.method == "POST":
        unm = request.POST.get("LoginName")
        pwd = request.POST.get("LoginPassword")
        if UserRegistrationDB.objects.filter(NAME=unm, PASSWORD=pwd).exists():
            request.session['NAME'] = unm
            request.session['PASSWORD'] = pwd
            return redirect(HomePage)
        else:
            return redirect(LoginSignUp)
    else:
        return redirect(LoginSignUp)

def UserLogout(request):
    del request.session['NAME']
    del request.session['PASSWORD']
    return redirect(LoginSignUp)

def FrontendBlog(request):
    cart = cartdbsave.objects.filter(usrname=request.session['NAME'])
    blog = BlogDB.objects.all()
    categories = CategoryDB.objects.all()
    return render(request, 'FrontendBlogDisplay.html', {'blog':blog, 'cart':cart,  'categories':categories})

def BlogSingle(request, blogid):
    cart = cartdbsave.objects.filter(usrname=request.session['NAME'])
    blog = BlogDB.objects.get(id=blogid)
    categories = CategoryDB.objects.all()
    return render(request, 'BlogSingle.html', {'blog':blog, 'cart':cart, 'categories':categories })

def CartDBSave(request):
    if request.method == "POST":
        siz = request.POST.get("size")
        username = request.POST.get("Usrname")
        productname = request.POST.get("Prodname")
        prodPRICE = request.POST.get("Prodprice")
        QUANT = request.POST.get("qnty")
        TOTALPr = request.POST.get("TotalPrice")
        obj = cartdbsave(size=siz,usrname=username, prodname=productname, qnty=QUANT, price=prodPRICE,
                                        totalprice=TOTALPr)
        obj.save()
        messages.success(request, "Added to Cart Successfully")
        return redirect(HomePage)

def cartPage(request):
    cart = cartdbsave.objects.filter(usrname=request.session['NAME'])
    categories = CategoryDB.objects.all()
    total_price = 0
    for i in cart:
        total_price = total_price + i.totalprice
    return render(request, 'cart.html', {'cart':cart, 'total_price':total_price,  'categories':categories})

def cartDelete(request,cartid):
    cart = cartdbsave.objects.filter(id=cartid)
    cart.delete()
    return redirect(cartPage)

def Checkout(request):
    cart = cartdbsave.objects.filter(usrname=request.session['NAME'])
    categories = CategoryDB.objects.all()
    total_price = 0
    for i in cart:
        total_price = total_price + i.totalprice
    return render(request, 'Checkout.html', {'cart': cart, 'total_price': total_price, 'categories':categories})

def CheckoutDBsave(request):
    if request.method == "POST":
        nmfirst = request.POST.get('firstname')
        nmlast = request.POST.get('lastname')
        countr = request.POST.get('country')
        addr = request.POST.get('address')
        city1 = request.POST.get('city')
        pncode = request.POST.get('pincode')
        mob = request.POST.get('mobile')
        Em = request.POST.get('email')
        obj = CheckoutDB(firstnm=nmfirst, lastnm=nmlast, country=countr, address=addr, city=city1, pincode=pncode,
                         phone=mob, email=Em)
        obj.save()
        messages.success(request, "Order Placed Successfully")
        return redirect(Checkout)


