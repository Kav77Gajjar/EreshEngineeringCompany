from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from django_ratelimit.decorators import ratelimit
from disposable_email_domains import blocklist
from django.core.exceptions import ValidationError
from .models import Blog, AboutMe, SocialLinks, Services


# common context for all views
def common_context():
    return {
        'about_me' : AboutMe.objects.first(),
        'posts' : Blog.objects.all().order_by("-created_at"),
        'service' : Services.objects.all(),
        'links' : SocialLinks.objects.all()
    }
# admin service
def about_me_view(request):
    return render(request, "Aatmbhav.html", common_context())

def blog_list(request):
    blogs = Blog.objects.all().order_by("-created_at")
    return render(request, "article.html", blogs, {'blogs': blogs})

def blog_short(request):
    context = common_context()
    context['posts'] = context['posts'][:3]
    return render(request, "Aatmbhav.html", context)

def blog_detail(request, slug):
    blog_detail = get_object_or_404(Blog, slug=slug)
    return render(request, 'article.html', {'blog_detail': blog_detail})

def social_view(request):
    return render(request, "Aatmbhav.html", common_context())

def service_view(request):
    context = common_context()
    # context['posts'] = context['posts'][:3]
    return render(request, "Aatmbhav.html", common_context())
# smtp service
@ratelimit(key='ip', rate='3/m', block=True)
def mail(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')

        def clean_email(self):
            email = self.cleaned_data['email']
            domain = email.split('@')[-1].lower()
            if domain in blocklist:
                raise ValidationError("Temporary emails are not allowed.")
            return email

        msg = "Hello you've got an mail"
        admin = "mkav8888@gmail.com"
        user = email
        # mail will be sent to admin
        subject = f"Hello {admin} you have a new message from {name} via your website"
        body = f"""
        <html>
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px;">
                <h2 style="color: #333;">You have a new message from {name}</h2>
                <hr>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Service:</strong> {service}</p>
                <p><strong>Message:</strong><br>         {message}</p>
                <hr>
                <p><a href="mailto:{email}" style="color: #1a73e8;">Reply to sender</a></p>
            </div>
        </body>
        </html>
        """

        send_mail(
            subject,
            msg,  # plain text version
            admin,
            [admin],
            html_message=body
        )
        # mail will be sent to user
        subject2 = f"From Aatmbhav.com: Thank You for Contacting Us"
        body2 = f"""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You for Contacting Us</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body style="font-family: 'Helvetica Neue', Arial, sans-serif; background-color: #f7fafc; margin: 0; padding: 0;">
    <!-- Preheader Text -->
    <div class="preheader" style="display: none; max-height: 0; overflow: hidden;">
        Thank you for contacting us. We appreciate your message and will get back to you soon.
    </div>

    <!-- Email Container -->
    <table class="responsive-table" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#f7fafc">
        <tr>
            <td align="center" valign="top">
                <!-- Main Content -->
                <table width="600" cellspacing="0" cellpadding="0" border="0" style="background-color: #ffffff; margin: 20px auto; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);">
                    <!-- Header with Logo -->
                    <tr>
                        <td align="center" style="padding: 30px 20px; border-bottom: 1px solid #e2e8f0;">
                            <img src="https://via.placeholder.com/200x60?text=Company+Logo" alt="Company Logo" width="200" style="max-width: 100%; height: auto; display: block;">
                        </td>
                    </tr>

                    <!-- Main Message -->
                    <tr>
                        <td style="padding: 30px 20px;">
                            <h1 style="font-size: 24px; font-weight: 600; color: #1a202c; margin-bottom: 20px; text-align: center;">Thank You for Contacting Us</h1>
                            <p style="font-size: 16px; line-height: 1.6; color: #4a5568; margin-bottom: 20px;">
                                Dear Valued Customer,
                            </p>
                            <p style="font-size: 16px; line-height: 1.6; color: #4a5568; margin-bottom: 20px;">
                                We sincerely appreciate you taking the time to reach out to us. Your message has been received, and we want to assure you that our team is reviewing it carefully.
                            </p>
                            <p style="font-size: 16px; line-height: 1.6; color: #4a5568; margin-bottom: 20px;">
                                One of our representatives will be in touch with you shortly to address your inquiry. We typically respond within 24-48 hours during business days.
                            </p>
                            <p style="font-size: 16px; line-height: 1.6; color: #4a5568; margin-bottom: 30px;">
                                Thank you for choosing our company. We value your trust and look forward to assisting you.
                            </p>

                            <!-- Call to Action -->
                            <table width="100%" cellspacing="0" cellpadding="0" border="0">
                                <tr>
                                    <td align="center" style="padding: 15px 0;">
                                        <a href="https://aatmbhav.com" style="display: inline-block; padding: 12px 24px; background-color: #4299e1; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: 600; font-size: 16px;">
                                            Visit Our Website
                                        </a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Social Media Links -->
                    <tr>
                        <td style="padding: 20px 0 30px; text-align: center;">
                            <p style="font-size: 14px; color: #718096; margin-bottom: 15px;">Connect with us on social media</p>
                            <table class="social-icons" align="center" cellspacing="0" cellpadding="0" border="0">
                                <tr>
                                    <td style="padding: 0 10px;">
                                        <a href="https://facebook.com/yourpage" style="display: inline-block; width: 40px; height: 40px; background-color: #3b5998; border-radius: 50%; text-align: center; line-height: 40px;">
                                            <i class="fab fa-facebook-f" style="color: #ffffff;"></i>
                                        </a>
                                    </td>
                                    <td style="padding: 0 10px;">
                                        <a href="https://twitter.com/yourpage" style="display: inline-block; width: 40px; height: 40px; background-color: #1da1f2; border-radius: 50%; text-align: center; line-height: 40px;">
                                            <i class="fab fa-twitter" style="color: #ffffff;"></i>
                                        </a>
                                    </td>
                                    <td style="padding: 0 10px;">
                                        <a href="https://instagram.com/yourpage" style="display: inline-block; width: 40px; height: 40px; background: linear-gradient(45deg, #405de6, #5851db, #833ab4, #c13584, #e1306c, #fd1d1d); border-radius: 50%; text-align: center; line-height: 40px;">
                                            <i class="fab fa-instagram" style="color: #ffffff;"></i>
                                        </a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="padding: 20px; background-color: #edf2f7; border-radius: 0 0 8px 8px; text-align: center;">
                            <p style="font-size: 12px; color: #718096; margin-bottom: 10px;">
                                &copy; 2025 Aatmbhav. All rights reserved.
                            </p>
                            <p style="font-size: 12px; color: #718096; margin-bottom: 0;">
                                <a href="#" style="color: #4299e1; text-decoration: none;">Privacy Policy</a> |
                                <a href="#" style="color: #4299e1; text-decoration: none;">Terms of Service</a>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
        """
        send_mail(subject=subject2, message=msg, from_email=admin, recipient_list=[email], html_message=body2)
        return HttpResponse("Mail sent successfully!")

    return render(request, "Aatmbhav.html")
