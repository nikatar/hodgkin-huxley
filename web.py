from flask import Flask, make_response, request
from hh import HodgkinHuxley
from flask import render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')


@app.route("/plot.png")
def plot():
    cm = float(request.args.get('cm'))
    gna = float(request.args.get('gna'))
    gk = float(request.args.get('gk'))
    gl = float(request.args.get('gl'))
    ena = float(request.args.get('ena'))
    ek = float(request.args.get('ek'))
    el = float(request.args.get('el'))

    runner = HodgkinHuxley()
    png_output = runner.Main(cm, gna, gk, gl, ena, ek, el)

    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == "__main__":
    app.run(debug=True)
