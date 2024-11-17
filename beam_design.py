
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>تصميم الكمرات</h1>
    <form action="/calculate" method="post">
        <label for="span">طول الكمرة (م):</label>
        <input type="number" step="0.01" id="span" name="span" required><br><br>
        <label for="load">الحمل المنتظم (ك.ن/م):</label>
        <input type="number" step="0.01" id="load" name="load" required><br><br>
        <label for="width">عرض القطاع (م):</label>
        <input type="number" step="0.01" id="width" name="width" required><br><br>
        <label for="depth">عمق القطاع (م):</label>
        <input type="number" step="0.01" id="depth" name="depth" required><br><br>
        <button type="submit">احسب</button>
    </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    span = float(request.form['span'])
    load = float(request.form['load'])
    width = float(request.form['width'])
    depth = float(request.form['depth'])
    
    # حساب العزم الأقصى
    moment = (load * span**2) / 8  # عزم الانحناء
    steel_area = (moment * 10**6) / (0.87 * 360 * (0.9 * depth))  # مساحة الحديد
    
    result = f'''
    <h1>نتائج التصميم</h1>
    <p>عزم الانحناء الأقصى: {moment:.2f} ك.ن.م</p>
    <p>مساحة الحديد المطلوبة: {steel_area:.2f} مم²</p>
    <a href="/">العودة</a>
    '''
    return result

if __name__ == '__main__':
    app.run(debug=True)
