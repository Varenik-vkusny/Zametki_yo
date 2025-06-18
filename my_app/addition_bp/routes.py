from flask import render_template, url_for, redirect, flash
from my_app import db
from my_app.models import Zametka
from my_app.forms import AdditionForm
from . import addition_bp

@addition_bp.route('/add_zametka', methods=['GET', 'POST'])
def add_zametka():
    form = AdditionForm()

    if form.validate_on_submit():
        
        new_zametka = Zametka(
            title = form.title.data,
            content = form.content.data
        )

        db.session.add(new_zametka)
        db.session.commit()
        flash('Заметка успешно добавлена!', 'success')

        return redirect(url_for('zametki_bp.all_zametki'))
    
    return render_template('addition_bp/add.html', title='Добавить заметку', form=form)