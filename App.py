from flask import Flask,render_template,request,jsonify
from File import Sort_Files






app = Flask(__name__,template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Confirm",methods=["post"])
def Confirm():
    data = request.form
    Sort_Files(data.get("SortingFile"),data.get("AudioFile"),data.get("VideoFile"),data.get("ImageFile"),data.get("TextFile"))
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)