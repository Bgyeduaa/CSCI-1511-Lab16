"""
Lab16_Bgyeduaa1.py
Author: Belinda Gyeduaa
Purpose: Retrieve and display the top 30 Hacker News submissions sorted by number of comments,
         with exception handling to avoid KeyErrors.
Date: 08/09/25
"""

from operator import itemgetter
import requests

def main():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url)
    print(f"Status code: {r.status_code}")

    submission_ids = r.json()
    submission_dicts = []

    for submission_id in submission_ids[:30]:
        try:
            url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
            r = requests.get(url)
            print(f"id: {submission_id}\tstatus: {r.status_code}")
            response_dict = r.json()

            submission_dict = {
                'title': response_dict.get('title', 'No title available'),
                'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
                'comments': response_dict.get('descendants', 0),  # default 0 if key missing
            }
            submission_dicts.append(submission_dict)

        except requests.exceptions.RequestException as e:
            print(f"Request failed for submission id {submission_id}: {e}")
        except Exception as e:
            print(f"Unexpected error processing submission id {submission_id}: {e}")

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"Discussion link: {submission_dict['hn_link']}")
        print(f"Comments: {submission_dict['comments']}")

if __name__ == "__main__":
    main()
