# app/testPosts.py

from django.test import TestCase
from app.models import Post

class PostTestCase (TestCase):
    def testPost (self):
        post = Post(title="My tittle", description= "Blurb", wiki= "Post body")
        self.assertEqual(post.title,"My tittle")
        self.assertEqual(post.description,"Blurb")
        self.assertEqual(post.wiki, "Post body")
