from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def mail(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')

        user = "mkav8888@gmail.com" #change here to your name

        subject = f"Hello {user} you have a new message from {name} via your website"
        body = f"""
        <html>
        <body>
        ----------------------------------------------------------------------------
        <h1>You have a new message from {name}<h1> 
        \n\n
        <h2>Details of sender :</h2>
        <p><h3><strong>Name:</strong><h3> <h4><i>{name}</i><h4></p>
        <p><h3><strong>Email:</strong><h3> <h4><i>{email}</i><h4></p>
        <p><h3><strong>Phone:</strong><h3> <h4><i>{phone}</i><h4></p>
        <p><h3><strong>Choice:</strong><h3> <h4><i>{service}</i><h4></p>
        <p><h3><strong>Message:</strong><h3>\n          <h4>{message}<h4></p>
        ----------------------------------------------------------------------------
        
        Wanna compose a mail to {user}?
        <p>Click Here<a href="mailto:{email}">here</a> to
        
        </body>
        </html>
        """

        recipients = ["mkav8888@gmail.com"]

        send_mail(subject, body, email, recipients)

        return HttpResponse("Mail sent successfully!")

    return render(request, "Aatmbhav.html")
