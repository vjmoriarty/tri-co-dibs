from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0ca67552c700a66330c9e395429584ff"
# Your Auth Token from twilio.com/console
auth_token  = "e5272a4a070a49fa8f39d8ce5b739ed1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12154200344", 
    from_="+12153020189",
    body="Tomorrow's forecast in Financial District, San Francisco is Clear",
  media_url="https://climacons.herokuapp.com/clear.png")

print(message.sid)


