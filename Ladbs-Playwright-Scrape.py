
# PLAYWRIGHT SCRIPT TO SCRAPE LADBS FOR MAIN SERVICE
# pip install playwright
# playwright install chromium
# python ladbs_scrape.py

from playwright.sync_api import sync_playwright
import csv, time, re

ADDRESSES = [
    "1065 S Holt Avenue, Los Angeles, CA 90035",
    "2104 Hauser Blvd., Los Angeles, CA 90016",
    "4287 Verdugo Rd., Los Angeles, CA 90065",
    # ... add all 63 from your MASTER DB
]

def extract_amps(text):
    m = re.findall(r'(\d{3,4})\s*A', text, re.I)
    return max([int(x) for x in m]) if m else None

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headful to bypass bot check
    page = browser.new_page()
    
    # LADBS PLR
    page.goto("https://www.ladbsservices2.lacity.org/OnlineServices/?service=plr")
    time.sleep(3)
    
    results = []
    for addr in ADDRESSES:
        try:
            # Clear and type address
            page.fill("input[name='address']", "")  # selector may vary - inspect
            page.fill("input[name='address']", addr.split(',')[0])
            page.click("button:has-text('Search')")
            page.wait_for_load_state()
            time.sleep(2)
            
            # Grab first permit rows
            rows = page.locator("table tr").all()
            for r in rows[:10]:
                txt = r.inner_text()
                if "Electrical" in txt or "400" in txt or "600" in txt or "Service" in txt:
                    amps = extract_amps(txt)
                    results.append([addr, txt, amps])
                    print(addr, txt[:200], amps)
        except Exception as e:
            print(f"Error {addr}: {e}")
            results.append([addr, f"ERROR {e}", ""])
    
    browser.close()

# Save
with open("ladbs_main_service_results.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["Address","Work Description","Parsed Amps"])
    w.writerows(results)

print("Done - check ladbs_main_service_results.csv")
