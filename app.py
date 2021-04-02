import json
import time

from flask import Flask
from flask import request


app = Flask(__name__)

novo_jogo = False

global pontos
global vida
global coordenadaX
global coordenadaY
global atirando

pontos = 0
vida = 100
coordenadaX = 0.0
coordenadaY = 0.0
atirando = False

@app.route('/novo-jogo')
def novo_jogo():
    global novo_jogo
    novo_jogo = True
    return json.dumps(['jogo iniciado'])

@app.route('/status')
def status():
    global novo_jogo
    if(novo_jogo == True):
        return json.dumps([f'pontos: {pontos}', f'vida: {vida}', f'coordenadaX: {coordenadaX}', f'coodenadaY: {coordenadaY}', f'atirando: {atirando}'])
    else:
        return json.dumps(['inicie um novo jogo'])


@app.route('/atualizar-status')
def atualizar_status():
    global novo_jogo

    if(novo_jogo == True):
        global pontos
        global vida
        global coordenadaX
        global coordenadaY
        global atirando

        pts = int(request.args.get('pontos', pontos))
        vd = int(request.args.get('vida', vida))
        cX = float(request.args.get('coordenadaX', coordenadaX))
        cY = float(request.args.get('coordenadaY', coordenadaY))
        at = bool(request.args.get('atirando', atirando))

        pontos = pts
        vida = vd
        coordenadaX = cX
        coordenadaY = cY
        atirando = at

        if(vida == 0):
            novo_jogo = False
        return json.dumps(['atualizado'])

    else:
        return json.dumps(['inicie um novo jogo'])

if __name__ == '__main__':
    app.run()