# Create your models here.
from django.db import models


class JyrTable(models.Model):
    id = models.BigIntegerField(blank=True,primary_key=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    box_id = models.TextField(blank=True, null=True)
    machine_name = models.TextField(blank=True, null=True)
    controller_system_status = models.TextField(blank=True, null=True)
    controller_system_alarm = models.TextField(blank=True, null=True)
    axes_spindle_speed_command = models.TextField(blank=True, null=True)
    controller_path_feedrate_actual = models.TextField(blank=True, null=True)
    controller_path_program_mainno = models.TextField(blank=True, null=True)
    controller_time_power = models.TextField(blank=True, null=True)
    controller_time_cutting = models.TextField(blank=True, null=True)
    controller_time_operation = models.TextField(blank=True, null=True)
    axes_spindle_speed_override = models.TextField(db_column='axes_spindle_speed-override', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    controller_path_feedrate_override = models.TextField(blank=True, null=True)
    axes_spindle_speed_actual = models.TextField(blank=True, null=True)
    controller_time_cycle = models.TextField(blank=True, null=True)
    controller_path_feedrate_command = models.TextField(blank=True, null=True)
    controller_path_axes_servo_names = models.TextField(blank=True, null=True)
    tools_numbe_now = models.TextField(blank=True, null=True)
    controller_part_total = models.TextField(blank=True, null=True)
    controller_part_count = models.TextField(blank=True, null=True)
    controller_part_require = models.TextField(blank=True, null=True)
    controller_system_message = models.TextField(blank=True, null=True)
    controller_system_mode = models.FloatField(blank=True, null=True)
    controller_path_pos_absolute = models.TextField(blank=True, null=True)
    controller_path_pos_relative = models.TextField(blank=True, null=True)
    controller_path_pos_machine = models.TextField(blank=True, null=True)
    controller_path_pos_distance = models.TextField(blank=True, null=True)
    controller_path_program_block = models.TextField(blank=True, null=True)
    controller_path_program_runno = models.TextField(blank=True, null=True)
    controller_path_program_rowno = models.TextField(blank=True, null=True)
    controller_path_axes_count_max = models.TextField(blank=True, null=True)
    controller_path_axes_count_now = models.TextField(blank=True, null=True)
    controller_path_axes_names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jyr_table'

class Post(models.Model):
    
    
    machine_name = models.CharField(max_length=40,primary_key=True)
    state = models.IntegerField(null=True)
    part_count = models.IntegerField(null=True)
    starting_part_count = models.IntegerField(null=True)
    activation = models.IntegerField(null=True)
    code = models.CharField(null=True,max_length=30)
    
    state_array = models.CharField(null=True,max_length=1440)

    state_time = models.DateTimeField(null=True,blank=True)
    starting_time = models.DateTimeField(null=True,blank=True)
    fixtime = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.machine_name
    
    def save(self, *args, **kwargs):
        super(Post, self).save()
        print("save")


