from rest_framework.test import APITestCase

from .factories import ResourceFactory


class ResourceTest(APITestCase):
    '''
    Test Driven Development Approach
    '''
    @classmethod
    def setUpTestData(cls):
        cls.r1, cls.r2, cls.r3 = ResourceFactory.create_batch(3)

    def test_locking_resource(self):
        # testing that resource r1 is free
        self.assertEqual(self.r1.status, self.r1.RELEASED)
        # call lock endpoint
        response = self.client.post(
            '/api/resources/request/{}/'.format(self.r1.id),
        )
        self.assertEqual(response.status_code, 200)
        # test that r1 is locked
        self.r1.refresh_from_db()
        self.assertEqual(self.r1.status, self.r1.LOCKED)

    def test_releasing_resource(self):
        self.r1.status = self.r1.LOCKED
        self.r1.save()
        # testing that resource r1 is locked
        self.assertEqual(self.r1.status, self.r1.LOCKED)
        # call lock endpoint
        response = self.client.post(
            '/api/resources/release/{}/'.format(self.r1.id),
        )
        self.assertEqual(response.status_code, 200)
        # test that r1 is locked
        self.r1.refresh_from_db()
        self.assertEqual(self.r1.status, self.r1.RELEASED)

    def test_requesting_locked_resource(self):
        self.r1.status = self.r1.LOCKED
        self.r1.save()
        response = self.client.post(
            '/api/resources/request/{}/'.format(self.r1.id),
        )
        self.assertEqual(response.status_code, 400)
        # test that r1 is locked
        self.r1.refresh_from_db()
        self.assertEqual(self.r1.status, self.r1.LOCKED)
