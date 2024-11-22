from django.test import TestCase
from django.contrib.auth import get_user_model
from todo.models import TaskItem

class TaskItemModelTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        
        self.task = TaskItem.objects.create(
            user=self.user,
            owner=self.user,
            title='Test Task',
            completed=False
        )

    def test_task_creation(self):
        """Test TaskItem model creation"""
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.user, self.user)
        self.assertEqual(self.task.owner, self.user)
        self.assertFalse(self.task.completed)
        self.assertTrue(self.task.created_at)
        self.assertTrue(self.task.updated_at)

    def test_task_str_method(self):
        """Test TaskItem string representation"""
        self.assertEqual(str(self.task), 'Test Task')
