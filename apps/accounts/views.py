from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.encoding import force_text
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login
from django.contrib import messages

from .models import User
from .forms import CustomUserCreationForm
from .tokens import account_activation_token

class SignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/registration/signup.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            
            # A user is not considered to be active unless she/he has verified her/his email-id.
            user.is_active = False
            user.save()
            
            # Send the account activation email.
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('accounts/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, '', html_message = message, from_email = '')
            return render(request, 'accounts/registration/account_activation_sent.html')
        return render(request, 'accounts/registration/signup.html', {'form': form})

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk = uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, 'Email-id confirmed successfully! Account activated.')
            return redirect('/')
        else:
            return render(request, 'accounts/registration/account_activation_invalid.html')