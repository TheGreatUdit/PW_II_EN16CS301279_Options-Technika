from django.contrib import admin

from OptionsTechnikaApp.models import contact_model, enquiry_model,register_model, course_assign,course_pro
class ContactAdmin(admin.ModelAdmin):
    list_display=['fullname','email','pno','query']
admin.site.register(contact_model,ContactAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=['brand','fname','lname','email','mobile','tele','source','campaign','comments','dob','gender','eduqual','address','city','state','country','pin','gname','gaddress','gmobile','gtele','fathname','mothname','status','subpos','sts1','sts2','sts3']
admin.site.register(enquiry_model,EnquiryAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display=['fullname','username','pro_pic','dob','gender','address','city','state','pno','email','pass1','pass2','inst_name_10','cgpa_10','board_10','major_10','start_date_10','end_date_10','inst_name_12','cgpa_12','board_12','major_12','start_date_12','end_date_12','inst_name_clg','cgpa_clg','uni_clg','major_clg','start_date_clg','end_date_clg','fath_name','fath_age','fath_occ','fath_qua','moth_name','moth_age','moth_occ','moth_qua','course','company']
admin.site.register(register_model,RegisterAdmin)

class AssignAdmin(admin.ModelAdmin):
    list_display=['course_name','course_company','assignment','remark']
admin.site.register(course_assign,AssignAdmin)

class ProAdmin(admin.ModelAdmin):
    list_display=['course_name','course_company','projects','remark']
admin.site.register(course_pro,ProAdmin)
