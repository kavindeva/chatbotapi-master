"""
   Module Name:  Chatbotapi
   Company Name: LAN Innovations
   Author Names: Sabarish K and Kavin D
   Last modified: 30-November-2021
   Description:
                Application Programming Interface for IAssist and WhatsappAPI
                ---------------------------------------------
   Chatbotapi is an API module for the chatBot application called IAssist. This API running in backend
   and integrated with the IAssist project. It aims to predict an rightful solution for an error message
   sent by user or customer with the developed deep learning sequential model. Through this API, user can
   send their error message in text manner or by uploading image or screenshots. This API will return the
   respective solution in an user interface chat area.
   Steps involved below:
   1. Get error message in text or image format from client side through REST API
   2. Clean error message
   3. Word Tokenizer for given error message
   4. Change error message sequence index into maximum length
   5. If it is an image, decode the binary image data and pass it to OCR
   6. Extract text from image using Optical Character Recognition(OCR)
   7. Load the trained model for prediction
   8. Predict an index value for given error message
   9. Return the index position
   10. Return the solution value for the respective index position.
   For more details check Github link below:
   https://github.com/kavindevarajan/IT_support_chatbot
"""

import os
import re
# import cv2
import json
import glob
import shutil
import asyncio
import requests
import logging
# import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from deepgram import Deepgram
from tesserocr import PyTessBaseAPI
from nltk.tokenize import word_tokenize
from tensorflow.keras.models import load_model
from flask import Flask, jsonify, request, Response
from tensorflow.keras.preprocessing.text import Tokenizer
from twilio.twiml.messaging_response import MessagingResponse
from tensorflow.keras.preprocessing.sequence import pad_sequences
from werkzeug.utils import secure_filename

# Initialize our application
app = Flask(__name__)
# To store uploaded images under this directory
app.config['UPLOAD_FOLDER'] = 'images/'
ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}

logger = logging.getLogger(__name__)
app.logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('model-execution.log')
file_handler.setFormatter(formatter)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)

app.logger.addHandler(file_handler)


# app.logger.addHandler(stream_handler)


def load_dataset(file_input):
    """A method to load the dataset in.csv format and separate Error messages,
    Resolutions and Unique error messages(without duplicates)."""
    df = pd.read_csv(file_input, encoding="latin1", names=["Error_Message", "Resolution"])
    resolution1 = df["Resolution"]
    unique_resolution1 = list(set(resolution1))
    error_message1 = list(df["Error_Message"])
    return resolution1, unique_resolution1, error_message1


# Load the dataFrame
resolution, unique_resolution, error_message = load_dataset("C:\\inetpub\\wwwroot\\iAssist_IT_support\\"
                                                            "Datasets\\chatDataset_all.csv")

# Convert resolution as string type
resolution = resolution.astype(str)

# Convert unique values as string and store it into a list
unique_resolution = list(map(str, unique_resolution))


def cleaning(sentences):
    """A method for cleaning and tokenizing the data in Error_Message using NLTK"""
    words = []
    for s in sentences:
        clean = re.sub(r'[^ a-zA-Z0-9]', " ", s)
        w = word_tokenize(clean)
        words.append([i.lower() for i in w])
    return words


def padding_doc(encoded, maxlength):
    """A method to pad all the sequences to get same length"""
    return pad_sequences(encoded, maxlen=maxlength, padding="post")


# Load the model output file to predict an input error_message
modelFile = load_model("C:\\inetpub\\wwwroot\\iAssist_IT_support\\model\\model_gitex.h5")

# Clean the input error message for tokenizing convenience
cleaned_words1 = cleaning(error_message)


def create_tokenizer(words, filters='/!"#$%&()*+,-.:;<=>?@[\]^_`{|}~'):
    """Define a Keras preprocessing called 'tokenizer' method from tensorflow to updates internal vocabulary based
    on a list of texts, lower case all the data and tokenize from words to sequence data."""
    token = Tokenizer(filters=filters)
    token.fit_on_texts(words)
    return token


def max_length(words):
    """Define function to find maximum length of message presence in error_message series"""
    return len(max(words, key=len))


word_tokenizer = create_tokenizer(cleaned_words1)
max_length = max_length(cleaned_words1)


# print(max_length)


def get_index_value(text1):
    """Extract the value of resolution and
    predict the text value and then return accuracy value"""
    uniqueResolution = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                        '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
                        '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',
                        '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61',
                        '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76',
                        '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91',
                        '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105',
                        '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118',
                        '119', '120']
    prediction = predictions(text1)

    # Return which class had accuracy level of above 0.7 and below 1.0
    resolution1 = get_final_output(prediction, uniqueResolution)

    # Separate only index values contains in numpy.int
    print(resolution1)
    resolution1 = int(resolution1[:3])
    app.logger.debug(resolution1)
    return resolution1


def predictions(textin):
    """Predict the confidential level of all unique resolutions for
    an error message sent by user and then return all prediction levels"""
    clean = re.sub(r'[^ a-zA-Z0-9*?%]', " ", textin)
    test_word = word_tokenize(clean)
    test_word = [w.lower() for w in test_word]

    # Tokenize the text data into a sequence
    test_ls = word_tokenizer.texts_to_sequences(test_word)

    # Check for unknown words
    if [] in test_ls:
        test_ls = list(filter(None, test_ls))
    test_ls = np.array(test_ls).reshape(1, len(test_ls))

    # Convert given error message's numerical index value into a maximum index value by adding zero's
    x = padding_doc(test_ls, max_length)
    prediction_out = modelFile.predict(x)
    return prediction_out


def get_final_output(predin, classes):
    """Return the resolution value which have higher confidential level"""
    resolution1 = None
    # Pick a numerical data from list of list
    predict = predin[0]

    # Convert a unique resolutions from list to numpy array
    classes = np.array(classes)

    # Sort the prediction values based on list index positions
    ids = np.argsort(-predict)

    # Change all the values in unique resolution's index positions as same as prediction values
    classes = classes[ids]

    # Now sort the prediction values in descending orders
    predict = -np.sort(-predict)

    # Return the only probability value between 0.7 to 1.0
    for i in range(predin.shape[1]):
        print("%s has confidence = %s" % (classes[i], (predict[i])))
        if 0.7 <= predict[i] <= 1.0:
            resolution1 = classes[i]
            app.logger.debug("%s has confidence = %s" % (classes[i], (predict[i])))
    return resolution1


def post_response(value):
    """Locate and return respective response value in response column
    for an error_message sent by the user"""
    df1 = pd.read_csv("C:\\inetpub\\wwwroot\\iAssist_IT_support\\Datasets\\"
                      "Reference_Resol.csv", encoding="latin1", names=["Response", "Resolution"])

    # Locate resolution index value if it is presence and return it's respective solution message
    df1 = df1.loc[df1.Resolution.isin([value])]
    df2 = df1['Response']
    # print(type(df2))
    return df2


def oc_recognition(images):
    with PyTessBaseAPI() as api:
        api.SetImageFile(images)
        t = api.GetUTF8Text()
        # p = str(api.AllWordConfidences())
    return t


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/bot")
def home():
    return jsonify("Welcome to Model Execution Application Programming Interface")


t1 = []


@app.route('/bot/app', methods=['POST'])
async def error_upload():
    # route http posts to this method
    # if request.method == 'POST':
    # Get data in json format
    if request.method == 'POST':
        if request.files:
            print('Sent image file')
            file = request.files['file']
            print(file)
            print('yes')
            if 'file' not in request.files:
                app.logger.debug("No file part in the request")
                response = jsonify({'message': 'No file part in the request'})
                response.status_code = 400
                return response
            if file.filename == '':
                app.logger.debug("No file selected for uploading")
                response = jsonify({'message': 'No file selected for uploading'})
                response.status_code = 400
                return response
            if file and allowed_file(file.filename):
                global t1
                app.logger.debug("OCR section")
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                app.logger.debug(filename)
                app.logger.debug("Image received successfully")
                folderpath1 = glob.glob('images/*')
                latest_file = max(folderpath1, key=os.path.getmtime)
                print(latest_file)
                if latest_file and filename:
                    with PyTessBaseAPI() as api_img:
                        api_img.SetImageFile(latest_file)
                        app.logger.debug("Processed OCR for received app-image {}".format(filename))
                        api_img.Recognize()
                        api_img.GetUTF8Text()
                        t = api_img.GetUTF8Text()
                        print(t)
                        t1 = list(t)
                if not t1:
                    app.logger.debug("No content in image")
                    data = "Please send me a clear picture with Error Message"
                    return jsonify(data)
                else:
                    index = get_index_value(t)
                    post = post_response(index)
                    post = post.to_json()
                    text = post[6:-2]
                    text1 = re.sub(r'\A:"', '', text)
                    text2 = re.sub(r"\\", "", text1)
                    data = re.sub(r'\Bu0092', "'", text2)
                    app.logger.debug("Solution fetched")
                    toSend = {"id": filename, "solution": data}
                    return jsonify(toSend)
            else:
                app.logger.debug("Sorry, allowed file types are .PNG or .JPEG/.JPG")
                data = jsonify({'message': 'Sorry, allowed file types are .PNG or .JPEG/.JPG'})
                data.status_code = 400
                return data
        elif request.get_json():
            error_data = request.get_json()
            error_data = error_data['data']
            app.logger.debug("Custom app text message received")
            index = get_index_value(error_data)
            post = post_response(index)
            post = post.to_json()

            # Slice row index value and return only solution message
            text = post[6:-2]
            text1 = re.sub(r'\A:"', '', text)
            text2 = re.sub(r"\\", "", text1)
            data = re.sub(r'\Bu0092', "'", text2)
            # print(data)
            app.logger.debug("Solution fetched")
            return jsonify(data)
    # elif request.data:
    #     # Request the image data in binary format
    #     image_file = request.data
    #     print(image_file)
    #     filename_path = "images/image{number}.png".format(number=1)
    #     # Convert binary data into numpy array
    #     np_array = np.frombuffer(image_file, np.uint8)
    #     np_image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    #     cv2.imwrite(filename_path, np_image)
    #     w = np_image.shape[1]
    #     h = np_image.shape[0]
    #
    #     if len(np_image.shape) > 2:
    #         np_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
    #         bpp = 3
    #     else:
    #         bpp = 1
    #     img_bytes = np_image.tobytes()
    #     bpl = bpp * w
    #     with PyTessBaseAPI() as api_img:
    #         api_img.SetImageBytes(imagedata=img_bytes,
    #                               width=w,
    #                               height=h,
    #                               bytes_per_pixel=bpp,
    #                               bytes_per_line=bpl)
    #         api_img.Recognize()
    #         api_img.GetUTF8Text()
    #         t = api_img.GetUTF8Text()
    #     t1 = list(t)
    #     if not t1:
    #         data = "Please send me a clear picture with Error Message"
    #     else:
    #         index = get_index_value(t)
    #         post = post_response(index)
    #         post = post.to_json()
    #         data = post[6:-2]


@app.route("/bot/whatsapp", methods=['POST'])
def whatsapp_upload():
    response = None
    imageName = None
    audioName = None
    if request.method == 'POST':
        if request.form.get("MediaContentType0") == "audio/ogg":
            app.logger.debug("Received whatsapp-audio data")
        elif request.form.get("MediaContentType0") == "image/jpeg":
            app.logger.debug("Received whatsapp-image data")
        elif request.form.get("NumMedia") == '0':
            app.logger.debug("Received whatsapp-JSON data")
        sampleData = request.form
        print(sampleData)
        if request.form.get('MediaUrl0'):
            PersonNumber1 = request.form.get("From")
            if request.form.get("MediaContentType0") == "image/jpeg":
                # print(request.form)
                # print(request.form.get("MediaContentType0"))
                app.logger.debug("Whatsapp-Image section")
                messageData = request.form
                messageJsonData = json.dumps(messageData, indent=4)
                imageID = request.form.get("MessageSid")
                ProfileName = request.form.get("ProfileName")
                PersonNumber = request.form.get("From")
                imageUrl = request.form.get("MediaUrl0")
                imageDirectory = Path("C:\\inetpub\\wwwroot\\iAssist_IT_support\\User_data")
                # print(imageID + '\n' + imageUrl + '\n' + PersonNumber + '\n' + ProfileName)
                jsonMessage = imageID + ".json"
                imageExtension = imageID + ".png"
                userFolder = imageDirectory / ProfileName
                requestImage = requests.get(imageUrl, stream=True)
                with open(imageDirectory / jsonMessage, 'w') as jsonfile:
                    jsonfile.write(messageJsonData)
                with open(imageDirectory / imageExtension, 'wb') as imagefile:
                    imagefile.write(requestImage.content)
                for fileName in os.listdir("C:\\inetpub\\wwwroot\\iAssist_IT_support\\User_data"):
                    if fileName.startswith(imageID):
                        imageName = fileName
                image = os.path.join(imageDirectory, imageName)
                # print(image)
                error_message2 = oc_recognition(image)
                message3 = list(error_message2)
                if not message3:
                    response = MessagingResponse()
                    response.message(body="Please send me a clear image with error message.", to=PersonNumber)
                else:
                    index3 = get_index_value(error_message2)
                    post = post_response(index3)
                    post = post.to_json()
                    text = post[6:-2]
                    text1 = re.sub(r'\A:"', '', text)
                    text2 = re.sub(r"\\", "", text1)
                    data = re.sub(r'\Bu0092', "'", text2)
                    app.logger.debug("Solution fetched")
                    response = MessagingResponse()
                    response.message(body=data, to=PersonNumber)
                imageName1 = os.path.join(imageDirectory, imageName)
                messageJsonData1 = os.path.join(imageDirectory, jsonMessage)
                pathDirectory = userFolder
                if os.path.isdir(pathDirectory):
                    print("True")
                    shutil.move(imageName1, userFolder)
                    shutil.move(messageJsonData1, userFolder)
                else:
                    print("False")
                    os.mkdir(os.path.join(imageDirectory, ProfileName))
                    shutil.move(imageName1, userFolder)
                    shutil.move(messageJsonData1, userFolder)
            elif request.form.get("MediaContentType0") == "audio/ogg":
                messageData = request.form
                messageJsonData = json.dumps(messageData, indent=4)
                audioID = request.form.get("MessageSid")
                ProfileName = request.form.get("ProfileName")
                PersonNumber = request.form.get("From")
                audioUrl = request.form.get("MediaUrl0")
                audioDirectory = Path("C:\\inetpub\\wwwroot\\iAssist_IT_support\\User_data")
                # print(audioID + '\n' + imageUrl + '\n' + PersonNumber + '\n' + ProfileName)
                jsonMessage = audioID + ".json"
                audioExtension = audioID + ".m4a"
                userFolder = audioDirectory / ProfileName
                requestAudio = requests.get(audioUrl, stream=True)
                with open(audioDirectory / jsonMessage, 'w') as jsonfile:
                    jsonfile.write(messageJsonData)
                with open(audioDirectory / audioExtension, 'wb') as audiofile:
                    audiofile.write(requestAudio.content)
                for fileName in os.listdir("C:\\inetpub\\wwwroot\\iAssist_IT_support\\User_data"):
                    if fileName.startswith(audioID):
                        audioName = fileName
                audioPath = os.path.join(audioDirectory, audioName)
                # Your Deepgram API Key
                apiKey = "244a7693c1162ff6b088250d3e618ade9831de8f"

                async def transcribe_audio(audio_file):
                    # Initialize the deepgram SDK
                    dg_client = Deepgram(apiKey)
                    # Open the audio file
                    with open(audio_file, 'rb') as audio:
                        # Replace mimetype as appropriate
                        source = {'buffer': audio, 'mimetype': 'audio/m4a'}
                        response1 = await dg_client.transcription.prerecorded(source, options={"punctuate": True})
                        # print(json.dumps(response1, indent=4))
                        return json.dumps(response1, indent=4)

                transcribedErrorMessage = asyncio.run(transcribe_audio(audioPath))
                with open("trancribedData.json", 'w') as jsonfile:
                    jsonfile.write(transcribedErrorMessage)
                jsonFile = open("trancribedData.json")
                fileData = json.load(jsonFile)
                transcribedErrorMessage1 = fileData["results"]["channels"][0]["alternatives"][0]["transcript"]
                # print(transcribedErrorMessage1)
                tr_message = list(transcribedErrorMessage1)
                if not tr_message:
                    response = MessagingResponse()
                    response.message(body="Please send me a clear audio with error message.", to=PersonNumber)
                else:

                    index3 = get_index_value(transcribedErrorMessage1)
                    post = post_response(index3)
                    post = post.to_json()
                    text = post[6:-2]
                    text1 = re.sub(r'\A:"', '', text)
                    text2 = re.sub(r"\\", "", text1)
                    data = re.sub(r'\Bu0092', "'", text2)
                    app.logger.debug("Solution fetched")
                    response = MessagingResponse()
                    response.message(body=data, to=PersonNumber)
                audioName1 = os.path.join(audioDirectory, audioName)
                messageJsonData1 = os.path.join(audioDirectory, jsonMessage)
                pathDirectory = userFolder
                if os.path.isdir(pathDirectory):
                    print("True")
                    shutil.move(audioName1, userFolder)
                    shutil.move(messageJsonData1, userFolder)
                else:
                    print("False")
                    os.mkdir(os.path.join(audioDirectory, ProfileName))
                    shutil.move(audioName1, userFolder)
                    shutil.move(messageJsonData1, userFolder)
            else:
                app.logger.debug("Received irrelevant file content")
                data = "Sorry, I can accept only audio or image files such as .PNG/.JPEG/.JPG"
                response = MessagingResponse()
                response.message(body=data, to=PersonNumber1)
        elif request.form.get("NumMedia") == '0':
            # print("received data from whatsapp")
            msg = request.form.get('Body')
            PersonNumber = request.form.get("From")
            # print(type(msg))
            index3 = get_index_value(msg)
            # print(type(index3))
            post = post_response(index3)
            post = post.to_json()
            text = post[6:-2]
            text1 = re.sub(r'\A:"', '', text)
            text2 = re.sub(r"\\", "", text1)
            data = re.sub(r'\Bu0092', "'", text2)
            app.logger.debug("Solution fetched")
            response = MessagingResponse()
            response.message(body=data, to=PersonNumber)
    return Response(str(response), mimetype="application/xml")


if __name__ == '__main__':
    # app.run()
    app.run()
