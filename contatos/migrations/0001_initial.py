# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('nascimento', models.DateTimeField(null=True)),
                ('telefone_fixo', models.CharField(max_length=20, verbose_name='Telefone fixo')),
                ('telefone_celular', models.CharField(max_length=20, verbose_name='Telefone celular')),
                ('email', models.EmailField(unique=True, max_length=300, verbose_name='E-mail')),
                ('endereco', models.CharField(max_length=80, verbose_name='Endereço')),
                ('complemento', models.CharField(max_length=30, verbose_name='Complemento')),
                ('uf', models.CharField(max_length=2, null=True, verbose_name='UF', choices=[('', 'Escolha uma opção'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MT', 'Mato Grosso'), ('MA', 'Maranhão'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('bairro', models.CharField(max_length=20, verbose_name='Bairro')),
                ('obs', models.TextField(null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-nome',),
                'verbose_name_plural': 'Contatos',
                'verbose_name': 'Contato',
            },
        ),
    ]
