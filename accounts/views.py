from accounts.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from accounts.forms import userFormm
from django.contrib.auth.hashers import make_password
from vendor.forms import vendor_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.utlis import send_verification_email

# Create your views here.


def registrationUser(request):
    form = userFormm()

    if request.method == 'POST':
        form = userFormm(request.POST)
        if form.is_valid():
            """
            Below code to retrive the date from which form show on 'HTML' page

            """
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email_address = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_password = User(first_name=first_name, last_name=last_name, password=make_password(
                password), username=username, email=email_address)
            # send_verification_email(request)
            user_password.save()
            list(messages.get_messages(request))
            messages.success(
                request, 'Your accounts has been submitted;')
        else:
            print(form.errors)

    return render(request, 'registrationUser.html', {"form": form})

    # form.save()
    # a=userFormm(
    #     first_name=first_name,
    #     last_name=last_name,
    #     username=username,
    #     email_address=email_address,
    #     password=pas
    # )
    # a.save()


# print(userFormm.objects.all())
"""(Below code use to) cryptography use foe encode any sting"""
# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# fernet = Fernet(key)
# encpassword = fernet.encrypt(password.encode())
# '\npassword:', encpassword,

im = User.objects.all()
# from vendor.forms import user_f


def registerVendorr(request):
    form = vendor_form()
    user = userFormm()
    venDor = {
        "form": form,
        "user": user,
        'dataBase': im
    }
    # from accounts.signals import post_save_user_profile
    if request.method == 'POST':
        form = vendor_form(request.POST, request.FILES)
        user = userFormm(request.POST)
        if form.is_valid():
            # first_name = request.POST['first_name']
            # last_name = request.POST['last_name']
            # password = request.POST['password']
            # confirm_password = request.POST["confirm_password"]
            vendor_name = request.POST['vendor_name']
            vendor_license = request.POST['vendor_license']
            # if first_name and last_name:
            #     # user.objects.create(user=user)
            #     # userprofile= post_save_user_profile
            #     print('user createed')
            #     # userprofile.save()
            #     # user.save()
            #     # form.save()
            # else:
            #     print('User Not CReated')

            # password = make_password(password)
            # confirm_password = make_password(confirm_password)
            print("Success")
            print(
                # 'first_name:', first_name,
                # '\n ''last_name:', last_name,
                # '\n ''password:', password,
                # '\n''confirm_password:', confirm_password,
                '\n' 'vendor name:', vendor_name,
                '\n''vendor license:', vendor_license)
            emailid = request.POST['get_id']
            if emailid:
                print(emailid)
                from vendor.models import vendor_model
                print(
                    '                      -----------------------------------------------                               ')
                # check_email=vendor_model.objects.all()
                # for i in check_email:
                # if i.id == emailid:
                # print(i)
                # messages.error(request,'This Email Already Registered In Anothor Vendor ')
                # else:
                vendor_modl = vendor_model(
                    vendor_name=vendor_name, vendor_license=vendor_license, user_id=emailid)

                vendor_modl.save()
                messages.success(request, 'Thank you for Registration')
            else:
                messages.error(request, 'Please Fill The Form Correctly')
            # form.user_id= emailid
            # form.save()
            # user.save()
            print('success')

        else:
            print(form.errors)
            print(user.errors)

    return render(request, 'registervendor.html', {"form": form, "user": user, 'im': im})


"""vendor views.py :"""
# from django.shortcuts import render
# from vendor.forms import vendor_form
# # Create your views here.
# def registrationVendor(request):
#     # vendor_user = vendorProfileForm
#     vendor_forms = vendor_form()
#     if request.method == 'POST':
#         vendor_forms=vendor_form(request.POST)
#     # return render(request, 'registervendor.html', {"form":vendor_forms,'form1':vendor_user})

"# messages in django?"
# def contact(request):
#     if request.method == 'POST':
#         ...
#         list(messages.get_messages(request))
#         messages.success(request, &quot;Your message has been submitted.&quot;)
#     return render(request, 'contact/contact.html')


def user_login(request):
    if request.user.is_authenticated:
        messages.error(request, "you are already logged in first log out")
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # check=True

                if login and user.role == 1:
                    # messages.success(request,"login succesful...!!")
                    return HttpResponseRedirect(reverse("accounts:user_dashboard"))
                elif login and user.role == 2:
                    return HttpResponseRedirect(reverse("accounts:cus_dashboard"))
                # elif login and user.role == None:
                #     return HttpResponseRedirect(reverse("accounts:dashboard2"), {'email': email, })
                else:
                    return HttpResponseRedirect(reverse("accounts:cus_dashboard"))
                #     return HttpResponseRedirect(reverse('admin'))
            else:
                return HttpResponse('User Is Not Activate')
        else:
            # return HttpResponse('Please Give Correct Id Password')
            messages.error(request, 'Please Give Correct Email And Password')
    # if check:
    #     messages.warning(request,"you are already logged in first log out")
    # else:
    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def dashboard2(request):
    return render(request, 'dashboard2.html')
