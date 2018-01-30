# Generated by Django 2.0.1 on 2018-01-30 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField()),
                ('intent', models.CharField(max_length=100)),
                ('influence', models.FloatField()),
                ('sentiment', models.FloatField()),
                ('popularity_score', models.FloatField()),
                ('figure_score', models.FloatField()),
                ('market_score', models.FloatField()),
                ('innovation_score', models.FloatField()),
                ('capital_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ActivityArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('external_url', models.CharField(max_length=1000)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('source_url', models.CharField(max_length=1000)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=20000)),
                ('impression', models.FloatField()),
                ('engagement', models.FloatField()),
                ('sentiment', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='article_image')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='brand_logo')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=1000)),
                ('baike_url', models.CharField(max_length=1000)),
                ('tianyancha_url', models.CharField(max_length=1000)),
                ('weibo_url', models.CharField(max_length=1000)),
                ('weixin_url', models.CharField(max_length=1000)),
                ('tieba_url', models.CharField(max_length=1000)),
                ('tmall_url', models.CharField(max_length=1000)),
                ('jd_url', models.CharField(max_length=1000)),
                ('job_url', models.CharField(max_length=1000)),
                ('total_popularity_score', models.FloatField()),
                ('total_figure_score', models.FloatField()),
                ('total_market_score', models.FloatField()),
                ('total_innovation_score', models.FloatField()),
                ('total_capital_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Brand')),
            ],
        ),
        migrations.AddField(
            model_name='articletag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Tag'),
        ),
        migrations.AddField(
            model_name='activityarticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Article'),
        ),
        migrations.AddField(
            model_name='activity',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Brand'),
        ),
    ]