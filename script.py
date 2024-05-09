# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/unlock', methods=['POST'])
# def unlock_desktop():
#     # Check if the request contains the correct trigger name
#     if request.form.get('name') == 'manshi':
#         # Code to unlock the desktop
#         # Replace this with the code to unlock your desktop
#         return 'Desktop unlocked successfully'
#     else:
#         return 'Incorrect trigger name'

# if __name__ == '__main__':
#     app.run(host='172.20.10.2', port=5000, debug=True)



# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/unlock', methods=['POST'])
# def unlock_desktop():
#     # Check if the request contains the correct trigger name
#     if request.form.get('name') == 'manshi':
#         # Code to unlock the desktop
#         # Replace this with the code to unlock your desktop
#         return 'Desktop unlocked successfully'
#     else:
#         return 'Incorrect trigger name'

# if __name__ == '__main__':
#     app.run(host='172.20.10.2', port=2501, debug=True)


# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/unlock', methods=['POST'])
# def unlock_desktop():
#     unlock_code = request.form.get('unlock_code')
#     # Check if the unlock code is correct
#     if unlock_code == '2501':
#         # Code to unlock the desktop (replace this with your actual unlock code)
#         # For demonstration purposes, let's print a message
#         print("Desktop unlocked successfully")
#         return 'Desktop unlocked successfully'
#     else:
#         return 'Incorrect unlock code'

# if __name__ == '__main__':
#     app.run(debug=True)
