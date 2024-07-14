# Twilio documentation's and Configurations
This document shows how to Integrate a Flask RestAPI with WhatsApp in development mode and deployment mode. 
And also it will explain how to do a hands-on practice on 
- Programmable SMS, 
- Programmable WhatsApp, 
- How to buy a new twilio number,
- How to setup a WhatsApp business profile,
- Working with Python SDK,
- Flask RestAPI,
- Twilio Sandbox and 
- Reference links.

## Step 1:
- Login to or create your own account here - [Twilio](https://www.twilio.com/)
- In twilio, it will works in project account based principles, that means you can create your own projects with $15
initial trial account use it for testing purpose and can able upgrade at any time by paying amount. 
- To make it an 
upgraded account have to pay for required each projects.
- To work in any projects first you have to enter into the respective project console.

## Step 2:
### Explore twilio basic console:
- **iAssist** - Project account name
- **Explore Products** - To choose what services needed from Twilio
- **Account SID** - Project account Security Identifier
- **Authorisation token** - Kind of password for that specific project. It can be used in appplication programmable
interface for authentication purpose.

![twilio-demo-1](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-1.png)

## Step 3:
### Explore products:
- **Messaging** - Send and receive messages via SMS, MMS, and WhatsApp

![twilio-demo-2](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-2.png)

- **Phone Numbers** - Choose from local or global numbers, Short Codes, Alphanumeric Sender IDs, etc.

![twilio-demo-3](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-3.png)

- **Developer tools - Studio and SDK** - Build IVRs and chatbots by connecting pre-packaged widgets in a visual editor

![twilio-demo-4](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-4.png)

## Step 4:
### Explore Messaging:
- **Try it out** - Try programmable SMS and programmable WhatsApp
- **Senders** - To setup a new WhatsApp sender (WhatsApp business profile approval), WhatsApp templates and buy a new twilio number
- **Settings** - Enable and disable Geo permissions and WhatsApp Sandbox settings (chat in trial mode)

![twilio-demo-6](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-6.png)

## Step 5: (Programmable Messaging):
### Senders:
![twilio-demo-7](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-7.png)

- **Try Send an SMS**

![twilio-demo-8](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-8.png)

- **Try Send a whatsApp message**

![twilio-demo-9](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-9.png)

- **WhatsApp enabled Senders** - List of approved numbers and to get new approval for WhatsApp senders

![twilio-demo-10](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-10.png)

- **Setting up an Endpoint URL and Company details** - For approved WhatsApp business senders

![twilio-demo-11](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-11.png)

### Settings:
- **WhatsApp Sandbox settings** - To send and receive messages from the Sandbox to your Application, configure your 
endpoint URLs. (Testing environment)

![twilio-demo-12](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-12.png)
- **Geo permission** - To give access or restrict to send and receive SMS and whatsapp messages in mentioned countries

![twilio-demo-13](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-13.png)

### Error logs
- **Log entries** - It will help to see all the status of send and received data with (Date, Time, Service type, 
Direction, From, To, #Segments, Status, Media content and Message body)

![twilio-demo-14](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-14.png)

## Step 6: (Phone Numbers)
**Active Numbers** - It will list all purchased numbers and To buy a new number

![twilio-demo-15](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-15.png)

- **Buy a Number** - Before buying a number choose what kind of services are required like (SMS, MMS, Voice and Fax) 
because some services are available in specified countries. So choose it accordingly

![twilio-demo-17](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-17.png)

- **SMS Endpoint URL** - To set an endpoint URL for send and receive messages in SMS go to phone numbers--->Active 
numbers---> choose your number to assign URL---> scroll down--->under (messaging section)--->In box of "A MESSAGE COMES IN"--->Enter URL

![twilio-demo-16](https://github.com/kavindevarajan/chatbotapi/blob/master/twilio-demo-images/twilio-demo-16.png)

## Reference Links:
1. [Flask RestAPI with Twilio](https://www.twilio.com/blog/2017/03/building-python-web-apps-with-flask.html) - Building Python web apps with Flask
2. [Install twilio](https://pypi.org/project/twilio/) - From python packet manager
3. [Twilio github documentation](https://github.com/twilio/twilio-python/) - Twilio python Github Documentation
4. [Twilio Documentation](https://www.twilio.com/docs/all) - All documentation of twilio
5. [API Reference](https://www.twilio.com/docs/api) - All twilio API Reference
6. [Python helper library -1](https://www.twilio.com/docs/libraries/python) - The Twilio Python Helper Library -1
7. [Python helper library -2](https://www.twilio.com/docs/libraries/reference/twilio-python/) - The Twilio Python Helper Library -2
8. [Twilio library references](https://www.twilio.com/docs/libraries/reference/twilio-python/7.11.0/README.html#documentation) - Twilio-Python Library references
9. [SMS documentation](https://www.twilio.com/docs/sms) - SMS with twilio programmable messaging
10. [SMS quickstart](https://www.twilio.com/docs/sms/quickstart/python) - SMS quickstart with python
11. [WhatsApp business API setup](https://www.twilio.com/docs/whatsapp) - The WhatsApp Business API with Twilio
12. [WhatsApp quickstart](https://www.twilio.com/docs/whatsapp/quickstart/python) - Programmable Messaging for WhatsApp and Python Quickstart
