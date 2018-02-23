from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


class PostModelCase(TestCase):

    def setUp(self):
        Post.objects.create(name='just a test', body='just a body', slug='just-a-slug')


    def test_name_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.name}'
        self.assertEqual(expected_object_name, 'just a test')

    def test_body_content(self):
        post = Post.objects.get(id=1)
        expected_object_body = f'{post.body}'
        self.assertEqual(expected_object_body, 'just a body')

    def test_slug_content(self):
        post = Post.objects.get(id=1)
        expected_object_slug = f'{post.slug}'
        self.assertEqual(expected_object_slug, 'just-a-slug')


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(name='another name', body='another body', slug='another-slug')

    def test_view_exists_proper_location(self):
        resp = self.client.get('/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('posts_home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('posts_home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts/home.html')