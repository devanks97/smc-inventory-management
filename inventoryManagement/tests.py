from django.test import TestCase, Client
from django.contrib.auth.models import User

from .modelsList.deviceListModel import deviceList
from .modelsList.recordModel import record
from .modelsList.recordSummaryModel import recordSummary

def create_user(self):
    self.username = "test_admin"
    self.password = User.objects.make_random_password()
    user, created = User.objects.get_or_create(username=self.username)
    user.set_password(self.password)
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
    self.user = user

def create_device(self)
    deviceName = "laptop" #lowercase
# class TestAdminPanel(TestCase):

    # def test_spider_admin(self):
        # self.create_user()
        # client = Client()
        # client.login(username=self.username, password=self.password)
        # admin_pages = [
            # "/",
            # "/auth/",
            # "/inventoryManagement/record/",
            # "/auth/group/",
            # "/inventoryManagement/record/add/",
            # "/inventoryManagement/record/export/",
            # "/inventoryManagement/record/import/",
            # "/inventoryManagement/recordsummary/",
            # "/auth/group/add/",
            # "/auth/user/",
            # "/auth/user/add/",
            # "/password_change/"
        # ]
        # for page in admin_pages:
            # resp = client.get(page)
            # assert resp.status_code == 200
            # assert "<!DOCTYPE html" in resp.content

class TestExport(TestCase):

    def test_import_case(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)


# Above code is licensed under the MIT License.