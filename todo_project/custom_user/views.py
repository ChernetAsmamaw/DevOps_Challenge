from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm

# Email Related Imports
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Automatically log the user in after registration
            
            # Email Notification
            try:
                template = render_to_string('custom_user/email_template.html', {'name': user.email})
                email = EmailMessage(
                    'Welcome to Todo App',
                    template,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                )
                email.content_subtype = "html"
                email.fail_silently = False
                email.send()
            except Exception as e:
                print(f"Error sending email: {e}")

            return redirect('todo:todo_list')  # Redirect to the todo list page
    else:
        form = UserRegistrationForm()
    return render(request, 'custom_user/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo:todo_list')  # Redirect to the todo list page
        else:
            error = "Invalid credentials"
            return render(request, 'custom_user/login.html', {'error': error})
    return render(request, 'custom_user/login.html')
