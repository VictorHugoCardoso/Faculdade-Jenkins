from django.contrib import admin
from .models import Aluno
from .models import Disciplina
from .models import AlunoDisciplina
from .models import Frequencia
from .models import Notas

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(AlunoDisciplina)
admin.site.register(Frequencia)
admin.site.register(Notas)

# Register your models here.
