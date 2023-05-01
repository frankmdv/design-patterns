from flask import Flask, render_template
from abstractFactory import *

app = Flask(__name__)



@app.route('/')
def index():

    medieval_factory = MedievalFactory()
    player1_unit = medieval_factory.create_unit()
    player2_building = medieval_factory.create_building()
    result_medieval = {
        "player1": player1_unit.attack(),
        "player2": player2_building.produce_unit().attack()
    }

    fantasy_factory = FantasyFactory()
    player1_unit = fantasy_factory.create_unit()
    player2_building = fantasy_factory.create_building()
    result_fantasy = {
        "player1": player1_unit.attack(),
        "player2": player2_building.produce_unit().attack()
    }

    return render_template('index.html', result_medieval=result_medieval, result_fantasy=result_fantasy)


if __name__ == '__main__':
    app.run(debug=True)