print('##############################################################################################')
print('                                  M A R K S H E E T                                           ')
print('##############################################################################################')
(input('Candidate Name: '))
(input('Father Name: '))
(input('Roll Number: '))

bio_marks = int(input('Please provide BIology Marks!'))
chem_marks = int(input('Please provide Chemistry Marks!'))
if bio_marks < 0 or bio_marks > 100:
    print('Invalid bio marks inoput')
if chem_marks < 0 or chem_marks> 100:
    print("Invalid chemistry marks inpout")