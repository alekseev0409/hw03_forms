from django.test import TestCase, Client
from ..models import Group, Post
from django.contrib.auth import get_user_model

User = get_user_model()


class StaticURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Group.objects.create(
            title='Тестовый заголовок',
            description='Тестовый текст',
            slug='slug')
        User.objects.create(
            first_name='Тестовый заголовок',
            last_name='Тестовый текст',
            username='Test',
            email='Тест'
        )
        user = User.objects.get(pk=1)
        Post.objects.create(
            text='текст',
            author=user,
            pk=1
        )

    # def test_homepage(self):
    #     guest_client = Client()
    #     try:
    #         response = guest_client.get('/')
    #         self.assertEqual(response.status_code, 200)
    #     except:
    #         assert False, 'Страница не отображается'

    def test_group(self):
        guest_client = Client()
        try:
            response = guest_client.get('/group/slug/')
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            print(e)
            assert False, 'Страница не отображается'

    def test_profile(self):
        guest_client = Client()
        try:
            response = guest_client.get('/profile/Test/')
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            print(e)
            assert False, 'Страница не отображается'

    def test_post(self):
        guest_client = Client()
        user = User.objects.get(pk=1)
        post = Post.objects.get(author=user)
        id = post.pk
        try:
            response = guest_client.get(f'/posts/{id}/')
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            print(e)
            assert False, 'Страница не отображается'
