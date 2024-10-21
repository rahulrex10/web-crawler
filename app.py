
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from flask import Flask, request, jsonify

app = Flask(__name__)

def crawl_url(root_url, depth):
    crawled_urls = []
    urls_to_crawl = [(root_url, 0)]
    visited = set()

    while urls_to_crawl:
        url, current_depth = urls_to_crawl.pop(0)
        if url not in visited and current_depth <= depth:
            try:
                response = requests.get(url)
                visited.add(url)
                if response.status_code == 200:
                    crawled_urls.append({"url": url, "depth": current_depth})
                    if current_depth < depth:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        for link in soup.find_all('a', href=True):
                            absolute_url = urljoin(url, link['href'])
                            if absolute_url not in visited:
                                urls_to_crawl.append((absolute_url, current_depth + 1))
            except requests.RequestException:
                pass

    return crawled_urls

@app.route('/api/crawl', methods=['POST'])
def crawl():
    data = request.get_json()
    root_url = data.get("root_url")
    depth = data.get("depth")

    if not root_url or depth is None:
        return jsonify({"status": "error", "message": "Invalid parameters"}), 400

    crawled_urls = crawl_url(root_url, depth)
    return jsonify({
        "status": "success",
        "root_url": root_url,
        "crawled_urls": crawled_urls,
        "total_crawled": len(crawled_urls)
    })

if __name__ == '__main__':
    app.run(debug=True)
