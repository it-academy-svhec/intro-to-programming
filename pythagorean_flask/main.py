from flask import Flask, render_template, request

app = Flask(__name__)


def compute_hypotenuse(leg_a, leg_b):
    return (leg_a ** 2 + leg_b ** 2) ** 0.5


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate')
def submit():
    leg_a = request.args.get('leg_a')
    leg_b = request.args.get('leg_b')

    hypotenuse = compute_hypotenuse(float(leg_a), float(leg_b))

    return render_template('index.html',
                           hypotenuse=round(hypotenuse, 4),
                           leg_a=leg_a,
                           leg_b=leg_b)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
