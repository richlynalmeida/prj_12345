# Generated by Django 4.0.8 on 2023-07-13 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a_hr', '0001_initial'),
        ('b_wbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_code', models.CharField(max_length=10, unique=True, verbose_name='Contract Code')),
                ('contract_title', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Contract Title')),
                ('contract_tender_costs', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18, null=True, verbose_name='Contract Tender Costs')),
                ('contract_award_costs', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=18, null=True, verbose_name='Contract Award Costs')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Contract Start Date')),
                ('finish_date', models.DateTimeField(blank=True, null=True, verbose_name='Contract Finish Date')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Contract Code Comments')),
            ],
            options={
                'verbose_name_plural': 'Contracts',
                'db_table': 'contract',
                'ordering': ['contract_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContractPricingStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_pricing_style_code', models.CharField(max_length=5, unique=True, verbose_name='Contract Pricing Style Code')),
                ('contract_pricing_style_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='Contract Pricing Style Title')),
            ],
            options={
                'verbose_name_plural': 'Contract Pricing Styles',
                'db_table': 'contract_pricing_style',
                'ordering': ['contract_pricing_style_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_type_code', models.CharField(max_length=2, unique=True, verbose_name='Contract Type Code')),
                ('contract_type_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='Contract Type Title')),
            ],
            options={
                'verbose_name_plural': 'Contract Types',
                'db_table': 'contract_type',
                'ordering': ['contract_type_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContractClauses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_clause_number', models.CharField(max_length=15, unique=True, verbose_name='Contract Clause Number')),
                ('contract_clause_title', models.CharField(max_length=55, unique=True, verbose_name='Contract Clause Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('contract', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='f_contracts.contract', verbose_name='Contract ID')),
            ],
            options={
                'verbose_name_plural': 'Contract Clauses',
                'db_table': 'contract_clause',
                'ordering': ['contract_clause_number'],
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_pricing_style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f_contracts.contractpricingstyle', verbose_name='Contract Pricing Style Code'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f_contracts.contracttype', verbose_name='Contract Type Code'),
        ),
        migrations.AddField(
            model_name='contract',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b_wbs.discipline', verbose_name='Discipline ID'),
        ),
        migrations.AddField(
            model_name='contract',
            name='parent_contract',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='f_contracts.contract', verbose_name='Parent Contract Code'),
        ),
        migrations.CreateModel(
            name='ContractSecondaryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_hr.company', verbose_name='Company ID')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f_contracts.contract', verbose_name='Contract ID')),
                ('stakeholder_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_hr.stakeholderroles', verbose_name='Stakeholder Role ID')),
            ],
            options={
                'verbose_name_plural': 'Contract Vendor Information',
                'db_table': 'contract_secondary_info',
                'managed': True,
                'unique_together': {('contract', 'company', 'stakeholder_role')},
            },
        ),
    ]
