from flask import Flask, redirect, render_template, url_for, jsonify, request
from discord_webhook import DiscordEmbed
from discord_webhook import DiscordWebhook

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', title='HOME PAGE', custom_css='style')

@app.route('/send',methods=['POST', 'GET'])
def send():
    data = request.form.to_dict()
    webhook_value = data["value"]
    webhook_url = data['url']
    bot = DiscordWebhook(url=webhook_url)
    Send = DiscordEmbed(title='', description=webhook_value, color=0x5c4d7d)
    bot.add_embed(Send)
    bot.execute()
    return redirect(url_for("homepage"))

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='8080')