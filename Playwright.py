import pytest
from playwright.sync_api import Page

@pytest.mark.parametrize("url", ["https://www.engeto.cz"])
def test_homepage_title(page: Page, url):
    page.goto(url)
    assert "ENGETO" in page.title()

def test_basic_status_ok(page: Page):
    response = page.goto("https://www.engeto.cz")
    assert response.status == 200

def test_kontakt_page_navigation(page: Page):
    page.goto("https://www.engeto.cz")
    # klikneme na odkaz "Kontakt"
    page.get_by_role("link", name="Kontakt").click()
    # ověříme, že titul stránky obsahuje "Kontakt"
    assert "Kontakt" in page.title()