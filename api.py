from flask import Flask, render_template, request, Response

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        num1 = (request.form["num1"])
        num2 = (request.form["num2"])
        num3 = (request.form["num3"])
        if((num1 != "" and num2 != "") and (num3 != "")):
            opc = request.form["opc"]
            if (opc == "soma"):
                return str(int(num1)+int(num2)+int(num3))
            elif (opc == "sub"):
                return str(int(num1)-int(num2)-int(num3))
            elif (opc == "div"):
                return str(int(num1)//int(num2)//int(num3))
            elif (opc == "mult"):
                return str(int(num1)*int(num2)*int(num3))
            elif (opc == "jurosS"):
                return str((int(num1)*int(num2)*int(num3))//100)
        else:
            return "Preencha todos os campos!"

@app.errorhandler(404)
def not_found(error):
    return render_template("erro.html")

app.run(port=3002, debug=True)