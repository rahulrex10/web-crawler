
# Web Crawler API

This project is a simple **web crawler API** built using Flask. It allows you to crawl a website starting from a given root URL up to a specified depth. The API returns a list of URLs found during the crawling process, with their respective depths.

## Features

- Crawl websites up to a given depth
- Collect all URLs starting from a root URL
- Returns results in a structured JSON format
- Uses Flask for API handling
- Implements a simple web crawling algorithm using BeautifulSoup and Requests

## API Contract

### Endpoint
**POST** `/api/crawl`

### Request Body (JSON)
```json
{
  "root_url": "string",  // The URL to start crawling from
  "depth": "integer"     // The maximum depth to crawl
}
```

### Response Body (JSON)
```json
{
  "status": "success",
  "root_url": "string",
  "crawled_urls": [
    {
      "url": "string",
      "depth": "integer"
    }
  ],
  "total_crawled": "integer"
}
```

### Example Usage

#### Request
```bash
curl -X POST http://localhost:5000/api/crawl -H "Content-Type: application/json" -d '{"root_url": "https://example.com", "depth": 2}'
```

#### Response
```json
{
  "status": "success",
  "root_url": "https://example.com",
  "crawled_urls": [
    {
      "url": "https://example.com/about",
      "depth": 1
    },
    {
      "url": "https://example.com/contact",
      "depth": 1
    }
  ],
  "total_crawled": 2
}
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/web_crawler_api.git
   ```

2. Navigate to the project directory:
   ```bash
   cd web_crawler_api
   ```

3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

1. Navigate to the `app` directory and run the Flask app:
   ```bash
   cd app
   python app.py
   ```

2. The API will run on `http://localhost:5000/`.

## Dependencies

- Flask
- Requests
- BeautifulSoup4

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
