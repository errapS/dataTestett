from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run-dbt', methods=['POST'])
def run_dbt():
    dbt_command = 'dbt run'
    subprocess.run(dbt_command, shell=True)
    return "dbt run initiated", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)