
import json
import pandas as pd

# Paste your JSON string here
input_str = '''[{"paid": [], "organic": [{"pos": 1, "url": "https://www.tripadvisor.com/Restaurants-g294226-Bali.html", "desc": "1. Akasa Jumeirah Bali. 4.9. (366 reviews) \\u00b7 2. Ambar Ubud Bar. 5.0. (827 reviews) \\u00b7 3. Koral Restaurant. 4.9. (1,513 reviews) \\u00b7 4. MoonLite Kitchen and Bar. 4.7.", "title": "THE 10 BEST Restaurants in Bali (Updated July 2025)", "url_shown": "https://www.tripadvisor.com\\u203a Asia \\u203a Indonesia \\u203a Bali", "pos_overall": 1, "favicon_text": "Tripadvisor"}, {"pos": 2, "url": "https://onbali.com/all-bali/best-restaurants-in-bali/", "desc": "6 days ago \\u2014 Craving the best eats in Bali? From luxury fine dining to local warungs loved by foodies, we've handpicked 41 must-visit restaurants.", "title": "Bali's Best Restaurants - Fine Dining & Local Gems (2025)", "url_shown": "https://onbali.com\\u203a All Bali", "pos_overall": 3, "favicon_text": "OnBali"}, {"pos": 3, "url": "https://www.balihoneymoonguide.com/explore/best-fine-dining-in-bali/", "desc": "May 14, 2025 \\u2014 Bali's best restaurants can be found where the high(er) end tourists are. Typical hotspots with the best restaurants are Ubud, Seminyak and Uluwatu.", "title": "The 14 Best Fine Dining Restaurants in Bali (with 2025 ...", "url_shown": "https://www.balihoneymoonguide.com\\u203a explore \\u203a best-f...", "pos_overall": 4, "favicon_text": "Bali Honeymoon Guide"}, {"pos": 4, "url": "https://www.theworlds50best.com/discovery/sitemap/indonesia/bali", "desc": "The best restaurants and bars in Bali ; 40 Thieves. Good-time expat bar ; Alila Villas Uluwatu. Enchanting minimalist marvel ; Amankila. Blissful Balinese bolthole.", "title": "The best Restaurants and Bars in Bali, Indonesia 2025", "url_shown": "https://www.theworlds50best.com\\u203a discovery \\u203a sitemap", "pos_overall": 5, "favicon_text": "The World's 50 Best Restaurants"}, {"pos": 5, "url": "https://www.reddit.com/r/finedining/comments/1aj1mtc/bali_recommendations/", "desc": "Cuca was our absolute favorite for high end dining. Honestly one of the best meals Ive ever had. Highly recommend Yuki in Uluwatu for a mid\\u00a0...", "title": "Bali Recommendations? : r/finedining", "url_shown": "10+ comments  \\u00b7  1 year ago", "pos_overall": 6, "favicon_text": "Reddit\\u00a0\\u00b7\\u00a0r/finedining"}], "local_pack": {"items": [{"cid": "6668208737899155760", "pos": 1, "title": "Mamasan Bali", "rating": 4.6, "address": "Asian", "rating_count": 0}, {"cid": "9850476580074208143", "pos": 2, "title": "This Is Bali - Balinese Food & Desserts", "rating": 4.9, "address": "Balinese restaurant", "rating_count": 0}, {"cid": "14357941300243390366", "pos": 3, "title": "Uma Garden Seminyak", "rating": 4.7, "address": "Steak", "rating_count": 0}], "pos_overall": 2}, "related_searches": [{"pos_overall": 7, "related_searches": ["Top 10 visit restaurants in bali indonesia", "Best visit restaurants in bali indonesia", "Best restaurants Bali Seminyak", "Top 10 best restaurant in Bali", "Restaurants in Bali Seminyak", "Best restaurants in Bali", "Coolest restaurants in Bali", "Fine dining Bali"], "related_searches_urls": ["https://www.google.com/search?num=5&sca_esv=91e9498f46de628c&gl=us&hl=en&q=Top+10+visit+restaurants+in+bali+indonesia&sa=X&ved=2ahUKEwiQqqGS7sOOAxX8xjgGHTZfJTUQ1QJ6BAgyEAE", "https://www.google.com/search?num=5&sca_esv=91e9498f46de628c&gl=us&hl=en&q=Best+visit+restaurants+in+bali+indonesia&sa=X&ved=2ahUKEwiQqqGS7sOOAxX8xjgGHTZfJTUQ1QJ6BAgxEAE", "https://www.google.com/search?num=5&sca_esv=91e9498f46de628c&gl=us&hl=en&q=Best+restaurants+Bali+Seminyak&sa=X&ved=2ahUKEwiQqqGS7sOOAxX8xjgGHTZfJTUQ1QJ6BAg6EAE", "https://www.google.com/search?num=5&sca_esv=91e9498f46de628c&gl=us&hl=en&q=Top+10+best+restaurant+in+Bali&sa=X&ved=2ahUKEwiQqqGS7sOOAxX8xjgGHTZfJTUQ1QJ6BAg5EAE", "https://www.google.com/search?num=5&sca_esv=91e9498f46de628c&gl=us&hl=en&q=Restaurants+in+Bali+Seminyak&sa=X&ved=2ahUKEwiQqqGS7sOOAxX8xjgGHTZfJTUQ1QJ6BAgzEAE", "https://www.google.com/search?num=5&sca_esv=91e9498f46de628c&gl=us&hl=en&q=Best+restaurants+in+Bali&sa=X&ved=2ahUKEwiQqqGS7sOOAxX8xjgGHTZfJTUQ1QJ6BAg1EAE", "https://www.google.com/search?num=5&sca_esv=91e9498f46de628c&gl=us&hl=en&q=Coolest+restaurants+in+Bali&sa=X&ved=2ahUKEwiQqqGS7sOOAxX8xjgGHTZfJTUQ1QJ6BAg7EAE", "https://www.google.com/search?num=5&sca_esv=91e9498f46de628c&gl=us&hl=en&q=Fine+dining+Bali&sa=X&ved=2ahUKEwiQqqGS7sOOAxX8xjgGHTZfJTUQ1QJ6BAg9EAE"]}], "search_information": {"query": "Visit restaurants in Bali Indonesia.", "showing_results_for": "Visit restaurants in Bali Indonesia.", "total_results_count": 9130000, "time_taken_displayed": null, "no_results_for_original_query_found": false}, "total_results_count": 9130000}]'''

# Parse the string to a Python object
data = json.loads(input_str)

# Function to flatten nested dicts/lists with full key path
def flatten(obj, parent_key=''):
    items = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            items.extend(flatten(v, new_key))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_key = f"{parent_key}[{i}]" if parent_key else f"[{i}]"
            items.extend(flatten(v, new_key))
    else:
        items.append((parent_key, obj))
    return items

flat_items = flatten(data)
df = pd.DataFrame(flat_items, columns=['Key', 'Value'])
print(df.to_string(index=False))

# Save to CSV and Excel
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)

# Save as key : value in a text file with a single header
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Key : Value\n')
    for k, v in flat_items:
        f.write(f"{k} : {v}\n")
