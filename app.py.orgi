from flask import Flask, render_template, request
import json

app = Flask(__name__)

# تحميل ملف JSON وتنظيمه حسب الصفحة
with open("data_fixed.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

data = {}
for item in raw_data:
    page = item.get("location", {}).get("الصفحة")
    if page:
        page_str = f"{int(page):03d}"  # تحويل الرقم إلى 3 خانات مثل "001"
        data.setdefault(page_str, []).append(item)

@app.route("/")
def root():
    return render_template("index.html", page="001", direction="rtl", items=[], image_url="https://surahquran.com/img/pages-quran/page001.png")

@app.route("/page/<page_id>")
def read_page(page_id):
    page_str = f"{int(page_id):03d}"
    page_data = data.get(page_str, [])
    direction = "rtl" if int(page_id) % 2 != 0 else "ltr"
    image_url = f"https://surahquran.com/img/pages-quran/page{page_str}.png"
    return render_template("index.html", 
                         page=page_str,
                         items=page_data,
                         direction=direction,
                         image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)

