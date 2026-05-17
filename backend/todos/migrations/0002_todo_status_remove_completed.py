from django.db import migrations, models


def migrate_completed_to_status(apps, schema_editor):
    Todo = apps.get_model("todos", "Todo")
    Todo.objects.filter(completed=True).update(status="completed")
    Todo.objects.filter(completed=False).update(status="pending")


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("in_progress", "In progress"),
                    ("completed", "Completed"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
        migrations.RunPython(migrate_completed_to_status, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="todo",
            name="completed",
        ),
    ]
