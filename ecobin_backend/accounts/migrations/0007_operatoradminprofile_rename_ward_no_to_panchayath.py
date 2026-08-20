from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_operatoronboarding_user_approved_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operatoradminprofile',
            old_name='ward_no',
            new_name='panchayath',
        ),
        migrations.AlterField(
            model_name='operatoradminprofile',
            name='panchayath',
            field=models.CharField(max_length=100),
        ),
    ]
