from flask import Flask, request, Response
import subprocess

app = Flask(__name__)

def run_script():
    process = subprocess.Popen(
        ["bash", "/home/ubuntu/aashuWorkspace/deployizzygo/deploy.sh"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )
    for line in iter(process.stdout.readline, ""):
        yield line
    process.stdout.close()
    process.wait()

@app.route('/deploy', methods=['POST'])
def deploy():
    return Response(run_script(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9717, threaded=True)
