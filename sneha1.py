import random


Global = 1
output = []

def Ffunction(count):
	fvalue = abs((13*count)-170)
	return fvalue


def ones(ranvalues):

	j=0
	subcount=0
	while(j<40):
		if ranvalues[j] ==1:
			subcount=subcount+1
		j=j+1	
	return subcount


while(Global<=100):
	i=0
	count=0
	local=0
	ranvalues=[]
	nxtlst=[]

	for i in range(40):
		a=random.randint(0,1)
		ranvalues.append(a)
	count	= ones(ranvalues)
	print(count)
	f_value=Ffunction(count)
	print(f_value)	



	while(local==0):


		for k in range(count):
			random_value=random.randint(0,len(ranvalues)-1)
			print("random index for flipping  "+str(random_value)+"\n")
			if ranvalues[random_value]==1:
				ranvalues[random_value]=0
			else:
				ranvalues[random_value]=1
			nxtlst.append(ranvalues)
			count_new=ones(ranvalues)
			f_new	=Ffunction(count_new)
			if f_value < f_new:
				count=count_new
				f_value=f_new
				f_temp=f_value
			highest_fitness=f_value
		output.append(highest_fitness)
		local = 1            

	Global += 1


with open("output.txt", "w") as txt_file:
    for line in output:
        txt_file.write(str(line) + ",")