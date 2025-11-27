import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Stáhne HTML obsah stránky a vrátí seznam všech odkazů (href).
    """
    try:
        response = requests.get(url)
        response.raise_for_status()      # vyhodí výjimku při chybě
        html = response.text

        # regulární výraz pro nalezení href="něco"
        hrefs = re.findall(r'href=["\'](.*?)["\']', html)

        return hrefs

    except Exception as e:
        print("Chyba při stahování:", e)
        return []


if __name__ == "__main__":
    url = "https://www.jcu.cz"
    links = download_url_and_get_all_hrefs(url)

    for link in links:
        print(link)
