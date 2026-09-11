from django.db import models

class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __strt__(self):
        """Devolve uma representação de uma string do modelo."""
        return self.text