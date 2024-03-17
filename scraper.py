from facebook_scraper import get_posts, _scraper
import json


def scrape_data(page_name):
    try:
        with open('mbasic.facebook.com_cookies.json', 'r') as file:
            _scraper.mbasic_headers = json.load(file)
        posts = []
        for post in get_posts(page_name, base_url="https://mbasic.facebook.com", start_url=f"https://mbasic.facebook.com/{page_name}?v=timeline", pages=5):
            posts.append({
                "text": post["text"],
                "likes": post["likes"],
                "comments": post["comments"],
                "shares": post["shares"],
                "time": post["time"].isoformat(),
            })
        return posts
    except Exception as e:
        print(e)
        pass
