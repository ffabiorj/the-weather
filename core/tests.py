from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """Get / must return status code 200."""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')


class TestForm(TestCase):
    def test_post(self):
        data = dict(name='Rio de Janeiro',)
        self.response = self.client.post('home', data)