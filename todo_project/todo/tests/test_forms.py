from django.test import TestCase
from todo.forms import TaskForm

class TaskFormTest(TestCase):
    def test_task_form_valid_data(self):
        """Test TaskForm with valid data"""
        form = TaskForm(data={
            'title': 'Test Task'
        })
        self.assertTrue(form.is_valid())

    def test_task_form_empty_data(self):
        """Test TaskForm with empty data"""
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)