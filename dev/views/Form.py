# myapp/views.py
from django.shortcuts import render, redirect
from dev.models import Applicant
from django.utils import timezone

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


# Email Configuration modules
from django.core.mail import send_mail
from django.utils import timezone

from .content import mail_content

def apply(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        preferred_internship_domain = request.POST.get('preferred_internship_domain')
        college = request.POST.get('college')
        contact_number = request.POST.get('contact_number')
        whatsapp_number = request.POST.get('whatsapp_number')
        highest_academic_qualification = request.POST.get('highest_academic_qualification')
        current_year = request.POST.get('current_year')
        where_learned_about_codad = request.POST.get('where_learned_about_codad')
        joined_using = request.POST.get('joined_using')
        accept_terms = 'accept_terms' in request.POST
        
                # Generate a password using name and year
        password = f"{email.split('@')[0]}{current_year}"  # You can customize this as needed
        hashed_password = make_password(password)

        # Check if the username already exists
        username = email.split('@')[0]
        try:
            # Try to retrieve the Applicant object with the specified email
            applicant = Applicant.objects.get(email=email)
            print("Applicant exists:", applicant.name)
        except:
            applicant = False
            print("Applicant does not exist")

        if not applicant:
            # Create a new user
            try:
                user = User.objects.create(
                    username=username,
                    email=email,
                    password=hashed_password,
                    first_name=name,
                    last_name=current_year,
                )
            except:
                pass
        try:
            Applicant.objects.get(email=email, preferred_internship_domain=preferred_internship_domain, current_year=current_year)
            return render(request,"error.html")
        except:
            Applicant.objects.create(
                email=email,
                name=name,
                gender=gender,
                preferred_internship_domain=preferred_internship_domain,
                college=college,
                contact_number=contact_number,
                whatsapp_number=whatsapp_number,
                highest_academic_qualification=highest_academic_qualification,
                current_year=current_year,
                where_learned_about_codad=where_learned_about_codad,
                joined_using=joined_using,
                accept_terms=accept_terms,
                updated_time=timezone.now(),
            )

        send_mail(
                'Unlocking Opportunities: Your Codad Internship Journey – Offer Letter and Exciting Projects Await!',                         # subject
                'We are thrilled to inform you that you have successfully secured a position in the Codad Internship Program! Congratulations on your achievement, and welcome to the Codad family. 🚀',      # body
                'sitejec@gmail.com',                        # sender Email
                [email],                                    # receiver mail
                html_message=mail_content(name,username,password,preferred_internship_domain),
                fail_silently=False,
        )

        print("email are sended")
        return redirect('login')  # Redirect to a success page

    return render(request, 'forms/apply.html')

def applicant_list(request):
    applicants = Applicant.objects.all()
    return render(request, 'forms/applicant_list.html', {'applicants': applicants})

"""

Hackthon
open source
workshops
startup

"""

'''
now im involving myself to web3 i hope tpg will help to make shine my feature

i wish to contributed into tpg to our success...
'''


# social midia, tecnical, general