from flask import render_template
from my_app import db
from my_app.models import Zametka
from . import zametki_bp

@zametki_bp.route('/zametki')
def all_zametki():
    zametki = Zametka.query.all()
    if not zametki:
        return render_template('zametki_bp/zametki.html', title='Ваши заметки', message='У вас нет заметок.')
    return render_template('zametki_bp/zametki.html', title = 'Ваши заметки', zametki = zametki)
