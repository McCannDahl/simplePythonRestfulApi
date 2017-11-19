#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

incomes = [
 { 'description': 'salary1', 'amount': 5000 },
 { 'description': 'salary2', 'amount': 6000 },
 { 'description': 'salary3', 'amount': 7000 },
 { 'description': 'salary4', 'amount': 8000 }
]


@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204

@app.route('/incomes/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in incomes if task['amount'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
