#!/usr/bin/env python3
"""
Simple HTTP Server for previewing the GAVG website locally
Run this script and visit http://localhost:8000 to view the website
"""

import http.server
import socketserver
import webbrowser
import os
import sys

# Change to the directory containing the HTML files
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def start_server():
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🌐 GAVG Website Preview Server")
            print(f"📁 Serving files from: {script_dir}")
            print(f"🔗 Local URL: http://localhost:{PORT}")
            print(f"🔗 Network URL: http://127.0.0.1:{PORT}")
            print("\n🚀 Opening browser automatically...")
            print("💡 Press Ctrl+C to stop the server\n")
            
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}')
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Try a different port or close other servers.")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()