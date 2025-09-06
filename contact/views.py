from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send email notification
            try:
                send_mail(
                    subject=f"Portfolio Contact: {contact_message.subject}",
                    message=f"""
                    New message from your portfolio website:
                    
                    Name: {contact_message.name}
                    Email: {contact_message.email}
                    Subject: {contact_message.subject}
                    
                    Message:
                    {contact_message.message}
                    """,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you! Your message has been sent successfully.')
            except Exception as e:
                messages.warning(request, 'Your message was saved but email notification failed.')
            
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})

