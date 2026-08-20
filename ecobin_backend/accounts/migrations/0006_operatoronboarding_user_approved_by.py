import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_operatoronboarding"),
    ]

    operations = [
        migrations.RenameField(
            model_name="operatoronboarding",
            old_name="operator",
            new_name="user",
        ),
        migrations.RemoveField(
            model_name="operatoronboarding",
            name="approved_by",
        ),
        migrations.AddField(
            model_name="operatoronboarding",
            name="approved_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="approved_staff_onboardings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]