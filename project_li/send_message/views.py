from django.shortcuts import render
from twilio.rest import TwilioRestClient
from .forms import Msg

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        form = Msg(request.POST)
        if form.is_valid():

            phone = form.cleaned_data['phone']
            msg = form.cleaned_data['msg']
            msg_body = 'Hello, ' + msg

            ACCOUNT_SID = "AC8676bd34528e9d15743d1e8d3bd9adc2"
            AUTH_TOKEN = "7bb3e76a868342b9b315d2d43ab83c23"
            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

            client.messages.create( to = phone, from_ = "+16176065186", body = msg_body,)
            result = 'Success!! "' + msg + '" is sending to ' + str(phone)

            return render(request, 'send_message.html', {'form': form, 'result': result})

    else:
        form = Msg()
        result = " "
    return render(request, 'send_message.html', {'form': form, 'result': result})