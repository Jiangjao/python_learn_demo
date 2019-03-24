# with open("C:/Users/Cherry/Desktop/game/ex26.py") as file:  
#     data = file.read()
#     print(data)

#	create	a	mapping	of	state	to	abbreviation 
# states = {'Oregon':'OR',
#                 'Florida':'FL',
#                 'California':'CA',
#                 'New York':	'NY',
#                 'Michigan':'MI' }

# #	create	a	basic	set	of	states	and	some	cities	in	them 
# cities =	{'CA':	'San	Francisco',	
#                 'MI':	'Detroit',
#                 'FL':	'Jacksonville' }
# #	add	some	more	cities 
# cities['NY'] =	'New York' 
# cities['OR'] =	'Portland'
# #	print	out	some	cities
# print('-' * 10 )	
# print("NY State has: ",	cities['NY'])	
# print("OR State has: ",	cities['OR'])	
# #	print	some	states 
# print('-' *	10)	 
# print("Michigan's	abbreviation	is:	",	states['Michigan'])	 
# print("Florida's	abbreviation	is:	",	states['Florida'])	
# #	do	it	by	using	the	state	then	cities	dict 
# print('-' * 10)	
# print("Michigan	has:	",	cities[states['Michigan']] )
# print("Florida	has:	",	cities[states['Florida']])	
# #	print	every	state	abbreviation 
# print('-' * 10)	 
# for	state,	abbrev	in	states.items():				
#     print("%s	is	abbreviated	%s"	%	(state,	abbrev))	
# #	print	every	city	in	state
# print('-' *	10)	 
# for	abbrev,	city	in	cities.items():				
#     print("%s	has	the	city	%s"	%	(abbrev,	city))	
# #	now	do	both	at	the	same	time 
# print('-' * 10)	 
# for	state,	abbrev	in	states.items():				
#     print("%s state	is	abbreviated	%s	and	has	city	%s"	%	(state,	abbrev,	cities[abbrev]))	
# print('-' * 10)	 
# #	safely	get	a	abbreviation	by	state	that	might	not	be	there 
# state = states.get('Texas')
# if	not	state:				
#     print("Sorry, no Texas.")	
# #	get	a	city	with	a	default	value 
# city = cities.get('TX',	'Does Not Exist') 
# print("The city for	the	state 'TX' is:	%s"	% city)	

# import hashmap
# #	create	a	mapping	of	state	to	abbreviation 
# states = hashmap.new()
# hashmap.set(states,	'Oregon',	'OR')
# hashmap.set(states,	'Florida',	'FL') 
# hashmap.set(states,	'California',	'CA') 
# hashmap.set(states,	'New	York',	'NY') 
# hashmap.set(states,	'Michigan',	'MI')
# #	create	a	basic	set	of	states	and	some	cities	in	them 
# cities	=	hashmap.new() 
# hashmap.set(cities,	'CA', 'San	Francisco') 
# hashmap.set(cities,	'MI', 'Detroit') 
# hashmap.set(cities,	'FL', 'Jacksonville')
# #	add	some	more	cities 
# hashmap.set(cities,	'NY', 'New	York') 
# hashmap.set(cities,	'OR', 'Portland')
# hashmap.set(cities,'Jz', 'Jin zhou');
# #	print	out	some	cities 
# print('-' * 10)	

# print("NY	State	has:	%s"	%	hashmap.get(cities,	'NY'))	 
# print("OR	State	has:	%s"	%	hashmap.get(cities,	'OR'))	

# #	print	some	states 
# print('-'	*	10)	 
# print("Michigan's	abbreviation	is:	%s"	%	hashmap.get(states,	'Michigan'))	 
# print("Florida's	abbreviation	is:	%s"	%	hashmap.get(states,	'Florida'))	

# #	do	it	by	using	the	state	then	cities	dict 
# print('-'	*	10)	 
# print("Michigan	has:	%s"	%	hashmap.get(cities,	hashmap.get(states,	'Michigan')))	 
# print("Florida	has:	%s"	%	hashmap.get(cities,	hashmap.get(states,	'Florida')))	

# #	print	every	state	abbreviation 
# print('-' * 10, hashmap.list(states))	

# #	print	every	city	in	state 
# print('-' *	10, hashmap.list(cities))	
# print('-' *	10 )
# state =	hashmap.get(states,	'Texas')	
# if	not	state:		
#     print("Sorry, no Texas.")	

# #	default	values	using	||=	with	the	nil	result #	can	you	do	this	on	one	line? 
# city = hashmap.get(cities, 'TX', 'Does	Not	Exist') 
# print("The city for	the	state 'TX'	is:	%s"	% city)	
# print("-" *20)
# print(hashmap.dump(states))

# class MyStuff(object):
#     def	__init__(self):
#         self.tangerine	=	"And	now	a	thousand	years	between"

#     def	apple(self):
#         print("I	AM	CLASSY	APPLES!")	

# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)

# class	Song(object):
#     def	__init__(self, lyrics):
#         self.lyrics = lyrics
        
#     def	sing_me_a_song(self):
#         for	line in	self.lyrics:												
#             print(line)

#     def LenofSong(self):
#         print(len(self.lyrics))	

# aa=["Happy	birthday	to	you",
#                         "I	don't	want	to	get	sued",																			
#                         "So	I'll	stop	right	there"]
# happy_bday	=	Song(aa)
# bulls_on_parade	=	Song(["They	rally	around	tha	family",																								
#                             "With	pockets	full	of	shells"])

# happy_bday.sing_me_a_song()

# happy_bday.LenofSong()

# bulls_on_parade.sing_me_a_song()

# import	random 
# from urllib import urlopen 
# import	sys
# WORD_URL	=	"http://learncodethehardway.org/words.txt" 
# WORDS	=	[]
# PHRASES	=	{	"class	%%%(%%%):":						
#             "Make	a	class	named	%%%	that	is-a	%%%.",				
#             "class	%%%(object):\n\tdef	__init__(self,	***)"	:						
#             "class	%%%	has-a	__init__	that	takes	self	and	***	parameters.",				
#             "class	%%%(object):\n\tdef	***(self,	@@@)":						
#             "class	%%%	has-a	function	named	***	that	takes	self	and	@@@	parameters.",				"***	=	%%%()":						"Set	***	to	an	instance	of	class	%%%.",				"***.***(@@@)":						"From	***	get	the	***	function,	and	call	it	with	parameters	self,	@@@.",				"***.***	=	'***'":
#             "From	***	get	the	***	attribute	and	set	it	to	'***'."   }

# #	do	they	want	to	drill	phrases	first 
# if	len(sys.argv)	==	2	and	sys.argv[1]	==	"english":				
#     PHRASE_FIRST	=	True 
# else:				
#     PHRASE_FIRST	=	False

# #	load	up	the	words	from	the	website 
# for	word in	urlopen(WORD_URL).readlines():				
#     WORDS.append(word.strip())


# def	convert(snippet,	phrase):				
#     class_names	=	[w.capitalize()	for	w	in
#     			    random.sample(WORDS,	snippet.count("%%%"))]
#     other_names	=	random.sample(WORDS,	snippet.count("***"))
#     results	=	[]
#     param_names	=	[]

#     for	i	in	range(0,	snippet.count("@@@")):								
#         param_count	=	random.randint(1,3)								
#         param_names.append(',	'.join(random.sample(WORDS,	param_count)))
        
#     for	sentence in snippet, phrase:
#         result = sentence[:]

# 		#	fake	class	names								
#         for	word in	class_names:												
#             result	=	result.replace("%%%",	word,	1)

# 	    #	fake	other	names								
#         for	word	in	other_names:												
#             result	=	result.replace("***",	word,	1)

# 	    #	fake	parameter	lists								
#         for	word	in	param_names:												
#             result	=	result.replace("@@@",	word,	1)
#         results.append(result)
#     return	results

# #	keep	going	until	they	hit	CTRL-D 
# try:				
#     while	True:								
#         snippets	=	PHRASES.keys()								
#         random.shuffle(snippets)
#         for	snippet	in	snippets:
#             phrase	=	PHRASES[snippet]												
#             question,	answer	=	convert(snippet,	phrase)												
#         if	PHRASE_FIRST:																
#             question,	answer	=	answer,	question
        
#         print(question)	
#         input("> ")												
#         print("ANSWER: %s\n\n" % answer)
# except	EOFError:				
#     print("\nBye")		


##	Animal	is-a	object	(yes,	sort	of	confusing)	look	at	the	extra	credit 
# class	Animal(object):				
#     pass

# ##	?? 
# class	Dog(Animal):

# 	def	__init__(self,	name):								
#         ##	??
#             self.name	=	name

# ##	?? 
# class	Cat(Animal):
#     def	__init__(self,	name):								
#         ##	??
#         self.name	=	name

# ##	?? 
# class	Person(object):
#     def	__init__(self,	name):								
#         ##	??
#         self.name	=	name
# 		##	Person	has-a	pet	of	some	kind
#         self.pet	=	None

# ##	?? 
# class	Employee(Person):
#     def	__init__(self,	name,	salary):								
#         ##	??	hmm	what	is	this	strange	magic?
#         super(Employee,	self).__init__(name)								
#         ##	??								
#         self.salary	=	salary

# ##	?? 
# class	Fish(object):				
#     def __init__(self):
#         print("Hi I'm a fish")
# ##	?? 
# class	Salmon(Fish):				
#     def __init__(self):
#         print("Hello jic")
# ##	?? 
# class	Halibut(Fish):				
#     pass

# ##	rover	is-a	Dog 
# rover	=	Dog("Rover")
# ##	?? 
# satan	=	Cat("Satan")
# ##	?? 
# mary	=	Person("Mary")
# ##	?? 
# mary.pet	=	satan
# ##	?? 
# frank	=	Employee("Frank",	120000)
# ##	?? 
# frank.pet	=	rover
# ##	?? 
# flipper	=	Fish()
# ##	?? 
# crouse	=	Salmon()
# ##	?? 
# harry	=	Halibut()

# from	sys	import	exit 
# from	random	import	randint

# class	Scene(object):
# 	def	enter(self):
#             print("This	scene is not yet configured. Subclass it and implement enter().")									
#             exit(1)


# class	Engine(object):
# 	def	__init__(self,	scene_map):
#             self.scene_map	=	scene_map
# 	def	play(self):
#             current_scene	=	self.scene_map.opening_scene()								
#             last_scene	=	self.scene_map.next_scene('finished')

#             while current_scene	!=	last_scene:												
#                 next_scene_name	=	current_scene.enter()												
#                 current_scene	=	self.scene_map.next_scene(next_scene_name)
# #	be	sure	to	print	out	the	last	scene								
#             current_scene.enter()

# class	Death(Scene):								
#     quips =	["You	died. You kinda	suck at	this.",									
#                 "Your mom	would	be	proud...if	she	were smarter.",									
#                 "Such a	luser.",									
#                 "I	have a small puppy that's better at this."]

#     def	enter(self):								
#             print(Death.quips[randint(0,	len(self.quips)-1)])									
#             exit(1)


# class	CentralCorridor(Scene):
#     def	enter(self):								
#         print("The Gothons	of Planet Percal	#25	have invaded your ship and destroyed")									
#         print("your	entire crew. You are the last surviving	member and your last")									
#         print("mission is to get the neutron destruct bomb from the	Weapons	Armory,")									
#         print("put	it	in	the	bridge,	and	blow the ship up after getting into an ")									
#         print("escape pod.")									
#         print("\n")									
#         print("You're running down the central corridor	to the Weapons Armory when")									
#         print("a Gothon	jumps out, red scaly skin, dark	grimy teeth, and evil clown	costume")									
#         print("flowing around his hate filled body. He's blocking the door to the")									
#         print("Armory and about	to	pull a weapon to blast you.")

#         action = input(" > ")

#         if	action	==	"shoot!":												
#             print("Quick on	the	draw you yank out your blaster and fire	it at the Gothon.")													
#             print("His	clown costume	is	flowing	and	moving	around	his	body, which throws")													
#             print("off	your aim.Your laser	hits hi costume	but	misses	him	entirely.This")													
#             print("completely ruins his	brand new costume his mother bought	him, which")													
#             print("makes him fly into an insane	rage and blast you repeatedly in the face until")													
#             print("you	are	dead.Then he eats you.")													
#             return	'death'

#         elif	action	==	"dodge!":												
#             print("Like	a world class boxer	you	dodge,	weave,	slip and slide right")													
#             print("as the Gothon's blaster	cranks	a laser past your head.")													
#             print("In the middle of	your artful	dodge your foot slips and	you")													
#             print("bang	your head on the metal	wall and	pass out.")													
#             print("You	wake up	shortly	after only to die as the Gothon	stomps on")													
#             print("your	head and eats you.")													
#             return	'death'
        
#         elif	action	==	"tell	a	joke":												
#             print("Lucky for you they made you learn Gothon insults	in	the	academy.")													
#             print("You	tell the one Gothon	joke you know:")													
#             print("Lbhe	zbgure	vf	fb	sng, jura fur	fvgf nebhaq	gur	ubhfr,	fur	fvgf	nebhaq	gur	ubhfr.")													
#             print("The	Gothon	stops,	tries	not	to	laugh,	then	busts	out	laughing	and	can't	move.")													
#             print("While	he's	laughing	you	run	up	and	shoot	him	square	in	the	head")													
#             print("putting	him	down,	then	jump	through	the	Weapon	Armory	door.")													
#             return	'laser_weapon_armory'

#         else:												
#             print("DOES	NOT	COMPUTE!")													
#             return	'central_corridor'

# class	LaserWeaponArmory(Scene):
# 	def	enter(self):								
#             print("You	do	a	dive	roll	into	the	Weapon	Armory,	crouch	and	scan	the	room")									
#             print("for	more	Gothons	that	might	be	hiding.		It's	dead	quiet,	too	quiet.")									
#             print("You	stand	up	and	run	to	the	far	side	of	the	room	and	find	the")									
#             print("neutron	bomb	in	its	container.		There's	a	keypad	lock	on	the	box")									
#             print("and	you	need	the	code	to	get	the	bomb	out.	If	you	get	the	code")									
#             print("wrong	10	times	then	the	lock	closes	forever	and	you	can't")									
#             print("get	the	bomb.The code	is	3	digits.")									
#             code	=	"%d%d%d"	%	(randint(1,9),	randint(1,9),	randint(1,9))								
#             guess	=	input("[keypad]> ")								
#             guesses	=	0

#             while	guess	!=	code	and	guesses	< 10:												
#                 print("BZZZZEDDD!")													
#                 guesses	+=	1												
#                 guess	= input("[keypad]> ")

#             if	guess	==	code:												
#                 print("The	container	clicks	open	and	the	seal	breaks,	letting	gas	out.")													
#                 print("You	grab	the	neutron	bomb	and	run	as	fast	as	you	can	to	the")													
#                 print("bridge	where	you	must	place	it	in	the	right	spot.")													
#                 return	'the_bridge'								
#             else:												
#                 print("The	lock	buzzes	one	last	time	and	then	you	hear	a	sickening")													
#                 print("melting	sound	as	the	mechanism	is	fused	together.")													
#                 print("You	decide	to	sit	there,	and	finally	the	Gothons	blow	up	the")													
#                 print("ship	from	their	ship	and	you	die.")													
#                 return	'death'


# class	TheBridge(Scene):
#     def	enter(self):
#         print("You	burst	onto	the	Bridge	with	the	netron	destruct	bomb")									
#         print("under	your	arm	and	surprise	5	Gothons	who	are	trying	to")									
#         print("take	control	of	the	ship.		Each	of	them	has	an	even	uglier")									
#         print("clown	costume	than	the	last.		They	haven't	pulled	their")									
#         print("weapons	out	yet,	as	they	see	the	active	bomb	under	your")									
#         print("arm	and	don't	want	to	set	it	off.")
        
#         action = input(" > ")

#         if	action	==	"throw	the	bomb":												
#             print("In	a	panic	you	throw	the	bomb	at	the	group	of	Gothons")													
#             print("and	make	a	leap	for	the	door.		Right	as	you	drop	it	a")													
#             print("Gothon	shoots	you	right	in	the	back	killing	you.")													
#             print("As	you	die	you	see	another	Gothon	frantically	try	to	disarm")													
#             print("the	bomb.	You	die	knowing	they	will	probably	blow	up	when")													
#             print("it	goes	off.")													
#             return	'death'

#         elif	action	==	"slowly	place	the	bomb":												
#             print("You	point	your	blaster	at	the	bomb	under	your	arm")													
#             print("and	the	Gothons	put	their	hands	up	and	start	to	sweat.")													
#             print("You	inch	backward	to	the	door,	open	it,	and	then	carefully")													
#             print("place	the	bomb	on	the	floor,	pointing	your	blaster	at	it.")													
#             print("You	then	jump	back	through	the	door,	punch	the	close	button")													
#             print("and	blast	the	lock	so	the	Gothons	can't	get	out.")													
#             print("Now	that	the	bomb	is	placed	you	run	to	the	escape	pod	to")													
#             print("get	off	this	tin	can.")													
#             return	'escape_pod'
        
#         else:												
#             print("DOES	NOT	COMPUTE!")													
#             return	"the_bridge"

# class	EscapePod(Scene):
#     def	enter(self):
#         print("You	rush	through	the	ship	desperately	trying	to	make	it	to")									
#         print("the	escape	pod	before	the	whole	ship	explodes.		It	seems	like")									
#         print("hardly	any	Gothons	are	on	the	ship,	so	your	run	is	clear	of")	
#         print("interference.		You	get	to	the	chamber	with	the	escape	pods,	and")									
#         print("now	need	to	pick	one	to	take.		Some	of	them	could	be	damaged")									
#         print("but	you	don't	have	time	to	look.		There's	5	pods,	which	one")									
#         print("do	you	take?")	
#         good_pod	=	randint(1,5)
#         guess	=	input("[pod	#]>	")

#         if	int(guess)	!=	good_pod:												
#             print("You	jump	into	pod	%s	and	hit	the	eject	button."	%	guess)													
#             print("The	pod	escapes	out	into	the	void	of	space,	then")													
#             print("implodes	as	the	hull	ruptures,	crushing	your	body")													
#             print("into	jam	jelly.")
#             return	'death'
#         else:												
#             print("You	jump	into	pod	%s	and	hit	the	eject	button."	%	guess)													
#             print("The	pod	easily	slides	out	into	space	heading	to")													
#             print("the	planet	below.		As	it	flies	to	the	planet,	you	look")													
#             print("back	and	see	your	ship	implode	then	explode	like	a")													
#             print("bright	star,	taking	out	the	Gothon	ship	at	the	same")													
#             print("time.		You	won!")
#             return	'finished'

# class	Finished(Scene):
#     def	enter(self):								
#         print("You	won!	Good	job.")									
#         return	'finished'


# class	Map(object):
#     scenes	=	{'central_corridor':	CentralCorridor(),								
#        'laser_weapon_armory':	LaserWeaponArmory(),								
#        'the_bridge':	TheBridge(),								
#        'escape_pod':	EscapePod(),								
#        'death':	Death(),								
#        'finished':	Finished(),}

#     def	__init__(self,	start_scene):
#         self.start_scene	=	start_scene
    
#     def	next_scene(self,	scene_name):
#         val	=	Map.scenes.get(scene_name)								
#         return	val

#     def	opening_scene(self):								
#         return	self.next_scene(self.start_scene)


# a_map  = Map('central_corridor') 
# a_game = Engine(a_map) 
# a_game.play()

# class Parent(object):

#     def implicit(self):
#         print("PARENT implicit")

#     def altered(self):
#         print("PARENT altered()")
    
# class Child(Parent):
#     def implicit(self):
#         print("CHILD implicit")

#     def altered(self):
#         print("CHILD ,BEFORE PARENT altered") 
#         super(Child, self).altered()
#         print("CHILD ,AFTER PARENT altered")

# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()

# class Other(object):
#     def override(self):
#         print("OTHER override()")
    
#     def implicit(self):
#         print("OTHER implicit()")
    
#     def altered(self):
#         print("OTHER altered()")

# class  Child(object):

#     def __init__(self):
#         self.other = Other()
    
#     def implicit(self):
#         self.other.implicit()

#     def override(self):
#         print("CHILD override")

#     def altered(self):
#         print("CHILD, BEFORE OTHER altered()")
#         self.other.altered()
#         print("CHILD, AFTER OTHER altered()")

# son = Child()

# son.implicit()
# son.override()
# son.altered()

# from thinkbayes import Pmf
# pmf = Pmf() 
# for x in [1,2,3,4,5,6]:
#     pmf.Set(x,1/6.0)

# print(pmf)

# import pandas as pd

# df=pd.read_csv("../game/data/HR.csv")

# # print(df.head(10))

# print(type(df))

# print(type(df['satisfaction_level']))

# print(df.mean())

# print(df['satisfaction_level'].mean())   #平均数

# print(df.median())    #中位数
# print("-------------")
# print(df.quantile(0.25))   #分位数

# print("-------------")
# print(df.mode())  #众数
# print("------------")
# print(type(df["department"].mode()))  #离散值，傻鬼？

# print(df['satisfaction_level'].std())  #标准差

# print(df.var()) #方差

# print(df.sum())   #求和

# print(df.skew())  #偏态系数

# print(df.kurt())   #分布函数

# import scipy.stats as ss 
# print(ss.norm())
# print(ss.norm._stats(moments="mvsk"))

# import pandas as pd 
# import numpy as np

# df=pd.read_csv('../game/data/HR.csv')
# sl_s=df['satisfaction_level']
# print(sl_s[sl_s.isnull()])

# print(df[df['satisfaction_level'].isnull()])
# sl_s=sl_s.dropna()

# print(sl_s)

# sl_s.max()
# sl_s.min()
# sl_s.mean()
# sl_s.median()
# sl_s.quantile(q=0.25)
# sl_s.skew()
# sl_s.kurt()

# print(np.histogram(sl_s.values,bins=np.arange(0.0,1.1,0.1)))

# le_s=df['last_evaluation']
# le_s[le_s.isnull()]

# print(le_s.mean())

# print(le_s.std())

# print(le_s.median())

# print(le_s.skew())

# print(le_s.kurt())

# print(le_s.max())

# print(le_s.min())

# print(le_s[le_s>1])

# q_low=le_s.quantile(q=0.25)
# q_high=le_s.quantile(q=0.75)
# q_intereval=q_high-q_low
# k=1.5

# le_s=le_s[le_s<q_high+q_high*k][le_s>q_low-q_low*k]
# print(le_s.quantile(q=0.25))

# print(le_s.quantile(q=0.75))

# print(q_high-q_low)

# print(np.histogram(le_s.values,bins=np.arange(0.0,1.1,0.1)))

# np_s=df['number_project']
# print(np_s[np_s.isnull()])

# np_s.mean()

# np_s.median()

# np_s.max()

# np_s.min()

# np_s.skew()

# np_s.kurt()

# print(np_s.value_counts())

# print(np_s.value_counts(normalize=True).sort_index())

# amh_s=df['average_monthly_hours']
# print(amh_s.mean())
# amh_s.std()

# amh_s.max()

# amh_s.min()

# amh_s.skew()

# amh_s.kurt()

# amh_s=amh_s[amh_s<amh_s.quantile(0.75)+1.5*(amh_s.quantile(0.75)-amh_s.quantile(0.25))][amh_s>amh_s.quantile(0.25)-1.5*(amh_s.quantile(0.75)-amh_s.quantile(0.25))]

# print(np.histogram(amh_s.values,bins=10))

# tsc_s=df['time_spend_company']

# print(tsc_s.value_counts().sort_index())

# print(tsc_s.mean())


# wa_s=df['Work_accident']

# print(wa_s.value_counts())

# print(wa_s.mean())

# pl5_s=df['promotion_last_5years']
# print(pl5_s.value_counts())

# s_s=df['salary']
# print(s_s.value_counts())
# s_s.where(s_s!='nme').dropna()

# d_s=df['department']
# print(d_s.value_counts(normalize=True))
# print(d_s.where(d_s!="sale").dropna())

# df=df.dropna(axis=0,how='any')
# df=df[df['last_evaluation']<1][df['salary']!='nme'][df['department']!='sale']
# print(df)
# print(df.groupby('department').mean())

# df.loc[:,['last_evaluation','department']]

# import seaborn as sns 
# import  matplotlib.pyplot as plt
# sns.set_style(style='dark')
# sns.countplot(x='salary',hue="department",data=df)
# plt.show()
# plt.title('SALARY')
# plt.xlabel('salary')
# plt.ylabel('Number')
# plt.xticks(np.arange(len(df['salary'].value_counts()))+0.5,df['salary'].value_counts().index)
# plt.axis([0,4,0,10000])
# plt.bar(np.arange(len(df['salary'].value_counts()))+0.5,df['salary'].value_counts(),width=0.5)
# for x, y in zip(np.arange(len(df['salary'].value_counts()))+0.5,df['salary'].value_counts()):
#     plt.text(x,y,y,ha="center",va='bottom')
# plt.show()

# f=plt.figure()
# f.add_subplot(1,3,1)
# sns.distplot(df['satisfaction_level'],bins=10)

# f.add_subplot(1,3,2)
# sns.distplot(df['last_evalution'],bins=10)

# plt.show()

# sns.boxplot(x=df['time_spend_company'],saturation=0.75,whis=3)
# plt.show()

# sub_df=df.groupby('time_spend_company').mean()
# sns.pointplot(sub_df.index,sub_df['left'])
# # sns.pointplot(x='time_spend_company',y='left',data=df)
# plt.show()
# lbs=df['department'].value_counts().index
# explodes=[0.1 if i=='sales' else 0 for i in lbs]
# plt.pie(df['department'].value_counts(normalize=True),explode=explodes,labels=lbs,autopct='%1.1f%%')
# plt.show()

# import numpy as np
# import scipy.stats as ss 

# norm_dist=ss.norm.rvs(size=20)

# ss.normaltest(norm_dist)


# ss.chi2_contingency([15,95],[85,5])

# ss.ttest_ind(ss.norm.rvs(size=100),ss.norm.rvs(size=20))

# print(ss.ttest_ind(ss.norm.rvs(size=10),ss.norm.rvs(size=20)))

# from statsmodels.graphics.api import qqplot

# from matplotlib import pyplot as plt

# plt.show(qqplot(ss.norm.rvs(size=100)))
# def myPCA(data,n_components=100000000):
#     mean_vals=np.mean(data,axis=0)
#     mid=data-mean_vals
#     cov_mat=np.cov(mid,rowvar=False)
#     from scipy import linalg
#     eig_vals,eig_vects=linalg.eig(np.mat(cov_mat))
#     eig_val_index=np.argsort(eig_vals)
#     eig_val_index=eig_val_index[:-(n_components+1):-1]
#     eig_vects=eig_vects[:,eig_val_index]
#     low_dim_mat=np.dot(mid,eig_vects)
#     return low_dim_mat,eig_vals

# import pandas as pd 
# s1=pd.Series([0.1,0.2,1.1,2.4,1.3,0.3,0.5])
# s2=pd.Series([0.5,0.4,1.2,2.5,1.1,0.7,0.1])

# s1.corr(s2,method='spearman')

# df=pd.DataFrame(np.array([s1,s2]).T)

# x=np.arrange(10).astype(np.float).reshape((10,1))

# y=x*3+4+np.random((10,1))

# from sklearn.linear_model import LinearRegression

# reg=LinearRegression()

# res=reg.fit(x,y)

# y_pred=reg.predict(x)

# data=np.array([np.array([2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1]),np.array([2.4,0.7,2.9,2.2,3,2.7,1.6,1.1,1.6,0.9])]).T

# from sklearn.decomposition import PCA

# lower_dim=PCA(n_components=1)

# lower_dim.fit(data)

# lower_dim.explained_variance_ratio_

# lower_dim.fit_transform(data)

# _*_ coding: utf-8 _*_

# """
# python_visual_animation.py by xianhu
# """

# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# from mpl_toolkits.mplot3d import Axes3D

# # 解决中文乱码问题
# myfont = fm.FontProperties(fname="/Library/Fonts/Songti.ttc", size=14)
# matplotlib.rcParams["axes.unicode_minus"] = False


# def simple_plot():
#     """
#     simple plot
#     """
#     # 生成画布
#     plt.figure(figsize=(8, 6), dpi=80)

#     # 打开交互模式
#     plt.ion()

#     # 循环
#     for index in range(100):
#         # 清除原有图像
#         plt.cla()

#         # 设定标题等
#         plt.title("动态曲线图", fontproperties=myfont)
#         plt.grid(True)

#         # 生成测试数据
#         x = np.linspace(-np.pi + 0.1*index, np.pi+0.1*index, 256, endpoint=True)
#         y_cos, y_sin = np.cos(x), np.sin(x)

#         # 设置X轴
#         plt.xlabel("X轴", fontproperties=myfont)
#         plt.xlim(-4 + 0.1*index, 4 + 0.1*index)
#         plt.xticks(np.linspace(-4 + 0.1*index, 4+0.1*index, 9, endpoint=True))

#         # 设置Y轴
#         plt.ylabel("Y轴", fontproperties=myfont)
#         plt.ylim(-1.0, 1.0)
#         plt.yticks(np.linspace(-1, 1, 9, endpoint=True))

#         # 画两条曲线
#         plt.plot(x, y_cos, "b--", linewidth=2.0, label="cos示例")
#         plt.plot(x, y_sin, "g-", linewidth=2.0, label="sin示例")

#         # 设置图例位置,loc可以为[upper, lower, left, right, center]
#         plt.legend(loc="upper left", prop=myfont, shadow=True)

#         # 暂停
#         plt.pause(0.1)

#     # 关闭交互模式
#     plt.ioff()

#     # 图形显示
#     plt.show()
#     return
# simple_plot()


# def scatter_plot():
#     """
#     scatter plot
#     """
#     # 打开交互模式
#     plt.ion()

#     # 循环
#     for index in range(50):
#         # 清除原有图像
#         # plt.cla()

#         # 设定标题等
#         plt.title("动态散点图", fontproperties=myfont)
#         plt.grid(True)

#         # 生成测试数据
#         point_count = 5
#         x_index = np.random.random(point_count)
#         y_index = np.random.random(point_count)

#         # 设置相关参数
#         color_list = np.random.random(point_count)
#         scale_list = np.random.random(point_count) * 100

#         # 画散点图
#         plt.scatter(x_index, y_index, s=scale_list, c=color_list, marker="o")

#         # 暂停
#         plt.pause(0.2)

#     # 关闭交互模式
#     plt.ioff()

#     # 显示图形
#     plt.show()
#     return
# scatter_plot()


# def three_dimension_scatter():
#     """
#     3d scatter plot
#     """
#     # 生成画布
#     fig = plt.figure()

#     # 打开交互模式
#     plt.ion()

#     # 循环
#     for index in range(50):
#         # 清除原有图像
#         fig.clf()

#         # 设定标题等
#         fig.suptitle("三维动态散点图", fontproperties=myfont)

#         # 生成测试数据
#         point_count = 100
#         x = np.random.random(point_count)
#         y = np.random.random(point_count)
#         z = np.random.random(point_count)
#         color = np.random.random(point_count)
#         scale = np.random.random(point_count) * 100

#         # 生成画布
#         ax = fig.add_subplot(111, projection="3d")

#         # 画三维散点图
#         ax.scatter(x, y, z, s=scale, c=color, marker=".")

#         # 设置坐标轴图标
#         ax.set_xlabel("X Label")
#         ax.set_ylabel("Y Label")
#         ax.set_zlabel("Z Label")

#         # 设置坐标轴范围
#         ax.set_xlim(0, 1)
#         ax.set_ylim(0, 1)
#         ax.set_zlim(0, 1)

#         # 暂停
#         plt.pause(0.2)

#     # 关闭交互模式
#     plt.ioff()

#     # 图形显示
#     plt.show()
#     return
# # three_dimension_scatter()
# import matplotlib.pyplot as plt
# import numpy as np
# import random

import re
import sys
'''
e^x的麦克劳林展开式: 
e^x= f（0）+ f′（0）x+ f″（0）x ²/ 2!+...+ fⁿ（0）x^n/n!+Rn(x）
=1+x+x^2/2!+x^3/3!+...+x^n/n!+Rn(x） 
'''

# # 阶乘函数
# def factorial(n):
#     x = 1
#     for i in range(1,n+1):
#         x = x * i
#     return x

# # y值函数
# def consY(n,x):
#     y = 1
#     for i in range(1,n):
#         y += x**i/factorial(i)
#     return y

# # 生成图像
# def moniPlot(n,x):
#     # 定义一个颜色集合
#     colors = ['g','b','black','cyan','lightgreen','yellow','deeppink','darkorchid']
#     plt.figure()
    
#     # 原函数
#     y = np.e**x
#     # 画原函数图像并进行标记
#     plt.plot(x,y,'r-',linewidth=2,label='e^x')
    
#     # 麦克劳林展开添加到图像上
#     for i in range(2,n):
#         y = consY(i,x)
#         # 随机选择颜色
#         color = colors[random.randint(0,len(colors)-1)]
#         linestyle = '--'
#         # 画图像，并对最后一个进行标记
#         if i == n:
#             plt.plot(x,y,color=color,linewidth=1,linestyle=linestyle,label="nearly e^x")
#         else:
#             plt.plot(x,y,color=color,linewidth=1,linestyle=linestyle)
#         plt.plot(x,y,color=color,linewidth=1,linestyle=linestyle)
#     #添加注释
#     plt.text(1.2, consY(10,3.9),"Maclaurin's series of e^x ",size=12)
    
#     # 将标记绘制图例，位置为于中间左侧
#     plt.legend(['e^x',"nearly e^x"], loc = 'center left')  
    
#     plt.show()


# # 定义 x , y
# x = np.linspace(1,4,80)
# # 原函数
# # y = np.e**x
# # Maclaurin展开 3项
# # y1 = consY(2,x)
# # 展开 4项
# # y2 = consY(3,x)
# # tylor 5项
# # y3 = consY(4,x)

# # 调用生成图像
# moniPlot(10,x)

# # 关闭图
# plt.close()

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(19680801)

# # example data
# mu = 100  # mean of distribution
# sigma = 15  # standard deviation of distribution
# x = mu + sigma * np.random.randn(437)

# num_bins = 50

# fig, ax = plt.subplots()

#这里应该一个一个点画出来，再用数组储存？
#也得画出原函数的，simple

# for i in range(1,np.e**x):
#     num_bins = i
# # the histogram of the data
# n, bins, patches = plt.hist(np.e**x, 1000, density=10)



# get the user's input
# from tkinter import *
 
# top = Tk()
# L1 = Label(top, text="函数")
# L1.pack( side = LEFT)
# E1 = Entry(top, bd =5)
# E1.pack(side = RIGHT)
# bar_width = E1.get()
# top.mainloop()

# # B = Button(top, text ="点我", command = getWidth)

# print(bar_width)

# bar_width = input("Enter your input: ");
# print("Received input is : ", bar_width) 

# bar_width=float(bar_width)
# t1 = np.arange(0.0, 3.0, bar_width)
# sum = 0
# t2 = []
# t3 = []

# def Name_function(funct):
#     return funct

# def get_function(x):
#     return  Name_function(np.e**(x))      

# # get the exactly(random) value of the X0 -- X1
# for i in range(0,len(t1)):
#    # print(i)
#    temp = get_function(t1[i])
#    t2.append(temp)
#    sum += get_function(t1[i])

#    temp2 = get_function(t1[i]+ bar_width/2)
#    t3.append(temp2)
# # shape mismatch: objects cannot be broadcast to a single shape  valueerror 少了若干value


# # for i in t1:
   
# #    # temp = get_function(i)
# #    # t2.append(get_function(i))
# #    # t3.append((get_function(i) + get_function(i))/2)
# #    sum += get_function(i)
#     # t3是临时变量

#  #添加注释
# plt.text(1.2, 12,"Maclaurin's series of e^x ",size=12)
# # for x in range(1,100):         
# plt.plot(t1,t2)

# # delete the last value of numpy list .yeah
# # del t3[-1]
# # print(t1)
# # t1.pop()

# # del the last one of t1
# t1 = np.delete(t1,-1)

# # del t3[-1]
# t3.pop()


# plt.bar(t1+bar_width/2,t3,facecolor='g', alpha=0.75,width=bar_width)
# # plt.axis([-1, 4, 0, 25])

# # the all area of rect...
# plt.text(1, 10, ' total area of rects is' + str(sum*bar_width))


# # # add a 'best fit' line
# # y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
# #      np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
# # ax.plot(bins, y, '--')
# # ax.set_xlabel('Smarts')
# # ax.set_ylabel('Probability density')
# # ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# # Tweak spacing to prevent clipping of ylabel
# # fig.tight_layout()
# # plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()

# 用bar代替histogram 似乎可以
# idea 0: get the more precise y_value
# idea 1: adjust bar_width,bar_width can be more less

# ValueError: cannot delete array elements  最后一个元素删除不能用 del[index] ? index ==负数？？
# 它不是list 是nump....  所以用delete就行

# interact emm...
# from tkinter import *   这个控件可以获取用户输入



# from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# import matplotlib.pyplot as plt
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import numpy as np


# fig = plt.figure()
# ax = fig.gca(projection='3d')

# # Make data.
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

# # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)

# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()

# This import registers the 3D projection, but is otherwise unused.
# from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
# from matplotlib import cm

# from matplotlib.collections import PolyCollection
# import matplotlib.pyplot as plt
# from matplotlib import colors as mcolors
# import numpy as np

# # 绘制混合图形
# # 绘制三维曲面
# fig = plt.figure()
 
# axes3d = Axes3D(fig)
 
# #!！面
# x = np.linspace(-10,10,100)
# y = np.linspace(-10,10,100)
 
# X,Y = np.meshgrid(x,y)
# Z = np.sqrt(X**2+Y**2)
 
# surf = axes3d.plot_surface(X,Y,Z,cmap=cm.coolwarm,
#                       linewidth=0, antialiased=False)
 
# # x = np.linspace(-10,30)
# # y = np.sin(x)
# # z = np.cos(x)+10
# # axes3d.plot(x,y,z,color = 'r')


# # # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)


# # Fixing random state for reproducibility
# np.random.seed(19680801)


# def cc(arg):
#     '''
#     Shorthand to convert 'named' colors to rgba format at 60% opacity.
#     '''
#     return mcolors.to_rgba(arg, alpha=0.6)


# def polygon_under_graph(xlist, ylist):
#     '''
#     Construct the vertex list which defines the polygon filling the space under
#     the (xlist, ylist) line graph.  Assumes the xs are in ascending order.
#     '''
#     return [(xlist[0], 100), *zip(xlist, ylist), (xlist[-1], 100)]


# # fig = plt.figure()
# # ax = fig.gca(projection='3d')

# # Make verts a list, verts[i] will be a list of (x,y) pairs defining polygon i
# verts = []

# # Set up the x sequence
# xs = np.linspace(-10,10,100)

# # The ith polygon will appear on the plane y = zs[i]
# zs = range(3)

# for i in zs:
#     ys = np.random.rand(len(xs))
#     verts.append(polygon_under_graph(xs, ys))

# poly = PolyCollection(verts ,facecolors=[cc('g'), cc('b'), cc('y')])
# axes3d.add_collection3d(poly, zs=zs, zdir='y')

# plt.show()
# 得到基础的3d图，还差切面分析和梯度下降
# 可以画出小平面 
# 思路一：将小平面缩小 
# 思路二：将曲面扩大

# Python - Python实现3D建模工具

# 本课程将基于OpenGL实现一般CAD软件都会具备的基础功能：渲染显示3D空间的画面并可以操作3D空间中物体。

# https://pyzh.readthedocs.io/en/latest/the-python-yield-keyword-explained.html 
# yield 的解释

# 生成器是可以迭代的，但是你 只可以读取它一次 
# 所有你可以使用 for .. in .. 语法的叫做一个迭代器：列表，字符串，文件……
# 你经常使用它们是因为你可以如你所愿的读取其中的元素，但是你把所有的值都存储到了内存中;
# 如果你有大量数据的话这个方式并不是你想要的,因为它并不把所有的值放在内存中，它是实时地生成数据:
# 当你调用这个函数的时候，函数内部的代码并不立马执行









import sys , re
from handlers import *
from util import *
from rules import *
# 这个模块的作用就是协调读入的文本和其他模块之间的关系
# 提供了存放'规则'和'过滤器'的列表

class Parser:
    """
    解释器父类
    读取.txt文件，应用rules并且控制handler
    """

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters= []
            
    def addRule(self, rule):
        """
        添加规则到规则列表
        """
        self.rules.append(rule)


    def addFilter(self, pattern, name):
        """
        添加过滤器到过滤器列表
        """
        def filter(block, handler): #创建过滤器
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        """
        解析
        """
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            #judge_list = True
            for rule in self.rules:
                if rule.condition(block):  #判断字符串属于哪一类规则
                    last = rule.action(block, self.handler) #运行规则处理字符串
            #judge_list = last
                    if last:
                        break
            #if not judge_list: self.handler.end('list')
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    纯文本解析器
    """

    def __init__(self, handler):
        Parser.__init__(self, handler) #调用父类构造函数

        #添加解析规则类
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule()) #最后添加段落规则，应为段落规则condition始终返回true

        #正则表达式
        #括号里表示保存为子组，与HTMLRender中的过滤器函数对应
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url') #url规则可改
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail') #可改


"""
运行程序
"""
handler = HTMLRenderer()          #定义
parser = BasicTextParser(handler) #初始化
parser.parse(sys.stdin)           #解析输入的文件，转换成html文件

'''这个程序的用途: 1、用来做代码高亮分析，如果改写成js版的话，可以做一个在线代码编辑器。
                   2、可以用来学习，供写博文用。 '''
'''运行方式：在cmd或者终端中输入
    python test.py < test_input.txt > test_output.html
    python表示用python.exe 运行test.py
    <表示从<之后的描述符输入，即从test_input.txt输入
    >表示从>之后的描述符输出，即输出到test_output.html'''