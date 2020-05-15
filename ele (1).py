t=int(input("Enter No. of Tests : "))
for k in range(t):
	print("Enter no of volunteers : ")
	n=int(input())
	ele_names=[]
	a_count=[]
	for i in range(n):
		print("Enter name of the candidate : ")
		name=input();
		ele_names.append(name)
		a_count.append(len(name))

	max=a_count[0]
	index=0
	for i,j in enumerate(a_count):
		if(j>max):
			max=j
			index=i
	sp_array=[]
	flag=1
	for x in ele_names:
		if(len(x)==max):
			sp_array.append({"name":x,"unique":len(set(x))})

	if(len(sp_array)!=1):
		max_unique=sp_array[0]['unique']
		parray=[]
		for x in sp_array:
			if(x['unique']>max_unique):
				max_unique=x['unique']
		for x in sp_array:
			if(x['unique']==max_unique):
				parray.append(x['name'])
		if(len(parray)!=1):
			ff_winner=parray[0]
			for x in parray:
				if x<ff_winner:
					ff_winner=x
			print("Winner is "+ff_winner)
		else:
			print("Winner is "+parray[0])
	else:
		print("Winner is ",sp_array[0]['name'])



	