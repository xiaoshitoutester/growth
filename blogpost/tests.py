from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from blogpost.views import view_post,index
from blogpost.models import Blogpost
import datetime


# Create your tests here.
# Test
class HomePageTest(TestCase):

    def test_index_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func,index)

    def test_home_page_return_current_content(self):
        response = index(HttpRequest())
        self.assertIn(b'<title>Welcome to my blog</title>',
                      response.content)

    def test_blogpost_blog_return_current_content(self):
        Blogpost.objects.create(title='xiaoxiao',author='admin',
                                slug='test_blog_url',body='xiaoxiao is very beautiful.',
                                posted=datetime.datetime.now)
        response = self.client.get('/blog/test_blog_url.html')
        self.assertIn(b'xiaoxiao',response.content)
        self.assertIn(b'xiaoxiao is very beautiful.',response.content)
