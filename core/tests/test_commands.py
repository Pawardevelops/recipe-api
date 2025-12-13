from django.test import SimpleTestCase
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError

@patch('core.management.commands.wait_for_db.Command.check_db')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, check_db):
        """Test waiting for database if database ready."""
        check_db.return_value = True
        call_command('wait_for_db')
        self.assertEqual(check_db.call_count, 1)
    
    def test_wait_for_db_not_ready(self, check_db):
        """Test waiting for database if database not ready."""
        check_db.side_effect = [OperationalError] * 5 + [True]
        call_command('wait_for_db')
        self.assertEqual(check_db.call_count, 6)
