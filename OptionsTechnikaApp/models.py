from django.db import models

class contact_model(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    pno=models.CharField(max_length=13)
    query=models.CharField(max_length=2000)
    def __str__(self):
        return self.email

class enquiry_model(models.Model):
    brand=models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50,primary_key=True)
    mobile = models.CharField(max_length=13)
    tele=models.CharField(max_length=10)
    source=models.CharField(max_length=20)
    campaign=models.CharField(max_length=25)
    comments=models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    eduqual=models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    city= models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country=models.CharField(max_length=15)
    pin=models.CharField(max_length=15)
    gname=models.CharField(max_length=20)
    gaddress=models.CharField(max_length=150)
    gmobile = models.CharField(max_length=13)
    gtele=models.CharField(max_length=10)
    fathname = models.CharField(max_length=50)
    mothname = models.CharField(max_length=50)
    status=models.CharField(max_length=20)
    subpos=models.CharField(max_length=10)
    sts1=models.CharField(max_length=100)
    sts2=models.CharField(max_length=100)
    sts3=models.CharField(max_length=100)
    def __str__(self):
        return self.email

class register_model(models.Model):
    fullname = models.CharField(max_length=60)
    username=models.CharField(max_length=30)
    pro_pic=models.ImageField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    city= models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    pno = models.CharField(max_length=13)
    email = models.EmailField(max_length=50,primary_key=True)
    pass1 = models.CharField(max_length=50)
    pass2=models.CharField(max_length=50)

    inst_name_10= models.CharField(max_length=50)
    cgpa_10 = models.IntegerField()
    board_10= models.CharField(max_length=40)
    major_10 = models.CharField(max_length=20)
    start_date_10=models.DateField()
    end_date_10=models.DateField()

    inst_name_12= models.CharField(max_length=50)
    cgpa_12= models.IntegerField()
    board_12= models.CharField(max_length=40)
    major_12 = models.CharField(max_length=20)
    start_date_12=models.DateField()
    end_date_12=models.DateField()

    inst_name_clg= models.CharField(max_length=50)
    cgpa_clg = models.IntegerField()
    uni_clg= models.CharField(max_length=50)
    major_clg = models.CharField(max_length=20)
    start_date_clg=models.DateField()
    end_date_clg=models.DateField()

    fath_name = models.CharField(max_length=50)
    fath_age = models.IntegerField()
    fath_occ = models.CharField(max_length=25)
    fath_qua = models.CharField(max_length=20)
    moth_name = models.CharField(max_length=50)
    moth_age = models.IntegerField()
    moth_occ = models.CharField(max_length=25)
    moth_qua = models.CharField(max_length=20)

    company = models.CharField(max_length=20)
    course = models.CharField(max_length=30)

    def __str__(self):
        return self.email

class course_assign(models.Model):
    course_name=models.CharField(max_length=20)
    course_company=models.CharField(max_length=20)
    assignment=models.CharField(max_length=5000)
    remark=models.CharField(max_length=2500)

    def __str__(self):
        return self.course_name

class course_pro(models.Model):
    course_name=models.CharField(max_length=20)
    course_company=models.CharField(max_length=20)
    projects=models.CharField(max_length=5000)
    remark=models.CharField(max_length=2500)

    def __str__(self):
        return self.course_name
