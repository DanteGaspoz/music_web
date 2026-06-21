from flask import Flask
from routes.search import search_bp
from database.models import db

app = Flask(__name__)

# SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///music_explorer.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
# Crear tablas
with app.app_context():
    db.create_all()

# Registrar rutas
app.register_blueprint(search_bp)

if __name__ == "__main__":
    app.run(debug=True)
