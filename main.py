from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://publicaccess.durham.gov.uk/online-applications/search.do?action=simple&searchType=Application")
        page.wait_for_load_state()

        page.fill("input[name='searchCriteria.simpleSearchString']", "big farm")
        page.click("input[value='Search']")
        page.wait_for_load_state()

        results = page.query_selector_all(".searchresult")
        proposals = [result.query_selector("a").inner_text() for result in results]

        next = page.query_selector("a.next")

        while next:
            page.wait_for_load_state()
            next.click()
            page.wait_for_load_state()
            next = page.query_selector("a.next")
            results = page.query_selector_all(".searchresult")
            proposals += [result.query_selector("a").inner_text() for result in results]

        file = open("proposals.txt", "w")
        file.write("\n".join(proposals) + "\n")
        file.close()

        while True:
            pass


if __name__ == "__main__":
    run()

