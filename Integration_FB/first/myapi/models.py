# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

# # Create your models here.
# # class Hero(models.Model):
# #     name = models.CharField(max_length=60)
# #     alias = models.CharField(max_length=60)
# #     def __str__(self):
# #         return self.name

# # class Location(models.Model):
# #     S_No         = models.IntegerField()   
# #     College_Name = models.CharField(max_length=150)
# #     Address      = models.CharField(max_length=300)
# #     Latitude     = models.FloatField()
# #     Longitude    = models.FloatField()
# #     District     = models.CharField(max_length=20)
# #     State        = models.CharField(max_length=20)
# #     Pincode      = models.IntegerField()
# #     Lat          = models.FloatField()
# #     Lng          = models.FloatField()
# #     def __str__(self):
# #         return self.S_No

# class Clg_score(models.Model):
#     clg_id          = models.IntegerField(null=True) 
#     elsi_clg_id     = models.IntegerField(null=True) 
#     college_name    = models.CharField(max_length=200)
#     state           = models.CharField(max_length=50)
#     district        = models.CharField(max_length=50)
#     robots_given    = models.IntegerField() 
#     eyrtc_allowed   = models.IntegerField() 
#     tbt_allowed     = models.IntegerField() 
#     completed       = models.IntegerField() 
#     wo_attend       = models.IntegerField() 
#     lab_inaugurated = models.IntegerField() 
#     score           = models.FloatField()

# class scoring_values(models.Model):
#     TBT_Allowed     = models.FloatField()
#     TBT_Completed   = models.FloatField()
#     WO_Attend       = models.FloatField()
#     Lab_InAug       = models.FloatField()
# # ------------------------------------------------------------------------------
class clg_score(models.Model):
    clg_id = models.IntegerField(blank=True, null=True)
    elsi_clg_id = models.IntegerField(blank=True, null=True)
    clg_code = models.TextField(blank=True, null=True)
    college_name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    robots_given = models.IntegerField(blank=True, null=True)
    eyrtc_allowed = models.IntegerField(blank=True, null=True)
    eyrtc_score = models.IntegerField(blank=True, null=True)
    tbt_allowed = models.IntegerField(blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    wo_attend = models.IntegerField(blank=True, null=True)
    lab_inaugurated = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'clg_score'

class scoring_district_wise(models.Model):
    district = models.TextField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'scoring_district_wise'

class scoring_state_wise(models.Model):
    state = models.TextField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'scoring_state_wise'

# # ------------------------------------------------------------------------------

# class ElsiCollegeDtls(models.Model):
#     id = models.IntegerField(primary_key=True)
#     clg_code = models.TextField(blank=True, null=True)
#     region_id = models.IntegerField(blank=True, null=True)
#     workshop_id = models.IntegerField(blank=True, null=True)
#     college_name = models.TextField(blank=True, null=True)
#     abbreviation = models.TextField(blank=True, null=True)
#     district = models.TextField(blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     state = models.TextField(blank=True, null=True)
#     pincode = models.IntegerField(blank=True, null=True)
#     college_type = models.TextField(blank=True, null=True)
#     principal_meet = models.IntegerField(blank=True, null=True)
#     robots_given = models.IntegerField(blank=True, null=True)
#     eyic_allowed = models.TextField(blank=True, null=True)
#     eyrtc_allowed = models.IntegerField(blank=True, null=True)
#     tbt_allowed = models.IntegerField(blank=True, null=True)
#     content_allowed = models.TextField(blank=True, null=True)
#     legal_docs = models.TextField(blank=True, null=True)
#     legal_docs_remarks = models.TextField(blank=True, null=True)
#     loi_status = models.IntegerField(blank=True, null=True)
#     loi_format = models.IntegerField(blank=True, null=True)
#     loi_remarks = models.TextField(blank=True, null=True)
#     po_status = models.TextField(blank=True, null=True)
#     po_remark = models.TextField(blank=True, null=True)
#     wo_reg = models.TextField(blank=True, null=True)
#     wo_invite = models.TextField(blank=True, null=True)
#     wo_confirm = models.TextField(blank=True, null=True)
#     wo_attend = models.IntegerField(blank=True, null=True)
#     hardware_given = models.TextField(blank=True, null=True)
#     lab_inaugurated = models.IntegerField(blank=True, null=True)
#     phase = models.TextField(blank=True, null=True)
#     eys2016_invites = models.TextField(blank=True, null=True)
#     team_verify = models.IntegerField(blank=True, null=True)
#     created_at = models.TextField(blank=True, null=True)
#     updated_at = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'elsi_college_dtls'


# class ElsiCompetitions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     year = models.TextField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     theme = models.TextField(blank=True, null=True)
#     phase = models.IntegerField(blank=True, null=True)
#     type = models.IntegerField(blank=True, null=True)
#     created_at = models.TextField(blank=True, null=True)
#     updated_at = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'elsi_competitions'


# class ElsiDepartments(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     main_branch = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'elsi_departments'


# class ElsiDesignations(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     type = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'elsi_designations'


# class ElsiState(models.Model):
#     id = models.IntegerField(primary_key=True)
#     code = models.TextField(blank=True, null=True)
#     state = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'elsi_state'


# class ElsiTeacherDtls(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.IntegerField(blank=True, null=True)
#     clg_id = models.IntegerField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     emailid = models.TextField(blank=True, null=True)
#     alt_email1 = models.TextField(blank=True, null=True)
#     alt_email2 = models.TextField(blank=True, null=True)
#     contact_num = models.TextField(blank=True, null=True)
#     alt_contact1 = models.TextField(blank=True, null=True)
#     department = models.TextField(blank=True, null=True)
#     designation = models.TextField(blank=True, null=True)
#     gender = models.TextField(blank=True, null=True)
#     coor_flag = models.IntegerField(blank=True, null=True)
#     wo_flag = models.IntegerField(blank=True, null=True)
#     workshop_id = models.IntegerField(blank=True, null=True)
#     wo_attendee = models.IntegerField(blank=True, null=True)
#     wo_count = models.IntegerField(blank=True, null=True)
#     eyrtc_flag = models.IntegerField(blank=True, null=True)
#     tbt_flag = models.IntegerField(blank=True, null=True)
#     eyic_flag = models.TextField(blank=True, null=True)
#     content_flag = models.TextField(blank=True, null=True)
#     status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
#     status_flag = models.TextField(blank=True, null=True)
#     modified_by = models.TextField(blank=True, null=True)
#     elsi_flag = models.TextField(blank=True, null=True)
#     remarks = models.TextField(blank=True, null=True)
#     login_created = models.TextField(blank=True, null=True)
#     created_at = models.TextField(blank=True, null=True)
#     updated_at = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'elsi_teacher_dtls'


# class NewScoring(models.Model):
#     id = models.IntegerField(primary_key=True)
#     elsi_clg_id = models.IntegerField(blank=True, null=True)
#     college_name = models.TextField(blank=True, null=True)
#     state = models.TextField(blank=True, null=True)
#     district = models.TextField(blank=True, null=True)
#     robots_given = models.IntegerField(blank=True, null=True)
#     eyrtc_allowed = models.IntegerField(blank=True, null=True)
#     tbt_allowed = models.IntegerField(blank=True, null=True)
#     completed = models.IntegerField(blank=True, null=True)
#     wo_attend = models.IntegerField(blank=True, null=True)
#     lab_inaugurated = models.IntegerField(blank=True, null=True)
#     score = models.FloatField(blank=True, null=True)

#     class Meta:
#         db_table = 'new_scoring'


# class ScoringCollegeWise(models.Model):
#     college_name = models.TextField(blank=True, null=True)
#     district = models.TextField(blank=True, null=True)
#     tbt_allowed = models.IntegerField(blank=True, null=True)
#     loi_status = models.IntegerField(blank=True, null=True)
#     wo_attend = models.IntegerField(blank=True, null=True)
#     lab_inaugurated = models.IntegerField(blank=True, null=True)
#     score = models.IntegerField(blank=True, null=True)

#     class Meta:
#         db_table = 'scoring_college_wise'




# class TbtCollegeDtls(models.Model):
#     id = models.IntegerField(primary_key=True)
#     elsi_clg_id = models.IntegerField(blank=True, null=True)
#     region_id = models.TextField(blank=True, null=True)
#     college_name = models.TextField(blank=True, null=True)
#     abbreviation = models.TextField(blank=True, null=True)
#     district = models.TextField(blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     state = models.TextField(blank=True, null=True)
#     pincode = models.TextField(blank=True, null=True)
#     college_type = models.TextField(blank=True, null=True)
#     principal_meet = models.IntegerField(blank=True, null=True)
#     robots_given = models.IntegerField(blank=True, null=True)
#     tbt_allowed = models.IntegerField(blank=True, null=True)
#     tbt_count = models.IntegerField(blank=True, null=True)
#     completed = models.IntegerField(blank=True, null=True)
#     legal_docs = models.IntegerField(blank=True, null=True)
#     legal_docs_remarks = models.TextField(blank=True, null=True)
#     loi_status = models.IntegerField(blank=True, null=True)
#     po_status = models.TextField(blank=True, null=True)
#     po_remark = models.TextField(blank=True, null=True)
#     wo_reg = models.TextField(blank=True, null=True)
#     wo_invite = models.TextField(blank=True, null=True)
#     wo_confirm = models.TextField(blank=True, null=True)
#     wo_attend = models.IntegerField(blank=True, null=True)
#     phase = models.TextField(blank=True, null=True)
#     lab_inaugrated = models.IntegerField(blank=True, null=True)
#     created_at = models.TextField(blank=True, null=True)
#     updated_at = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'tbt_college_dtls'


# class TbtStatusComplete(models.Model):
#     id = models.IntegerField(primary_key=True)
#     team_id = models.IntegerField(blank=True, null=True)
#     task0_noc = models.TextField(blank=True, null=True)
#     task1_status = models.TextField(blank=True, null=True)
#     task1_bonus_marks = models.TextField(blank=True, null=True)
#     task1_total_marks = models.TextField(blank=True, null=True)
#     task1_graded = models.TextField(blank=True, null=True)
#     task2_status = models.TextField(blank=True, null=True)
#     task2_bonus_marks = models.TextField(blank=True, null=True)
#     task2_total_marks = models.TextField(blank=True, null=True)
#     task2_graded = models.TextField(blank=True, null=True)
#     task3_status = models.TextField(blank=True, null=True)
#     task3_bonus_marks = models.TextField(blank=True, null=True)
#     task3_total_marks = models.TextField(blank=True, null=True)
#     task3_graded = models.TextField(blank=True, null=True)
#     task4_status = models.TextField(blank=True, null=True)
#     task4_bonus_marks = models.TextField(blank=True, null=True)
#     task4_total_marks = models.TextField(blank=True, null=True)
#     task4_graded = models.TextField(blank=True, null=True)
#     task5_status = models.TextField(blank=True, null=True)
#     task5_bonus_marks = models.TextField(blank=True, null=True)
#     task5_total_marks = models.TextField(blank=True, null=True)
#     task5_graded = models.TextField(blank=True, null=True)
#     task6_status = models.TextField(blank=True, null=True)
#     task6_bonus_marks = models.TextField(blank=True, null=True)
#     task6_total_marks = models.TextField(blank=True, null=True)
#     task6_graded = models.TextField(blank=True, null=True)
#     tbt_completed = models.IntegerField(blank=True, null=True)
#     award_grade = models.TextField(blank=True, null=True)
#     names_ok = models.TextField(blank=True, null=True)
#     bonus_task_downloaded = models.TextField(blank=True, null=True)
#     profile_photo_request = models.TextField(blank=True, null=True)
#     completed_in_days = models.TextField(blank=True, null=True)
#     created_at = models.TextField(blank=True, null=True)
#     updated_at = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'tbt_status_complete'


# class TbtTeacherDtls(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.IntegerField(blank=True, null=True)
#     tbt_clg_id = models.IntegerField(blank=True, null=True)
#     team_id = models.IntegerField(blank=True, null=True)
#     elsi_tch_id = models.IntegerField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     name_on_cheque = models.TextField(blank=True, null=True)
#     cheque_issued = models.TextField(blank=True, null=True)
#     account_number = models.TextField(blank=True, null=True)
#     account_holders_name = models.TextField(blank=True, null=True)
#     bank_name = models.TextField(blank=True, null=True)
#     bank_address = models.TextField(blank=True, null=True)
#     account_type = models.TextField(blank=True, null=True)
#     ifsc_code = models.TextField(db_column='IFSC_code', blank=True, null=True)  # Field name made lowercase.
#     bankdtl_added_date = models.TextField(blank=True, null=True)
#     emailid = models.TextField(blank=True, null=True)
#     alt_email1 = models.TextField(blank=True, null=True)
#     alt_email2 = models.TextField(blank=True, null=True)
#     contact_num = models.TextField(blank=True, null=True)
#     alt_contact1 = models.TextField(blank=True, null=True)
#     alt_contact2 = models.TextField(blank=True, null=True)
#     department = models.TextField(blank=True, null=True)
#     designation = models.TextField(blank=True, null=True)
#     gender = models.TextField(blank=True, null=True)
#     coor_flag = models.TextField(blank=True, null=True)
#     tbt_flag = models.IntegerField(blank=True, null=True)
#     submitted_to_office = models.TextField(blank=True, null=True)
#     submitted_to_cert_team = models.TextField(blank=True, null=True)
#     remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
#     login_created = models.TextField(blank=True, null=True)
#     profile_photo = models.TextField(blank=True, null=True)
#     created_at = models.TextField(blank=True, null=True)
#     updated_at = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'tbt_teacher_dtls'


# class TbtTeams(models.Model):
#     team_id = models.IntegerField(blank=True, null=True)
#     tbt_clg_id = models.IntegerField(blank=True, null=True)
#     tbt_phase = models.IntegerField(blank=True, null=True)
#     tl_id = models.IntegerField(blank=True, null=True)
#     tm1_id = models.IntegerField(blank=True, null=True)
#     tm2_id = models.IntegerField(blank=True, null=True)
#     tm3_id = models.IntegerField(blank=True, null=True)
#     year = models.TextField(blank=True, null=True)
#     created_at = models.TextField(blank=True, null=True)
#     updated_at = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'tbt_teams'


# class WorkshopDtls(models.Model):
#     id = models.IntegerField(primary_key=True)
#     region_id = models.IntegerField(blank=True, null=True)
#     clg_id = models.IntegerField(blank=True, null=True)
#     active = models.TextField(blank=True, null=True)
#     workshop_team = models.TextField(blank=True, null=True)
#     start_date = models.TextField(blank=True, null=True)
#     end_date = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'workshop_dtls'


# class WorkshopParticipants(models.Model):
#     id = models.IntegerField(primary_key=True)
#     workshop_id = models.IntegerField(blank=True, null=True)
#     clg_id = models.IntegerField(blank=True, null=True)
#     tch_id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'workshop_participants'