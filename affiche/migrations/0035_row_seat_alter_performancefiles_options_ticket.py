# Generated by Django 4.2.13 on 2024-06-13 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0034_performancefiles_for_performance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('is_reserved', models.BooleanField(default=False)),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affiche.row')),
            ],
        ),
        migrations.AlterModelOptions(
            name='performancefiles',
            options={'verbose_name_plural': 'Performance Files'},
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=100)),
                ('purchase_time', models.DateTimeField(auto_now_add=True)),
                ('seat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='affiche.seat')),
            ],
        ),
    ]
