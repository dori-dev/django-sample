from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note


class NotesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user: User = User.objects.create(
            first_name='mohammad',
            last_name='dori',
            username='dori.dev',
            email='mr.dori.dev@gmail.com',
        )
        cls.user.set_password('1234')
        cls.user.save()

    def setUp(self) -> None:
        self.now = datetime.now()
        Note.objects.create(
            title='sample note',
            author=User.objects.first(),
            body='sample note body')

    def _first_note(self) -> Note:
        return Note.objects.first()

    def test_note_title_content(self):
        self.assertEqual(self._first_note().title, 'sample note')

    def test_note_str(self):
        self.assertEqual(str(self._first_note()), 'sample note')

    def test_note_body_content(self):
        self.assertEqual(self._first_note().body, 'sample note body')

    def test_note_created_date(self):
        note_created: datetime = self._first_note().created
        interval = note_created.timestamp() - self.now.timestamp()
        self.assertEqual(round(interval), 0)

    def test_note_author(self):
        author: User = self._first_note().author
        self.assertEqual(author, User.objects.first())
        self.assertEqual(author.username, 'dori.dev')
        self.assertEqual(
            Note.objects.get(author__username='dori.dev'),
            self._first_note())

    def test_delete_note_page(self):
        self.client.force_login(
            User.objects.get(username='dori.dev')
        )
        self.client.get(f'/delete/{self._first_note().id}/')
        self.assertEqual(self._first_note(), None)


class NotesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user: User = User.objects.create(
            first_name='mohammad',
            last_name='dori',
            username='dori.dev',
            email='mr.dori.dev@gmail.com',
        )
        cls.user.set_password('1234')
        cls.user.save()

    def setUp(self) -> None:
        self.client.force_login(
            User.objects.get(username='dori.dev')
        )
        Note.objects.create(
            title='the sample note title',
            author=User.objects.first(),
            body='the sample note body'
        )

    def _note_id(self) -> int:
        return Note.objects.first().id

    def _response(self, url: str) -> None:
        return self.client.get(url)

    # test pages template use
    def test_index_page_template(self):
        self.assertTemplateUsed(
            self._response(reverse('notes:index')), 'notes/index.html')

    def test_create_page_template(self):
        self.assertTemplateUsed(
            self._response(reverse('notes:create')), 'notes/create.html')

    def test_detail_page_template(self):
        url = reverse('notes:detail', args=(self._note_id(),))
        self.assertTemplateUsed(
            self._response(url), 'notes/detail.html')

    def test_update_page_template(self):
        url = reverse('notes:update', args=(self._note_id(),))
        self.assertTemplateUsed(
            self._response(url), 'notes/update.html')

    # test create note and update note views
    def test_create_and_update_note(self):
        now = datetime.now()
        response = self.client.post(
            reverse('notes:create'),
            {
                'title': 'new note',
                'body': 'body for new note'
            })
        self.assertEqual(response.status_code, 302)
        note: Note = Note.objects.last()
        self.assertEqual(note.id, 2)
        self.assertEqual(note.title, 'new note')
        self.assertEqual(note.body, 'body for new note')
        created: datetime = note.created
        interval = created.timestamp() - now.timestamp()
        self.assertEqual(round(interval), 0)

    def test_update_note(self):
        response = self.client.post(
            reverse('notes:update', args=(1,)),
            {
                'title': 'updated title',
                'body': 'updated body'
            })
        self.assertEqual(response.status_code, 302)
        note: Note = Note.objects.first()
        self.assertEqual(note.id, 1)
        self.assertEqual(note.title, 'updated title')
        self.assertEqual(note.body, 'updated body')


class NotesUrlTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user: User = User.objects.create(
            first_name='mohammad',
            last_name='dori',
            username='dori.dev',
            email='mr.dori.dev@gmail.com',
        )
        cls.user.set_password('1234')
        cls.user.save()

    def setUp(self) -> None:
        Note.objects.create(
            title='note 1',
            author=User.objects.first(),
            body='note 1 body'
        )

    def _note_id(self) -> int:
        return Note.objects.first().id

    def _status_code(self, url: str) -> int:
        response = self.client.get(url)
        return response.status_code

    def _login(self) -> None:
        self.client.force_login(
            User.objects.get(username='dori.dev')
        )

    # test pages url name content
    def test_index_url_name_content(self):
        self.assertEqual(reverse('notes:index'), '/')

    def test_create_url_name_content(self):
        self.assertEqual(reverse('notes:create'), '/create/')

    def test_detail_url_name_content(self):
        self.assertEqual(
            reverse('notes:detail', args=(self._note_id(),)),
            '/detail/1/')

    def test_update_url_name_content(self):
        self.assertEqual(
            reverse('notes:update', args=(self._note_id(),)),
            '/update/1/')

    def test_delete_url_name_content(self):
        self.assertEqual(
            reverse('notes:delete', args=(self._note_id(),)),
            '/delete/1/')

    # test pages status code
    def test_index_page_status_code(self):
        self.assertEqual(self._status_code(reverse('notes:index')), 200)

    def test_create_page_status_code(self):
        self._login()
        self.assertEqual(self._status_code(reverse('notes:create')), 200)

    def test_detail_page_status_code(self):
        self._login()
        url = reverse('notes:detail', args=(self._note_id(),))
        self.assertEqual(self._status_code(url), 200)

    def test_update_page_status_code(self):
        self._login()
        url = reverse('notes:update', args=(self._note_id(),))
        self.assertEqual(self._status_code(url), 200)

    def test_delete_page_status_code(self):
        self._login()
        url = reverse('notes:delete', args=(self._note_id(),))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0], ('/', 302))
