from flask import Flask, jsonify
from datetime import date
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)

tempo = date.today()

spec = FlaskPydanticSpec('flask',
                        title='Segunda API - SENAI',
                        version='1.0.0')
spec.register(app)

@app.route('/dia_hoje/<dia>-<mes>-<ano>')
def valores_hoje(dia, mes, ano):
    """
    API para calcular a diferença entre duas datas inseridas

    ## Endpoint:
    `GET /dias/<data_str>

    ## Parâmetros:
    - `data_str' (str): ** Data no formato "DD-MM-YYYY" ** (exemplo: "15-03-2025").
    - ** Qualquer outro formato resultará em erro .**

    ## Resposta (JSON):
    {
        "status": "passado"
        "d_atual": "xx/yy/ww",
        "d_inserido": "xx/yy/ww",
        "dias_diferente": 0,
        "mes_diferente": 0,
        "ano_diferente": 0,
        }

    ## Erros possíveis:
    - Se `data_str' não estiver no formato correto, retorna erro ** 400 Bad Request **:
    json

    :param dia:
    :param mes:
    :param ano:
    :return:
    """

    try:
        dia:int(dia)
        mes:int(mes)
        ano:int(ano)
        data = date(dia, mes, ano)
        numero_inserido = tempo - data
        if numero_inserido.days < 0:
            print('A data inserida está no futuro')
            status = 'futuro'

        elif numero_inserido.days > 0:
            print('A data inserida está no passado')
            status = 'passado'

        else:
            print('A data inserida está mesmo dia')
            status = 'presente'

        d_atual = tempo.strftime('%d/%m/%Y')

        d_inserida = d_atual.strftime('%d/%m/%Y')

        dias_diferente = abs(numero_inserido.days)

        mes_diferente = dias_diferente // 30

        ano_diferente = dias_diferente // 360

        return jsonify({"status": status,
                        "d_atual": d_atual,
                        "d_inserido": d_inserida,
                        "dias_diferente": dias_diferente,
                        "mes_diferente": mes_diferente,
                        "ano_diferente": ano_diferente,
        })

    except ValueError:
        return jsonify({"Data incorreto"})

if __name__ == '__main__':
    app.run(debug=True)
