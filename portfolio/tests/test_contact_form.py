from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from portfolio.models import Contact
from django.core.cache import cache
import time

class ContactFormTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('portfolio:contact')
        # Limpa o cache antes de cada teste
        cache.clear()
        
    def test_normal_submission(self):
        """Testa um envio normal do formulário"""
        time.sleep(3)  # Espera 3 segundos para simular preenchimento humano
        data = {
            'name': 'Teste Normal',
            'email': 'teste@exemplo.com',
            'subject': 'Teste de Contato',
            'message': 'Esta é uma mensagem de teste normal.',
            'timestamp': time.time() - 5  # Simula 5 segundos de preenchimento
        }
        
        response = self.client.post(self.url, data)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 1)  # Verifica se o email foi enviado
        
    def test_honeypot_filled(self):
        """Testa que o formulário é rejeitado quando o honeypot é preenchido"""
        data = {
            'name': 'Bot Malicioso',
            'email': 'bot@spam.com',
            'subject': 'Spam',
            'message': 'Spam message',
            'website': 'http://spam.com',  # Honeypot preenchido
            'timestamp': time.time()
        }
        
        response = self.client.post(self.url, data)
        self.assertEqual(Contact.objects.count(), 0)  # Não deve criar contato
        self.assertEqual(len(mail.outbox), 0)  # Não deve enviar email
        
    def test_too_fast_submission(self):
        """Testa que o formulário é rejeitado quando preenchido muito rápido"""
        data = {
            'name': 'Bot Rápido',
            'email': 'bot@rapido.com',
            'subject': 'Teste Rápido',
            'message': 'Mensagem enviada muito rápido',
            'timestamp': time.time()  # Timestamp atual = preenchimento instantâneo
        }
        
        response = self.client.post(self.url, data)
        self.assertEqual(Contact.objects.count(), 0)
        self.assertEqual(len(mail.outbox), 0)
        
    def test_rate_limiting(self):
        """Testa o limite de envios por IP"""
        data = {
            'name': 'Teste Rate Limit',
            'email': 'teste@ratelimit.com',
            'subject': 'Teste',
            'message': 'Teste de limite de envios',
            'timestamp': time.time() - 5
        }
        
        # Faz 5 submissões (deve funcionar)
        for i in range(5):
            time.sleep(3)  # Espera para não cair na validação de tempo
            response = self.client.post(self.url, data)
            self.assertEqual(response.status_code, 200)
        
        # A sexta submissão deve falhar
        time.sleep(3)
        response = self.client.post(self.url, data)
        self.assertEqual(Contact.objects.count(), 5)  # Apenas 5 devem ser criados
        
    def test_metadata_saved(self):
        """Testa se os metadados (IP, User Agent) são salvos"""
        time.sleep(3)
        data = {
            'name': 'Teste Metadata',
            'email': 'teste@metadata.com',
            'subject': 'Teste Metadata',
            'message': 'Teste de salvamento de metadata',
            'timestamp': time.time() - 5
        }
        
        response = self.client.post(
            self.url, 
            data,
            HTTP_USER_AGENT='Test Browser',
            REMOTE_ADDR='127.0.0.1'
        )
        
        contact = Contact.objects.first()
        self.assertEqual(contact.ip_address, '127.0.0.1')
        self.assertEqual(contact.user_agent, 'Test Browser')
        self.assertTrue(contact.submission_time >= 3)  # Deve ter levado pelo menos 3 segundos
