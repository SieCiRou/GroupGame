from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/group', methods=['POST'])
def group():
    names = request.form['names'].split('\n')
    names = [name.strip() for name in names if name.strip()]
    num_groups = int(request.form['num_groups'])
    
    # 隨機打亂名字
    random.shuffle(names)
    
    # 計算每組人數
    group_size = len(names) // num_groups
    extra = len(names) % num_groups
    
    # 分組
    groups = []
    print(groups)
    start = 0
    for i in range(num_groups):
        size = group_size + (1 if i < extra else 0)
        groups.append(names[start:start + size])
        start += size
    
    return render_template('result.html', groups=groups)

if __name__ == '__main__':
    app.run(debug=True)