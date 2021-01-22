from flask import Flask

app = Flask(__name__)

# Routing
@app.route('/')
def index():
    name = 'Timmy'
    return f"Hello {name}!"
# Dynamic Routing
@app.route('/<name>')
def print_name(name):
    return f"Hello there {name}"
#  
# Start server with environment variable
# In terminal do the following:
#  
# export FLASK_APP=<name_of_file> i.e. app.py
#  

# Debugging in Flask
#
# Reloader
#   - Watches all file changes
#   - Usefull during development
# 
# Debugger
#   - A web based tool
#   - Interactive stack trace
#   - If running flask with env-var (i.e. FLASK_APP=app.py)
#       - export FLASK_DEBUG=1
#   - If running flask programatically
#   - Pass debug=True in app.run (i.e. app.run(debug=True))
#

#
# Command-Line Options
#
# flask or flask --help: Displays all commands
#


# Start server programatically
if __name__ == '__main__':
    app.run(debug=True)