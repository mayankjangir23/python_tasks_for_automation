from twilio.rest import Client
#enter your twilio creadentials here...
account_sid = 'enter your twilio account sid here'
auth_token = 'enter the token id here'
twilio_phone_number = 'enter your twilio phone numbers here'

to_phone_number = input("Enter the recipient's phone number (with country code, e.g., +91...): ")
message_body = input("Enter your message: ")

client = Client(account_sid, auth_token)

try:
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=to_phone_number
    )
    print(f"✅ Message sent successfully! SID: {message.sid}")
except Exception as e:
    print("❌ Failed to send message.")
    print("Error:", e)
