# Generated by Django 4.2.1 on 2024-05-01 10:00

from django.db import migrations

def populate_permissions(apps, schema_editor):
    PERMISSIONS = [
        #Training - Students
        ('can add student training', 'can_add_student_training'),
        ('can edit student training', 'can_edit_student_training'),
        ('can view student training', 'can_view_student_training'),
        ('can delete student training', 'can_delete_student_training'),
        ('can approve student training', 'can_approve_student_training'),

        #Test - Students
        ('can add student test', 'can_add_student_test'),
        ('can edit student test', 'can_edit_student_test'),
        ('can view student test', 'can_view_student_test'),
        ('can delete student test', 'can_delete_student_test'),
        ('can approve student test', 'can_approve_student_test'),

        #Role Assignment
        ('can assign role', 'can_assign_role'),

        #Reports
        ('can view organization report', 'can_view_organization_report'),
        ('can view state report', 'can_view_state_report'),
        ('can view district report', 'can_view_district_report'),
        ('can view city report', 'can_view_city_report'),
        ('can view school report', 'can_view_school_report'),
        
        #Bulk School Registration
        ('allow bulk school registration', 'allow_bulk_school_registration'),

         #Training - Teachers
        ('can add teacher training', 'can_add_teacher_training'),
        ('can edit teacher training', 'can_edit_teacher_training'),
        ('can view teacher training', 'can_view_teacher_training'),
        ('can delete teacher training', 'can_delete_teacher_training'),
        ('can approve teacher training', 'can_approve_teacher_training'),

        #Test - Teachers
        ('can add teacher test', 'can_add_teacher_test'),
        ('can edit teacher test', 'can_edit_teacher_test'),
        ('can view teacher test', 'can_view_teacher_test'),
        ('can delete teacher test', 'can_delete_teacher_test'),
        ('can approve teacher test', 'can_approve_teacher_test'),

    ]
    Permission = apps.get_model('accounts', 'Permission')
    for name, codename in PERMISSIONS:
        Permission.objects.create(name=name, codename=codename)


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_auto_20240501_1530"),
    ]

    operations = [migrations.RunPython(populate_permissions)]