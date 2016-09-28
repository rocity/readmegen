from flask import Flask, render_template, send_file, request
from datetime import date
from io import BytesIO

app = Flask(__name__)

@app.route('/create', methods=['POST', 'GET'])
def create_form():
    today = date.today()

    if request.method == 'POST':

        file = BytesIO()

        titlestr = '# %s\n' % request.form['title']
        file.write(titlestr.encode('utf-8'))
        file.write('## Items\n'.encode('utf-8'))

        for item in request.form.getlist('item'):
            if len(item):
                itemstr = '- %s\n' % item
                file.write(itemstr.encode('utf-8'))

        file.seek(0)
        return send_file(file,
                            attachment_filename='README.md',
                            as_attachment=True
                            )

    return render_template('create.html', today=today)