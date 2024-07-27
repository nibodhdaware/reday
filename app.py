from flask import Flask, jsonify, render_template, request
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/save_journal', methods=['POST'])
def save_journal():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    journal_name = request.cookies.get('journalTitle')
    timestamp = datetime.now().isoformat()
    
    if not title or not content or not journal_name:
        return jsonify({"error": "Missing title, content or Journal name"})
    
    response = supabase.table('journal').insert({
        'j_name': journal_name,
        'j_title': title,
        'j_content': content,
        'j_date': timestamp
    }).execute()

    if response.status_code == 200:
        return jsonify({"message": "Journal entry saved successfully"})
    else:
        return jsonify({"error": "Failed to save journal"})

if __name__ == "__main__":
    app.run(debug=True, port=8080)