from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate
from datetime import datetime
import time
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.POST:
        username=request.POST['Email']
        Password=request.POST['Password']
        print(username,'##',Password)
        user=authenticate(username=username,password=Password)
        print(user)
        if user is not None:
            # login(request,user)
            if user.usertype=='admin':
                id=user.id
                request.session['uid']=id
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('/adminHome')
            elif user.usertype=='user':
                id=user.id
                request.session['uid']=id
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('/userHome')
            elif user.usertype=='clinic':
                id=user.id
                request.session['uid']=id
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('/clinicHome')
            elif user.usertype=='dogwalker':
                id=user.id
                request.session['uid']=id
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('/dogwalkerHome')
            elif user.usertype=='centre':
                id=user.id
                request.session['uid']=id
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('/carecentreHome')
            elif user.usertype=='shop':
                id=user.id
                request.session['uid']=id
                request.session['type']='shop'
                messages.info(request,"Login Successfull")
                return redirect('/shopHome')
            else:
                messages.info(request,"username or password invalid")
                return redirect('/login')
    return render(request,'login.html')


def customer_Register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['Email']
        password=request.POST['Password']
        Address=request.POST['Address']
        phonenumber=request.POST['phone']
        district=request.POST['district']
        
        if Login.objects.filter(username=email).exists():
            print("user already exists")
            msg="user already exists"
            messages.info(request,msg)
        else:
            q=Login.objects.create_user(username=email,usertype='user',password=password,viewpassword=password)
            q.save()
            regqry=Customer.objects.create(customer_name=name,district=district,email=email,Address=Address,phonenumber=phonenumber,user=q)
            regqry.save()
            msg="Customer Registered Successfully"
            messages.info(request,msg)
            print("msg",msg)
            
        return redirect('/login')

    return render(request,'customer_register.html')
    


def clinic_register(request):
    if request.POST:
        name=request.POST['clinicname']
        email=request.POST['Email']
        password=request.POST['Password']
        Address=request.POST['Address']
        phonenumber=request.POST['phone']
        owned=request.POST['owned_by']
        license_no=request.POST['license']
        district=request.POST['district']
        start=request.POST['start']
        end=request.POST['end']
        
        if clinic.objects.filter(email=email,phonenumber=phonenumber).exists():
            print("user already exists")
            msg="user already exists"
            messages.info(request,msg)
        else:
            q=Login.objects.create_user(username=email,usertype='clinic',password=password,viewpassword=password,is_active=0)
            q.save()
            regqry=clinic.objects.create(clinic_name=name,district=district,starttime=start,Endtime=end,license_no=license_no,email=email,Address=Address,phonenumber=phonenumber,owned_by=owned,user=q)
            regqry.save()
            msg="Veterinary Clinics Registered Suceesfully."
            messages.info(request,msg)
            print("msg",msg)
    
            
        return redirect('/login')

    return render(request,'clinics_register.html')


def dogwalker_register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['Email']
        password=request.POST['Password']
        Address=request.POST['Address']
        phonenumber=request.POST['phone']
        licence_no=request.POST['license']
        district=request.POST['district']
        
        if Dogwalkers.objects.filter(email=email,phonenumber=phonenumber).exists():
            print("user already exists")
            msg="user already exists"
            messages.info(request,msg)
        else:
            q=Login.objects.create_user(username=email,usertype='dogwalker',password=password,viewpassword=password,is_active=0)
            q.save()
            regqry=Dogwalkers.objects.create(name=name,district=district,license_no=licence_no,email=email,Address=Address,phonenumber=phonenumber,user=q)
            regqry.save()
            msg="Dog Walkers Registered Successfully"
            messages.info(request,msg)
            print("msg",msg)
    
            
        return redirect('/login')

    return render(request,'dogwalkers.html')

def carecentre_register(request):
    if request.POST:
        name=request.POST['centrename']
        email=request.POST['Email']
        password=request.POST['Password']
        Address=request.POST['Address']
        phonenumber=request.POST['phone']
        owner=request.POST['owner']
        licence_no=request.POST['license']
        district=request.POST['district']
        if PetcareCentre.objects.filter(email=email,phonenumber=phonenumber).exists():
            print("user already exists")
            msg="user already exists"
            messages.info(request,msg)
        else:
            q=Login.objects.create_user(username=email,usertype='centre',password=password,viewpassword=password,is_active=0)
            q.save()
            regqry=PetcareCentre.objects.create(carecentre=name,district=district,license_no=licence_no,email=email,Address=Address,phonenumber=phonenumber,owner_name=owner,user=q)
            regqry.save()
            msg="Pet Care Centres Registerd Successfully"
            messages.info(request,msg)
            print("msg",msg)
        
        return redirect('/login')

    return render(request,'carecentre_register.html')

def petshop_register(request):
    if request.POST:
        name=request.POST['shopname']
        email=request.POST['Email']
        password=request.POST['Password']
        Address=request.POST['Address']
        phonenumber=request.POST['phone']
        owner=request.POST['ownername']
        licence_no=request.POST['license']
        district=request.POST['district']
        if Petshops.objects.filter(email=email,phonenumber=phonenumber).exists():
            print("user already exists")
            msg="user already exists"
            messages.info(request,msg)
        else:
            q=Login.objects.create_user(username=email,usertype='shop',password=password,viewpassword=password,is_active=0)
            q.save()
            regqry=Petshops.objects.create(shop_name=name,district=district,license_no=licence_no,email=email,Address=Address,phonenumber=phonenumber,owner_name=owner,user=q)
            regqry.save()
            msg="Pet Shops Registered successfully"
            messages.info(request,msg)
            print("msg",msg)
            
        return redirect('/login')

    return render(request,'petshop_register.html')



###################  ADMIN ##################

def adminHome(request):
    return render(request,'Admin/adminHome.html')

def view_dogwalkers_admin(request):
    qry=Dogwalkers.objects.all()
    return render(request,'Admin/dogwalkers_view.html',{'qry':qry})

def view_clinics_admin(request):
    qry=clinic.objects.all()
    return render(request,'Admin/clinics_view.html',{'qry':qry})

def view_carecentres_admin(request):
    qry=PetcareCentre.objects.all()
    return render(request,'Admin/carecentres_view.html',{'qry':qry})

def view_petshops_admin(request):
    qry=Petshops.objects.all()
    return render(request,'Admin/shops_view.html',{'qry':qry})

def view_customer_admin(request):
    qry=Customer.objects.all()
    return render(request,'Admin/customer_view.html',{'qry':qry})



def Delete_user(request):
    id=request.GET.get('id')
    print("44444444444444444444444444444444444444444",id)
    qy=Login.objects.filter(id=id).delete()
    msg="Deleted successfully"
    messages.info(request,msg)
    print("msg",msg)
    return redirect('/view_customer_admin')

def Delete_clinic(request):
    id=request.GET.get('id')
    qy=Login.objects.filter(id=id).delete()
    msg="Deleted successfully"
    messages.info(request,msg)
    print("msg",msg)
    return redirect('/view_clinics_admin')

def Delete_centre(request):
    id=request.GET.get('id')
    qy=Login.objects.filter(id=id).delete()
    msg="Deleted successfully"
    messages.info(request,msg)
    print("msg",msg)
    return redirect('/view_carecentre_admin')

def Delete_shop(request):
    id=request.GET.get('id')
    qy=Login.objects.filter(id=id).delete()
    msg="Deleted successfully"
    messages.info(request,msg)
    print("msg",msg)
    return redirect('/view_petshop_admin')

def Delete_walkers(request):
    id=request.GET.get('id')
    qy=Login.objects.filter(id=id).delete()
    msg="Deleted successfully"
    messages.info(request,msg)
    print("msg",msg)
    return redirect('/view_dogwalker_admin')

def approveclinic(request):
    status=request.GET['status']
    id=request.GET['id']
    clin=Login.objects.get(id=id)
    clin.is_active=int(status)
    clin.save()
    if status == '1':
        messages.info(request,"clinics Approved successfully")
    else:
        messages.info(request,"clinics Rejected successfully")
    return redirect('/view_clinics_admin')

def approvedogwalker(request):
    status=request.GET['status']
    id=request.GET['id']
    clin=Login.objects.get(id=id)
    clin.is_active=int(status)
    clin.save()
    if status == '1':
        messages.info(request,"Dogwalker Approved successfully")
    else:
        messages.info(request,"Dogwalker Rejected successfully")
    return redirect('/view_dogwalker_admin')


def approveshops(request):
    status=request.GET['status']
    id=request.GET['id']
    shop=Login.objects.get(id=id)
    shop.is_active=int(status)
    shop.save()
    if status == '1':
        messages.info(request,"Shops Approved successfully")
    else:
        messages.info(request,"Shops Rejected successfully")
    return redirect('/view_petshop_admin')

def approvecentre(request):
    status=request.GET['status']
    id=request.GET['id']
    ctr=Login.objects.get(id=id)
    ctr.is_active=int(status)
    ctr.save()
    if status == '1':
        messages.info(request,"centers Approved successfully")
    else:
        messages.info(request,"centers Rejected successfully")
    return redirect('/view_carecentre_admin')

def viewcomplaint(request):
    qry=Complaint.objects.all()
    return render(request,'Admin/viewcomplaint.html',{'qry':qry})


#####################  Clinic ######################

def clinicHome(request):
    return render(request,'Clinic/clinicHome.html')

def doctor_register(request):
    uid=request.session['uid']
    if request.POST:
        name=request.POST['name']
        phonenumber=request.POST['phone']
        register_no=request.POST['register']
        qualification=request.POST['qualification']
        clin=clinic.objects.get(user=uid)
        regqry=VeterinaryDoctors.objects.create(name=name,clinic=clin,phonenumber=phonenumber,register_no=register_no,qualification=qualification)
        regqry.save()
        msg="Registered successfully"
        messages.info(request,msg)            
        return redirect('/clinicHome')
    return render(request,'Clinic/vetDoctor_register.html')

def view_doctors(request):
    uid=request.session['uid']
    qry=VeterinaryDoctors.objects.filter(clinic__user_id=uid)
    return render(request,'Clinic/doctor_view.html',{'qry':qry})

def Delete_doctor(request):
    id=request.GET.get('id')
    qy=Login.objects.filter(id=id).delete()
    return redirect('/view_doctor')

def view_doctorbooking(request):
    uid=request.session['uid']
    uuid=clinic.objects.get(user=uid)
    qy=Bookingdoctor.objects.filter(doctor__clinic_id=uuid)
    return render(request,'Clinic/view_doctorbookings.html',{'qy':qy})

def doctor_accept(request):
    id=request.GET.get('id')
    qy=Bookingdoctor.objects.filter(id=id).update(status='Accepted')
    msg="Booking Accepted "
    messages.info(request,msg)
    print("msg",msg)
    return redirect('/view_bookdoctor')

def doctor_reject(request):
    uid=request.session['uid']
    id=request.GET.get('id')
    qy=Bookingdoctor.objects.filter(id=id).update(status='rejected')
    msg="Booking Regected"
    messages.info(request,msg)
    print("msg",msg)
    return redirect('/view_bookdoctor')

def viewfeedback_clinic(request):
    uid=request.session['uid']
    qy=feedback_clinic.objects.filter(clinic__user=uid)
    return render(request,'Clinic/viewfeedback_clinic.html',{'qy':qy})


########################   SHOP ############################
def shopHome(request):
    return render(request,'Shop/shopHome.html')

def add_pets(request):
    uid=request.session['uid']
    # id= request.GET.get('id')
    shop=Petshops.objects.get(user=uid)
    if request.method =='POST':
        image=request.FILES['im']
        name=request.POST['name']
        about=request.POST['about']
        stock=request.POST['stock']
        cost=request.POST['cost']
        if Pet.objects.filter(name=name,shop=shop).exists():
            print("already exist")
            msg=" already exists"
            messages.info(request,msg)
        else:
            qry=Pet.objects.create(name=name,about=about,stock=stock,cost=cost,shop=shop,image=image)
            qry.save()
            messages.info(request,"Add Pets successfully")
            return redirect('/shopHome')
    return render(request,'Shop/addpets.html')

def add_products(request):
    uid=request.session['uid']
    # id= request.GET.get('id')
    shop=Petshops.objects.get(user=uid)
    if request.POST:
        image=request.FILES['img']
        about=request.POST['about']
        name=request.POST['name']
        cost=request.POST['cost']
        stock=request.POST['stock']
        if Product.objects.filter(name=name,shop=shop).exists():
            print("already exist")
            msg="already exists"
            messages.info(request,msg)
        else:
            qy=Product.objects.create(stock=stock,about=about,name=name,cost=cost,shop=shop,image=image)
            qy.save()
            messages.info(request,"Add products successfully")
            return redirect('/shopHome')
    return render(request,'Shop/addproducts.html')

def viewpetlist_shop(request):
    qry=Pet.objects.all()
    return render(request,'Shop/view_pets.html',{'qry':qry})

def Updatepet(request):
    id=request.GET.get('id')
    qy=Pet.objects.filter(id=id)
    if request.POST:
        stock=request.POST['stock']
        cost=request.POST['cost']
        qry=Pet.objects.get(id=id)
        qry.stock=stock
        qry.cost=cost
        qry.save()
        messages.info(request,"updated ")
        return redirect('/viewpetlist')
    return render(request,'Shop/updatepets.html',{'qy':qy}) 
   
def DeletePet(request):
     id=request.GET.get('id')
     qry=Pet.objects.filter(id=id).delete()
     messages.info(request,"Deleted ")
     return HttpResponseRedirect('/viewpetlist')

def viewproducts_shop(request):
    qy=Product.objects.all()
    return render(request,'Shop/viewproducts.html',{'qy':qy})

def Updateproduct(request):
    id=request.GET.get('id')
    qy=Product.objects.filter(id=id)
    if request.POST:
        cost=request.POST['cost']
        stock=request.POST['stock']
        qry=Product.objects.get(id=id)
        qry.cost=cost
        qry.stock=stock
        qry.save()
        messages.info(request,"update successfully")
        return redirect('/viewproduct')
    return render(request,'Shop/updateproducts.html',{'qy':qy})
    
def DeleteProduct(request):
     id=request.GET.get('id')
     qry=Product.objects.filter(id=id).delete()
     messages.info(request,"delete successfully")
     return HttpResponseRedirect('/viewproduct')

def viewadoptedpet(request):
    uid=request.session['uid']
    qy=Adoption.objects.filter(pet__shop__user=uid)
    return render(request,'Shop/view_adoptpet.html',{'qy':qy})

def acceptadoption(request):
    id=request.GET.get('id')
    book=Adoption.objects.get(id=id)
    book.status='accepted'
    book.save()
    messages.info(request,"Accept successfully")
    return redirect('/viewadoptedlist')
    
def rejectadoption(request):
    id=request.GET.get('id')
    book=Adoption.objects.get(id=id)
    book.status='Rejected'
    book.save()
    messages.info(request,"reject successfully")
    return redirect('/viewadoptedlist')

def viewfeedback_shop(request):
    uid=request.session['uid']
    qy=feedback_shop.objects.filter(shop__user=uid)
    return render(request,'Shop/viewfeedback_shop.html',{'qy':qy})

def viewpurchasedproducts(request):
    uid = request.session['uid']
    shops_for_user = Petshops.objects.filter(user=uid)   
    if shops_for_user.exists():
        shop = shops_for_user.first()  
        products_in_shop = Product.objects.filter(shop=shop)
        data = Cart.objects.filter(product__in=products_in_shop)
        return render(request, 'Shop/userpurchased_products.html', {'data': data})
    




#################################   CARE CENTRE  ###########################

def carecentreHome(request):
    return render(request,'centre/carecentreHome.html')

def Addservice_centre(request):
    uid=request.session['uid']
    id=request.GET.get('id')
    centre=PetcareCentre.objects.get(user=uid)
    if request.POST:
        service=request.POST['service']
        description=request.POST['description']
        rate=request.POST['rate']
        if CentreAddservices.objects.filter(service=service, centre=centre).exists():
            messages.info(request,"Already exist")
            print("already exist")
        else:
            qry=CentreAddservices.objects.create(service=service,rate=rate,description=description,centre=centre)
            qry.save()
            messages.info(request,"service added successfully")
            return redirect('/carecentreHome')
    return render(request,'centre/addservice_centre.html')

def viewaddservice_centre(request):
    uid=request.session['uid']
    qy=CentreAddservices.objects.filter(centre__user=uid)
    return render(request,'centre/viewaddservice_centre.html',{'qy':qy})

def updateaddservice_centre(request):
    id=request.GET.get('id')
    qy=CentreAddservices.objects.filter(id=id)
    if request.POST:
        rate=request.POST['rate']
        description=request.POST['description']
        qry=CentreAddservices.objects.get(id=id)
        qry.rate=rate
        qry.description=description
        qry.save()
        messages.info(request,"update successfully")
        return redirect('/viewaddservice_centre')
    return render(request,'centre/updateservice_centre.html',{'qy':qy})

def viewbookcarecentre_centre(request):
    uid=request.session['uid']
    ctr=PetcareCentre.objects.get(user=uid)
    qry = BookCarecentre.objects.filter(centre=ctr)
    return render(request,'centre/view carecentrebooking_centre.html',{'qry':qry})

def acceptBooking_centre(request):
    id=request.GET.get('id')
    if request.POST:
        amount=request.POST['amount']
        book=BookCarecentre.objects.get(id=id)
        days=book.days
        total=int(days)*int(amount)
        book.amount_day=amount
        book.total=total
        book.status='Accept'
        book.save()
        messages.info(request,"Accept successfully")
        return redirect('/viewbookcarecentre_centre')
    return render(request,'centre/amount.html')

def rejectbooking_centre(request):
    id=request.GET.get('id')
    book=BookCarecentre.objects.get(id=id)
    book.status='Reject'
    book.save()
    messages.info(request,"reject successfully")
    return redirect('/viewbookcarecentre_centre')

def viewbookedservice(request):
    uid=request.session['uid']
    ctr=PetcareCentre.objects.get(user=uid)
    qry=bookcentreservice.objects.filter(Service__centre=ctr)
    return render(request,'centre/viewservicebooking_centre.html',{'qry':qry})

def acceptservice_centre(request):
    id=request.GET.get('id')
    book=bookcentreservice.objects.get(id=id)
    book.status='Accept'
    book.save()
    messages.info(request,"Accept successfully")
    return redirect('/viewservicebooking_centre')
    
def rejectservice_centre(request):
    id=request.GET.get('id')
    book=bookcentreservice.objects.get(id=id)
    book.status='Reject'
    book.save()
    messages.info(request,"reject successfully")
    return redirect('/viewservicebooking_centre')

def viewfeedback_centre(request):
    uid=request.session['uid']
    qy=feedback_centre.objects.filter(centre__user=uid)
    return render(request,'centre/viewfeedback_cntr.html',{'qy':qy})

def Deleteservice_centre(request):
    id=request.GET.get('id')
    qry=CentreAddservices.objects.filter(id=id).delete()
    messages.info(request,"Deleted Successfully")
    return HttpResponseRedirect('/viewaddservice_centre')

def Deleteservice(request):
    id=request.GET.get('id')
    qry=walkerAddservices.objects.filter(id=id).delete()
    messages.info(request,"Deleted Successfully")
    return HttpResponseRedirect('/viewaddservice_walker')

########################   CUSTOMER  ############################

def userHome(request):
    return render(request,'customer/userHome.html')

from datetime import datetime
from django.shortcuts import get_object_or_404

def userview_clinics(request):
    district = request.GET.get('district', None)   
    if district:
        qry = clinic.objects.filter(district__icontains=district, user__is_active=1)
    else:
        qry = clinic.objects.filter(user__is_active=1)
    current_day = datetime.now().strftime('%A')   
    # current_time = datetime.now().time()
    # shoptime_list = []  

    # for clinic_instance in qry:
    #     stime = datetime.strptime(str(clinic_instance.starttime), '%H:%M:%S').time()
    #     etime = datetime.strptime(str(clinic_instance.Endtime), '%H:%M:%S').time()

    #     if current_time <= stime or current_time >= etime:
    #         shoptime_list.append(1)  
    #     else:
    #         shoptime_list.append(0)  
    context = {'qry': qry,"current_day":current_day}
    return render(request, 'customer/clinic_userview.html', context)


def userview_dogwalkers(request):
    district = request.GET.get('district', None)    
    if district:
        qry = Dogwalkers.objects.filter(district__icontains=district, user__is_active=1)
    else:
        qry = Dogwalkers.objects.filter(user__is_active=1)
    return render(request,'customer/dogwalkers_userview.html',{'qry':qry})

def userview_carecentre(request):
    district = request.GET.get('district', None)    
    if district:
        pet_care_centres = PetcareCentre.objects.filter(district__icontains=district, user__is_active=1)
    else:
        pet_care_centres = PetcareCentre.objects.filter(user__is_active=1)    
    context = {'qry': pet_care_centres}
    return render(request,'customer/carecentre_userview.html',context)

def userview_shop(request):
    district = request.GET.get('district', None)   
    if district:
        qry = Petshops.objects.filter(district__icontains=district, user__is_active=1)
    else:
        qry = Petshops.objects.filter(user__is_active=1)
    return render(request,'customer/shop_userview.html',{'qry':qry})

def book_doctor(request):
    uid=request.session['uid']
    id=request.GET.get('id')
    qy=VeterinaryDoctors.objects.all()
    if request.POST:
        time=request.POST['Time']
        date=request.POST['Date']
        doctor=VeterinaryDoctors.objects.get(id=id)
        uuid=Customer.objects.get(user_id=uid)
        if Bookingdoctor.objects.filter(Time=time,date=date).exists():
            print("already exists")
            msg="Entered date and time not available.choose another one"
            messages.info(request,msg)
        else:
            booking=Bookingdoctor.objects.create(doctor=doctor,user=uuid,Time=time,date=date)
            booking.save()
            messages.info(request,"successfully booked")
            return redirect('/viewdoctorbooking_user')
    return render(request,'customer/bookdoctor.html',{'qy':qy})

def clinic_details(request):
    id = request.GET.get('id')
    current_day = datetime.now().strftime('%A')
    doc=VeterinaryDoctors.objects.filter(clinic=id)
    return render(request,'customer/clinicdetail.html',{'doc':doc,"current_day":current_day})

def centre_services(request):
    id=request.GET.get('id')  
    qry=CentreAddservices.objects.filter(centre=id)
    print(qry)
    return render(request,'customer/centredetail.html',{'qry':qry})

def view_pets_user(request):
    id=request.GET.get('id')
    qry=Pet.objects.filter(shop=id).all()
    return render(request,'customer/view_pets.html',{'qry':qry})

def Adopt_pet(request):
    id=request.GET.get('id')
    uid=request.session['uid']
    pet=Pet.objects.get(id=id)
    cus=Customer.objects.get(user=uid)
    qy=Adoption.objects.create(pet=pet,user=cus)
    return redirect('/viewpets_user')

def viewadoption(request):
    uid = request.session['uid']
    data = Adoption.objects.filter(user__user_id=uid)
    return render(request, 'customer/viewadoption.html', {"data":data})

def viewaddservice_user(request):
    id=request.GET.get('id')
    qy=walkerAddservices.objects.filter(walker_id=id)
    return render(request,'customer/viewwalkerservice_user.html',{'qy':qy, 'walker_id': id})

def view_products_user(request):
    id = request.GET.get('id')
    qry = Product.objects.filter(shop=id)
    uid = request.session.get('uid')  
    
    if request.POST:
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        product = Product.objects.get(id=product_id)
        customer = Customer.objects.get(user=uid)
        price = int(product.cost)
        amt = price * quantity        
        order, created = Order.objects.get_or_create(customer=customer, status='Pending', defaults={'amount': 0})        
        cart_product = Cart.objects.filter(product=product, order=order)
        if cart_product.exists():
            messages.warning(request, "This item is already in your cart.")
        else:
            order.amount += amt  
            order.save()
            cart = Cart.objects.create(product=product, order=order, qty=quantity, amt=amt)
            cart.save()
            messages.info(request, "Item carted")        
        return redirect('/viewcart')    
    return render(request, 'customer/viewproducts_user.html', {'qry': qry})

from django.core.exceptions import ObjectDoesNotExist
def viewcart(request):
    uid = request.session['uid']  
    try:
        order = Order.objects.get(customer__user_id=uid, status='Pending')
        oid = order.id
        amt=order.amount
        carts = Cart.objects.filter(order__customer__user_id=uid, status='pending')
    except ObjectDoesNotExist:
        oid = None
        amt = None
        carts = []
    return render(request,'customer/cart.html',{'carts':carts,'oid':oid,'amt':amt})

def makePurchse(request):
    id = request.GET['id']
    order = Order.objects.get(id=id)
    if request.POST:
        order.status = "Paid"
        carts = Cart.objects.filter(order__id=id)
        for c in carts:
            pid = c.product.id
            qty = c.qty
            product = Product.objects.get(id=pid)
            product.stock -= qty
            product.save()
            c.status = "Paid"
            c.save()
        order.save()
        messages.info(request,"Paid successfully")
        return redirect("/viewpurchase")
    return render(request, "customer/payment.html")

def viewpurchase(request):
    uid = request.session['uid']
    data = Order.objects.filter(customer__user_id=uid,status='Paid')
    return render(request, 'customer/ViewPurchase.html', {"data":data})

def ViewItems(request):
    uid = request.session['uid']
    id = request.GET['id']
    data = Cart.objects.filter(order__id=id)
    return render(request, "customer/viewitems.html", {"data":data})

def complaint_Doctor(request):
    uid=request.session['uid']
    print(uid)
    id=request.GET.get('id')
    print(id)
    uuid=Customer.objects.get(user_id=uid)
    cid=VeterinaryDoctors.objects.get(id=id)
    print(cid)
    if request.POST:
        complaint=request.POST['complaint']
        qry=Complaint.objects.create(complaint=complaint,complainter=uuid,user=cid)
        qry.save()
        messages.info(request," successfull")
        return redirect('/userHome')
    return render(request,'customer/addcomplaint.html')

def book_centreservice(request):
    uid=request.session['uid']
    id=request.GET.get('id')
    if request.POST:
        service=CentreAddservices.objects.get(id=id)
        customer=Customer.objects.get(user=uid)
        date=request.POST['date']
        time=request.POST['time']
        if bookcentreservice.objects.filter(date=date,time=time,Service=service).exists():
            messages.info(request,"Already exist booking.change time or date")
        else:
            bs=bookcentreservice.objects.create(date=date,time=time,Service=service,customer=customer)
            bs.save()
            return redirect('/viewservicebooking')       
    return render(request,'customer/bookcentreservice.html')


def book_dogwalkers(request):
    uid=request.session['uid']
    id=request.GET.get('id')
    qy=Dogwalkers.objects.filter(id=id)
    services = walkerAddservices.objects.filter(walker_id=id)
    if request.POST:
        walkin=request.POST['walkin']
        walkout=request.POST['walkout']
        service_id = request.POST['service']
        
        walker=Dogwalkers.objects.get(id=id)
        uuid=Customer.objects.get(user=uid)
        service = walkerAddservices.objects.get(id=service_id)
        
        walkin_time=datetime.strptime(walkin,'%H:%M')
        walkout_time=datetime.strptime(walkout,'%H:%M')
        duration=(walkout_time-walkin_time).total_seconds()/3600
        totalcharge= duration * service.rate
        
        conflicting_bookings = BookingDogwalker.objects.filter(walker=walker,walkin_time__gte=walkin_time,walkout_time__lte=walkin_time) |\
                               BookingDogwalker.objects.filter(walker=walker, walkin_time__gte=walkout_time, walkout_time__lte=walkout_time)
        if conflicting_bookings.exists():
            messages.error(request, "Sorry, this time slot is already booked.")
            return redirect(f'/bookDogwalker/?id={id}')
        else:
            booking=BookingDogwalker.objects.create(walker=walker,user=uuid,service=service,walkin_time=walkin,walkout_time=walkout,totalcharge=totalcharge)
            booking.save()
            messages.info(request,"Booked successfully")
            return redirect('/view_Dogwalkerbookingdetail')
    return render(request,'customer/bookDogwalkers.html',{'qy':qy, 'services': services})

def viewwalkerbooking_user(request):
    uid=request.session['uid']
    uuid=Customer.objects.get(user=uid)
    qry=BookingDogwalker.objects.filter(user=uuid).all()
    return render(request,'customer/dogwalker_bookingdetail.html',{'qry':qry})

def viewDoctorbookingdetails_user(request):
    uid=request.session['uid']
    uuid=Customer.objects.get(user=uid)
    qy=Bookingdoctor.objects.filter(user=uuid)
    return render(request,'customer/viewdoctorbookings.html',{'qy':qy})

def addcomplaint(request):
    uid=request.session['uid']
    if request.POST:
        complaint=request.POST['complaint']
        user=Customer.objects.get(user=uid)
        com=Complaint.objects.create(complaint=complaint,complainter=user)
        com.save()
        return redirect('/userHome')
    return render(request,'customer/addcomplaint.html')


def feedback_care(request):
    uid=request.session['uid']
    print(uid)
    id=request.GET.get('id')
    print(id)
    uuid=Customer.objects.get(user_id=uid)
    centre=PetcareCentre.objects.get(id=id)
    # cid=BookCarecentre.objects.get(id=id)
    # centre=cid.centre
    if request.POST:
        feedback=request.POST['feedback']
        qry=feedback_centre.objects.create(feedback=feedback,user=uuid,centre=centre)
        qry.save()
        messages.info(request,"feedback sented successfully")
        return redirect('/userHome')
    return render(request,'customer/feedback.html', {'target_name': centre.carecentre, 'type': 'Centre'})

def feedback_clinics(request):
    uid=request.session['uid']
    print(uid)
    id=request.GET.get('id')
    print(id)
    uuid=Customer.objects.get(user_id=uid)
    cid=clinic.objects.get(id=id)
    print(cid)
    if request.POST:
        feedback=request.POST['feedback']
        qry=feedback_clinic.objects.create(feedback=feedback,user=uuid,clinic=cid)
        qry.save()
        messages.info(request,"feedback sented successfully")
        return redirect('/userHome')
    return render(request,'customer/feedback.html', {'target_name': cid.clinic_name, 'type': 'Clinic'})

def feedback_shops(request):
    uid=request.session['uid']
    print(uid)
    id=request.GET.get('id')
    print(id)
    uuid=Customer.objects.get(user_id=uid)
    cid=Petshops.objects.get(id=id)
    print(cid)
    if request.POST:
        feedback=request.POST['feedback']
        qry=feedback_shop.objects.create(feedback=feedback,user=uuid,shop=cid)
        qry.save()
        messages.info(request,"feedback sented successfully")
        return redirect('/userHome')
    return render(request,'customer/feedback.html', {'target_name': cid.shop_name, 'type': 'Shop'})

def feedback_walkers(request):
    uid=request.session['uid']
    id=request.GET.get('id')
    uuid=Customer.objects.get(user_id=uid)
    cid=Dogwalkers.objects.get(id=id)
    if request.POST:
        feedback=request.POST['feedback']
        qry=feedback_walker.objects.create(feedback=feedback,user=uuid,walker=cid)
        qry.save()
        messages.info(request,"feedback sented successfully")
        return redirect('/userHome')
    return render(request,'customer/feedback.html', {'target_name': cid.name, 'type': 'Dog Walker'})

def carecentrepayment(request):
    id=request.GET.get('id')
    if request.POST:
        qry=BookCarecentre.objects.get(id=id)
        qry.status='paid'
        qry.save()
        messages.info(request,"Paid successfully")
        return redirect('/viewbookcarecentre')
    return render(request,'customer/payment.html')

def walkerbookingpayment(request):
    id=request.GET.get('id')
    if request.POST:
        qry=BookingDogwalker.objects.get(id=id)
        qry.workstatus='paid'
        qry.save()
        messages.info(request,"Paid successfully")
        return redirect('/view_Dogwalkerbookingdetail')
    return render(request,'customer/payment.html')

def servicebookingpayment(request):
    id=request.GET.get('id')
    if request.POST:
        qry=bookcentreservice.objects.get(id=id)
        qry.status='paid'
        qry.save()
        messages.info(request,"Paid successfully")
        return redirect('/viewservicebooking')
    return render(request,'customer/payment.html')

def doctorbookingpayment(request):
    id=request.GET.get('id')
    if request.POST:
        qry=Bookingdoctor.objects.get(id=id)
        qry.status='paid'
        qry.save()
        messages.info(request,"Paid successfully")
        return redirect('/viewdoctorbooking_user')
    return render(request,'customer/payment.html')

def Adoptpayment(request):
    id=request.GET.get('id')
    if request.POST:
        qry=Adoption.objects.get(id=id)
        qry.status='paid'
        qry.save()
        Pet.objects.update(status='Adopted')
        messages.info(request,"Paid successfully")
        return redirect('/viewadoption')
    return render(request,'customer/payment.html')

def cancel_carecentreBooking(request):
    id=request.GET.get('id')
    qry=BookCarecentre.objects.filter(id=id).update(status='canceled')
    # BookCarecentre.objects.filter(id=id).delete()
    messages.info(request,"Canceled")
    return redirect('/viewbookcarecentre')

def cancel_serviceBooking(request):
    id=request.GET.get('id')
    qry=bookcentreservice.objects.filter(id=id).update(status='canceled')
    # bookcentreservice.objects.filter(id=id).delete()
    messages.info(request,"Canceled")
    return redirect('/viewservicebooking')

def cancel_doctorBooking(request):
    id=request.GET.get('id')
    qry=Bookingdoctor.objects.filter(id=id).update(status='canceled')
    # Bookingdoctor.objects.filter(id=id).delete()
    messages.info(request,"Canceled")
    return redirect('/viewdoctorbooking_user')

def cancel_Adoption(request):
    id=request.GET.get('id')
    qry=Adoption.objects.filter(id=id).update(status='canceled')
    # Adoption.objects.filter(id=id).delete()
    messages.info(request,"Canceled")
    return redirect('/viewadoption')

def cancel_dogwalking(request):
    id=request.GET.get('id')
    qry=BookingDogwalker.objects.filter(id=id).update(workstatus='canceled')
    # BookingDogwalker.objects.filter(id=id).delete()
    messages.info(request,"Canceled")
    return redirect('/view_Dogwalkerbookingdetail')

def viewservicebookings(request):
    uid=request.session['uid']
    user=Customer.objects.get(user=uid)
    qry=bookcentreservice.objects.filter(customer=user)
    return render(request,'customer/viewservicebooking.html',{'qry':qry})


def userview_shelter(request):
    qry=PetcareCentre.objects.all()
    return render(request,'customer/carecentre_shelter.html',{'qry':qry})

def removecartitem(request):
    id=request.GET.get('id')
    uid=request.session['uid']
    data=Cart.objects.get(id=id)
    oid = data.order.id
    cAmt = data.order.amount
    amt = data.amt
    order = Order.objects.get(id=oid)
    newAmt = int(cAmt) - int(amt)
    order.amount = newAmt
    order.save()
    data.delete()
    messages.info(request,"Item removed from cart")
    return redirect('/viewcart')
    
def bookcarecentre(request):
    id=request.GET.get('id')
    uid=request.session['uid']
    if request.POST:
        pet=request.POST['pet']
        about=request.POST['about']
        days=request.POST['days']
        date=request.POST['date']
        centre=PetcareCentre.objects.get(id=id)
        customer=Customer.objects.get(user=uid)
        book=BookCarecentre.objects.create(pet=pet,about=about,days=days,centre=centre,startdate=date,customer=customer)
        book.save()
        messages.info(request,"Booked successfully")
        return redirect('/viewbookcarecentre')

    return render(request,'customer/carecentrebooking.html') 

def viewbookcarecentre(request):
    uid=request.session['uid']
    qry=BookCarecentre.objects.filter(customer__user_id=uid)
    return render(request,'customer/viewbookcarecentre.html',{'qry':qry})

def viewshopfeedbacks(request):
    id=request.GET.get('id')
    qy=feedback_shop.objects.filter(shop__id=id)
    return render(request,'customer/shopfeedback.html',{'qy':qy})

def viewcentrefeedbacks(request):
    id=request.GET.get('id')
    qy=feedback_centre.objects.filter(centre__id=id)
    return render(request,'customer/centrefeedback.html',{'qy':qy})

def viewclinicfeedbacks(request):
    id=request.GET.get('id')
    qy=feedback_clinic.objects.filter(clinic__id=id)
    return render(request,'customer/clinicfeedback.html',{'qy':qy})

def viewwalkerfeedbacks(request):
    id=request.GET.get('id')
    qy=feedback_walker.objects.filter(walker__id=id)
    return render(request,'customer/walkerfeedback.html',{'qy':qy})
    

####################  DOGWALKER #####################

def dogwalkerHome(request):
    return render(request,'dogwalker/dogwalkerHome.html')

def view_walkerbooking(request):
    uid=request.session['uid']
    uuid=Dogwalkers.objects.get(user=uid)
    qy=BookingDogwalker.objects.filter(walker=uuid).all()
    return render(request,'dogwalker/view_walkerbookings.html',{'qy':qy})

def dogwalker_accept(request):
    uid=request.session['uid']
    id=request.GET.get('id')
    # walker=Dogwalkers.objects.filter(user=uid).update(status='Busy')
    qy=BookingDogwalker.objects.filter(id=id).update(workstatus='Accepted')
    messages.info(request,"Accept successfully")
    return redirect('/view_bookDogwalker')

def completewalk(request):
    id=request.GET.get('id')
    # walker=Dogwalkers.objects.filter(user=uid).update(status='Free')
    qy=BookingDogwalker.objects.filter(id=id).update(workstatus='Completed')
    return redirect('/view_bookDogwalker')

def Addservice(request):
    uid=request.session['uid']
    id=request.GET.get('id')
    hosp=Dogwalkers.objects.get(user=uid)
    if request.POST:
        serv=request.POST['service']
        rate=request.POST['rate']
        
        if walkerAddservices.objects.filter(service=serv, walker=hosp).exists():
            print("already exist")
            msg="Already exist"
            messages.info(request,msg)

        else:
            qry=walkerAddservices.objects.create(service=serv,walker=hosp,rate=rate)
            qry.save()
            msg="Added Successfully"
            messages.info(request,msg)

            return redirect('/dogwalkerHome')
    return render(request,'dogwalker/addservices.html')

def viewaddservice(request):
    uid=request.session['uid']
    qy=walkerAddservices.objects.filter(walker__user=uid)
    return render(request,'dogwalker/viewaddservice.html',{'qy':qy})

def Deleteaddservice(request):
    id=request.GET.get('id')
    qry=walkerAddservices.objects.filter(id=id).delete()
    msg="Deleted Successfully"
    messages.info(request,msg)
    return HttpResponseRedirect('/viewaddservice')

def viewfeedback_walker(request):
    uid=request.session['uid']
    qy=feedback_walker.objects.filter(walker__user=uid)
    return render(request,'dogwalker/viewfeedback_walker.html',{'qy':qy})











