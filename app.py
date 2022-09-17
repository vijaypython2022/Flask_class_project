from p1 import create_app, db
import os

config_name = os.getenv('Flask_config', 'development')
app = create_app(config_name)
with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True,port=6000)
