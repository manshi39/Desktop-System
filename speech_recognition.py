# # from flask import Flask, request

# # app = Flask(__name__)

# # # Predefined script trigger name
# # SCRIPT_TRIGGER_NAME = "manshi"

# # @app.route('/activate_desktop', methods=['POST'])
# # def activate_desktop():
# #     # Receive name input from the request
# #     name = request.form.get('name')

# #     # Check if the name matches the predefined script trigger
# #     if name.lower() == SCRIPT_TRIGGER_NAME:
# #         # Execute predefined script to activate the desktop
# #         # Replace this with your logic to activate the desktop
# #         activate_desktop_script()
# #         return 'Desktop activated successfully', 200
# #     else:
# #         return 'Name does not match the predefined trigger', 400

# # def activate_desktop_script():
# #     # Implement logic to activate the desktop
# #     print("Desktop activated")

# # if __name__ == '__main__':
# #     app.run(host='172.20.10.2', port=8080)





# from flask import Flask, request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)



# @app.route('/activate_desktop', methods=['POST'])
# def activate_desktop():
#     try:
#         # Assuming the name is sent in the request body
#         name = request.form.get('name')

#         # Replace 'manshi' with the trigger name
#         if name.lower() == 'manshi':
#             # Implement logic to activate the desktop
#             # For example, send a signal to the desktop or execute a command
#             print("Desktop activated successfully")
#             return "Desktop activated successfully", 200
#         else:
#             return "Name does not match the trigger", 400
#     except Exception as e:
#         print("Error activating desktop:", e)
#         return "Error activating desktop", 500

# if __name__ == '__main__':
#     app.run(host='172.0.0.1', port=9102)
   



from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

SCRIPT_TRIGGER_NAME = "manshi"  # Predefined script trigger name

@app.route('/activate_desktop', methods=['POST'])
def activate_desktop():
    try:
        # Receive name input from the request
        name = request.form.get('name')

        # Check if the name matches the predefined script trigger
        if name.lower() == SCRIPT_TRIGGER_NAME:
            # Execute predefined script to activate the desktop
            # Replace this with your logic to activate the desktop
            activate_desktop_script()
            return 'Desktop activated successfully', 200
        else:
            return 'Name does not match the predefined trigger', 400
    except Exception as e:
        print("Error activating desktop:", e)
        return "Error activating desktop", 500

def activate_desktop_script():
    # Implement logic to activate the desktop
    print("Desktop activated")

if __name__ == '__main__':
    app.run(host='172.0.0.1', port=9102)
