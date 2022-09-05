from p1 import create_app
import os

config_name=os.getenv('Flask_config','development')
app=create_app(config_name)

if __name__=='__main__':
    app.run(debug=True,port=3000)
