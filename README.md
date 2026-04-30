## Title
Pima Indians Diabetes Dataset

## Description
This dataset was originally collected by the National Institute of Diabetes and Digestive and Kidney Diseases in the United States. The purpose of the dataset is to predict whether a patient has diabetes or not based on certain medical measurements. All patients in this dataset are females, at least 21 years old and of Pima Indian heritage — a Native American population that has one of the highest rates of diabetes in the world.

## Column Description
**pregnancy** - This record shows how many times a patient has been pregnant, having multiple pregnacy can develop type2 diabetics.

**Glucose** - This indicate the level of glucose to be a dibetic patient(Normal glucose → below 140 mg/dL, Pre-diabetic → 140 to 199 mg/dL, Diabetic → 200 mg/dL and above)

**BloodPressure** - This is the diastolic blood pressure measured in millimetres of mercury (mm Hg). Normal blood pressure → below 80 mm Hg, High blood pressure → 80 mm Hg and above.

**SkinThickness** - This measures the thickness of the triceps skin fold in millimetres.

**Insulin** - This records the level of insulin in the blood after 2 hours measured in micro units per millilitre (mu U/ml). Normal insulin → 16 to 166 mu U/ml, Above 166 → abnormally high — possible insulin resistance.

**BMI** stands for Body Mass Index. It is calculated from a person's weight and height:BMI = weight (kg) / height (m)²

**DiabetesPedigreeFunction** - This is a score that measures how likely a person is to get diabetes based on their family history, Higher score → stronger family history of diabetes → higher risk, Lower score → weaker family history → lower risk

**Age** - This is the age of the patient in years.
Outcome - This is the target column — the answer your model is trying to predict

## Problem Solved
The problem to solved is, based on the patient medical measurement which is the columns does the patient has diabetics or not because of that i choose outcome to be my target because it has the answer yes=1, No=0, all other column are feature column that will help me predict the answer.
