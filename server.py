from flask import Flask, render_template, request, jsonify
import pandas as pd


app = Flask(__name__)

# Mock API call; replace with actual data source
def fetch_building_permits(date_range):
    # Replace this with your API call or database query
    # For demonstration purposes, it's returning static data
    data = get_data_from_api_or_db(date_range)
    df = pd.DataFrame(data)
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    
    permits_df = fetch_building_permits(start_date, end_date)

    # Convert DataFrame to list of dictionaries for JSON serialization
    markers_data = permits_df.to_dict(orient='records')

    return jsonify(markers_data)

if __name__ == '__main__':
    app.run(debug=True)



