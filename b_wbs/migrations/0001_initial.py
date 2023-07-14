# Generated by Django 4.0.8 on 2023-07-13 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostTypeClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_type_class_code', models.CharField(max_length=10, unique=True, verbose_name='Cost Type Class Code')),
                ('cost_type_class_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='Cost Type Class Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Cost Type Classes',
                'db_table': 'cost_type_class',
                'ordering': ['cost_type_class_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(max_length=5, unique=True, verbose_name='Department Code')),
                ('department_title', models.CharField(max_length=55, unique=True, verbose_name='Department Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Departments',
                'db_table': 'department',
                'ordering': ['department_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_code', models.CharField(max_length=5, unique=True, verbose_name='Discipline Code')),
                ('discipline_title', models.CharField(max_length=55, unique=True, verbose_name='Discipline Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Disciplines',
                'db_table': 'discipline',
                'ordering': ['discipline_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FacilitySystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_system_code', models.CharField(max_length=5, unique=True, verbose_name='Facility System Code')),
                ('facility_system_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='Facility System Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Facility Systems',
                'db_table': 'facility_system',
                'ordering': ['facility_system_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PmbL03WpExecutionStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmb_L03_wp_exe_style_code', models.CharField(max_length=5, unique=True, verbose_name='PMB L03 Execution Style Code')),
                ('pmb_L03_wp_exe_style_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='PMB L03 Execution Style Title')),
            ],
            options={
                'verbose_name_plural': 'PMB L03 Work Package Execution Styles',
                'db_table': 'pmb_L03_wp_exe_style',
                'ordering': ['pmb_L03_wp_exe_style_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PmbL03WpExecutionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmb_L03_wp_exe_type_code', models.CharField(max_length=5, unique=True, verbose_name='PMB L03 Execution Type Code')),
                ('pmb_L03_wp_exe_type_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='PMB L03 WP Execution Type Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'PMB L03 Work Package Execution Types',
                'db_table': 'pmb_L03_wp_exe_type',
                'ordering': ['pmb_L03_wp_exe_type_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PmbL03WpStatusType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmb_L03_wp_status_code', models.CharField(max_length=5, unique=True, verbose_name='PMB L03 WP Status Code')),
                ('pmb_L03_wp_status_title', models.CharField(max_length=55, unique=True, verbose_name='PMB L03 WP Status Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'PMB L03 WP Status Types',
                'db_table': 'pmb_L03_wp_status_type',
                'ordering': ['pmb_L03_wp_status_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PmbL04WpStatusType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmb_L04_wp_status_code', models.CharField(max_length=5, unique=True, verbose_name='PMB L04 WP Status Code')),
                ('pmb_L04_wp_status_title', models.CharField(max_length=55, unique=True, verbose_name='PMB L04 WP Status Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'PMB L04 WP Status Types',
                'db_table': 'pmb_L04_wp_status_type',
                'ordering': ['pmb_L04_wp_status_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WBSType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wbs_type_code', models.CharField(max_length=5, unique=True, verbose_name='WBS Type Code')),
                ('wbs_type_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='WBS Type Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'WBS Types',
                'db_table': 'wbs_type',
                'ordering': ['wbs_type_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WBS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wbs_code', models.CharField(max_length=5, unique=True, verbose_name='WBS Code')),
                ('wbs_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='WBS Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('wbs_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='b_wbs.wbstype', verbose_name='WBS Type ID')),
            ],
            options={
                'verbose_name_plural': 'WBS',
                'db_table': 'wbs',
                'ordering': ['wbs_code'],
                'managed': True,
                'unique_together': {('wbs_type', 'wbs_code')},
            },
        ),
        migrations.CreateModel(
            name='PmbL04WpExecutionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmb_L04_wp_exe_type_code', models.CharField(max_length=5, unique=True, verbose_name='PMB L04 WP Execution Type Code')),
                ('pmb_L04_wp_exe_type_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='PMB L04 WP Execution Type Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('pmb_L03_wp_exe_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='b_wbs.pmbl03wpexecutiontype', verbose_name='PMB L03 WP Execution Type ID')),
            ],
            options={
                'verbose_name_plural': 'PMB L04 Work Package Execution Types',
                'db_table': 'pmb_L04_wp_exe_type',
                'ordering': ['pmb_L04_wp_exe_type_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_type_code', models.CharField(max_length=20, unique=True, verbose_name='Cost Type Code')),
                ('cost_type_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='Cost Type Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('cost_type_class', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='b_wbs.costtypeclass', verbose_name='Cost Type Class ID')),
            ],
            options={
                'verbose_name_plural': 'Cost Types',
                'db_table': 'cost_type',
                'ordering': ['cost_type_code'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WAS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_code', models.CharField(max_length=5, unique=True, verbose_name='WAS Code')),
                ('was_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='WAS Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('wbs', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='b_wbs.wbs', verbose_name='WBS ID')),
            ],
            options={
                'verbose_name_plural': 'Work Areas',
                'db_table': 'was',
                'ordering': ['was_code'],
                'managed': True,
                'unique_together': {('wbs', 'was_code')},
            },
        ),
        migrations.CreateModel(
            name='FacilitySystemDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_system_detail_code', models.CharField(max_length=15, unique=True, verbose_name='Facility System Detail Code')),
                ('facility_system_detail_title', models.CharField(blank=True, max_length=55, null=True, unique=True, verbose_name='Facility System Detail Title')),
                ('comments', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Comments')),
                ('facility_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='b_wbs.facilitysystem', verbose_name='Facility System ID')),
            ],
            options={
                'verbose_name_plural': 'Facility System Details',
                'db_table': 'facility_system_detail',
                'ordering': ['facility_system_detail_code'],
                'managed': True,
                'unique_together': {('facility_system', 'facility_system_detail_code')},
            },
        ),
    ]
