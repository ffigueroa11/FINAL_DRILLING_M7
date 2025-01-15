from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Químico",
            ciudad="Chillan",
            pais="Chile"
        )

    def test_laboratorio_data(self):

        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio Químico")
        self.assertEqual(laboratorio.ciudad, "Chillan")
        self.assertEqual(laboratorio.pais, "Chile")

    def test_laboratorio_detail_url(self):

        response = self.client.get(f'/laboratorio/{self.laboratorio.id}/')
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_detail_reverse(self):

        url = reverse('laboratorio_detail', args=[self.laboratorio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_detail_template(self):

        url = reverse('laboratorio_detail', args=[self.laboratorio.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'laboratorio_detail.html')
        self.assertContains(response, "Laboratorio Químico")
        self.assertContains(response, "Chillan")
        self.assertContains(response, "Chile")

