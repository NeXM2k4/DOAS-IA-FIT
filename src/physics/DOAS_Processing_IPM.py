#Measurement variables
mai_pth='../DOAS_Test_Measurements/MAiZ_Mea_Tecapa_2025_11_26/'
#mai_pth=/mnt/PS/PS_Proyectos/2025_DataPrototypeMAiZ/MAiZ_Mea_Tecapa_2025_11_26/'
#mai_pth='/home/jcuadra/Downloads/MAiZ_Mea_Tecapa_2025_11_26/'
clb_pth=mai_pth+'Data_Calibration/'
ofs_pth=mai_pth+'Data_Offsets/'
ref_pth=mai_pth+'Data_Reference/'
mea_pth=mai_pth+'Data_Spectrum_Intensities/'
cnt_pth=mai_pth+'MAiZ_Measurements_Control_2025_11_26'
rlt_pth=mai_pth+'Data_Results/'
ofs_clr="green"
ref_clr="red"
mea_clr="blue"
mea_date="2025-11-26"
mea_sets=98
mea_azi=[0,30,60,90,120,150]
mea_ele=[0,15,30,60,75,90]
pix_num=3648
mea_wav_sta=350
mea_wav_end=750
mea_scns=3
mea_intg=1000000 #units in microseconds.

#OD fitler iir butter parameters
od_frq_sr=35 ##od_frq_sr=optical density frecuency samplerate. Float variable. Units in Hz.
od_lowcut=5 #od_lowcut=optical density lowcut. Float variable. Units in Hz.
od_highcut=15 #od_highcut=optical density highcut. Float variable. Units in Hz.
od_fctr_lwc=0.5 #od_fctr_hgc=optical density factor low cut. Float variable. No units.
od_fctr_hgc=0.5 #od_fctr_hgc=optical density factor high cut. Float variable. No units.
od_typ='band' #od_irf_typ=optical density IR frecuency type. String variable. No units.

#Calibration parameters
clbrtn_wav_sta=630#640#680#690
clbrtn_wav_end=645#685#705#700
clbrtn_db_pth="../Data_Calibration/"
clbrtn_db_fil="neon_limpio_air.txt"
clbrtn_lbl="Ne"
clbrtn_wav_scl=1e-1 #clbrtn_wav_scl=calibration wavelength scale. float variable. Scale factor and units arbitrary wavelegth to convert to nm.
clbrtn_wav_scl=1e-1 #clbrtn_wav_scl=calibration wavelength scale. float variable. Scale factor and units arbitrary wavelegth to convert to nm.
clbrtn_ofs_gss=250 #clbrtn_ofs_gss=calibration offset guess. Float variable. Units in a.u.
clbrtn_ofs_bnd=[-500,500] #clbrtn_ofs_bnd=calibration offset bound. Float list of [2] shape. Units in a.u.
clbrtn_shf_gss=-4 #clbrtn_shf_gss=calibration shift. Float variable. Units in nm.
clbrtn_shf_bnd=[-20,20] #clbrtn_shf_bnd=calibration shift bound=calibration shift. Float list of [2] shape. Units in nm.
clbrtn_amp_gss=0.2 #clbrtn_amp_gss=calibration amplitude guess. Float variable. Units in nm.
clbrtn_amp_bnd=[0.1,10] #clbrtn_amp_bnd=calibration amplitude bound. Float list of [2] shape. Units in nm.
clbrtn_wdt_gss=0.5 #clbrtn_wdt_gss=calibration width guess. Float variable. Units in nm.
clbrtn_wdt_bnd=[0.05,1] #clbrtn_wdt_gss=calibration width bound. Float list of [2] shape. Units in nm.

#Absorption Cross Sections (ACS) variables
gs_num=4
gs_clr=["purple","cyan","gold","lime","orange"]
gs_lab=["O4","CHOCHO","OClO","NO2","HONO"]
gs_lab_latex=[r"$\mathrm{O}_{4}$",r"$\mathrm{CHOCHO}$",r"$\mathrm{ClO}_{2}$",r"$\mathrm{NO}_{2}$",r"$\mathrm{HONO}$"]
gs_mm=[63.9960,58.0400,67.4500,46.0055,47.0130] #gas molar mass. List of float variables with dimentions [gs_num]. Units in g/mol
gs_acs_nts=[1.0e-4,1.0e-4,1.0e-4,1.0e-4,1.0e-4] #gas_acs_nts=gases absorption cross section units. List of float variables with dimention [gs_num]. Units in m2/molecules.
gs_acs_pth="../Data_Cross_Section/"
gs_acs_fil=[
    "O4_FinkenzellerVolkamer_2022",
    "CHOCHO_Bauerle_1998",
    "OClO_Bogumil_2003",
    "NO2_Burrows_1998",
    "HONO_Bongartz_1994",
    ]
gs_acs_inter_knd='cubic' #gas_acs_inter_knd=gas absorption cross section interpolation kind. String variable. No units.
gs_acs_inter_fv="extrapolate" #gas_acs_inter_fv=gas absorption cross section interpolation fill value. String variable. No units.

#Extintion Particulate Matter (EPM) variables
pm_num=1
pm_clr=["black"]
pm_ext_inter_knd='cubic' #pm_ext_inter_knd=particulate matter Extintion (coeficient) interpolation kind. String variable. No units.
pm_ext_inter_fv="extrapolate" #pm_ext_inter_fv=particulate matter Extintion (coeficient) interpolation fill value. String variable. No units.
pm_lab=["PM2.5","PM10"]
pm_mm=[30,80]
pm_lab_latex=[r"$\mathrm{PM}_{2.5}$",r"$\mathrm{PM}_{10}$"]

#Fit variables
fit_wav_sta=370
fit_wav_end=410
fit_slw_plynml=3
L_scl=1e3
C_scl=1e0
PM_scl=1e0
#Guesses
L_gss=12
CGs_gss=1e-5
ACS_shf_gss=0.5
ACS_sqz_gss=-0.001
ACS_bsl_gss=-0.5
CPM_gss=1e-5
EPM_shf_gss=0.5
EPM_sqz_gss=-0.001
EPM_bsl_gss=-0.5
#Bounds
L_bnds=[5,25]
CGs_bnds=[-1e3,1e3]
ACS_shf_bnds=[-15,15]
ACS_sqz_bnds=[-0.1,0.1]
ACS_bsl_bnds=[-0.8,0.8]
CPM_bnds=[-1e3,1e3]
EPM_shf_bnds=[-15,15]
EPM_sqz_bnds=[-0.1,0.1]
EPM_bsl_bnds=[-0.8,0.8]

#Saving paramenters
database_sep=","
database_dcmls=5
database_sep_spcr=3
database_sep_smbl=" "
database_pow_pstv=1/10
database_pow_ngtv=10
database_errcol="Error"
Pth_header="Path"
Pth_units="km"
Gs_headers=['Time','Con','SCD','Shift','Squeeze']#,'Baseline']
PM_headers=['Time','Con','Dis','Shift','Squeeze']#,'Baseline']
Gs_units=['HH:MM:SS','ug/m3','molecules/m2','nm','-']#,'ug/m3']
PM_units=['HH:MM:SS','ug/m3','molecules/m2','nm','-']#,'ug/m3']

#Terminal parameters
rtfit_prmtrsCM=['L']
rtfit_prmtrsGs=['Con','Shift','Squeeze']#,'Baseline']
rtfit_prmtrsPM=['Con','Shift','Squeeze']#,'Baseline']

#Plot parameters
#General settings
rfsh_wait=1
#Settings title
title_size=16
#Settings Calibration
clbrtn_xlbl="Wavelength (nm)"
clbrtn_ylbl="Calibration I (a.u.)"
clbrtn_clr=["orange","seagreen"]
clbrtn_lbl=[clbrtn_lbl+" measured",clbrtn_lbl+" fited"]
clbrtn_lw=2.0
clbrtn_ls="-"
clbrtn_fit_clr="gray"
clbrtn_fit_lw=1.5
clbrtn_fit_ls='-'
#Settings Offset Reference Measurement
orm_xlbl="Wavelength (nm)"
orm_ylbl="Intensity (a.u.)"
orm_lw=[4.0,4.0,4.0]
orm_ls=['-','-','-']
orm_lbl=["Offset","Reference","Measurement"]
orm_clr=["green","red","blue"]
#Settings Dirty Clean Slow Fast
dcsfr_xlbl="Wavelength (nm)"
dcsfr_ylbl="Optical Density"
dcsfr_lw=[4.0,4.0,4.0,4.0,4.0]
dcsfr_ls=['-','-','-','-','-']
dcsfr_lbl=["Dirty","Clean","Slow","Fast","remaining"]
dcsfr_clr=["coral","gray","orange","darkgreen","teal"]
#Settings for fit
fit_lw=2.0
fit_ls='-'
fit_lbl="Simulated OD"
fit_clr="gray"
rmng_xlbl="Wavelength (nm)"
rmng_ylbl="Remaining OD"
rmng_lbl="Remaining"
rmng_lw=2.0
rmng_ls='-'
rmng_lbl="Simulated OD"
rmng_clr="red"
#Settings for ACS Gas
acs_xlbl="Wavelength (nm)"
acs_ylbl=["ACS",r"$\left( \frac{ \mathrm{m}^{2} }{ \mathrm{molecules} } \right)$"]
acs_lbl=["Measured","Simulated"]
acs_clr=["coral","gray"]
acs_lw=2.0
acs_ls=['-','-']
#General setting for SCD, CGS, Ext, CPM
hms_rttn=60
rtfit_headersGs=['Time','Con','SCD','Shift','Squeeze']#,'Baseline']
rtfit_headersPM=['Time','Con','Dis','Shift','Squeeze']#,'Baseline']
rtfit_unitsGs=['HH:MM:SS','ug/m3','molecules/m2','nm','-']#,'ug/m3']
rtfit_unitsPM=['HH:MM:SS','ug/m3','molecules/m2','nm','-']#,'ug/m3']
rtfit_dcmls=5
#Settings for SCD y Con Gas
gscd_xlbl="Time (HH:MM:SS)"
gscd_ylbl=["SCD",r"$\left( \frac{ \mathrm{m}^{2} }{ \mathrm{molecules} } \right)$"]
gscd_lw=2.0
gscd_ls=['-',':','--','-.',(0,(1,1)),(0,(1,10)),(0,(5,1)),(0,(5,10)),(0,(3,1,1,1)),(0,(3,10,1,10))]
gscd_mk=[',','o','v','^','<','>','s','p','P','*']
gscd_mk_sz=8
gcon_xlbl="Time (HH:MM:SS)"
gcon_ylbl=["Con",r"$\left( \frac{ \mu\mathrm{g} }{ \mathrm{m}^{3} } \right)$"]
gcon_lw=2.0
gcon_ls=['-',':','--','-.',(0,(1,1)),(0,(1,10)),(0,(5,1)),(0,(5,10)),(0,(3,1,1,1)),(0,(3,10,1,10))]
gcon_mk=[',','o','v','^','<','>','s','p','P','*']
gcon_mk_sz=8
gcon_scl=1e6 #Convertion from g to ug
#Settings for EXT PM
#Settings for ACS Gas
ext_xlbl="Wavelength (nm)"
ext_ylbl=["Ext",r"$\left( \frac{ \mathrm{m}^{2} }{ \mathrm{molecules} } \right)$"]
ext_lw=2.0
ext_ls=['-','-']
ext_lbl=["Measured","Simulated"]
ext_clr=["coral","gray"]
#Settings for DIS PM
pmdis_xlbl="Time (HH:MM:SS)"
pmdis_ylbl=["Ext",r"$\left( \frac{ \mathrm{m}^{2} }{ \mathrm{molecules} } \right)$"]
pmdis_lw=2.0
pmdis_ls=['-',':','--','-.',(0,(1,1)),(0,(1,10)),(0,(5,1)),(0,(5,10)),(0,(3,1,1,1)),(0,(3,10,1,10))]
pmdis_mk=[',','o','v','^','<','>','s','p','P','*']
pmdis_mk_sz=8
pmcon_xlbl="Time (HH:MM:SS)"
pmcon_ylbl=["Con",r"$\left( \frac{ \mu\mathrm{g} }{ \mathrm{m}^{3} } \right)$"]
pmcon_lw=2.0
pmcon_ls=['-',':','--','-.',(0,(1,1)),(0,(1,10)),(0,(5,1)),(0,(5,10)),(0,(3,1,1,1)),(0,(3,10,1,10))]
pmcon_mk=[',','o','v','^','<','>','s','p','P','*']
pmcon_mk_sz=8
pmcon_scl=1e6 #Convertion from g to ug
#Automatic variables
mea_azi_num=len(mea_azi)
mea_ele_num=len(mea_ele)
clbrtn_num=0
