#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    # Define your data here as a dictionary
    data = {
        "message": "Hello, World!"
    }
    # Use jsonify to return the data in JSON format
    return jsonify(data)
