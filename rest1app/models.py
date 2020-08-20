from django.db import models
from django.http import HttpResponseServerError
from rest_framework.exceptions import APIException


# declare a new model with a name "GeeksModel"
class Article(models.Model):
        # fields of the model
    title = models.CharField(max_length = 2)
    description = models.TextField(max_length = 2)
    body = models.TextField(max_length = 200)



        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title



    def test_api_can_get_a_articlelist(self):
        """Test the api can get a given bucketlist."""
        arti = Article.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': arti.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_201_OK)
        self.assertContains(response, arti)

    def test_api_can_update_articlelist(self):
        """Test the api can update a given bucketlist."""
        change_articlelist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': arti.id}),
            change_articlelist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_articlelist(self):
        """Test the api can delete a bucketlist."""
        arti1 = Article.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': arti1.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
