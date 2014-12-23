"""Parse.py (parse.adb)"""
import string
import re
import pdb
from dict_line import WordsDict
from addons import LatinAddons
from stem_list import Stems
from uniques import Uniques
from inflects import Inflects


class Parse:

	def __init__(self, words_dict=WordsDict, addons=LatinAddons, stems=Stems, uniques=Uniques, inflects=Inflects ):

		self.punctuation_transtable = {ord(c): None for c in string.punctuation}
		self.dict = words_dict
		self.addons = addons
		self.stems = stems
		self.uniques = uniques
		self.inflects = inflects

		self.stems.sort(key=len)
		self.inflects.sort(key=lambda x: len(x['ending']))

		return

	def parse_line(self, line):
		""" Parse a line of words delimited by spaces"""
		out = []
		for word in line.split(" "):
			out.append( self.parse( word ) )
		return out

	def parse(self, input_string, direction="latin_to_english"):
		"""
		Parse an input string as a Latin word and look it up in the Words dictionary.

		Return dictionary and grammatical data formatted in a similar manner as original
		Words program.

		"""
		out = []

		s = self.sanitize(input_string)

		# Do the lookup based on the direction of the parse 
		if direction == "latin_to_english":
			out = self.latin_to_english(s)

		else:
			out = self.english_to_latin(s)

		out = self._format_output(out)

		return out

	def latin_to_english(self, s):
		"""Find dictionary information from Latin word"""
		out = []
		is_unique = False
		infls = []

		# Split enclitics
		s, out = self._split_enclitic( s )

		# Check against list of uniques
		for u in self.uniques:
			if s == u['orth']:
				out.append(u)
				is_unique = True

		# If it's not in the list of uniques
		if not is_unique:

			# Check against inflection list
			for infl in self.inflects:
				if s.endswith( infl['ending'] ):
					infls.append( infl )


			# For each inflection match, check suffixes
			"""
			for 
			for suffix in self.addons['suffixes']:
				if s.endswith( suffix['orth'] ):
					s = re.sub ( suffix['orth'] + "$", "", s )
			"""

			# Run against stems
			match_stems = self._check_stems( s, infls )

			# Lookup dict info
			out = self._lookup_stems( match_stems, out )

		return out


	def english_to_latin(self, s):
		"""Find dictionary information from English word"""
		out = []

		return out


	def _check_stems(self, s, infls):
		"""Determine word form and definition""" 
		match_stems = []

		# For each of the inflections that is a match, strip the inflection from the end of the word
		# and look up the stripped word (w) in the stems
		for infl in infls:
			w = re.sub ( infl['ending'] + "$", "", s )

			for stem in self.stems:
				if w == stem['orth']: 

					# If the inflection and stem identify as the same part of speech
					if (
							infl['pos'] == stem['pos']
						or (
								infl['pos'] in ["VPAR", "V"]
							and stem['pos'] in ["VPAR", "V"]
							)
						):

						# Ensure the inflections apply to the correct stem decl/conj/etc
						if infl['n'][0] == stem['n'][0]:
							is_in_match_stems = False 

							# If this stem is already in the match_stems list, add infl to that stem
							for i, mst in enumerate(match_stems):
								if stem == mst['st']:
									match_stems[i]['infls'].append( infl )
									is_in_match_stems = True

							if not is_in_match_stems:
								match_stems.append({ 'st':stem, 'infls':[infl] })

		return match_stems 


	def _lookup_stems(self, match_stems, out):
		"""Lookup stems in dictionary"""

		for stem in match_stems:
			for word in self.dict:
				# Lookup by id
				if stem['st']['wid'] == word['id']:

					# If word already in out, add stem to word stems
					is_in_out = False 
					for i, w in enumerate(out):
						if 'id' in w['w'] and word['id'] == w['w']['id']:
							is_in_out = True
							out[i]['stems'].append(stem)
							break
					if not is_in_out:
						word = self._get_word_endings( word )
						out.append({'w':word, 'stems':[stem]})

		return out 


	def _split_enclitic(self, s):
		"""Split enclitic ending from word"""
		out = [] 

		# Test the different tackons / packons as specified in addons.py
		for e in self.addons['tackons']:
			if s.endswith( e['orth'] ):
				out.append( { 'w' : e } )
				s = re.sub( e['orth'] + "$", "", s)
				break

		if s.startswith( "qu" ):
			for e in self.addons['packons']:
				if s.endswith( e['orth'] ):
					out.append( { 'w' : e } )
					s = re.sub( e['orth'] + "$", "", s)
					break

		else:
			for e in self.addons['not_packons']:
				if s.endswith( e['orth'] ):
					out.append( { 'w' : e } )
					s = re.sub( e['orth'] + "$", "", s)
					break

		return s, out

	def _get_word_endings(self, word):
		"""Get the word endings for the stems in the Dictionary; 
		eventually this should be phased out in favor of including the
		endings in the words in the dict_line dict""" 
		len_w_p = len( word['parts'] )

		for inf in self.inflects:
			# If the conjugation/declesion is a match AND the part of speech is a match (regularize V/VPAR)
			if (
					inf['n'] == word['n']
				and (
						inf['pos'] == word['pos']
					or (
							inf['pos'] in ["V", "VPAR"]
						and word['pos'] in ["V", "VPAR"]
						)
					)
				):

				# If the word is a verb, get the 4 principle parts 
				if word['pos'] in ["V", "VPAR"]:
					# Pres act ind first singular
					if len_w_p > 0:
						if inf['form'] == "PRES  ACTIVE  IND  1 S":
							word['parts'][0] = word['parts'][0] + inf['ending']

					# Pres act inf
					if len_w_p > 1:
						if inf['form'] == "PRES  ACTIVE  INF  0 X":
							word['parts'][1] = word['parts'][1] + inf['ending']

					# Perf act ind first singular
					if len_w_p > 2:
						if inf['form'] == "PERF  ACTIVE  IND  1 S":
							word['parts'][2] = word['parts'][2] + inf['ending']

					# Perfect passive participle
					if len_w_p > 3:
						if inf['form'] == "NOM S M PRES PASSIVE PPL":
							word['parts'][3] = word['parts'][3] + inf['ending']


				# If the word is a noun or adjective, get the nominative and genetive singular forms
				elif word['pos'] in ["N", "ADJ"]:
					# Nominative singular 
					if len_w_p > 0:
						if inf['form'].startswith("NOM S"):
							word['parts'][0] = word['parts'][0] + inf['ending']

					# Genitive singular 
					if len_w_p > 1:
						if inf['form'].startswith("GEN S"):
							word['parts'][1] = word['parts'][1] + inf['ending']

				# Otherwise, think of something better to do later
				else:
					pass

		return word

	def sanitize(self, input_string):
		"""Sanitize the input string from all punct and numbers, make lowercase"""

		s = input_string
		s = s.translate(self.punctuation_transtable).lower()
		s = s.replace("—", "")
		s = re.sub("\d", "", s)	

		return s

	def _format_output(self, out, type="condensed"):
		"""Format the output in the designated type"""
		new_out = []

		for word in out:
			obj = {
					'orth': [],
					'senses': word['w']['senses'],
					'infls': []
				}

			try:
				obj['orth'] = word['w']['parts']
			except:
				obj['orth'] = [word['w']['orth']]

			for stem in word['stems']:
				infls = []
				for infl in stem['infls']:
					infls.append({
							'ending' : infl['ending'],
							'form' : infl['form']
						})

				obj['infls'].extend(infls)

			new_out.append( obj )

		return new_out 
