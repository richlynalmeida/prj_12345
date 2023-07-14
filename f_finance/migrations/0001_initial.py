# Generated by Django 4.0.8 on 2023-07-13 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('z_tab_pmb_quantum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceTransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finance_transaction_type_code', models.CharField(max_length=1, unique=True, verbose_name='Finance Transaction Type Code')),
                ('finance_transaction_type_title', models.CharField(max_length=55, unique=True, verbose_name='Finance Transaction Type Title')),
                ('contract_flag', models.CharField(default='N', max_length=1, verbose_name='Contract Flag')),
            ],
            options={
                'verbose_name_plural': 'Finance Transaction Types',
                'db_table': 'finance_transaction_type',
                'ordering': ['finance_transaction_type_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PmbL03WpAccountsReceivable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_date', models.DateTimeField(verbose_name='Calendar Date')),
                ('ar_costs', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18, null=True, verbose_name='AR Costs')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('pmb_L03_wp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_tab_pmb_quantum.pmbl03wp', verbose_name='PMB L03 WP ID')),
            ],
            options={
                'verbose_name_plural': 'PMB L03 WP Accounts Receivable',
                'db_table': 'pmb_L03_wp_ar',
                'ordering': ['pmb_L03_wp', 'calendar_date'],
                'managed': True,
                'unique_together': {('pmb_L03_wp', 'calendar_date')},
            },
        ),
        migrations.CreateModel(
            name='PmbL03WpAccountsPayable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_date', models.DateTimeField(verbose_name='Calendar Date')),
                ('ap_costs', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18, null=True, verbose_name='AP Costs')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('pmb_L03_wp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_tab_pmb_quantum.pmbl03wp', verbose_name='PMB L03 WP ID')),
            ],
            options={
                'verbose_name_plural': 'PMB L03 WP Accounts Payable',
                'db_table': 'pmb_L03_wp_ap',
                'ordering': ['pmb_L03_wp', 'calendar_date'],
                'managed': True,
                'unique_together': {('pmb_L03_wp', 'calendar_date')},
            },
        ),
    ]
