# Author: The Triangle Development Team

from superdesk.tests import TestCase
from triangle.publish.formatters.triangle_apple_news_formatter import TriangleAppleNewsFormatter

class TriangleAppleNewsFormatterTest(TestCase):
    def setUp(self):
        self.formatter = TriangleAppleNewsFormatter()
        self.maxDiff = None

    
