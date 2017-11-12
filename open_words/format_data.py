"""format_data"""
import pdb
import json



def import_dicts():
	data = []
	with open('DICTLINE.GEN', encoding="ISO-8859-1") as f:
		for i, line in enumerate( f ):

			orth = line[0:19].replace("zzz", "-").strip()
			parts = [orth]

			if len( line[19:38].strip() ) > 0:
				parts.append( line[19:38].replace("zzz", "-").strip() )

			if len( line[38:57].strip() ) > 0:
				parts.append( line[38:57].replace("zzz", "-").strip() )

			if len( line[57:76].strip() ) > 0:
				parts.append( line[57:76].replace("zzz", "-").strip() )

			if len( line[83:87].strip() ) > 0:
				n = line[83:87].strip().split(" ")
				for n_i, v in enumerate(n):
					try: 
						n[n_i] = int(v)
					except ValueError:
						pass

			senses = line[109:].strip().split(";")
			new_senses = []
			for sense in senses:
				sense = sense.strip()
				if len( sense ):
					new_senses.append(sense)


			data.append({
				'id' : i + 1,
				'orth' : orth, 
				'parts' : parts, 
				'pos' : line[76:83].strip(),
				'form' : line[83:100].strip(),
				'n' : n,
				'senses' : new_senses 
				})

	with open('data.json', 'w') as out:
	    json.dump(data, out)

	return





def import_stems():

	data = []
	with open('STEMLIST.GEN') as f:
		for line in f:

			if len( line[26:30].strip() ) > 0:
				n = line[26:30].strip().split(" ")
				for i, v in enumerate(n):
					try: 
						n[i] = int(v)
					except ValueError:
						pass

			data.append({
				'orth' : line[0:19].strip(),
				'pos' : line[19:26].strip(),
				'form' : line[26:45].strip(),
				'n' : n,
				'wid' : int(line[50:].strip())
				})

	with open('data.json', 'w') as out:
	    json.dump(data, out)

	return 



def import_suffixes():

	with open('suffixes.txt') as f:

		i = 0
		obj = {}
		data = []

		for line in f:

			if i == 0:
				obj['orth'] = line.replace("PREFIX", "").replace("SUFFIX", "").strip()

			elif i == 1:
				obj['pos'] = line[0].strip()
				obj['form'] = line[0:].strip()

			elif i == 2:
				obj['senses'] = [line.strip()]


			i = i + 1
			if i == 3:
				data.append(obj)
				obj = {}
				i = 0

	with open('data.json', 'w') as out:
	    json.dump(data, out)


	return


def import_prefixes():

	with open('prefixes.txt') as f:

		i = 0
		obj = {}
		data = []

		for line in f:

			if i == 0:
				obj['orth'] = line.replace("PREFIX", "").strip()

			elif i == 1:
				obj['pos'] = line[0].strip()
				obj['form'] = line[0:].strip()

			elif i == 2:
				obj['senses'] = [line.strip()]


			i = i + 1
			if i == 3:
				data.append(obj)
				obj = {}
				i = 0

	with open('data.json', 'w') as out:
	    json.dump(data, out)


	return

def import_uniques():

	with open('UNIQUES.LAT') as f:

		i = 0
		obj = {}
		data = []

		for line in f:

			if i == 0:
				obj['orth'] = line.strip()

			elif i == 1:
				obj['pos'] = line[0].strip()
				obj['form'] = line[1:52].strip()

			elif i == 2:
				obj['senses'] = [line.strip()]


			i = i + 1
			if i == 3:
				data.append(obj)
				obj = {}
				i = 0

	with open('data.json', 'w') as out:
	    json.dump(data, out)


	return

def import_inflects():

	with open('INFLECTS.LAT') as f:

		i = 0
		obj = {}
		data = []

		for i, line in enumerate(f):

			if len(line.strip()) > 0 and not line.strip().startswith("--"):
				n = [] 

				# Nouns

				# No ending
				if i in range(26,40):

					n = parse_infl_type(line[7:21]) 

					data.append({
							'ending' : "",
							'n' : n,
							'note' : "",
							'pos' : line[0:7].strip(),
							'form' : line[7:21].strip()
						})

				# 1st declension
				elif i in range(63, 85):

					n = parse_infl_type(line[6:9]) 

					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# 1st declension Greek	
				elif i in range(93, 99):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(103, 113):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(118, 127):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Second declension
				elif i in range(139, 159):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(166, 175):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Second declension er
				elif i in range(183, 186):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "er",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Second declension ius / ium 
				elif i in range(194, 201):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "ius/ium",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Second declension ius / ium 
				elif i in range(209, 214):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "ius/ium",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Second declension greek 
				elif i in range(220, 229):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(236, 245):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(250, 254):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(261, 265):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Third declension
				elif i in range(279, 299):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(305, 313):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "stem_ends_in_cons",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(322, 332):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "i-stems_m-f",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(339, 347):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "i-stems_n",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Third declension greek
				elif i in range(353, 359):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(363, 373):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(380, 393):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(403, 420):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})


				# Fourth declension	
				elif i in range(427, 449):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Fourth delcension u
				elif i in range(454, 463):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "u",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(468, 474):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "jesus_jesu",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Fifth declension
				elif i in range(479, 498):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Fifth declension
				elif i in range(479, 498):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Abbreviations  
				elif i in range(501, 502):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "abbreviation",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Not declined 
				elif i in range(504, 505):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "not_declined",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Adjective

				# First declension
				elif i in range(515, 552):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(558, 581):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(588, 625):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(633, 646):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "first_and_second",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(650, 693):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "nullus_alius",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(701, 765):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Third declension adj
				elif i in range(701, 765):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(773, 795):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(801, 812):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "two_endings",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(817, 828):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "three_endings",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})
				elif i in range(834, 846):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[23:33].strip(),
							'n' : n,
							'note' : "greek",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Verbs 

				# First conjugation
				elif i in range(857, 1021):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})

				# Second conjugation
				elif i in range(1037, 1159):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})

				# Third conjugation
				elif i in range(1173, 1301):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})
				elif i in range(1311, 1450):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "irregular",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})

				# Fourth conjugation
				elif i in range(1459, 1558):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})

				# Esse
				elif i in range(1569, 1678):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "like_to_be",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})

				# ire 
				elif i in range(1690, 1856):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "eo_ire",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})

				# volere` 
				elif i in range(1869, 1936):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "volere",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})

				# defective 
				elif i in range(1951, 2083):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "defective",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})

				# kludge 
				elif i in range(2097, 2137):

					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[38:52].strip(),
							'n' : n,
							'note' : "",
							'pos' : line[0:6].strip(),
							'form' : line[10:34].strip()
						})

				# Participles / Supine 

				# participles 1-3
				elif i in range(2144, 2618):

					n = parse_infl_type(line[5:8]) 
					data.append({
							'ending' : line[38:51].strip(),
							'n' : n,
							'note' : "participles",
							'pos' : line[0:5].strip(),
							'form' : line[9:34].strip()
						})

				# supine 
				elif i in range(2627, 2630):
					n = parse_infl_type(line[7:10]) 
					data.append({
							'ending' : line[24:30].strip(),
							'n' : n,
							'note' : "supine",
							'pos' : line[0:7].strip(),
							'form' : line[11:20].strip()
						})

				# Pronouns
				elif i in range(2686, 2965):
					n = parse_infl_type(line[6:9]) 
					data.append({
							'ending' : line[24:52].strip(),
							'n' : n,
							'note' : "pronoun",
							'pos' : line[0:6].strip(),
							'form' : line[10:17].strip()
						})

				# Numerals
				elif i in range(2971, 3941):
					n = parse_infl_type(line[7:10]) 
					data.append({
							'ending' : line[32:52].strip(),
							'n' : n,
							'note' : "numeral",
							'pos' : line[0:7].strip(),
							'form' : line[11:19].strip()
						})



	with open('data.json', 'w') as out:
	    json.dump(data, out)


	return

def parse_infl_type(s):

	if len( s.strip() ) > 0:
		n = s.strip().split(" ")
		for i, v in enumerate(n):
			try: 
				n[i] = int(v)
			except ValueError:
				pass

	return n