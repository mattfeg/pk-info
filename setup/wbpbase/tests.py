from django.test import TestCase

# Create your tests here.
class TestWBPBase(TestCase):
    def test_index_page_uses_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wbpbase/index.html', 'Not using index.html')
    
    def test_grid_page_uses_template(self):
        response = self.client.get('/grid/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wbpbase/grid.html', 'Not using grid.html')
    
    def test_contact_page_uses_template(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wbpbase/contact.html', 'Not using contact.html')
    
    def test_register_page_uses_template(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wbpbase/register.html', 'Not using register.html')

if __name__ == '__main__':
    TestWBPBase.main()