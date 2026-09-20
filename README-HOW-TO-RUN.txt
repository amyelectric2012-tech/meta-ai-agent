
HOW TO RUN PLAYWRIGHT SCRIPT - MAIN ELECTRIC SERVICE SEARCH

OPTION 1: RUN LOCALLY ON YOUR WINDOWS/MAC (RECOMMENDED)

1. Install Python:
   - Download from python.org (check "Add to PATH")

2. Open Terminal / Command Prompt:
   - Windows: Press Win+R, type cmd, Enter
   - Mac: Open Terminal

3. Install needed tools:
   pip install playwright pandas openpyxl
   playwright install chromium

4. Download files to SAME folder:
   - ladbs_playwright_scrape_FULL.py (this script)
   - MASTER-Electric-Service-DB-V2-MAIN-SERVICE-ALL.xlsx (your DB)

5. Run:
   python ladbs_playwright_scrape_FULL.py

   A Chrome window will open and automatically search LADBS for each address.
   It will pause a bit for each - don't close it.

6. Results:
   - ladbs_main_service_results.csv will be created
   - MASTER-DB-V3-UPDATED-WITH-LADBS.xlsx will have new columns

TROUBLESHOOTING:
- If LADBS blocks you: run with headless=False (already set) and solve captcha manually once
- If selector not found: LADBS changed layout - open https://www.ladbsservices2.lacity.org/OnlineServices/?service=plr manually,
  right-click address box -> Inspect -> copy its id/name and update script line: page.fill("YOUR_SELECTOR", short_addr)

OPTION 2: RUN FOR BUILDZOOM (EASIER, NO BOT BLOCK)

BuildZoom is easier to scrape - replace URL with:
https://www.buildzoom.com/address/{address-slug}

Example:
pip install playwright
playwright install
python -m playwright codegen https://www.buildzoom.com  # to record selectors

OPTION 3: IF YOU WANT ME TO RUN IT HERE
I cannot run full Chrome in this sandbox (no browser binary). 
But you can upload the ladbs_main_service_results.csv back here and I will merge it into your MASTER DB V4 covering all.

FOR EV CHARGER / LADWP ESR:
For LADWP properties, after you get amperage, also need:
https://www.ladwp.com/ladwp/faces/wcnav_externalId/r-fa-esr-engineering?_adf.ctrl-state=...
Request Service Confirmation Letter.

