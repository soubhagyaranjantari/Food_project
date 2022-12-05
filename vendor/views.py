from django.shortcuts import render
from accounts.forms import userFormm
from django.contrib.auth.hashers import make_password
from vendor.forms import vendor_form
from django.contrib import messages

# def registerVendorr(request):
#     form = vendor_form()
#     user = userFormm()
#     venDor={
#         "form":form,
#         "user":user
#     }
#     if request.method == 'POST':
#         form=vendor_form(request.POST)
#         user=userFormm(request.POST)
#         if form.is_valid():
#             first_name = request.POST['first_name']    
#             last_name = request.POST['last_name']
#             vendor_name = request.POST['vendor_name']
#             vendor_license = request.POST['vendor_license']
#             password = request.POST['password']
#             confirm_password = request.POST["confirm_password"]
#             # password = make_password(password)
#             # confirm_password = make_password(confirm_password)
#             print("Success")
#             print(
#                 'first_name:', first_name,
#                 '\n ''last_name:', last_name,
#                 '\n ''password:',password,
#                 '\n''confirm_password:',confirm_password,
#                 '\n' 'vendor name:',vendor_name,
#                 '\n''vendor license:',vendor_license)
#             # user.save()
#             # form.save()
#         else:
#             print(form.errors)
#             print(user.errors)
        
#     return render(request,'registervendor.html',context=venDor)
    