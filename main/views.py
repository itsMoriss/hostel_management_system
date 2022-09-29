from django.shortcuts import render,redirect
from .models import MessMenu
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib import messages
from django.db.models import Q
from .models import StudentLeave,Hostel,FeePaid,College,FeeRecords
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

@login_required
def index(request):
    context = {}
    return render(request,'main/index.html',context)

@login_required
def user_registration(request):
    if request.method == 'POST':
        inputFirstName = request.POST['inputFirstName']
        inputLastName = request.POST['inputLastName']
        inputUsername = request.POST['inputUsername']
        inputRole = request.POST['inputRole']
        inputEmail = request.POST['inputEmail']
        inputPassword1 = request.POST['inputPassword1']
        inputPassword2 = request.POST['inputPassword2']
        print(inputRole,' of type ',type(inputRole))
        # print(inputFirstName,inputLastName,inputUsername,inputRole,inputEmail,inputPassword1,inputPassword2)
        try:
            new_user = User.objects.create_user(username=inputUsername,email=inputEmail,password=inputPassword2,
                first_name=inputFirstName,last_name=inputLastName)
            new_profile = Profile.objects.get_or_create(user=new_user)[0]
            print(new_profile)
            new_profile.role = inputRole
            new_profile.save()
            messages.success(request, 'User Created Successfully')
            # print('user done')
        except Exception as e:
            messages.error(request, 'User not created, ',e)
            print(e)

        return redirect('main:user_registration')
    # messages.info(request, 'Just loaded the page')
    context = {}
    return render(request,'main/user-registration.html',context)

@login_required
def user_profile(request):
    profile = Profile.objects.filter(user=request.user)[0]
    context = {'profile':profile}
    return render(request,'main/profile.html',context)

@login_required
def edit_profile(request,pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile_id = request.POST['profile_id']
        profile = Profile.objects.get(id=profile_id)
        inputID = request.POST['inputID']
        inputPhone = request.POST['inputPhone']

        profile.id_number = inputID 
        profile.phone = inputPhone
        profile.save()
        return redirect('main:edit_profile',profile_id)
    context = {'profile':profile}
    return render(request,'main/profile.html',context)

@login_required
def admin_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}
    return render(request,'main/admin-dashboard.html',context)

@login_required
def admin_details(request):
    profile = Profile.objects.filter(user=request.user)[0]
    context = {'profile':profile}
    return render(request,'main/admin-details.html',context)

@login_required
def mess_details(request):
    menus = MessMenu.objects.all()
    context = {'menus':menus}
    
    return render(request,'main/mess-details.html',context)

@login_required
def add_mess_menu(request):
    if request.method == 'POST':
        inputDay = request.POST['inputDay']
        inputBreakfast = request.POST['inputBreakfast']
        inputBreakfastPrice = request.POST['inputBreakfastPrice']
        inputLunch = request.POST['inputLunch']
        inputLunchPrice = request.POST['inputLunchPrice']
        inputDinner = request.POST['inputDinner']
        inputDinnerPrice = request.POST['inputDinnerPrice']
        menu = MessMenu.objects.create(day=inputDay,breakfast=inputBreakfast,
        breakfast_price=inputBreakfastPrice,lunch=inputLunch,lunch_price=inputLunchPrice,dinner=inputDinner
        ,dinner_price=inputDinnerPrice)
        return redirect('main:mess_details')
    context = {}
    return render(request,'main/add-mess-menu.html',context)

@login_required
def add_hostel(request):
    if request.method == 'POST':
        inputHostel = request.POST['inputHostelName']

        hostel = Hostel.objects.create(hostel_name=inputHostel)
        return redirect('main:index')
    context = {}
    return render(request,'main/add-hostel.html',context)


@login_required
def student_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}
    return render(request,'main/student-dashboard.html',context)

@login_required
def hostel_leave_details(request):
    context = {}
    return render(request,'main/hostel-leave-details.html',context)

@login_required
def edit_hostel_staff(request,pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile_id = request.POST['profile_id']
        inputFirstName = request.POST['inputFirstName']
        inputLastName = request.POST['inputLastName']
        inputUsername = request.POST['inputUsername']
        inputID = request.POST['inputID']
        inputAddress = request.POST['inputAddress']
        inputPhone = request.POST['inputPhone']
        inputRole = request.POST['inputRole']
       
        user = User.objects.get(username=inputUsername)
        user.first_name = inputFirstName
        user.last_name = inputLastName
        user.save()
        profile.id_number = inputID 
        profile.phone = inputPhone
        profile.role = inputRole
        profile.address = inputAddress

        profile.save()

        return redirect('main:hostel_staff_details')
    context = {'profile':profile}
    return render(request,'main/edit-hostel-staff.html',context)

@login_required
def hostel_staff_details(request):
    profiles = Profile.objects.filter(Q(role__icontains='Janitor') |
    Q(role__icontains='Staff') | Q(role__icontains='house keeping'))

    context = {'profiles':profiles}
    return render(request,'main/hostel-staff-details.html',context)

@login_required
def student_details(request):
    profiles = Profile.objects.filter(role='Student')
    context = {'profiles':profiles}
    return render(request,'main/student-details.html',context)

@login_required
def delete_student(request,pk):
    student = User.objects.get(pk=pk)
    print(vars(student))
    student.delete()
    return redirect('main:student_details')

@login_required
def delete_menu(request,pk):
    menu = MessMenu.objects.get(pk=pk)
    # print(vars(student))
    menu.delete()
    return redirect('main:mess_details')


@login_required
def edit_student(request,pk):
    hostels = Hostel.objects.all()
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile_id = request.POST['profile_id']
        inputFirstName = request.POST['inputFirstName']
        inputLastName = request.POST['inputLastName']
        inputUsername = request.POST['inputUsername']
        inputID = request.POST['inputID']
        inputCollege = request.POST['inputCollege']
        inputYear = request.POST['inputYear']
        inputSemester = request.POST['inputSemester']
        inputHostel = request.POST['inputHostel']
        inputRoomNumber = request.POST['inputRoomNumber']
        inputPhone = request.POST['inputPhone']
        # inputEmail = request.POST['inputEmail']

        user = User.objects.get(username=inputUsername)
        user.first_name = inputFirstName
        user.last_name = inputLastName
        user.save()
        # print(user, 'user is the user')

        profile.id_number = inputID 
        profile.college = inputCollege
        profile.semester = inputSemester
        profile.hostel = inputHostel
        profile.room_number = inputRoomNumber
        profile.year = inputYear
        profile.phone = inputPhone
        profile.save()

        # print('is the profile ',profile)
        return redirect('main:edit_student',profile_id)
    context = {'profile':profile,'hostels':hostels}
    return render(request,'main/edit-student.html',context)


@login_required
def student_leave(request):
    profile = Profile.objects.get(user=request.user)
    results = []
    students_leave = ''
    if request.method == "POST":
        query = request.POST['search']
        if query == '':
            query = 'None'
            return redirect('main:student_leave')

        students_query = User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(username__icontains=query))
        context = {'profile':profile,'students':students_query}
        return render(request,'main/student-leave.html',context)
    else:
        students_leave = StudentLeave.objects.all()
    context = {'profile':profile,'students_leave':students_leave}
    return render(request,'main/student-leave.html',context)

@login_required
def add_student_leave(request,pk):
    student = User.objects.get(id=pk)
    if request.method == 'POST':
        place_visiting = request.POST['inputPlaceVisiting']
        date_departing = request.POST['inputDepartureDate']
        date_arriving = request.POST['inputArrivalDate']
        reason = request.POST['textAreaReason']
        
        student_leave_add = StudentLeave.objects.create(user=student,place_visiting=place_visiting,
            departure_date=date_departing,arrival_date=date_arriving,reason=reason)
        return redirect('main:all_students_leave')

    context = {'student':student}
    return render(request,'main/add-students-leave.html',context)

@login_required
def add_school_fees(request):
    fees = FeePaid.objects.all()
    if request.method == 'POST':
        amount = request.POST['inputAmount']
        student_id = request.POST['inputStudentID']
    
        school_fees = FeePaid.objects.create(amount=amount,student_id=student_id)
        moris = User.objects.get(username='moriss')
        # print(moriso.profile.hostel)
        # moris = Profile.objects.filter(user=moriso)[0]
        # print('Username ', moris.username)
        college_students = College.objects.filter(students__id=moris.id)[0]
        # print(college_students,' variables ',vars(college_students))
        more = ''
        for stu in college_students.students.all():
            # print(stu,' with variables ',vars(stu))
            more = stu

        print(more.username,' first name ',more.first_name,' student id', more.profile.id_number)
        fee_paid = FeePaid.objects.filter(student_id=more.profile.id_number)
        total_fees = fee_paid.aggregate(Sum('amount')).get('amount__sum', 0.00)
        balance = float(college_students.fee_amount) - float(total_fees)
        fee_record = FeeRecords.objects.get_or_create(student_id=more.profile.id_number)[0]
        print(fee_record , ' is the new fee record')
        fee_record.student_name =more.username
        fee_record.college = college_students.college_name
        fee_record.amount_paid = total_fees
        fee_record.balance = balance
        fee_record.save()
        print(' more has paid ', total_fees, ' of fees', college_students.fee_amount, ' balance ',balance)
        print(fee_record)
        return redirect('main:add_school_fees')

    context = {'fees':fees}
    return render(request,'main/add-fees.html',context)

@login_required
def fees_records(request):
    records = FeeRecords.objects.all()
    context= {'records':records}
    return render(request,'main/fees-records.html',context)
@login_required
def all_students_leave(request):
    students_leave = StudentLeave.objects.all()
    context = {'students_leave':students_leave}
    return render(request,'main/all-students-leave.html',context)
@login_required
def search_student(request,pk=None):
    profile = Profile.objects.get(user=request.user)
    results = []
    if request.method == "POST":
        query = request.POST['search']
        if query == '':
            query = 'None'
            return redirect('main:admin_details')

        students_query = User.objects.filter(Q(first_name__icontains=query) | 
        Q(last_name__icontains=query) | Q(username__icontains=query))
        context = {'profile':profile,'students':students_query}
        return render(request,'main/students-search.html',context)
 
    context = {'profile':profile}

    return render(request,'main/students-search.html',context)
