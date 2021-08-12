#importing libraries
import pandas as pd
from flask import Flask, render_template, request

#declare the app
app = Flask(__name__)

#start the app route which is '/'
@app.route('/', methods=['GET'])
#declare the main function
def main():
    return render_template('index.html')

#form submission route
@app.route('/score',methods=['POST'])
def score():
    #extract the data from post request
    HIG_Household_Count = float(request.form['HIG_Household_Count'])
    HIG_People_Count = float(request.form['HIG_People_Count'])
    LIG_Household_Count = float(request.form['LIG_Household_Count'])	
    LIG_People_Count = float(request.form['LIG_People_Count'])
    MIG_Household_Count = float(request.form['MIG_Household_Count'])
    MIG_People_Count = float(request.form['MIG_People_Count'])
    Clinic = float(request.form['Clinic'])
    Hospital = float(request.form['Hospital'])
    A = float(request.form['A'])
    B = float(request.form['B'])
    C = float(request.form['C'])
    Chemist_Stores = float(request.form['Chemist_Stores'])
    Monthly_Sale = float(request.form['Monthly_Sale'])
    Rent = float(request.form['Rent'])
    Sq_Ft = float(request.form['Sq_Ft'])
    
    ####
    Rent_per_Sq_Ft	= Rent / Sq_Ft
    bins= pd.cut(Rent_per_Sq_Ft, bins=[0,100,150,200,300,400,10000],labels=['0-99','100-149','150-199','200-299','300-399','above'],right=True)

    if bins == 0-99:
        target_HIG_Household_Count= 3297
        target_HIG_People_Count= 13199
        target_LIG_Household_Count=446
        target_LIG_People_Count=1786
        target_MIG_Household_Count= 5022
        target_MIG_People_Count= 20077
        target_Clinic= 74
        target_Hospital= 67
        target_A=75
        target_B=41
        target_C=23
        target_Chemist_Stores=41
        target_Monthly_Sale=6
        target_Rent=87884
    
    elif bins == 100-149:
        target_HIG_Household_Count= 4405
        target_HIG_People_Count= 17626	
        target_LIG_Household_Count=616
        target_LIG_People_Count=2467
        target_MIG_Household_Count= 6210
        target_MIG_People_Count= 24846
        target_Clinic= 80
        target_Hospital= 94
        target_A=94
        target_B=48
        target_C=28
        target_Chemist_Stores=45
        target_Monthly_Sale=7
        target_Rent=107305
    
    elif bins == 150-199:
        target_HIG_Household_Count= 6840
        target_HIG_People_Count= 27362
        target_LIG_Household_Count=403
        LIG_People_Count=1613
        target_MIG_Household_Count= 4071
        target_MIG_People_Count= 16287
        target_Clinic= 53
        target_Hospital= 88
        target_A=99
        target_B=21
        target_C=20
        target_Chemist_Stores=36
        target_Monthly_Sale=8
        target_Rent=162503
    
    elif bins == 200-299:
        target_HIG_Household_Count= 64983
        target_HIG_People_Count= 31044
        target_LIG_Household_Count=826
        LIG_People_Count=3304
        target_MIG_Household_Count= 4564
        target_MIG_People_Count= 18252
        target_Clinic= 55
        target_Hospital= 43
        target_A=37
        target_B=40
        target_C=16	
        target_Chemist_Stores=34
        target_Monthly_Sale=8
        target_Rent=159079

    elif bins == 300-399:
        target_HIG_Household_Count= 6736
        target_HIG_People_Count= 26941
        target_LIG_Household_Count=50
        LIG_People_Count=202
        target_MIG_Household_Count= 4990
        target_MIG_People_Count= 19165
        target_Clinic= 44
        target_Hospital= 42
        target_A=46
        target_B=23
        target_C=28
        target_Chemist_Stores=25
        target_Monthly_Sale=9
        target_Rent=298339

    else :
        target_HIG_Household_Count= 10741
        target_HIG_People_Count= 42949
        target_LIG_Household_Count=931
        LIG_People_Count=3725
        target_MIG_Household_Count= 3225
        target_MIG_People_Count= 12880
        target_Clinic= 88
        target_Hospital= 44
        target_A=74
        target_B=36
        target_C=18
        target_Chemist_Stores=30
        target_Monthly_Sale=13
        target_Rent=321899

    ###############

    if HIG_Household_Count <= target_HIG_Household_Count:
        score1=HIG_Household_Count/target_HIG_Household_Count*0.5*25
    else:
        score1=0.5*25
    if HIG_People_Count <= target_HIG_People_Count:
        score2=HIG_People_Count/target_HIG_People_Count*0.5*10
    else:
        score2=0.5*10
    if LIG_Household_Count <= target_LIG_Household_Count:
        score3=LIG_Household_Count/target_LIG_Household_Count*0.2*25
    else:
        score3=0.2*25
    if LIG_People_Count <= target_LIG_People_Count:
        score4=LIG_People_Count/LIG_People_Count*0.2*10
    else:
        score4=0.2*10
    if MIG_Household_Count <= target_MIG_Household_Count:
        score5=MIG_Household_Count/target_MIG_Household_Count.item()*0.3*25
    else:
        score5=0.3*25
    if MIG_People_Count <= target_MIG_People_Count:
        score6=MIG_People_Count/target_MIG_People_Count*0.3*10
    else:
        score6=0.3*10
    if Clinic <=  target_Clinic:
        score7=Clinic/target_Clinic*15
    else:
        score7=15
    if Hospital <=  target_Hospital:
        score8=Hospital/target_Hospital*10
    else:
        score8=10
    if A <=  target_A:
        score9=A/target_A*0.5*30
    else:
        score9=0.5*30
    if B <=  target_B:
        score10=B/target_B*0.3*30
    else:
        score10=0.3*30
    if C <=  target_C:
        score11=C/target_C*0.2*30
    else:
        score11=0.2*30
    if Chemist_Stores <=  target_Chemist_Stores:
        score12=Chemist_Stores/target_Chemist_Stores*5
    else:
        score12=5
    if Monthly_Sale <=  target_Monthly_Sale:
        score13=Monthly_Sale/target_Monthly_Sale*5
    else:
        score13=5


    
    final_score =score1+score2+score3+score4+score5+score6+score7+score8+score9+score10+score11+score12+score13


    return render_template('score.html', score = final_score)


if __name__ == "__main__":
    app.run(debug=True)
