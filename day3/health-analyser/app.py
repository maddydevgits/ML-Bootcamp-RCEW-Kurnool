from flask import Flask,render_template,request

app=Flask(__name__)

import numpy as np
import pandas as pd

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
 l2.append(0)

df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X=df[l1]

y=df[["prognosis"]]
np.ravel(y)
# print(y)

tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

from sklearn import tree

clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
clf3 = clf3.fit(X,y)

from sklearn.metrics import accuracy_score
y_pred=clf3.predict(X_test)

from sklearn.ensemble import RandomForestClassifier
clf4 = RandomForestClassifier()
clf4 = clf4.fit(X,np.ravel(y))

from sklearn.metrics import accuracy_score
y_pred=clf4.predict(X_test)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb=gnb.fit(X,np.ravel(y))

from sklearn.metrics import accuracy_score
y_pred=gnb.predict(X_test)


@app.route('/')
def gets_connected():
 return(render_template('log.html'))

@app.route('/login',methods=['POST'])
def login_user():
 username=request.form['userid']
 password=request.form['pwd']
 if username=='admin' and password=='1234':
  return(render_template('reg.html'))
 else:
  return(render_template('log.html', err_log='Username and Password Invalid'))
 
@app.route('/evaluate',methods=['POST'])
def evaluate_user():
 name=request.form['name']
 aadhaar=request.form['aadhaar']
 district=request.form['district']
 village=request.form['village']
 phone = request.form['phone']
 age = request.form['age']
 gender=request.form['gender']
 symptoms=request.form['symptoms']
 symptoms=symptoms.split('\r\n')
 #print(symptoms)
 for k in range(0,len(l1)):
  for z in symptoms:
   if(z==l1[k]):
    l2[k]=1
 inputtest=[l2]
 predict=clf3.predict(inputtest)
 predicted=predict[0]
 h='no'
 for a in range(0,len(disease)):
  if(predicted==a):
   h='yes'
   break
 if(h=='yes'):
  #print(disease[a])
  h=disease[a]
 if (h=='Fungal infection'):
  medicines='Fluconazole tab ,  if chronic - voriconazole tab (Fungal Infection)'
 elif(h=='Allergy'):
  medicines='Cetrizine tab ,  Levocetrizine tab ,  Loratidine tab, '
 elif(h=='GERD'):
  medicines='Raveprazole tab ,  Lansoprazole tab ,  Esomeprazole tab ,  Dexlansoprazole tab'
 elif(h=='Chronic cholestasis'):
  medicines='Piparcillin tazobactum injection'
 elif(h=='Drug Reaction'):
  medicines='Avil tab'
 elif(h=='Peptic ulcer diseae'):
  medicines='Raveprazole tab ,  Lansoprazole tab ,  Esomeprazole tab ,  Dexlansoprazole tab'
 elif(h=='AIDS'):
  medicines='Dolutegravir tab ,  Antiretroviral drug ,  Tenofovar tab ,  Lamivudine tab ,  Triomune tab ,  Darunavir tab'
 elif(h=='Diabetes'):
  medicines='Glimepride tab ,  Metformin tab ,  Gliclazide tab'
 elif(h=='Gastroenteritis'):
  medicines='Raveprazole tab \r,  Lansoprazole tab \r,  Esomeprazole tab \r,  Dexlansoprazole tab'
 elif(h=='Bronchial Asthma'):
  medicines='Doxiffillin tab ,  Levosolbutomol Bromexyne syrup ,  Asebrofithillin tab ,  Theophylline tab ,  Buducorte inhaler ,  Foracorte Forte inhaler'
 elif(h=='Hypertension'):
  medicines='Amlodipine tab ,  Ditiazem tab ,  Isravipine tab ,  Nicardipine tab ,  Verapimil tab'
 elif(h=='Migraine'):
  medicines='Paracetamol tab ,  Naproxen tab'
 elif(h=='Cervical spondylosis'):
  medicines='Indomethacin tab ,  Piroxicam tab ,  Naproxen tab ,  Methylpregnisolin tab ,  Ibuprofin tab ,  Baclofen tab ,  Cyclobenzaprine tab ,  Aceclophenac'
 elif(h=='Paralysis (brain hemorrhage)'):
  medicines='Anafranil tab ,  Clomipranime tab ,  methylphenidate tab'
 elif(h=='Jaundice'):
  medicines='Live52 tab'
 elif(h=='Malaria'):
  medicines='Ivermectin tab ,  Chloroquine Phosphate tab ,  Larinate 200mg tab ,  injections 60mg, ,  Mefloquine Artesunate tab'
 elif(h=='Chicken pox'):
  medicines='Immune System ,  Acyclovir tab 800mg ,  Valacyclovir tab'
 elif(h=='Dengue'):
  medicines='Paracetamol ,  Aspirin ,  Immune System'
 elif(h=='Typhoid'):
  medicines='Ciprofloxacin tab ,  Oflaxacin tab ,  Norflaxacin tab ,  Amoxycillin Clavu 625mg tab ,  Levofloxacin tab'
 elif(h=='hepatitis A'):
  medicines='Get Doctor Prescription'
 elif(h=='Hepatitis B'):
  medicines='Get Doctor Prescription'
 elif(h=='Hepatitis C'):
  medicines='Get Doctor Prescription'
 elif(h=='Hepatitis D'):
  medicines='Get Doctor Prescription'
 elif(h=='Hepatitis E'):
  medicines='Get Doctor Prescription'
 elif(h=='Alcoholic hepatitis'):
  medicines='Metadoxine tab'
 elif(h=='Tuberculosis'):
  medicines='Ethambutol tab ,  Pyrazinamide tab ,  Cycloserine tab ,  Ethionamide tab ,  Levofloxacin tab ,  Kanamycan tab'
 elif(h=='Common Cold'):
  medicines='Immune System ,  Phenylephrine Hydrochloride + Chlorpheniramine Malete tab ,  Levocetrizine tab ,  Cetrizine tab'
 elif(h=='Pneumonia'):
  medicines='Azithromycin tab ,  Linezolid tab ,  Delafloxacin tab Clindamycin tab ,  Doxycycline tab ,  Ertapenem tab ,  Lincosamide tab'
 elif(h=='Dimorphic hemmorhoids(piles)'):
  medicines='Pilex tab ,  Pilenil tab'
 elif(h=='Heart attack'):
  medicines='Sorbitrate tab'
 elif(h=='Varicose veins'):
  medicines='Polydocanal Injection ,  Sodium Tetradecyl Sulphate Injection ,  Ibuprofin tab ,  Paracetomal tab'
 elif(h=='Hypothyroidism'):
  medicines='Levothyroxine Soduim tab ,  Pyridoxin Hydrochloride sustained released tab ,  Tirosint capsules ,  Levoxyl tab ,  Synthroid tab ,  Unithroid tab'
 elif(h=='Hyperthyroidism'):
  medicines='Levothyroxine Soduim tab ,  Pyridoxin Hydrochloride sustained released tab ,  Tirosint capsules ,  Levoxyl tab ,  Synthroid tab ,  Unithroid tab'
 elif(h=='Hypoglycemia'):
  medicines='Glucose tab'
 elif(h=='Osteoarthristis'):
  medicines='Glucosamine Sulphate tab ,  Ibuprofin tab ,  Naproxen tab'
 elif(h=='Arthritis'):
  medicines='Glucosamine Sulphate tab ,  Ibuprofin tab ,  Naproxen tab'
 elif(h=='(vertigo) Paroymsal  Positional Vertigo'):
  medicines='Sinarzine tab ,  Flunarzine tab'
 elif(h=='Acne'):
  medicines='Clindamycin Phosphate & Nicotinamde Gel ,  Adapalene Benzylperoxide Gel '
 elif(h=='Urinary tract infection'):
  medicines='Oflaxacin tab ,  Norfloxacin tab ,  Siprofloxacin tab ,  Tinidazole tab'
 elif(h=='Psoriasis'):
  medicines='Aloe vera creams ,  White soft paraffin Gel  ,  Flucanazole tab (Optional if itchy) ,  Clobetasole Propionite and Salicylicacid Gel'
 elif(h=='Impetigo'):
  medicines='Mupirosin Ointment ,  Retamulin Ointment ,  Amoxycillin Potassium Clavunate'
 return (render_template('out.html',medicines=medicines,disease_details=h,fname=name,adhaar=aadhaar,district=district,village=village,phone=phone,age=age,gender=gender))

if __name__=="__main__":
 app.run(debug=True)