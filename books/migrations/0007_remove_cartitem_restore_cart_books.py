# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.AddField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(to='books.book', verbose_name='Товары'),
        ),
    ]
