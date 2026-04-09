from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=40,null=True)
    viewpassword=models.CharField(max_length=40,null=True)

class Customer(models.Model):
    customer_name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=60,null=True)
    phonenumber=models.CharField(max_length=40,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    district=models.CharField(max_length=50,null=True)
    
class Dogwalkers(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    phonenumber=models.CharField(max_length=50,null=True)
    license_no=models.CharField(max_length=50,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    charge=models.IntegerField(null=True)
    district=models.CharField(max_length=50,null=True)

class walkerAddservices(models.Model):
    service=models.CharField(max_length=40,null=True)
    rate=models.IntegerField(null=True)
    walker=models.ForeignKey(Dogwalkers,on_delete=models.CASCADE,null=True)


class clinic(models.Model):
    clinic_name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    phonenumber=models.CharField(max_length=50,null=True)
    owned_by=models.CharField(max_length=50,null=True)
    license_no=models.CharField(max_length=50,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    starttime=models.TimeField(null=True)
    Endtime=models.TimeField(null=True)
    district=models.CharField(max_length=50,null=True)

class VeterinaryDoctors(models.Model):
    name=models.CharField(max_length=50,null=True)
    phonenumber=models.CharField(max_length=50,null=True)
    register_no=models.CharField(max_length=50,null=True)
    qualification=models.CharField(max_length=50,null=True)
    clinic=models.ForeignKey(clinic,on_delete=models.CASCADE,null=True)
    
class Petshops(models.Model):
    shop_name=models.CharField(max_length=60,null=True)
    owner_name=models.CharField(max_length=60,null=True)
    email=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    phonenumber=models.CharField(max_length=50,null=True)
    license_no=models.CharField(max_length=50,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    district=models.CharField(max_length=50,null=True)

class PetcareCentre(models.Model):
    carecentre=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    Address=models.CharField(max_length=50,null=True)
    phonenumber=models.CharField(max_length=50,null=True)
    owner_name=models.CharField(max_length=50,null=True)
    license_no=models.CharField(max_length=50,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    district=models.CharField(max_length=50,null=True)

class Complaint(models.Model):
    complaint=models.CharField(max_length=50,null=True)
    Date=models.DateTimeField(auto_now_add=True,null=True)
    complainter=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)

class Bookingdoctor(models.Model):
    doctor=models.ForeignKey(VeterinaryDoctors,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    Time=models.TimeField(null=True)
    b_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,null=True,default='Booked')

class BookingDogwalker(models.Model):
    walker=models.ForeignKey(Dogwalkers,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    service=models.ForeignKey(walkerAddservices,on_delete=models.CASCADE,null=True)
    walkin_time=models.TimeField(null=True)
    walkout_time=models.TimeField(null=True)
    b_date=models.DateTimeField(auto_now_add=True)
    totalcharge=models.CharField(max_length=50,null=True)
    workstatus=models.CharField(max_length=50,null=True,default='pending')

class Pet(models.Model):
    name=models.CharField(max_length=40,null=True)
    breed=models.CharField(max_length=40,null=True)
    image=models.ImageField(upload_to="uploadImage",max_length=None,null=True)
    about=models.CharField(max_length=150,null=True)
    cost=models.IntegerField(null=True)
    shop=models.ForeignKey(Petshops,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=40,null=True,default='available')

class Adoption(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE,null=True)
    adopted_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=40,null=True,default='requested')

class Product(models.Model):
    about=models.CharField(max_length=50,null=True)
    image=models.ImageField(upload_to="uploadImage",max_length=None,null=True)
    name=models.CharField(max_length=50,null=True)
    cost=models.IntegerField(null=True)
    stock=models.IntegerField(null=True)
    shop=models.ForeignKey(Petshops,on_delete=models.CASCADE,null=True)

class CentreAddservices(models.Model):
    service=models.CharField(max_length=40,null=True)
    description=models.CharField(max_length=40,null=True)
    rate=models.IntegerField(null=True)
    centre=models.ForeignKey(PetcareCentre,on_delete=models.CASCADE,null=True)



class feedback_clinic(models.Model):
    feedback=models.CharField(max_length=50,null=True)
    Date=models.DateTimeField(auto_now_add=True,null=True)
    clinic=models.ForeignKey(clinic,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)

class feedback_centre(models.Model):
    feedback=models.CharField(max_length=50,null=True)
    Date=models.DateTimeField(auto_now_add=True,null=True)
    centre=models.ForeignKey(PetcareCentre,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)

class feedback_shop(models.Model):
    feedback=models.CharField(max_length=50,null=True)
    Date=models.DateTimeField(auto_now_add=True,null=True)
    shop=models.ForeignKey(Petshops,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)

class feedback_walker(models.Model):
    feedback=models.CharField(max_length=50,null=True)
    Date=models.DateTimeField(auto_now_add=True,null=True)
    walker=models.ForeignKey(Dogwalkers,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    date=models.DateField(auto_now_add=True)
    amount=models.IntegerField(null=True)
    status=models.CharField(max_length=40,default='Pending',null=True)

class Cart(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    qty=models.IntegerField(null=True)
    amt=models.IntegerField(null=True)
    date=models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=40,default='pending',null=True)

class BookCarecentre(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    startdate=models.DateField(null=True)
    centre=models.ForeignKey(PetcareCentre,on_delete=models.CASCADE,null=True)
    pet=models.CharField(max_length=40,null=True)
    days=models.IntegerField(null=True)
    about=models.CharField(max_length=100,null=True)
    amount_day=models.IntegerField(null=True)
    total=models.IntegerField(null=True)
    booked_date=models.DateTimeField(auto_now_add=True,null=True) 
    status=models.CharField(max_length=40,default='booked',null=True)

class bookcentreservice(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    Service=models.ForeignKey(CentreAddservices,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    submitted_date=models.DateTimeField(auto_now_add=True,null=True)
    time=models.TimeField(null=True)
    centre=models.ForeignKey(PetcareCentre,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=40,default='booked',null=True)


    





    
