from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.views import MenuItemsView

class MenuItemsViewTest(TestCase):
    databases = {'default'}

    MainTestUser = 0
    TestUrl = 'restaurant:menuitems:memu_items_list'
    TestUsers = [
        ('UserTest1', 'init1234!'),
    ]
    TestDatas = list()
    TestDatasAddsIndex = 0
    TestDatasAdds = (
            {
                'title': '1 Title',
                'price': 1230.45,
                'inventory': -2,
            },
            {
                'title': '2 Title',
                'price': 987.65,
                'inventory': -20,
            },
        )

    def setUp(self) -> None:
        self.TestDatasAddsIndex = 0
        self.TestDatas = [
            {
                'title': 'Title',
                'price': 123.45,
                'inventory': -2,
            },
            {
                'title': 'Title 2',
                'price': 67.89,
                'inventory': -4,
            },
            {
                'title': 'Title 3',
                'price': 24.68,
                'inventory': 7,
            },
        ]

        for testUser in self.TestUsers:
            User.objects.create_user(username=testUser[0], password=testUser[1])

        for testItem in self.TestDatas:
            Menu.objects.create(title = testItem['title'],
                                price = testItem['price'],
                                inventory = testItem['inventory'],
                                )

    def test_menuitems_post_auth(self):
        url = reverse(self.TestUrl)
        self.assertTrue(self.client.login(username=self.TestUsers[self.MainTestUser][0],
                                          password=self.TestUsers[self.MainTestUser][1],
                                          )
                        )
        self.menuitems_post_check(url)
        self.test_menuitems_get_auth()

    def test_menuitems_post_anon(self):
        url = reverse(self.TestUrl)
        self.client.logout()
        self.menuitems_post_check(url)
        self.test_menuitems_get_anon()

    def menuitems_post_check(self, url):
        response = self.client.post(url,self.TestDatasAdds[self.TestDatasAddsIndex])
        self.assertEqual(response.status_code, 201)
        self.TestDatas.append(self.TestDatasAdds[self.TestDatasAddsIndex])
        self.TestDatasAddsIndex += 1

    def test_menuitems_get_auth(self):
        url = reverse(self.TestUrl)
        self.assertTrue(self.client.login(username=self.TestUsers[self.MainTestUser][0],
                                          password=self.TestUsers[self.MainTestUser][1],
                                          )
                        )
        response = self.client.get(url)
        self.menuitems_get_check(response)

    def test_menuitems_get_anon(self):
        url = reverse(self.TestUrl)
        self.client.logout()
        response = self.client.get(url)
        self.menuitems_get_check(response)

    def menuitems_get_check(self,response):
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data),len(self.TestDatas))
        for data in response.data:
            self.assertTrue(any(testData.get('title') == data['title']
                                for testData in self.TestDatas))