# Generated by Django 3.2.5 on 2022-04-02 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('specialization', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceProvider',
            fields=[
                ('provider_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('provider_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=200)),
                ('menu_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('patient_dob', models.DateField(blank=True, default=None, null=True)),
                ('patient_insurance_member_id', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('patient_insurance_group_id', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('blood_type', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('address', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('zipCode', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('emergency_contact_firstname', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('emergency_contact_lastname', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('emergency_contact_phone_number', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('emergency_contact_email', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('allergies', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('medicationFollowed', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('preExistingMedicalConditions', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('anyOtherMedicalDetails', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update_date', models.DateTimeField(null=True)),
                ('patient_insurance_provider_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.insuranceprovider')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shift_Timings',
            fields=[
                ('shift_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('shift_type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SHSUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.roles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('records_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('document', models.JSONField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('last_modified_date', models.DateTimeField(null=True)),
                ('document_type', models.CharField(choices=[('D', 'Diagnosis'), ('P', 'Prescription'), ('L', 'LabReport')], max_length=1)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('payment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('admit_fee', models.IntegerField()),
                ('discharge_fee', models.IntegerField()),
                ('supplies_fee', models.IntegerField()),
                ('consultation_fee', models.IntegerField()),
                ('overall_payment', models.IntegerField()),
                ('payment_generated_date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('unpaid', 'unpaid'), ('paid', 'paid')], default='unpaid', max_length=200)),
                ('payment_update_date', models.DateTimeField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='update_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='update_user', to='secure_hospital_system.shsuser'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_user', to='secure_hospital_system.shsuser'),
        ),
        migrations.CreateModel(
            name='Menu_Mapping',
            fields=[
                ('menu_map_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_default', models.BooleanField()),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.menu')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.roles')),
            ],
        ),
        migrations.CreateModel(
            name='Lab_Test',
            fields=[
                ('lab_test_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('recommended_test', models.TextField(max_length=200)),
                ('recommended_date', models.DateField()),
                ('action_taken_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Denied', 'Denied'), ('Completed', 'Completed')], default='Pending', max_length=200)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.patient')),
                ('record', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.records')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_availability_booked',
            fields=[
                ('booking_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateTimeField(null=True)),
                ('appointment_start_time', models.TimeField()),
                ('appointment_end_time', models.TimeField()),
                ('booking_request_timestamp', models.DateTimeField(auto_now_add=True)),
                ('approved_date', models.DateTimeField(default=None, null=True)),
                ('status', models.CharField(choices=[('approved', 'approved'), ('pending', 'pending'), ('denied', 'denied')], default='pending', max_length=200)),
                ('approver_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.shsuser')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.patient')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='shift_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.shift_timings'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.shsuser'),
        ),
        migrations.CreateModel(
            name='Claim_Request',
            fields=[
                ('claim_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('claim_status', models.CharField(choices=[('approved', 'approved'), ('pending', 'pending'), ('denied', 'denied')], default='pending', max_length=200)),
                ('claim_raised_date', models.DateTimeField()),
                ('claim_update_date', models.DateTimeField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.patient')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secure_hospital_system.payments')),
            ],
        ),
    ]
