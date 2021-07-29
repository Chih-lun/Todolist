from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

class Task():
    def __init__(self,id,content):
        self.id = id
        self.content = content

todo = []

@app.route('/',methods=['GET','POST'])
def home():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    if request.method == 'POST':
        id = len(todo)
        stuff = request.form['stuff']
        if stuff == '':
            return render_template('index.html',todo=todo,date=date)
        todo.append(Task(id=id,content=stuff))
        return render_template('index.html',todo=todo,date=date)
    return render_template('index.html',todo=todo,date=date)

@app.route('/delete',methods=['GET'])
def delete():
    for i in todo:
        if request.args.get('item') == str(i):
            todo.remove(i)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)