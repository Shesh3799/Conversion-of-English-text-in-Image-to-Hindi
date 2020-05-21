import pytesseract
from PIL import Image
from googletrans import Translator
from nltk.tokenize import sent_tokenize
from autocorrect import Speller
from flask import Flask,render_template,request,flash,redirect,url_for
import os
import json
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "images//"
app.config["CACHE_TYPE"] = "null"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/',methods=['GET','POST'])
def home():
    address = "static/result/res" + str(1) + ".jpg"
    print(address)
    return render_template('index.html',addr=address)

@app.route('/detect',methods=['GET','POST'])
def detect():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], "test.jpg"))
        img = Image.open("images//test.jpg")

        pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
        result = pytesseract.image_to_string(img)
        with open('abc.txt', mode='w')as file:
            file.write(result)  # writes the extracted text in abc.txt file
        print("<-----EXTRACTED TEXT----->")
        print(result)
        spell = Speller(lang='en')
        new = spell(result)
        print("<-----OUTPUT AFTER SPELLING CORRECTION----->")
        print(new)
        paragraph = sent_tokenize(new)
        print("<-----SENTENCE TOKENIZE OUTPUT----->")
        print(paragraph)
        
        print("<-----LIST OF SENTENCES BEFORE TRANSLATION AND AFTER TOKENIZING-----> ")
        translator = Translator()
        completeSentence = ''
        for sentence in paragraph:
            print(sentence)
            translate = translator.translate(sentence, src='en', dest='hi')
            completeSentence = completeSentence + translate.text
        
            print("<-----COMPLETE TEXT AFTER TRANSLATION------>")
            print(completeSentence)
        return render_template('index.html',result1=result,resut2="Shesh",result3=completeSentence)


    return render_template('index.html')

if __name__=="__main__":
     app.run(port=5000, debug=True)
