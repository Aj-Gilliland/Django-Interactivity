
from django.test import SimpleTestCase

class TestWarmUp(SimpleTestCase):
    def test_Chocolate(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&positive_number=2")
        self.assertContains(response, "ChoCho")

    def test_Chocolate2(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&positive_number=3")
        self.assertContains(response, "ChoChoCho")

    def test_abc(self):
        response = self.client.get("/warmup-2/font-times/?word=Abc&positive_number=3")
        self.assertContains(response, "AbcAbcAbc")

class TestLogic(SimpleTestCase):
    def test_1_2_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?num1=1&num2=2&num3=3")
        self.assertContains(response, 6)

    def test_2_13_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?num1=2&num2=13&num3=1")
        self.assertContains(response, 3)

    def test_3_2_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?num1=2&num2=1&num3=14")
        self.assertContains(response, 3)
    
class TestString(SimpleTestCase):
    def test_abcxyz(self):
        response = self.client.get("/string-2/xyz-there/?stringThing=abcxyz")
        self.assertContains(response, True)

    def test_abc_xyz(self):
        response = self.client.get("/string-2/xyz-there/?stringThing=abc.xyz")
        self.assertContains(response, False)

    def test_xyz(self):
        response = self.client.get("/string-2/xyz-there/?stringThing=xyz.abc")
        self.assertContains(response, True)

class TestLists(SimpleTestCase):
    def test_1_2_3_4_100(self):
        response = self.client.get("/list-2/centered-average/?num1=1&num2=2&num3=3&num4=4&num5=100")
        self.assertContains(response, 3)

    def test_5_3_4_6_2(self):
        response = self.client.get("/list-2/centered-average/?num1=5&num2=3&num3=4&num4=6&num5=2")
        self.assertContains(response, 4)

    def test_4_4_4_4_5(self):
        response = self.client.get("/list-2/centered-average/?num1=4&num2=4&num3=4&num4=4&num5=5")
        self.assertContains(response, 4)






