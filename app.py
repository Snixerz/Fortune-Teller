from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fortune.html')

@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    return render_template('index.html')

@app.route('/fortune_results')
def fortune_results():
    name = request.args.get('name')
    drink = request.args.get('drink')
    animal = request.args.get('animal')
    city = request.args.get('city')
    fortune = {
        'name' :  name,
        'drink' : drink,
        'animal' : animal,
        'city' : city
    }

    return render_template('fortune_results.html', fortune=fortune)
if __name__ == '__main__':
    app.run()