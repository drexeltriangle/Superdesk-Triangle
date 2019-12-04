# Author: The Triangle Development Team

from superdesk.tests import TestCase
from triangle.publish.formatters.triangle_apple_news_formatter import TriangleAppleNewsFormatter

class TriangleAppleNewsFormatterTests(TestCase):
    def setUp(self):
        self.formatter = TriangleAppleNewsFormatter()
        self.maxDiff = None
    
    def test_type_is_apple_news(self):
        self.assertEqual("Triangle Apple News", self.formatter.format_type)