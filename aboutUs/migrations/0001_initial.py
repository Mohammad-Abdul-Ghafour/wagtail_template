# Generated by Django 4.0.3 on 2022-03-14 12:43

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.core.fields.StreamField([('simple_banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'About Us Page',
                'verbose_name_plural': 'About Us Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]