from django.http import HttpResponseRedirect
from django.test import TestCase
from django.utils import timezone

from polls.models import Question

# CA3 - TEST CASE
# TESTING DEFAULT SECURITY ISSUES


class SecurityChecksTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text='Test Post',
            pub_date=timezone.now())

    def test_css_attack(self):
        response = self.client.get(f'/polls/{self.question.id}/')
        self.assertNotContains(response, '<script>', status_code=200)

    def test_sql_injection_attack(self):
        question_id = "' OR 1=1--"
        response = self.client.get(f'/polls/{question_id}/')
        self.assertEqual(response.status_code, 404)

    def test_redirection_attack(self):
        response = self.client.get('/polls/')
        if isinstance(response, HttpResponseRedirect):
            self.assertNotEqual(response.url, 'https://www.google.com')