from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item

# Create your tests here.
class ItemModelTest(TestCase):
    def setUp(self):
        # Criando um usuário para associar com o item
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Criando um item para teste
        self.item = Item.objects.create(
            user_name=self.user,
            item_name='Teste Item',
            item_drescription='Descrição do Item',
            image='pictures/test.jpg'
        )

    def test_item_creation(self):
        # Testa se o item foi criado corretamente
        self.assertEqual(self.item.item_name, 'Teste Item')
        self.assertEqual(self.item.item_drescription, 'Descrição do Item')
        self.assertEqual(self.item.user_name.username, 'testuser')
        self.assertEqual(str(self.item), 'Teste Item')
    
    def test_item_default_image(self):
        # Testa se a imagem padrão é usada quando não é fornecida
        item_without_image = Item.objects.create(
            user_name=self.user,
            item_name='Item Sem Imagem',
            item_drescription='Descrição do Item'
        )
        self.assertEqual(item_without_image.image.name, 'Images/None/Noimg.jpg')

    def test_item_update(self):
        # Atualiza o item e testa se a atualização foi bem sucedida
        self.item.item_name = 'Novo Nome'
        self.item.save()
        self.assertEqual(self.item.item_name, 'Novo Nome')

    def test_item_delete(self):
        # Deleta o item e testa se ele foi removido do banco de dados
        item_id = self.item.id
        self.item.delete()
        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(id=item_id)
