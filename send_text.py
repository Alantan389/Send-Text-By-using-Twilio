# Your Account SID from twilio.com/console
account_sid = "your account sid"
# Your Auth Token from twilio.com/console
auth_token  = "your auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16266287239", 
    from_="+15622060553",
    body="Hello, how are you doing ")

print(message.sid)
