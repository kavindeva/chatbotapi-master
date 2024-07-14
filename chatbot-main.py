# import json
import re
# import boto3
# import pandas as pd
# import datetime
from flask import request
from flask import Flask, Response
from twilio.twiml.messaging_response import MessagingResponse

# Initialize our application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images/'


@app.route("/home")
def index():
    return "Welcome to uaq-ftz chatbot service"


# language_en = "en"
# language_ar = "ar"
# language_hi = "hi"
# language_ru = "ru"
# language_ml = "ml"
# language_ta = "ta"
# preferredLanguage = language_en
# print(preferredLanguage)
userData = {}
requirementsData = {}


@app.route("/whatsapp/", methods=['POST', 'GET'])
def whatsapp_upload():
    response = MessagingResponse()
    if request.method == 'POST':
        if request.form:
            userNewResponse = ["hi", "hello", "hi UAQ-FTZ", "hello UAQ-FTZ"]
            userFinalResponse = ["thanks", "thank you", "that's all", "good", "fine", "great", "okay", "ok"]
            # print("received data from whatsapp")
            # print(request.form)
            msg = request.form.get('Body')
            # print(type(msg))
            # print(msg)
            ProfileName = request.form.get("ProfileName")
            # WaID = request.form.get("WaId")
            # waid = int(WaID)
            # print(WaID)
            PersonNumber = request.form.get("From")
            senderNumber = request.form.get("To")
            # print(senderNumber)
            # print(type(msg))

            def rule_process(querymessage):
                # global preferredLanguage
                global userData
                global requirementsData
                if querymessage.lower() in userNewResponse:
                    # print("Greeting matched")
                    data = f"*Hello {ProfileName}!*\nWelcome to Umm Al Quwain Free Trade Zone Bot Assist." \
                           f" Please let me know whether you are an existing customer or not. *Yes / No*"
                    replyData = data
                elif re.findall("yes", querymessage.lower()):
                    # print("second loop")
                    # preferredLanguage = "en"
                    data = f"*Welcome back {ProfileName}*, what would you like to do today?\n" \
                           f"1. Setting up a New Company\n2. License Renewal\n3. Amendments\n" \
                           f"4. Visa Inquiries\n5. Complaints & Grievances\n6. Appreciation"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("no", querymessage.lower()):
                    # print("1 loop")
                    # global preferredLanguage
                    # preferredLanguage = "ar"
                    data = f"*Can you please share a few details with me?*\n1. Name\n2. Email ID\n3. Country" \
                           f"\n4. Phone\n*Note:* Please provide your informations by separating comma(,)"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall(',', querymessage.lower()):
                    # print("1 loop")
                    # global preferredLanguage
                    # preferredLanguage = "ar"
                    userData1 = re.split(',', querymessage)
                    userData['Name'] = userData1[0]
                    userData['Email ID'] = userData1[1]
                    userData['Country'] = userData1[2]
                    userData['Phone'] = userData1[3]
                    data = f"Your given customer details are\n1. Name : {userData['Name']}," \
                           f"\n2. Email ID : {userData['Email ID']},\n3. Country : {userData['Country']},\n4. " \
                           f"Phone number : {userData['Phone']}.\nPlease type *Right*" \
                           f" if it is right or type *Wrong* to change the data."
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("right", querymessage.lower()):
                    # print("1 loop")
                    # global preferredLanguage
                    # preferredLanguage = "ar"
                    data = f"*Thank you for providing your details. Kindly choose from the following " \
                           f"license options for your new company.*\n1. Commercial license\n2. " \
                           f"Consultancy\n3. Industrial\n4. Freelance Permit\n5. Service License"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("setting up a new company", querymessage.lower()):
                    # print("2 loop")
                    # global preferredLanguage
                    # preferredLanguage = "hi"
                    data = f"*Kindly choose from the following license options for your new company.*\n" \
                           f"1. Commercial license\n2. Consultancy\n3. Industrial\n" \
                           f"4. Freelance Permit\n5. Service License"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("new license", querymessage.lower()):
                    # print("2 loop")
                    # global preferredLanguage
                    # preferredLanguage = "hi"
                    data = f"*Kindly choose from the following license options for your new company.*\n" \
                           f"1. Commercial license\n2. Consultancy\n3. Industrial\n" \
                           f"4. Freelance Permit\n5. Service License"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("commercial license", querymessage.lower()):
                    # print("3 loop")
                    # global preferredLanguage
                    # preferredLanguage = "ru"
                    data = f"*What type of a commercial trading license are you looking at*\n\n*1. Commercial Trading" \
                           f" license:* A business engaging in the purchase and sales of goods in the UAE or outside" \
                           f" the UAE are granted commercial licenses. Commercial licenses authorise the import," \
                           f" export, storing and distribution of items specified on the license.\n\n*2. General" \
                           f" Trading license:* General Trading License comes under the broader category of " \
                           f"commercial license. This enables the licensee to trade in a wider range of activities " \
                           f"and gives the freedom and flexibility to trade in any commodity which is permitted " \
                           f"within the UAE.\n\n*Please choose your license type*\n1. General Trading " \
                           f"license\n2. Commercial Trading license"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("commercial trading", querymessage.lower()):
                    # print("3 loop")
                    # global preferredLanguage
                    # preferredLanguage = "ru"
                    requirementsData["license type"] = "Commercial Trading License"
                    print(requirementsData)
                    data = f"*Choose your Entity type*\n1. Free Zone Establishment - 1 Partner\n2. Free zone " \
                           f"company - Multiple partner\n3. Branch - Branch of a company\n\n*And please select the " \
                           f"activities of your choice, so that we can curate a package for you.*\n1. Sharing " \
                           f"Office\n2. Dedicated Office\n3. Warehouse\n4. Land\n\n*Note:* Please provide " \
                           f"your requirements by separating ampersand(&)"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("general trading", querymessage.lower()):
                    # print("3 loop")
                    # global preferredLanguage
                    # preferredLanguage = "ru"
                    requirementsData["license type"] = "General Trading License"
                    print(requirementsData)
                    data = f"*Choose your Entity type*\n1. Free Zone Establishment - 1 Partner\n2. Free zone " \
                           f"company - Multiple partner\n3. Branch - Branch of a company\n\n*And please fill in a " \
                           f"few details so that we can curate a package for you.*\n1. Sharing office\n2. " \
                           f"Dedicated office\n3. Warehouse\n4. Land\n\n*Note:* Please provide " \
                           f"your requirements by separating ampersand(&)"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("consultancy", querymessage.lower()):
                    # print("4 loop")
                    # global preferredLanguage
                    # preferredLanguage = "ml"
                    requirementsData["license type"] = "Consultancy License"
                    data = f"Choose your Entity type*\n1. Free Zone Establishment - 1 Partner\n2. Free zone " \
                           f"company - Multiple partner\n3. Branch - Branch of a company\n\nConsultancy " \
                           f"License is for entities which offer expert or professional " \
                           f"advice and is issued to all manner of professionals including artisans " \
                           f"and craftsmen. It allows two similar activities.\n*Please select the activities " \
                           f"of your choice.*\n1. Sharing office\n2. Dedicated office\n3. Warehouse\n4. Land"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("industrial", querymessage.lower()):
                    # print("5 loop")
                    # global preferredLanguage
                    # preferredLanguage = "ta"
                    requirementsData["license type"] = "Industrial License"
                    data = f"*Choose your Entity type*\n1. Free Zone Establishment - 1 Partner\n2. Free zone " \
                           f"company - Multiple partner\n3. Branch - Branch of a company\n\nIndustrial License" \
                           f" enables the licensee to import raw materials, then" \
                           f" manufacture/ process / assemble / package the specified products, and " \
                           f"export the finished product. It allows the holder to import raw materials " \
                           f"for the purpose of manufacturing, processing and/or assembly of specified products. " \
                           f"Please select the activities of your choice. (or free text for typing the activity)"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("freelance permit", querymessage.lower()):
                    # print("6 loop")
                    requirementsData["license type"] = "Freelance License"
                    data = f"Freelance Permit allows an individual to operate as a freelance " \
                           f"professional, and conduct business in one’s birth name as opposed " \
                           f"to a brand name or company. The Freelance Permit is designed for individuals " \
                           f"who operate in technology, media and film sectors, and is issued to " \
                           f"talent roles, creative roles and selected administrative roles.\n" \
                           f"*Please select your activity so that we can curate a package for you.*"
                    replyData = data
                elif re.findall("service license", querymessage.lower()):
                    # print("7 loop")
                    # customerAmount = customerPaymentAmount[int(customerIndexValue)]
                    # # print(customerAmount)
                    requirementsData["license type"] = "Service License"
                    data = f"Choose your Entity type*\n1. Free Zone Establishment - 1 Partner\n2. Free zone " \
                           f"company - Multiple partner\n3. Branch - Branch of a company\n\nService License" \
                           f" is for service providers. It permits the licensee to carry out the" \
                           f" services specified on the license within the Free Zone, such as Logistics; Courier " \
                           f"Services; Insurance Service Provider; Travel Agency; Tour Services; Car Rental etc."
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("sharing office", querymessage.lower()):
                    # print("8 loop")
                    requirementsData1 = re.split('&', querymessage)
                    print(requirementsData1)
                    requirementsData["entity type"] = requirementsData1[0]
                    requirementsData["facility type"] = requirementsData1[1]
                    print(requirementsData)
                    data = f"Shape your future with our well-planned, impeccably designed " \
                           f"executive offices and co-working spaces that are located in " \
                           f"the headquarters of Umm Al Quwain Free Trade Zone Authority.\n\n" \
                           f"*Please provide us your requirements details below*\n1. Size in " \
                           f"(Square Metre)\n2. Nature of Business\n3. No of Visa required\n\n*" \
                           f"Note:* Please provide your requirements by separating ampersand(&)"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("dedicated office", querymessage.lower()):
                    # print("8 loop")
                    requirementsData1 = re.split('&', querymessage)
                    requirementsData["entity type"] = requirementsData1[0]
                    requirementsData["facility type"] = requirementsData1[1]
                    print(requirementsData)
                    data = f"Shape your future with our well-planned, impeccably designed " \
                           f"executive offices and co-working spaces that are located in " \
                           f"the headquarters of Umm Al Quwain Free Trade Zone Authority.\n\n" \
                           f"*Please provide us your requirements details below*\n1. Size in " \
                           f"(Square Metre)\n2. Nature of Business\n3. No of Visa required\n\n*" \
                           f"Note:* Please provide your requirements by separating ampersand(&)"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("warehouse", querymessage.lower()):
                    # print("8 loop")
                    requirementsData1 = re.split('&', querymessage)
                    requirementsData["entity type"] = requirementsData1[0]
                    requirementsData["facility type"] = requirementsData1[1]
                    data = f"Our prominence as a logistics hub in the region, makes it vital for us to offer " \
                           f"our stakeholders pre-built warehouses for storage and light manufacturing activities." \
                           f"\n\n*Please provide us your requirements details below*\n1. Size in " \
                           f"(Square Metre)\n2. Nature of Business\n3. No of Visa required\n\n*" \
                           f"Note:* Please provide your requirements by separating ampersand(&)"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall("land", querymessage.lower()):
                    # print("8 loop")
                    requirementsData1 = re.split('&', querymessage)
                    requirementsData["entity type"] = requirementsData1[0]
                    requirementsData["facility type"] = requirementsData1[1]
                    data = f"Our premium location on a major highway provides easy access to all Emirates " \
                           f"as well as major sea and airports, thereby giving you a great business address." \
                           f"*\n\nPlease provide us your requirements details below*\n1. Size in " \
                           f"(Square Metre)\n2. Nature of Business\n3. No of Visa required\n\n*" \
                           f"Note:* Please provide your requirements by separating ampersand(&). *Your " \
                           f"response should be like this 450sqm & Software solutions & 10*"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall('sqm', querymessage.lower()):
                    # print("8 loop")
                    requirementsData1 = re.split('&', querymessage)
                    requirementsData["size"] = requirementsData1[0]
                    requirementsData["nature of business"] = requirementsData1[1]
                    requirementsData["no of visas"] = requirementsData1[2]
                    print(requirementsData)
                    data = f"Your given requirement details are\n1. License type: {requirementsData['license type']}" \
                           f",\n2. Entity type : {requirementsData['entity type']},\n3. Facility type : " \
                           f"{requirementsData['facility type']},\n4. Size : {requirementsData['size']},\n5. " \
                           f"Nature of business : {requirementsData['nature of business']},\n6. No of visas : " \
                           f"{requirementsData['no of visas']}.\n\nPlease type *Confirm* if all you provided " \
                           f"details are correct or type *Cancel*"
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                elif re.findall('confirm', querymessage.lower()):
                    data = None
                    if requirementsData['license type'] == 'Commercial Trading License':
                        data = f"Thank you for filling in the details. Your package cost is AED 20500. The " \
                               f"subsequent renewal will be AED 18500. Our sales representative will revert " \
                               f"to you with rest of your package details shortly."
                    if requirementsData['license type'] == 'General Trading License':
                        data = f"Your package cost is AED 27500. You are eligible for 3 visas.Thank you for " \
                               f"filling in the details, our sales representative will revert to you with a" \
                               f" package curated for you on your email id shortly."
                    if requirementsData['license type'] == 'Consultancy License':
                        data = f"Thank you for filling in the details. Your package cost is AED 20500. The " \
                               f"subsequent renewal will be AED 18500. Our sales representative will revert " \
                               f"to you with rest of your package details shortly."
                    if requirementsData['license type'] == 'Industrial License':
                        data = f"Thank you for filling in the details, our sales representative will revert to you" \
                               f" with a package curated for you on your email id shortly."
                    if requirementsData['license type'] == 'Freelance License':
                        data = f"Thank you for filling in the details.  Your package cost is AED 16500. " \
                               f"The subsequent renewal will be AED 14500. Our sales representative " \
                               f"will revert to you with rest of your package details shortly."
                    if requirementsData['license type'] == 'Service License':
                        data = f"Thank you for filling in the details. Your package cost is AED 20500. The " \
                               f"subsequent renewal will be AED 18500. Our sales representative will revert " \
                               f"to you with rest of your package details shortly."
                    replyData = data
                elif re.findall('license renewal', querymessage.lower()):
                    data = f"For inquires related to your license renewal, please contact renewals@uaqftz.com." \
                           f"  Is there anything else that I can help you with?"
                    replyData = data
                elif re.findall('amendments', querymessage.lower()):
                    data = f"For all your license amendment related inquiries, please contact cs@uaqftz.com. " \
                           f"Is there anything else that I can help you with?"
                    replyData = data
                elif re.findall('visa inqui', querymessage.lower()):
                    data = f"For all visa related inquiries, please contact vs@uaqftz.com.  Is there anything" \
                           f" else that I can help you with?"
                    replyData = data
                elif re.findall('complain', querymessage.lower()):
                    data = f"Sorry to learn that. Please provide your feedback so that we can improve our services."
                    replyData = data
                elif re.findall('feedback', querymessage.lower()):
                    data = f"Thank you for your feedback, we will incorporate your feedback and improve our " \
                           f"services for you. Is there anything else that I can help you with?"
                    replyData = data
                elif re.findall('appreciat', querymessage.lower()):
                    data = f"We would love to hear from you. Please tell us about your experience with us."
                    replyData = data
                elif querymessage.lower() in userFinalResponse:
                    # print("15 loop")
                    data = "Thank you for utilizing our FTZ Assist. Please feel free to reach us at " \
                           "anytime. Have a great day {name}".format(name=ProfileName)
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                else:
                    # print("16 loop")
                    data = "Invalid keywords!. Please enter complete valid keywords."
                    # data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                    #                                  TargetLanguageCode=preferredLanguage)
                    # translatedText = data1.get('TranslatedText')
                    replyData = data
                return replyData

            replyData1 = rule_process(msg)
            response.message(body=replyData1, to=PersonNumber, from_=senderNumber)
    return Response(str(response), mimetype="application/xml")


if __name__ == '__main__':
    app.run()
