from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def dropdown():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('success.html', colours=colours)

@app.route('/result',methods=['GET','POST'])
def result():
    result = request.form.get('colours')
    return str(result)

if __name__ == "__main__":
    app.run()