from flask import Flask, request, jsonify

app = Flask(__name__)

components = {
    \"CPU\": {\"budget\": \"AMD Ryzen 5 5600X\", \"mid\": \"AMD Ryzen 7 5800X3D\", \"high\": \"Intel Core i7-13700KF\"},
    \"GPU\": {\"budget\": \"NVIDIA RTX 3060 Ti\", \"mid\": \"NVIDIA RTX 4070\", \"high\": \"AMD RX 7900 XTX\"},
    \"RAM\": \"16 GB DDR4-3600 MHz\",
    \"SSD\": \"1 TB NVMe SSD\",
    \"PSU\": \"750W 80+ Gold\",
    \"Case\": \"Cooler Master NR600\"
}

fps_estimates = {\"Fortnite\": {\"budget\": 180, \"mid\": 280, \"high\": 360}}

@app.route('/build', methods=['POST'])\ndef recommend_build():\n    data = request.json\n    budget = data.get('budget', 'mid').lower()\n    game = data.get('game', 'Fortnite')\n    fps_target = fps_estimates.get(game, {}).get(budget, \"unbekannt\")\n\n    build = {\n        \"CPU\": components[\"CPU\"].get(budget, \"Unbekannt\"),\n        \"GPU\": components[\"GPU\"].get(budget, \"Unbekannt\"),\n        \"RAM\": components[\"RAM\"],\n        \"SSD\": components[\"SSD\"],\n        \"PSU\": components[\"PSU\"],\n        \"Case\": components[\"Case\"],\n        \"FPS (geschätzt)\": f\"{fps_target} FPS in {game}\"\n    }\n\n    return jsonify(build)\n\nif __name__ == '__main__':\n    app.run(debug=True)
