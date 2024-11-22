from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from todo.models import TaskItem

class TaskViewsTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.User = get_user_model()
        
        # Create test user
        self.user = self.User.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        
        # Create another user for permission testing
        self.other_user = self.User.objects.create_user(
            email='other@example.com',
            password='testpass123'
        )
        
        # Create a test task
        self.task = TaskItem.objects.create(
            user=self.user,
            owner=self.user,
            title='Test Task',
            completed=False
        )

    def test_todo_list_view(self):
        """Test todo list view"""
        # Test unauthorized access
        response = self.client.get(reverse('todo:todo_list'))
        self.assertEqual(response.status_code, 302)  # Redirects to login
        
        # Test authorized access
        self.client.login(email='test@example.com', password='testpass123')
        response = self.client.get(reverse('todo:todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        self.assertContains(response, 'Test Task')

    def test_add_task(self):
        """Test adding a new task"""
        self.client.login(email='test@example.com', password='testpass123')
        
        # Test GET request
        response = self.client.get(reverse('todo:add_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_form.html')
        
        # Test POST request
        response = self.client.post(reverse('todo:add_task'), {
            'title': 'New Test Task'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful creation
        
        # Verify task was created
        self.assertTrue(TaskItem.objects.filter(title='New Test Task').exists())

    def test_edit_task(self):
        """Test editing an existing task"""
        self.client.login(email='test@example.com', password='testpass123')
        
        # Test GET request
        response = self.client.get(reverse('todo:edit_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_form.html')
        
        # Test POST request
        response = self.client.post(
            reverse('todo:edit_task', args=[self.task.id]),
            {'title': 'Updated Test Task'}
        )
        self.assertEqual(response.status_code, 302)  # Redirects after successful update
        
        # Verify task was updated
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Test Task')

    def test_delete_task(self):
        """Test deleting a task"""
        self.client.login(email='test@example.com', password='testpass123')
        
        # Test GET request (confirmation page)
        response = self.client.get(reverse('todo:delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_confirm_delete.html')
        
        # Test POST request (actual deletion)
        response = self.client.post(reverse('todo:delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after successful deletion
        
        # Verify task was deleted
        self.assertFalse(TaskItem.objects.filter(id=self.task.id).exists())

    def test_task_privacy(self):
        """Test that users can only access their own tasks"""
        self.client.login(email='other@example.com', password='testpass123')
        
        # Try to access another user's task
        response = self.client.get(reverse('todo:edit_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 404)
        
        # Try to delete another user's task
        response = self.client.post(reverse('todo:delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 404)
        
        # Verify task still exists
        self.assertTrue(TaskItem.objects.filter(id=self.task.id).exists())