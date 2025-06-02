from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# تحميل البيانات من ملف JSON
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), 'data_fixed.json')
    with open(file_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    
    data = {}
    for item in raw_data:
        page = item.get("location", {}).get("الصفحة")
        if page:
            page_str = f"{int(page):03d}"
            data.setdefault(page_str, []).append(item)
    return data

data = load_data()

@app.route("/")
def root():
    return render_template("index.html", 
                         page="001",
                         direction="rtl",
                         items=[],
                         image_url="https://surahquran.com/img/pages-quran/page001.png")

@app.route("/page/<page_id>")
def read_page(page_id):
    try:
        page_str = f"{int(page_id):03d}"
        page_data = data.get(page_str, [])
        direction = "rtl" if int(page_id) % 2 != 0 else "ltr"
        image_url = f"https://surahquran.com/img/pages-quran/page{page_str}.png"
        return render_template("index.html",
                             page=page_str,
                             items=page_data,
                             direction=direction,
                             image_url=image_url)
    except ValueError:
        return "رقم الصفحة غير صحيح", 400

if __name__ == "__main__":
    app.run()

