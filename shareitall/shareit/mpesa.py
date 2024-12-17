 import requests
import base64
from requests.auth import HTTPBasicAuth
from datetime import datetime
import logging
import json


class Mpesa:
    @staticmethod
    def stk_push(donor_name, donor_phone_number, amount):
        # Ensure phone_number and amount are not None
        if not donor_phone_number or not amount or not donor_name:
            raise ValueError("Phone number, amount, and donor name are required for the donation.")


        # Convert amount to float to ensure it's serializable
        amount = float(amount)

        # URL for the STK push API endpoint
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        # Authentication credentials (Use the actual values from your M-Pesa account)
        api_key = "PYE5F2SYv1wrejnkfGEN4JmfJyCkx4QuMY506di8AdNKM0Ob"
        api_secret = "XBP6lJdpj7UtCbd6YgafhzScXvHxgzGEsDIt3GPhlcmfqvQpha2a3ZxUV266xd6q"
        shortcode = "174379"  # Your Business Shortcode
        lipa_na_mpesa_online_shortcode = "174379"  # Same as your Business Shortcode
        lipa_na_mpesa_online_shortcode_key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"  # Your PassKey

        # Headers for the request
        headers = {
            'Authorization': 'Bearer ' + Mpesa.get_access_token(api_key, api_secret),
            'Content-Type': 'application/json'
        }

        # Prepare the request payload
        payload = {
            "BusinessShortCode": 174379,
            "Password": Mpesa.generate_password(shortcode, lipa_na_mpesa_online_shortcode_key, Mpesa.get_timestamp()),
            "Timestamp": Mpesa.get_timestamp(),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": donor_phone_number,  # Use actual donor phone number
            "PartyB": 174379,
            "PhoneNumber": donor_phone_number,  # Use actual donor phone number
            "CallBackURL": "https://mydomain.com/path",  # Change to your actual callback URL
            "AccountReference": "Donation from {}".format(donor_name),  # Include donor's name
            "TransactionDesc": "Payment for donation"
        }

        # Making the request to the Safaricom API
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()  # Return the response in JSON format
        except requests.exceptions.RequestException as e:
            logging.error(f"Error in M-Pesa STK push: {e}")
            raise ValueError("There was an issue processing your donation. Please try again later.")

    @staticmethod
    def get_access_token(consumer_key, consumer_secret):
        """
        :return: auth token for mpesa api calls
        """
        oauth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        response = requests.get(oauth_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        # Check if the response is successful
        if response.status_code == 200:
            access_token = json.loads(response.text).get('access_token', None)
            if not access_token:
                raise ValueError("Failed to retrieve access token.")
            return access_token
        else:
            raise ValueError("Failed to retrieve access token. Status code: {}".format(response.status_code))

    @staticmethod
    def generate_password(shortcode, lipa_na_mpesa_online_passkey, timestamp=None):
        """
        Generates the password required for the M-Pesa STK push request.
        :param shortcode: Business shortcode
        :param lipa_na_mpesa_online_passkey: Passkey provided by Safaricom
        :param timestamp: Current timestamp in the format yyyyMMddHHmmss
        :return: Encoded password string
        """
        if not timestamp:
            timestamp = Mpesa.get_timestamp()
        # Password = Base64 encoded value of BusinessShortCode + LipaNaMpesaPassKey + Timestamp
        password_string = "{}{}{}".format(shortcode, lipa_na_mpesa_online_passkey, timestamp)
        encoded = base64.b64encode(password_string.encode('utf-8')).decode('utf-8')
        return encoded

    @staticmethod
    def get_timestamp():
        # Returns the current timestamp in the required format (yyyyMMddHHmmss)
        return datetime.now().strftime('%Y%m%d%H%M%S')
