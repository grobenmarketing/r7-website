#!/usr/bin/env python3
"""
Simple HTTP server for serving static HTML files
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    """HTTP request handler with cache control disabled"""
    
    def end_headers(self):
        # Disable caching for all requests
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server(port=5000):
    """Run the HTTP server on the specified port"""
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print(f"Server running on http://0.0.0.0:{port}")
    print(f"Serving files from: {os.getcwd()}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
