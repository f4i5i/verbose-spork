# Generated by Django 3.0.3 on 2020-02-25 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(max_length=1000)),
                ('desc', models.TextField(max_length=1000)),
                ('time', models.TextField(max_length=1000)),
                ('loc', models.TextField(max_length=1000)),
                ('locdesc', models.TextField(max_length=1000)),
                ('venue', models.TextField(max_length=1000)),
                ('rtime', models.TextField(max_length=1000)),
                ('status', models.TextField(max_length=1000)),
                ('isteam', models.TextField(max_length=1000)),
                ('hascomps', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlfortournement', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champ', models.TextField(max_length=1000)),
                ('status', models.TextField(max_length=1000)),
                ('dates', models.TextField(max_length=1000)),
                ('datesdesc', models.TextField(max_length=1000)),
                ('champdesc', models.TextField(max_length=1000)),
                ('location', models.TextField(max_length=1000)),
                ('events', models.TextField(max_length=1000)),
                ('phases', models.TextField(max_length=1000)),
                ('locations', models.TextField(max_length=1000)),
                ('isfinished', models.BooleanField()),
                ('urltournement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urlfortour', to='scrape.Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.TextField(max_length=1000)),
                ('away', models.TextField(max_length=1000)),
                ('home_reg', models.TextField(max_length=1000)),
                ('home_org', models.TextField(max_length=1000)),
                ('home_orgdesc', models.TextField(max_length=1000)),
                ('away_reg', models.TextField(max_length=1000)),
                ('away_org', models.TextField(max_length=1000)),
                ('away_orgdesc', models.TextField(max_length=1000)),
                ('team_a', models.TextField(blank=True, max_length=1000, null=True)),
                ('team_b', models.TextField(blank=True, max_length=1000, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='scrape.Matches')),
            ],
        ),
        migrations.AddField(
            model_name='matches',
            name='champ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='champinfo', to='scrape.TournamentInfo'),
        ),
    ]
