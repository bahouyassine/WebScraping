from EbayScraper import EbayScraper

scraper = EbayScraper()
search_term = "PC with Ryzen 5 7600X"
num_pages = 2
items = scraper._get_items(f"{scraper.base_url}?_nkw={search_term.replace(' ', '+')}&_pgn={num_pages}")
df = scraper.dataFrame
df.to_csv('sample_file.csv', index=False)