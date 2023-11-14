from django.test import SimpleTestCase

# Create your tests here.
class TestHeyYou(SimpleTestCase):
    def test_hey_AJ(self):
        response = self.client.get("/hey/?name=AJ")
        self.assertContains(response, "Hey, AJ!")

    def test_hey_rjay(self):
        response = self.client.get("/hey/?name=rjay")
        self.assertContains(response, "Hey, rjay!")