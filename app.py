import json

from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("home.html",red_zone=read_red_zones())


def read_red_zones():
    # Opening JSON file
    f = open('red_zone.json', )

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    red_zones={}
    for zone in data:
        # {'Singasandra, Bengaluru, Karnataka': {'center': {'lat': 12.88027485,
        #                                                   'lng': 77.65475374894244}},
        #
        red_zones[zone['Location']]={'center':{'lat':zone['lat'],'lng':zone['long']}}


    return red_zones



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
