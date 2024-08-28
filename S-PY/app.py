from flask import Flask, request, jsonify
import requests  # Make sure to install the requests library

app = Flask(__name__)


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    mailer_group = data['mailer_group']
    user = data['user']
    password = data['password']  # Make sure to handle passwords securely!
    status = mailer_subscription(mailer_group, user, password)
    return jsonify({'status': status.text}), status.status_code


def mailer_subscription(mailer_group, user, password):
    subscribe_mail = f"https://xyz.com/mailer/subscribe.do/{mailer_group}/{user}"
    subscribed_status = requests.get(subscribe_mail, auth=(
        user, password))  # This should probably be a POST request
    return subscribed_status


if __name__ == "__main__":
    app.run(debug=True)
