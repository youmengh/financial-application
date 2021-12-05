# Generated by Django 3.2.9 on 2021-12-05 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_num', models.IntegerField()),
                ('account_name', models.CharField(default='My Account', max_length=100)),
                ('account_type', models.CharField(default='Checking', max_length=100)),
                ('account_bal', models.DecimalField(decimal_places=1, max_digits=100)),
                ('bank_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.bank')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
            ],
        ),
    ]
