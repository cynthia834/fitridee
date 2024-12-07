import requests  # Correct import for requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import BicycleForm, CustomUserCreationForm
from .models import Bicycle


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def bicycle_list(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'bicycle_list.html', {'bicycles': bicycles})


def upload_bicycle(request):
    if request.method == 'POST':
        form = BicycleForm(request.POST, request.FILES)
        if form.is_valid():
            bicycle = form.save(commit=False)
            bicycle.owner = request.user
            bicycle.save()
            return redirect('bicycle_list')
    else:
        form = BicycleForm()
    return render(request, 'upload_bicycle.html', {'form': form})


def generate_access_token():
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(url, auth=requests.auth.HTTPBasicAuth('your_consumer_key', 'your_consumer_secret'))
    return response.json()['access_token']



def stk_push(access_token):
    url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    from datetime import datetime
    import base64

    business_short_code = '174379'
    lipa_na_mpesa_online_passkey = 'your_lipa_na_mpesa_online_passkey'
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    data_to_encode = business_short_code + lipa_na_mpesa_online_passkey + timestamp
    password = base64.b64encode(data_to_encode.encode()).decode('utf-8')

    payload = {
        'BusinessShortCode': business_short_code,
        'Password': password,
        'Timestamp': timestamp,
        'TransactionType': 'CustomerPayBillOnline',
        'Amount': '1',
        'PartyA': '254704199332',  # Replace with customer's phone number
        'PartyB': business_short_code,
        'PhoneNumber': '254740321377',  # Replace with customer's phone number
        'CallBackURL': 'https://yourdomain.com/callback',
        'AccountReference': 'Test123',
        'TransactionDesc': 'Test Payment'
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()


# Example usage
access_token = generate_access_token()
response = stk_push(access_token)
print(response)
