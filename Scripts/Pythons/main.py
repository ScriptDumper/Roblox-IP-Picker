from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/v1/ip', methods=['GET'])
def get_public_ip():
    # URL to get the public IP address
    url = 'https://v4.ident.me'  
    # Custom User-Agent to mimic a browser
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    
    try:
        # Get the User-Agent from the incoming request
        user_agent = request.headers.get('User-Agent')
        
        # Make a request to the URL to fetch the public IP
        response = requests.get(url, headers=headers)
        ip_address = response.text.strip()
        
        # Return a JSON response with the IP and User-Agent
        return jsonify({
            'IP': ip_address,
            'User-Agent': user_agent
        })
    
    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app on host 0.0.0.0 and port 8080
    app.run(host='0.0.0.0', port=8080)
