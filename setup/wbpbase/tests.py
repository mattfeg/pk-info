from django.test import TestCase

# Create your tests here.
def TestWBPBase(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_index_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wbpbase/index.html')
    
    def test_grid_page(self):
        response = self.client.get('grid/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wbpbase/grid.html')
    
    def test_contact_page(self):
        response = self.client.get('contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wbpbase/contact.html')
    
    def test_register_page(self):
        response = self.client.get('register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wbpbase/register.html')

if __name__ == '__main__':
    TestWBPBase.main()