from flask import Flask

import shlex
import subprocess

app = Flask(__name__)

@app.route("/")
def hello_world():
    BASE_NAME = 'A_1-rwy_v10'
    CFG = f'{BASE_NAME}.cfg'
    DAT = f'{BASE_NAME}.dat'
    cmd = shlex.split(f'java -jar JaamSim2022-02.jar -h {CFG}')
    p = subprocess.Popen(cmd)
    p.wait()

    # Fetch the result
    with open(DAT, "r") as f:
        result = f.read()
    
    return result
