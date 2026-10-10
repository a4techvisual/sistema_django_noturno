from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_paciente_sintomas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='nome',
            field=models.CharField(max_length=150),
        ),
    ]
