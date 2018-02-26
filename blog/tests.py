from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Page

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.page = Page.objects.create(
            title='A good title',
            body='A good body',
            author=self.user
        )

    def test_string_representation(self):
        post = Page(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_page_content(self):
        self.assertEqual(f'{self.page.title}', 'A good title')
        self.assertEqual(f'{self.page.body}', 'A good body')
        self.assertEqual(f'{self.page.author}', 'testuser')

    def test_post_list_view(self):
        response = self.client.get(reverse('Blog Pages'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A good body')
        self.assertTemplateUsed(response, 'blog/pages/home.html')

    def test_post_detail_view(self):
        response = self.client.get('/blog/pages/detail/1/')
        no_response = self.client.get('/blog/pages/detail/4000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertContains(response, 'A good body')


