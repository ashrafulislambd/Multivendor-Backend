# Generated by Django 4.2.11 on 2024-08-24 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_alter_product_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('unpaird', 'Unpaid'), ('card', 'Credit/Debit Card'), ('bkash', 'bKash'), ('nagad', 'Nagad')], max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.order')),
            ],
        ),
    ]
