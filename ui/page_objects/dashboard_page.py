from .base_page import BasePage

class DashboardPage(BasePage):

    header = "//header[@class='AppHeader']"

    def open_site(self):
        self.page.goto('https://github.com/')

    def verify_dashboard_page(self):
        return self.page.url == 'https://github.com/'
