from flask import Flask, render_template, redirect, url_for
from form import TextoVoz
import os
from services.text_service import text_to_voice

app = Flask(__name__)
app.config['SECRET_KEY'] = "Hola_chao_secret_key"

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def inicio():
    form = TextoVoz()
    if form.validate_on_submit():
        text_to_voice(
            form.text.data
        )
        return redirect(url_for('inicio'))
    return render_template("index.html", form=form)

if __name__ == '__main__':

    app.run(debug=True)
