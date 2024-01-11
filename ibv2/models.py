from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.dispatch import receiver
from django.db.models.signals import pre_save
from PIL import Image

class Destaque(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens_destaques')
    texto = RichTextUploadingField()
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Publicacoes(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.CharField(max_length=250)
    imagem = models.ImageField(upload_to='imagens_publicacoes')
    texto = RichTextUploadingField()
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Programacao(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.CharField(max_length=20)
    hora = models.CharField(max_length=5)

    def __str__(self):
        return self.titulo

class Eventos(models.Model):
    titulo=models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens_eventos')

    def __str__(self):
        return self.titulo

class Classificados(models.Model):
    titulo=models.CharField(max_length=100)
    banner = models.ImageField(upload_to='banner_classificados')
    contato=models.CharField(max_length=11)

    def __str__(self):
        return self.titulo

def redimensionar_imagem(sender, instance, **kwargs):
    if hasattr(instance, 'imagem'):
        max_size = (800, 800)  # Tamanho máximo desejado
        image_path = instance.imagem.path

        try:
            with Image.open(image_path) as img:
                img.thumbnail(max_size)
                img.save(image_path)
        except Exception as e:
            # Adicione um log para registrar o erro
            print(f"Erro ao redimensionar a imagem: {str(e)}")

# Aplicar o sinal para todas as classes de modelos relevantes
@receiver(pre_save, sender=Destaque)
@receiver(pre_save, sender=Publicacoes)
@receiver(pre_save, sender=Programacao)
@receiver(pre_save, sender=Classificados)
@receiver(pre_save, sender=Eventos)
def pre_save_handler(sender, instance, **kwargs):
    redimensionar_imagem(sender, instance, **kwargs)
