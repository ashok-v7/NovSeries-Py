from flask import Flask, render_template, request

app = Flask(__name__)

# Function to fetch information based on ID


def fetch_information(id):
    # Sample data - replace this with your actual data or fetching logic
    information = {
        "123": {
            "id": "123",
            "item2": "Information for item 2",
            "item3": "Information for item 3",
        }
    }
    return information.get(id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetch', methods=['POST'])
def fetch():
    id = request.form['id']
    information = fetch_information(id)
    return render_template('result.html', information=information)


if __name__ == '__main__':
    app.run(debug=True)
