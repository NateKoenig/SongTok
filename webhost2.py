from flask import Flask, redirect, render_template, url_for, request
import validators
import requests
from TikTokApi import TikTokApi
import string
import random

#TODO:
# - Fix the url, it's a tik tok link and need it to be an mp3
# - Check if valid tik tok link, not just valid url (we can just given an error too, not a big deal)
# - Output song on a different page? Use redirect if so. If not, how to output/display?
# - If invalid url, display a message saying so

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "POST":
		url_input = request.form["link"]
		valid = validators.url('{}'.format(url_input))
		if valid == True:
			#cookies
			verifyFp="verify_kon4ht8t_cXlUzSMR_D9IQ_4viA_BfCh_Z6QwNIYLNtIf"
			#api = TikTokApi.get_instance(custom_verifyFp=verifyFp, custom_did=did)
			api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

			#retrieve video from url
			video = api.get_Video_By_TikTok(url_input)

			#download tiktok video into mp3 (use aws s3)



			#From https://docs.audd.io
			data = {
	    		'api_token': '4d50671c81da7437891a11846780852b',
	    		'url': '{}'.format(url_input),
			}
			result = requests.post('https://api.audd.io/recognizeWithOffset/', data=data)
			#console.log(result)
			return result.text
		else:
			return render_template("index.html")
	else:

		return render_template("index.html")


if __name__ == "__main__":
	app.run()


#Code to download tik toks
# did=''.join(random.choice(string.digits) for num in range(19))
# verifyFp="verify_kon4ht8t_cXlUzSMR_D9IQ_4viA_BfCh_Z6QwNIYLNtIf"
#api = TikTokApi.get_instance(custom_verifyFp=verifyFp, custom_did=did)
# api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
# print(api.trending())

# from pathlib import Path
# Path("downloads").mkdir(exist_ok=True) # creates folder
# for i in range(len(tiktoks)):
    # data = api.get_Video_By_TikTok(tiktoks[i])# bytes of the video
    # with open("downloads/{}.mp4".format(str(i)), 'wb') as output:
        # output.write(data) # saves data to the mp4 file


#Helpful reads:
#https://medium.com/analytics-vidhya/download-tiktoks-with-python-dcbd79a5237f
#https://www.youtube.com/watch?v=zwLmLfVI-VQ
#https://yanwei-liu.medium.com/how-to-use-ffmpeg-on-python-2ba3fa360ba7
#https://docs.audd.io
