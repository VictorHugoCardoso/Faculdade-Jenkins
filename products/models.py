from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.description


class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nomeAluno = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeAluno


class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nomeDisciplina = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeDisciplina


class AlunoDisciplina(models.Model):
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    discliplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.aluno, self.discliplina)


class Frequencia(models.Model):
    id = models.AutoField(primary_key=True)
    presente = models.IntegerField()
    data = models.CharField(max_length=100, null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    discliplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.id, self.presente, self.data, self.aluno, self.discliplina)
class Notas(models.Model):
    id = models.AutoField(primary_key=True)
    nota1 = models.DecimalField(max_digits=9, decimal_places=2, default=0,null=True)
    nota2 = models.DecimalField(max_digits=9, decimal_places=2, default=0,null=True)
    nota3 = models.DecimalField(max_digits=9, decimal_places=2, default=0,null=True)
    nota4 = models.DecimalField(max_digits=9, decimal_places=2, default=0,null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    discliplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

