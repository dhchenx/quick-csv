from quickcsv.file import *
# read a csv file
list_model=qc_read('data/test.csv')
for idx,model in enumerate(list_model):
    print(model)
    list_model[idx]['id']=idx
# save a csv file
qc_write('data/test1.csv',list_model)

# write a text file
qc_twrite('data/text1.txt',"Hello World!")
# read a text file
print(qc_tread('data/text1.txt'))

