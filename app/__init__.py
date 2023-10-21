from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

# Vistas
from app import home, auth, post

db = SQLAlchemy()
ckeditor = CKEditor()

def create_app():
  app = Flask(__name__)
  
  # Cargando configuracion
  app.config.from_object('config.Config')
  db.init_app(app)
  ckeditor.init_app(app)
  
  # Configuracion del idioma
  import locale
  locale.setlocale(locale.LC_ALL, 'es_ES')
  
  # Registrar vistas
  app.register_blueprint(home.bp)
  app.register_blueprint(auth.bp)
  app.register_blueprint(post.bp)
  
  # Models
  from .models import User, Post
  
  with app.app_context():
    db.create_all()

  return app