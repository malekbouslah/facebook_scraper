import requests

def test_scrape_page():
    response = requests.post("http://localhost:8000/scrape/facebook")
    assert response.status_code == 200
    assert "page_name" in response.json()
    assert "posts" in response.json()
