from flask import Flask, request, jsonify

app = Flask(__name__)

# Route für die Startseite
@app.route('/')
def home():
    return 'Willkommen auf meiner Seite!'

# Deine bestehenden Routen (z.B. für PC-Bauten)
components = {
    "CPU": {"budget": "AMD Ryzen 5 5600X", "mid": "AMD Ryzen 7 5800X3D", "high": "Intel Core i7-13700KF"},
    "GPU": {"budget": "NVIDIA RTX 3060 Ti", "mid": "NVIDIA RTX 4070", "high": "AMD RX 7900 XTX"},
    "RAM": "16 GB DDR4-3600 MHz",
    "SSD": "1 TB NVMe SSD",
    "PSU": "750W 80+ Gold",
    "Case": "Cooler Master NR600"
}

fps_estimates = {"Fortnite": {"budget": 180, "mid": 280, "high": 360}}

@app.route('/build', methods=['POST'])
def recommend_build():
    data = request.json
    budget = data.get('budget', 'mid').lower()
    game = data.get('game', 'Fortnite')
    fps_target = fps_estimates.get(game, {}).get(budget, "unbekannt")

    build = {
        "CPU": components["CPU"].get(budget, "Unbekannt"),
        "GPU": components["GPU"].get(budget, "Unbekannt"),
        "RAM": components["RAM"],
        "SSD": components["SSD"],
        "PSU": components["PSU"],
        "Case": components["Case"],
        "FPS (geschätzt)": f"{fps_target} FPS in {game}"
    }

    return jsonify(build)

if __name__ == '__main__':
    app.run(debug=True)

