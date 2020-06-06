from django.shortcuts import render,redirect
from django.http import HttpResponse
from OptionsTechnikaApp.models import contact_model,enquiry_model,course_assign,course_pro,register_model,alumini_model
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.urls import reverse
from OptionsTechnikaApp.forms import SignUpForm
from facepplib import FacePP, exceptions
import cv2
import smtplib
import requests
import random


def index(request):
    return render(request,'OptionsTechnikaApp/index.html',{'nbar':'index'})
def courses(request):
    return render(request,'OptionsTechnikaApp/courses.html',{'nbar':'courses'})
def details(request):
    return render(request,'OptionsTechnikaApp/details.html')
def about(request):
    return render(request,'OptionsTechnikaApp/about.html',{'nbar':'about'})
def team(request):
    return render(request,'OptionsTechnikaApp/team.html',{'nbar':'team'})

def contact(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        email=request.POST['email']
        pno=request.POST['pno']
        query=request.POST['query']
        con_obj = contact_model(fullname=fullname, email=email,pno=pno,query=query)
        con_obj.save()
        return render(request,'OptionsTechnikaApp/contact.html',{'nbar':'contact'})
    else:
        return render(request,'OptionsTechnikaApp/contact.html',{'nbar':'contact'})

def ibm(request):
    return render(request,'IbmModule/index.html')
def software(request):
    return render(request,'IbmModule/software.html')
def solution(request):
    return render(request,'IbmModule/solution.html')

def error(request):
    return render(request,'Dashboard/404.html')

def register(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        username=request.POST['username']
        pro_pic=username+".png"
        dob=request.POST['dob']
        gender=request.POST['gender']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        pno=request.POST['pno']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        inst_name_10=request.POST['inst_name_10']
        cgpa_10=request.POST['cgpa_10']
        board_10=request.POST['board_10']
        major_10=request.POST['major_10']
        start_date_10=request.POST['start_date_10']
        end_date_10=request.POST['end_date_10']

        inst_name_12=request.POST['inst_name_12']
        cgpa_12=request.POST['cgpa_12']
        board_12=request.POST['board_12']
        major_12=request.POST['major_12']
        start_date_12=request.POST['start_date_12']
        end_date_12=request.POST['end_date_12']

        inst_name_clg=request.POST['inst_name_clg']
        cgpa_clg=request.POST['cgpa_clg']
        uni_clg=request.POST['uni_clg']
        major_clg=request.POST['major_clg']
        start_date_clg=request.POST['start_date_clg']
        end_date_clg=request.POST['end_date_clg']

        fath_name=request.POST['fath_name']
        fath_age=request.POST['fath_age']
        fath_occ=request.POST['fath_occ']
        fath_qua=request.POST['fath_qua']
        moth_name=request.POST['moth_name']
        moth_age=request.POST['moth_age']
        moth_occ=request.POST['moth_occ']
        moth_qua=request.POST['moth_qua']
        company=request.POST['company']
        course=request.POST['course']
        reg_obj = register_model(fullname=fullname,username=username,pro_pic=pro_pic,dob=dob,gender=gender,address=address,city=city,state=state, pno=pno,email=email,pass1=pass1,pass2=pass2,major_10=major_10,major_12=major_12,major_clg=major_clg,start_date_10=start_date_10,start_date_12=start_date_12,start_date_clg=start_date_clg,end_date_10=end_date_10,end_date_12=end_date_12,end_date_clg=end_date_clg,board_10=board_10,board_12=board_12,uni_clg=uni_clg,cgpa_10=cgpa_10,cgpa_12=cgpa_12,cgpa_clg=cgpa_clg, inst_name_10=inst_name_10,inst_name_12=inst_name_12,inst_name_clg=inst_name_clg, moth_age=moth_age,moth_occ=moth_occ,moth_qua=moth_qua,moth_name=moth_name,fath_age=fath_age,fath_occ=fath_occ,fath_qua=fath_qua,fath_name=fath_name, company=company, course= course)
        reg_obj.save()
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame= cap.read()
                if ret == True:
                    cv2.imshow('frame', frame)
                    k=cv2.waitKey(1)
                    if k == ord('q'):
                        break
                    elif k == ord('s'):
                        img_name="media/"+username+".png"
                        cv2.imwrite(img_name,frame)
                        break
            cap.release()
            cv2.destroyAllWindows()


        return render(request,'OptionsTechnikaApp/register.html',{"form":form,"username":username})
    else:
        form=SignUpForm()
        return render(request,'OptionsTechnikaApp/register.html',{"form":form})


@login_required
def counsellor(request,username):
    enquire_list=enquiry_model.objects.filter(status='Enquiry')
    enquire_count=enquiry_model.objects.filter(status='Enquiry').count()
    confirm_list=enquiry_model.objects.filter(status='Confirmed')
    unpaid_count=enquiry_model.objects.filter(status='Confirmed').count()
    paid_count=enquiry_model.objects.filter(status='Paid').count()
    old_enquiry_count=enquiry_model.objects.filter(status='Old_Enquiry').count()
    enquiry_count=enquire_count+old_enquiry_count
    confirm_count=unpaid_count+paid_count
    profile_lst=register_model.objects.filter(username=username)
    mydict={"enquire_list":enquire_list,"enquiry_count":enquiry_count,"confirm_list":confirm_list,"confirm_count":confirm_count,"paid_count":paid_count,"unpaid_count":unpaid_count,"profile_lst":profile_lst}
    return render(request,'Dashboard/counsellor.html',context=mydict)
@login_required
def editenquiry(request,username,email):
    profile_lst=register_model.objects.filter(username=username)
    enquire_list=enquiry_model.objects.filter(email=email)
    mydict={"enquire_list":enquire_list,"profile_lst":profile_lst}
    if request.method=='POST':
        up_enq=request.POST['up_enq']
        up_pos=request.POST['up_pos']
        up_sts1=request.POST['up_sts1']
        up_sts2=request.POST['up_sts2']
        up_sts3=request.POST['up_sts3']
        if up_sts1=='' and up_sts2=='' and up_sts3=='':
            enquiry_model.objects.filter(email=email).update(status=up_enq,subpos=up_pos)
        elif up_sts1=='' and up_sts2=='':
            enquiry_model.objects.filter(email=email).update(status=up_enq,subpos=up_pos,sts3=up_sts3)
        elif up_sts1=='' and up_sts3=='':
            enquiry_model.objects.filter(email=email).update(status=up_enq,subpos=up_pos,sts2=up_sts2)
        elif up_sts3=='' and up_sts2=='':
            enquiry_model.objects.filter(email=email).update(status=up_enq,subpos=up_pos,sts1=up_sts1)
        elif up_sts1=='':
            enquiry_model.objects.filter(email=email).update(status=up_enq,subpos=up_pos,sts2=up_sts2,sts3=up_sts3)
        elif up_sts2=='':
            enquiry_model.objects.filter(email=email).update(status=up_enq,subpos=up_pos,sts1=up_sts1,sts3=up_sts3)
        elif up_sts3=='':
            enquiry_model.objects.filter(email=email).update(status=up_enq,subpos=up_pos,sts2=up_sts2,sts1=up_sts1)
        else:
            enquiry_model.objects.filter(email=email).update(status=up_enq,subpos=up_pos,sts1=up_sts1,sts2=up_sts2,sts3=up_sts3)
        return render(request,'Dashboard/counsellor2.html',context=mydict)
    else:
        return render(request,'Dashboard/counsellor2.html',context=mydict)
@login_required
def coun_profile(request,username):
    profile_lst=register_model.objects.filter(username=username)
    return render(request,"Dashboard/coun_profile.html",{"profile_lst":profile_lst})

@login_required
def faculty(request,username,actn):
    assign_list=course_assign.objects.all()
    pro_list=course_pro.objects.all()
    profile_lst=register_model.objects.filter(username=username)
    mydict={"assign_list":assign_list,"pro_list":pro_list,"profile_lst":profile_lst}
    if request.method=='POST':
        if(actn=="assign"):
            asgn_cou=request.POST['asgn_cou']
            asgn_comp=request.POST['asgn_comp']
            asgn_asgn=request.POST['asgn_asgn']
            asgn_rmk=request.POST['asgn_rmk']
            assign_obj=course_assign(course_name=asgn_cou,course_company=asgn_comp,assignment=asgn_asgn,remark=asgn_rmk)
            assign_obj.save()
        elif(actn=="pro"):
            pro_cou=request.POST['pro_cou']
            pro_comp=request.POST['pro_comp']
            pro_pro=request.POST['pro_pro']
            pro_rmk=request.POST['pro_rmk']
            pro_obj=course_pro(course_name=pro_cou,course_company=pro_comp,projects=pro_pro,remark=pro_rmk)
            pro_obj.save()
        return render(request,'Dashboard/faculty.html',context=mydict)
    else:
        return render(request,'Dashboard/faculty.html',context=mydict)
@login_required
def fac_profile(request,username,actn):
    profile_lst=register_model.objects.filter(username=username)
    return render(request,"Dashboard/fac_profile.html",{"profile_lst":profile_lst})

@login_required
def student(request,username):
    company=register_model.objects.filter(username=username).values('company')
    company=company[0]['company']
    course=register_model.objects.filter(username=username).values('course')
    course=course[0]['course']
    assign_list=course_assign.objects.filter(course_name=course,course_company=company)
    pro_list=course_pro.objects.filter(course_name=course,course_company=company)
    profile_lst=register_model.objects.filter(username=username)
    mydict={"assign_list":assign_list,"pro_list":pro_list,"profile_lst":profile_lst}
    return render(request,'Dashboard/student.html',context=mydict)
@login_required
def stu_profile(request,username):
    profile_lst=register_model.objects.filter(username=username)
    return render(request,"Dashboard/stu_profile.html",{"profile_lst":profile_lst})

def login(request):
    if request.session.get('s_id') is None:
        if request.method=='POST':
            user=request.POST['user']
            pass1=request.POST['pass1']
            record_user=register_model.objects.filter(username=user).values('username')
            if record_user.exists():
                email=register_model.objects.filter(username=user).values('email')
                emailid=email[0]['email']
                sub_pos=enquiry_model.objects.filter(email=emailid).values('subpos')
                subpos=sub_pos[0]['subpos']
                if(subpos=='NA'):
                    return render(request,'OptionsTechnikaApp/login.html',{'msg':"First Register",'nbar':'login'})
                else:
                    user1=auth.authenticate(username=user,password=pass1)
                    if user1 is not None:
                        auth.login(request,user1)
                        request.session['s_id'] = user
                        if(subpos=='F_IBM'):
                            fac_url='/faculty/'+user+'/'+emailid
                            return redirect(fac_url)
                        elif(subpos=='C_IBM'):
                            coun_url='/counsellor/'+user
                            return redirect(coun_url)
                        elif(subpos=='Stu_IBM'):
                            stu_url='/student/'+user
                            return redirect(stu_url)
                    else:
                        return render(request,'OptionsTechnikaApp/login.html',{'msg':'Invalid Credentials!','nbar':'login'})
            else:
                return render(request,'OptionsTechnikaApp/login.html',{'msg':'Invalid Username!','nbar':'login'})
        else:
            return render(request,'OptionsTechnikaApp/login.html',{'nbar':'login',"log":"Login"})
    else:
        dec={"log":"Logout"}
        return redirect('logout')

def logout(request):
    del request.session['s_id']
    auth.logout(request)
    return redirect('login1')

def enquiry(request):
    if request.method=='POST':
        brand=request.POST['brand']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        tele=request.POST['tele']
        source=request.POST['source']
        campaign=request.POST['campaign']
        comments=request.POST['comments']
        dob = request.POST['dob']
        gender = request.POST['gender']
        eduqual=request.POST['eduqual']
        address =request.POST['address']
        city= request.POST['city']
        state = request.POST['state']
        country=request.POST['country']
        pin=request.POST['pin']
        gname=request.POST['gname']
        gaddress=request.POST['gaddress']
        gmobile = request.POST['gmobile']
        gtele=request.POST['gtele']
        fathname = request.POST['fathname']
        mothname =request.POST['mothname']
        status="Enquiry"
        subpos="NA"
        sts1="NA"
        sts2="NA"
        sts3="NA"
        URL = 'https://www.sms4india.com/api/v1/sendCampaign'
        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
                'apikey':apiKey,
                'secret':secretKey,
                'usetype':useType,
                'phone': phoneNo,
                'message':textMessage,
                'senderid':senderId
            }
            return requests.post(reqUrl, req_params)
        otp1=random.randint(400000, 900000)
        var1="The otp generated for mobile verfication of Options Technika website is"+str(otp1)
        response = sendPostRequest(URL, '3CY1FIB3G5P1BPSE1CD8IHVXAEGXT0K8', '62NU85BC8X8T5L25', 'stage', mobile,
                               'niteshkarmakar27@gmail.com', var1)


        enq_obj = enquiry_model(brand=brand,fname=fname,lname=lname,email=email,mobile=mobile,tele=tele,source=source,campaign=campaign,comments=comments,dob=dob,gender=gender,eduqual=eduqual,address=address,city=city,state=state,country=country,pin=pin,gname=gname,gaddress=gaddress,gmobile=gmobile,gtele=gtele,fathname=fathname,mothname=mothname,status=status,subpos=subpos,sts1=sts1,sts2=sts2,sts3=sts3)
        enq_obj.save()
        return render(request,'OptionsTechnikaApp/enquiry.html',{'nbar':'enquiry'})
    else:
        return render(request,'OptionsTechnikaApp/enquiry.html',{'nbar':'enquiry'})

def wallof(request):
    return render(request,'wof/fp.html')

def alumini(request):
    video = cv2.VideoCapture(0)

    while True:

        check, frame = video.read()
        cv2.imshow("capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            showPic = cv2.imwrite("media/woff/file11.jpg", frame)
            break


    video.release()
    cv2.destroyAllWindows()

    api_key='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'
    app_ = FacePP(api_key=api_key,api_secret=api_secret)
    img_files= alumini_model.objects.all()
    i=0
    stat=-1
    for img in img_files:
        i=i+1
        img_file1="media/"+f"{img.filepath}"
        # img_file1='static/images/woff/'+img_file1_temp
        img_file2='media/woff/file11.jpg'
        cmp_=app_.compare.get(image_file1=img_file1, image_file2=img_file2)
        if cmp_.confidence>90:
            stat=1
            global alm
            alm= img
            break
        elif i>=len(img_files)-1:
            stat=0
    if(stat==1):

        return render(request,'wof/alumini.html',{'alm':alm})
    else:
        # return HttpResponse("not match")
        return render(request,'Dashboard/404.html')

def addalumini(request):
    if request.method=='POST':
        fullname=request.POST['al_name']
        email=request.POST['email']
        al_pic="woff/"+email+".png"
        company=request.POST['company']
        age=request.POST['age']
        salary=request.POST['salary']
        alu_obj = alumini_model(name=fullname,filepath=al_pic,age=age,email=email,company=company, salary=salary)
        alu_obj.save()

        cap = cv2.VideoCapture(0)
        while True:
            ret, frame= cap.read()
            if ret == True:
                cv2.imshow('frame', frame)
                k=cv2.waitKey(1)
                if k == ord('q'):
                    break
                elif k == ord('s'):
                    img_name="media/woff/"+email+".png"
                    cv2.imwrite(img_name,frame)
                    break
        cap.release()
        cv2.destroyAllWindows()
        return render(request,'OptionsTechnikaApp/addalumni.html')
    else:
        return render(request,'OptionsTechnikaApp/addalumni.html')
