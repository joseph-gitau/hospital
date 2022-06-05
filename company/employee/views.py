from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Employee, User
from accounts.models import UserProfileInfo
from accounts.forms import  UserCreateForm,UserProfileForm
# from .models import User,UserProfileInfo
# from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View
# from .forms import  UserCreateForm,UserProfileForm,LoginForm
from django.shortcuts import render,redirect 
from django.http.response import HttpResponseRedirect, HttpResponse

import pyautogui as pu


# Create your views here. 
class SignUpView(View):
    model = User,UserProfileInfo
    #login_url = reverse_lazy('login')
    form_class = UserCreateForm
    template_name = "signup.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST, request.FILES or None)


        if form.is_valid():
            # Cleaned(normalized) data
            city = form.cleaned_data.get('city')
            contact_no = form.cleaned_data.get('contactno')
            date_of_birth = form.cleaned_data.get('dob')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            confirm_password = form.cleaned_data.get('confirm_password')
            image = form.cleaned_data.get('image')


            # check if the password match
            if password == confirm_password:
                if not User.objects.filter(email=email).exists():


                    if  User.objects.filter(username=username).exists():
                        pu.alert("Username already exists.Registration Failed.Try again.")
                        return HttpResponseRedirect(reverse_lazy('employee/create'))
                        # return reverse_lazy('employees-list')
                    else:
                        new_user = User.objects.create_user(username=username, password=password, email=email,
                        first_name=firstname, last_name=lastname)
                        new_user.save()
                        user= User.objects.get(username=username)
                        p_form = UserProfileForm()
                        p_form = p_form.save(commit=False)
                        p_form.user = user
                        p_form.dob = date_of_birth
                        p_form.username=username
                        p_form.city = city
                        p_form.contactno = contact_no
                        p_form.image = image
                        p_form.save()
                        pu.alert( text="New User Created Successfully",title="Success")
                        # Create UserProfile model
                        return HttpResponseRedirect(reverse_lazy('employees-list'))

                        
                else:
                    pu.alert('Registration Failed - Try different email address')
                    return HttpResponseRedirect(reverse_lazy('employee/create'))
                # return HttpResponse('Form not valid')
                    # return reverse_lazy('employees-list')

            else:
                pu.alert("password and confirmpassword does not match.Try again")
                return HttpResponseRedirect(reverse_lazy('employee/create'))
        
        # return HttpResponse('Form not valid')

        else:
            pu.alert("Something went wrong.Try again")
            return HttpResponse('Form not valid')
            # return HttpResponseRedirect(reverse_lazy('employee/create')) 
    # return HttpResponseRedirect(reverse_lazy('employees-list')) 

# Only logged in superuser can see this view
class EmployeeCreateViewOld(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Employee
    template_name = "create.html"
    # template_name = "signup.html"
    fields=['eid','ename','eemail', 'epassword','econtact','edob']
    login_url = 'login'  #if not authenticated redirect to login page

    ''' model = UserProfileInfo
    template_name = "create.html"
    fields=['username'] '''
    
        

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # url to redirect after successfully creation
    def get_success_url(self):
         #Displaying message of successful creation of new employee
         pu.alert(text='New Employee Created Successfully',title='Create',button='OK')
         return reverse_lazy('employees-list')


# Only logged in superuser can see this view
class EmployeeListView(LoginRequiredMixin,UserPassesTestMixin,ListView):

    model = Employee
    template_name = 'show.html'
    context_object_name = 'employees'
    paginate_by = 5
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser


    def get_queryset(self):  # new

        if self.request.method == "GET":
            query = self.request.GET.get('search')  # your input name is 'search'
            print('Search word:' + str(query))
        if query:
            return Employee.objects.filter(ename__icontains=query)

        else:
            return Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        employees = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(employees, self.paginate_by)
        try:
            employees = paginator.page(page)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        context['employees'] = employees
        return context



# Only logged in superuser can see this view
class EmployeeDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):

    model = Employee
    template_name = 'detail.html'
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser
   

# Only logged in superuser can see this view
class EmployeeUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Employee
    template_name = 'update.html'
    # specify the fields
    fields = ['eid', 'ename', 'eemail', 'econtact', 'edob']
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # updating details
    # url to redirect after successfully updation
    def get_success_url(self):
         # Displaying message of successful updation of  employee
         pu.alert(text='Employee Info Updated Successfully', title='Update', button='OK')
         return reverse_lazy('employees-list')



# Only logged in superuser can see this view
class EmployeeDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Employee
    template_name = 'delete.html'
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # url to redirect after successfully deletion
    def get_success_url(self):
        # Displaying message of successful deletion of employee
         pu.alert(text='Employee Deleted Successfully', title='Delete', button='OK')
         return reverse_lazy('employees-list')










