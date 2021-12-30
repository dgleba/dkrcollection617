from django.db import models

# Create your models here.

class Load_Spectrum(models.Model):
    load_spectrum_identification=              models.CharField(max_length=252, blank=True, default='', null=True)
    time_bin_hours_1=                          models.IntegerField(blank=True, null=True)
    speed_bin_1=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_1=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_2=                          models.IntegerField(blank=True, null=True)
    speed_bin_2=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_2=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_3=                          models.IntegerField(blank=True, null=True)
    speed_bin_3=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_3=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_4=                          models.IntegerField(blank=True, null=True)
    speed_bin_4=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_4=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_5=                          models.IntegerField(blank=True, null=True)
    speed_bin_5=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_5=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_6=                          models.IntegerField(blank=True, null=True)
    speed_bin_6=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_6=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_7=                          models.IntegerField(blank=True, null=True)
    speed_bin_7=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_7=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_8=                          models.IntegerField(blank=True, null=True)
    speed_bin_8=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_8=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_9=                          models.IntegerField(blank=True, null=True)
    speed_bin_9=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_9=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_10=                          models.IntegerField(blank=True, null=True)
    speed_bin_10=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_10=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_11=                          models.IntegerField(blank=True, null=True)
    speed_bin_11=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_11=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_12=                          models.IntegerField(blank=True, null=True)
    speed_bin_12=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_12=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_13=                          models.IntegerField(blank=True, null=True)
    speed_bin_13=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_13=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_14=                          models.IntegerField(blank=True, null=True)
    speed_bin_14=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_14=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_15=                          models.IntegerField(blank=True, null=True)
    speed_bin_15=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_15=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_16=                          models.IntegerField(blank=True, null=True)
    speed_bin_16=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_16=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_17=                          models.IntegerField(blank=True, null=True)
    speed_bin_17=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_17=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_18=                          models.IntegerField(blank=True, null=True)
    speed_bin_18=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_18=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_19=                          models.IntegerField(blank=True, null=True)
    speed_bin_19=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_19=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_20=                          models.IntegerField(blank=True, null=True)
    speed_bin_20=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_20=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_21=                          models.IntegerField(blank=True, null=True)
    speed_bin_21=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_21=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_22=                          models.IntegerField(blank=True, null=True)
    speed_bin_22=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_22=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_23=                          models.IntegerField(blank=True, null=True)
    speed_bin_23=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_23=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_24=                          models.IntegerField(blank=True, null=True)
    speed_bin_24=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_24=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_25=                          models.IntegerField(blank=True, null=True)
    speed_bin_25=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_25=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_26=                          models.IntegerField(blank=True, null=True)
    speed_bin_26=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_26=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_27=                          models.IntegerField(blank=True, null=True)
    speed_bin_27=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_27=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_28=                          models.IntegerField(blank=True, null=True)
    speed_bin_28=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_28=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_29=                          models.IntegerField(blank=True, null=True)
    speed_bin_29=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_29=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_30=                          models.IntegerField(blank=True, null=True)
    speed_bin_30=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_30=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_31=                          models.IntegerField(blank=True, null=True)
    speed_bin_31=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_31=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_32=                          models.IntegerField(blank=True, null=True)
    speed_bin_32=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_32=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_33=                          models.IntegerField(blank=True, null=True)
    speed_bin_33=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_33=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_34=                          models.IntegerField(blank=True, null=True)
    speed_bin_34=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_34=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_35=                          models.IntegerField(blank=True, null=True)
    speed_bin_35=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_35=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_36=                          models.IntegerField(blank=True, null=True)
    speed_bin_36=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_36=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_37=                          models.IntegerField(blank=True, null=True)
    speed_bin_37=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_37=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_38=                          models.IntegerField(blank=True, null=True)
    speed_bin_38=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_38=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_39=                          models.IntegerField(blank=True, null=True)
    speed_bin_39=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_39=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_40=                          models.IntegerField(blank=True, null=True)
    speed_bin_40=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_40=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_41=                          models.IntegerField(blank=True, null=True)
    speed_bin_41=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_41=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_42=                          models.IntegerField(blank=True, null=True)
    speed_bin_42=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_42=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_43=                          models.IntegerField(blank=True, null=True)
    speed_bin_43=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_43=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_44=                          models.IntegerField(blank=True, null=True)
    speed_bin_44=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_44=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_45=                          models.IntegerField(blank=True, null=True)
    speed_bin_45=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_45=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_46=                          models.IntegerField(blank=True, null=True)
    speed_bin_46=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_46=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_47=                          models.IntegerField(blank=True, null=True)
    speed_bin_47=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_47=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_48=                          models.IntegerField(blank=True, null=True)
    speed_bin_48=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_48=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    time_bin_hours_49=                          models.IntegerField(blank=True, null=True)
    speed_bin_49=                               models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    torque_bin_49=                              models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    sort_order = models.IntegerField(blank=True, null=True, default=50)
    active_status = models.IntegerField(blank=True, null=True, default=1)
    
    def __str__(self):
        return  str(self.id) + " - " + self.load_spectrum_identification + " - " + str(self.time_bin_hours_1)
        
class Material(models.Model):
    lable=                                     models.CharField(max_length=252, blank=True, default='')
    load_spectrums = models.ManyToManyField(Load_Spectrum)
    treatment_type=                            models.CharField(max_length=252, blank=True, default='')
    material_type=                             models.CharField(max_length=252, blank=True, default='')
    surface_hardness=                          models.CharField(max_length=252, blank=True, default='')
    surface_hardness_unit=                     models.CharField(max_length=252, blank=True, default='')
    core_hardness=                             models.CharField(max_length=252, blank=True, default='')
    core_hardness_unit=                        models.CharField(max_length=252, blank=True, default='')
    hardness_depth_mm=                         models.CharField(max_length=252, blank=True, default='')
    tensile_strength_N_per_mm2=                models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    yield_point_N_per_mm2=                     models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    youngs_modulus_N_per_mm2=                  models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    poissons_ratio=                            models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    density_kg_per_m3=                         models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    coefficient_of_therma_expansion_10e_6_per_c=models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    specific_heat_capacity_J_per_kg_k=         models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    specific_heat_conductivity_W_per_m_K=      models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    endurance_limit_root_N_per_mm2=            models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    endurance_limit_flank_N_per_mm3=           models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    quality_iso_6336_5=                        models.CharField(max_length=252, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    sort_order = models.IntegerField(blank=True, null=True, default=50)
    active_status = models.IntegerField(blank=True, null=True, default=1)
    
    def __str__(self):
        return  str(self.id) + " - " + self.lable


class Gear(models.Model):
    source=                                    models.CharField(max_length=252, blank=True, default='')
    materials = models.ManyToManyField(Material)
    gear_identification=                       models.CharField(max_length=252, blank=True, default='')
    data_approximated=                         models.BooleanField()
    gear_quality=                              models.IntegerField(blank=True, null=True)
    gear_supplier=                             models.CharField(max_length=252, blank=True, default='')
    number_of_teeth=                           models.IntegerField(blank=True, null=True)
    gear_type=                                 models.CharField(max_length=252, blank=True, default='')
    material_id=                               models.IntegerField(blank=True, null=True)
    normal_pressure_angle_deg=                 models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    gear_pitch_dia_mm=                         models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    face_width_mm=                             models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    gear_tip_dia_mm=                           models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    root_diameter=                             models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    assembled_to=                              models.CharField(max_length=252, blank=True, default='')
    assembled_type=                            models.CharField(max_length=252, blank=True, default='')
    tooth_thickness_tolerance=                 models.CharField(max_length=252, blank=True, default='')
    tangential_force_n=                        models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    contact_stress_mpa=                        models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    root_stress_mpa=                           models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    transverse_contact_ratio=                  models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    total_contact_ratio=                       models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    profile_crowning=                          models.IntegerField(blank=True, null=True)
    lead_crowning=                             models.IntegerField(blank=True, null=True)
    profile_angle_deviation_microm=            models.IntegerField(blank=True, null=True)
    helix_slope_deviation_microm=              models.IntegerField(blank=True, null=True)
    cumulative_pitch_error_microm=             models.CharField(max_length=252, blank=True, default='')
    total_composite_action_tolerance_microm=   models.CharField(max_length=252, blank=True, default='')
    profile_form_deviation_microm=             models.CharField(max_length=252, blank=True, default='')
    helix_slope_deviation_microm=              models.CharField(max_length=252, blank=True, default='')
    powder_metal=                              models.BooleanField()
    soft_machining=                            models.BooleanField()
    heat_treatment=                            models.BooleanField()
    sizing=                                    models.CharField(max_length=252, blank=True, default='')
    densification=                             models.BooleanField()
    hard_finishing=                            models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    sort_order = models.IntegerField(blank=True, null=True, default=50)
    active_status = models.IntegerField(blank=True, null=True, default=1)
    
    def __str__(self):
        return  str(self.id) + " - " + self.gear_identification

class Stage(models.Model):
    stage_identification=                      models.CharField(max_length=252, blank=True, default='', null=True)
    gears = models.ManyToManyField(Gear)
    source=                                    models.CharField(max_length=252, blank=True, default='')
    topology=                                  models.CharField(max_length=252, blank=True, default='')
    center_distance_mm=                        models.IntegerField(blank=True, null=True)
    module_mm=                                 models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    helix_angle_deg=                           models.IntegerField(blank=True, null=True)
    reduction_ratio=                           models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    input_shaft_bearing_configuration=         models.CharField(max_length=252, blank=True, null=True)
    output_shaft_bearing_configuration=        models.CharField(max_length=252, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    sort_order = models.IntegerField(blank=True, null=True, default=50)
    active_status = models.IntegerField(blank=True, null=True, default=1)
    
    def __str__(self):
        return  str(self.id) + " - " + self.stage_identification

class Application(models.Model):
    # one to many.. vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    # Gleba said to move the relationship to vehicles model...
    # vehicles = models.ManyToManyField(Vehicle)
    # vehicle_id = models.IntegerField(blank=True, null=True)
    application_identification = models.CharField(max_length=252, blank=True, default='')
    stages = models.ManyToManyField(Stage)
    source = models.CharField(max_length=252, blank=True, default='')
    application = models.CharField(max_length=252, blank=True, default='')
    pts_topology = models.CharField(max_length=252, blank=True, default='')
    num_speeds = models.CharField(max_length=252, blank=True, null=True)
    pts_supplier = models.CharField(max_length=252, blank=True, null=True)
    total_gear_ratio = models.CharField(max_length=252, blank=True, null=True)
    total_center_distance_mm = models.CharField(max_length=252, blank=True, null=True)
    differential_type = models.CharField(max_length=252, blank=True, null=True)
    pts_mass_kg = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    pts_length_mm = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    pts_width_mm = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    pts_height_mm = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    pts_power_density_kw_per_kg = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    pts_specific_power_kw_per_mm3 = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    kisssys_kisssoft_model_link = models.CharField(max_length=252, blank=True, null=True)
    load_spectrum_id = models.CharField(max_length=252, blank=True, null=True)
    lubrication = models.CharField(max_length=252, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sort_order = models.IntegerField(blank=True, null=True)
    active_status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return  str(self.id) + " - " + self.source +  " - " + self.application +  " - " +  self.pts_topology 




class Vehicle(models.Model):
    vehicle_identification = models.CharField(max_length=252, blank=True, default='')
    vehicle_maker = models.CharField(max_length=252, blank=True, default='')
    vehicle_model = models.CharField(max_length=252, blank=True, default='')
    applications = models.ManyToManyField(Application)
    vehicle_class_si_vehicle_segment = models.CharField(max_length=252, blank=True, null=True)
    maximum_speed_kph = models.BigIntegerField(blank=True, null=True)
    number_of_electric_motors = models.BigIntegerField(blank=True, null=True)
    max_motor_power_kw = models.IntegerField(db_column='max_ motor_power_kw', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    max_motor_torque_nm = models.BigIntegerField(blank=True, null=True)
    max_motor_speed_rpm = models.BigIntegerField(blank=True, null=True)
    source = models.CharField(max_length=252, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sort_order = models.IntegerField(blank=True, null=True)
    active_status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return  str(self.id) + " - " + self.vehicle_maker +  " - " + self.vehicle_model

    # class Meta:
    #     # managed = False
    #     db_table = 'ptsapp_vehicle'




