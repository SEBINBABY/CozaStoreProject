from django.urls import path
from Frontend import views

urlpatterns = [
    path('HomePage/', views.HomePage, name='HomePage'),
    path('ProductsPage/<catname>/', views.ProductsPage, name='ProductsPage'),
    path('ContactPage/', views.ContactPage, name='ContactPage'),
    path('ContactPageSave/', views.ContactPageSave, name='ContactPageSave'),
    path('AboutPage/', views.AboutPage, name='AboutPage'),
    path('SingleProduct/<int:proid>/', views.SingleProduct, name='SingleProduct'),


    path('LoginSignUp/', views.LoginSignUp, name='LoginSignUp'),
    path('UserRegistrationDBsave/', views.UserRegistrationDBsave, name='UserRegistrationDBsave'),
    path('UserLogin/', views.UserLogin, name='UserLogin'),
    path('UserLogout/', views.UserLogout, name='UserLogout'),


    path('FrontendBlog/', views.FrontendBlog, name='FrontendBlog'),
    path('BlogSingle/<int:blogid>/', views.BlogSingle, name='BlogSingle'),

    path('CartDBSave/', views.CartDBSave, name='CartDBSave'),
    path('cartPage/', views.cartPage, name='cartPage'),
    path('Checkout/', views.Checkout, name='Checkout'),
    path('CheckoutDBsave/', views.CheckoutDBsave, name='CheckoutDBsave'),
    path('cartDelete/<int:cartid>/', views.cartDelete, name='cartDelete'),

]