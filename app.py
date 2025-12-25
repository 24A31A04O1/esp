
from flask import Flask, render_template, redirect, url_for
from supabase import create_client

app = Flask(__name__)

SUPABASE_URL = "https://ofyhamnfkpgtnujmqgiv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9meWhhbW5ma3BndG51am1xZ2l2Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NTM4MzIyMiwiZXhwIjoyMDgwOTU5MjIyfQ.YLtXejHgDlLr1es0suj06eP1-WUp7kBriaLgSVf37Ds"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)



@app.route("/")
def index():
    data = supabase.table("devices").select("*").execute()
    return render_template("index.html", devices=data.data)

@app.route("/on")
def on():
    supabase.table("devices").update(
        {"status": True}
    ).eq("device_name", "light1").execute()
    return redirect(url_for("index"))

@app.route("/off")
def off():
    supabase.table("devices").update(
        {"status": False}
    ).eq("device_name", "light1").execute()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
