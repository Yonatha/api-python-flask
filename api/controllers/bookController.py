# -*- coding: utf-8 -*-
from api import app

from flask import jsonify
from api.config.database import session as db
from api.model.patient import Patient

books_db = [
    {'id': 0, 'title': 'O Poder do Hábito'},
    {'id': 1, 'title': 'O segredo da mente milionária'},
    {'id': 2, 'title': 'Passos de gigante'}
]


@app.route('/')
def get():
    patients = db.query(Patient.name).limit(5).all()
    return jsonify({'patients': [dict(patient) for patient in patients]})
