from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id' : 1,
        'Contact' : '9987644456',
        'Name' : 'Rakesh',
        'done' : False
    },
    {
        'id': 2,
        'Contact': '9939434021',
        'Name' : 'Ramesh', 
        'done': False
    }
]
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'title': request.json['Name'],
        'description': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)