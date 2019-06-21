from flask import *
import pdfkit, os, uuid

app = Flask(__name__)

Download_PATH = '/Users/davidxiong/Desktop/Other'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
Download_FOLDER = os.path.join(APP_ROOT, Download_PATH)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/api/wkhtmltopdf_url", methods=['POST'])
def wkhtmltopdfurl():
    url = request.form['URL']
    try:
        filename = str(uuid.uuid4()) + '.pdf'
        config = pdfkit.configuration(wkhtmltopdf= 'timetable.html')
        pdfkit.from_url(url, filename,configuration=config)
        pdfDownload = open(filename, 'rb').read()
        os.remove(filename)
        return Response(
            pdfDownload,
            mimetype="application/pdf",
            headers={
                "Content-disposition": "attachment; filename=" + filename,
                "Content-type": "application/force-download"
            }
        )
    except ValueError:
        print("Oops! ")
if __name__ == '__main__':
    app.run(debug='True')