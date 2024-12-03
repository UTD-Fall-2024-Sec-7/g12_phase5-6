import unittest
from datastorage import datastorage
from transactionClass import transactionClass
from newsHandler import newsHandler


class TestSystem(unittest.TestCase):

    def setUp(self):
        # Initialize services for testing
        self.storage = datastorage()
        self.transaction_service = transactionClass()
        self.api_key = "ct1nmb9r01qoprggpfk0ct1nmb9r01qoprggpfkg"
        self.news_service = newsHandler(self.api_key)

    def test_register_user(self):
        # Test user registration
        result = self.storage.register_user("test_user", "password123")
        self.assertTrue(result, "User registration failed when it should succeed.")

        # Test duplicate registration
        result = self.storage.register_user("test_user", "password123")
        self.assertFalse(result, "Duplicate user registration should fail.")

    def test_login_validation(self):
        # Register and validate login
        self.storage.register_user("test_user", "password123")
        result = self.storage.validate_login("test_user", "password123")
        self.assertTrue(result, "Valid login credentials failed validation.")

        # Test invalid login
        result = self.storage.validate_login("test_user", "wrongpassword")
        self.assertFalse(result, "Invalid password should not validate.")

    def test_follow_congressman(self):
        # Register and follow a congressman
        self.storage.register_user("test_user", "password123")
        result = self.storage.follow_congressman("test_user", "Josh Gottheimer")
        self.assertTrue(result, "Failed to follow a valid congressman.")

        # Check followed congressmen
        followed = self.storage.get_followed_congressmen("test_user")
        self.assertIn("Josh Gottheimer", followed, "Followed congressman not found in the list.")

    def test_list_all_congressmen(self):
        # Check congressmen listing
        congressmen = self.storage.list_all_congressmen()
        self.assertIsInstance(congressmen, list, "Congressmen list should be a list.")
        self.assertGreater(len(congressmen), 0, "Congressmen list should not be empty.")

    def test_get_recent_trades(self):
        # Note: Actual API calls would require mocking
        try:
            self.transaction_service.get_recent_trades("Josh Gottheimer")
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "Fetching recent trades failed unexpectedly.")

    def test_news_fetching(self):
        # Fetch and display news for a valid category
        news = self.news_service.getNews("general")
        self.assertIsNotNone(news, "News fetching should not return None for a valid category.")

    def test_news_show(self):
        # Simulate news showing
        news = [{"id": 1, "headline": "Breaking News", "source": "Example", "url": "http://example.com"}]
        try:
            self.news_service.show(news)
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "Showing news failed unexpectedly.")


if __name__ == "__main__":
    unittest.main()
