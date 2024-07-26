from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/v1/ip', methods=['GET'])
def get_public_ip():
    url = 'https://v4.ident.me' # Other Website
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    
    try:
        user_agent = request.headers.get('User-Agent')
        
        response = requests.get(url, headers=headers)
        ip_address = response.text.strip()
        
        # JSON Response LOL
        return jsonify({
            'IP': ip_address
	          'User-Agent': user_agent
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
