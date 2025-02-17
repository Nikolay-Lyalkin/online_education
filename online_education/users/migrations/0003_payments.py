# Generated by Django 5.1.4 on 2024-12-17 11:47

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_alter_course_description_alter_course_preview_and_more"),
        ("users", "0002_alter_user_options_user_avatar_user_city_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_payment",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Дата оплаты"
                    ),
                ),
                (
                    "sum_payment",
                    models.PositiveIntegerField(verbose_name="Сумма платежа"),
                ),
                (
                    "method_payment",
                    models.CharField(
                        choices=[
                            ("cash", "Наличные"),
                            ("transfer_to_account", "перевод на счёт"),
                        ],
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="paid_course",
                        to="materials.course",
                        verbose_name="курс",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="paid_lesson",
                        to="materials.lesson",
                        verbose_name="урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платёж",
                "verbose_name_plural": "Платежи",
                "db_table": "payments",
            },
        ),
    ]
