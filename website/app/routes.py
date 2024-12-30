from flask import Flask, send_from_directory
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    # Serve the HTML file directly
    return send_from_directory('website', 'index.html')

@app.route('/matches')
def matches():
    return send_from_directory('website', 'matches.html')

@app.route('/players')
def players():
    return send_from_directory('website', 'players.html')

@app.route('/teams')
def teams():
    return send_from_directory('website', 'teams.html')

@app.route('/login')
def login():
    return send_from_directory('website', 'login.html')

@app.route('/signup')
def signup():
    return send_from_directory('website', 'signup.html')

@app.route('/news')
def news():
    return send_from_directory('website', 'news.html')

API_KEY = "YOUR_API_KEY"

@app.route('/compare-players', methods=['GET'])
def compare_players():
    # Get parameters from the frontend
    batter = request.args.get('batter')
    bowler = request.args.get('bowler')
    year = request.args.get('year')

    # API URLs for batter and bowler stats
    batter_url = f"https://cricapi.com/api/playerStats?apikey={API_KEY}&pid={get_player_id(batter)}"
    bowler_url = f"https://cricapi.com/api/playerStats?apikey={API_KEY}&pid={get_player_id(bowler)}"

    # Fetch batter and bowler data
    batter_response = requests.get(batter_url).json()
    bowler_response = requests.get(bowler_url).json()

    # Format response data
    data = {
        "batter": {
            "name": batter,
            "matches": batter_response.get("data", {}).get("matches", "N/A"),
            "runs": batter_response.get("data", {}).get("batting", {}).get("runs", "N/A"),
        },
        "bowler": {
            "name": bowler,
            "matches": bowler_response.get("data", {}).get("matches", "N/A"),
            "wickets": bowler_response.get("data", {}).get("bowling", {}).get("wickets", "N/A"),
        }
    }
    return jsonify(data)

def get_player_id(player_name):
    """Map player names to IDs. Replace this with a dynamic search API call if available."""
    player_ids = {
        "Virat Kohli": "253802",
        "Joe Root": "303669",
        "Steve Smith": "267192",
        "Jasprit Bumrah": "625383",
        "Shaheen Afridi": "1011295",
        "Pat Cummins": "489889"
    }
    return player_ids.get(player_name, None)
