from django.contrib import admin
from myblogong.contato.models import Contato

class ContatoAdmin(admin.ModelAdmin):
	model = Contato
	list_display = ['contato_nome', 'contato_email', 'contato_favorito'] # Campos que serão mostrados no display
	list_filter = ['contato_sexo', 'contato_estado_civil'] #como será realizado o filtro
	search_fields = ['contato_nome']
	save_on_top = True

admin.site.register(Contato, ContatoAdmin) # Para registrar no admin site passando como parametros, a tabela Contato na Classe ContatoAdmin

