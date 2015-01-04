"""
Parse.py (relating to Words's parse.adb)

Parse a word or list of input words and return word form and 
definition

"""

__author__ = "Luke Hollis <luke@segetes.io>)"
__license__ = 'MIT License. See LICENSE.'

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
		"""Provide a modular structure for loading the parser data"""

		# Parser data
		self.dict = words_dict
		self.addons = addons
		self.stems = stems
		self.uniques = uniques
		self.inflects = inflects

		# Useful for sanitizing string for parsing
		self.punctuation_transtable = {ord(c): None for c in string.punctuation}

		# Sort by length
		self.stems.sort(key=len)

		# Sort by length of ending
		self.inflects.sort(key=lambda x: len(x['ending']))

		return

	def parse_line(self, line):
		"""Parse a line of words delimited by spaces"""
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
		"""Find definition and word formation from Latin word"""
		is_unique = False
		out = []

		# Split enclitics
		s, out = self._split_enclitic( s )

		# Check against list of uniques
		for u in self.uniques:
			if s == u['orth']:
				out.append({'w':u, 'stems':[]})
				is_unique = True
				break

		# If it's not in the list of uniques
		if not is_unique:
			out = self._find_forms( s )

		return out


	def english_to_latin(self, s):
		"""Find definition and word formation from English word"""
		out = []

		return out

	def _find_forms(self, s, reduced=False):
		infls = []
		out = []

		# Check against inflection list
		for infl in self.inflects:
			if s.endswith( infl['ending'] ):
				infls.append( infl )


		# Run against stems
		match_stems = self._check_stems( s, infls )

		# Lookup dict info
		if reduced:
			# If it is reduced, we don't need to lookup the word ends
			# (or we'll end up with some pretty wonky words)
			out = self._lookup_stems( match_stems, out, False )
		else:
			out = self._lookup_stems( match_stems, out )

		# If no matches, reduce
		if not reduced:
			r_out = self._reduce( s )

			# If there's useful data after reducing, extend out w/data
			if r_out:
				out.extend( r_out )

		return out


	def _check_stems(self, s, infls):
		"""
		For each inflection that was a match, remove the inflection from
		the end of the word string and then check the resulting stem against
		the list of stems loaded in __init__
		""" 
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

		# While we're working out the kinks in the word form taxonomies	
		if len(match_stems) == 0:
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
							# Ensure it's the base form 
							if infl['n'][0] == 0:
								is_in_match_stems = False 

								# If this stem is already in the match_stems list, add infl to that stem
								for i, mst in enumerate(match_stems):
									if stem == mst['st']:
										match_stems[i]['infls'].append( infl )
										is_in_match_stems = True

								if not is_in_match_stems:
									match_stems.append({ 'st':stem, 'infls':[infl] })



		return match_stems 


	def _lookup_stems(self, match_stems, out, get_word_ends=True):
		"""Find the word id mentioned in the stem in the dictionary"""

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

					# If the word isn't in the out yet 
					if not is_in_out:

						# Lookup word ends 
						if get_word_ends:
							word = self._get_word_endings( word )

						# Finally, append new word to out
						out.append({'w':word, 'stems':[stem]})

		return out 


	def _split_enclitic(self, s):
		"""Split enclitic ending from word"""
		out = [] 

		# Test the different tackons / packons as specified in addons.py
		for e in self.addons['tackons']:
			if s.endswith( e['orth'] ):

				# Standardize data format
				e['form'] = e['orth']

				# Est exception
				if s != "est":
					out.append( { 'w' : e, "stems" : [] } )
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
		"""
		Get the word endings for the stems in the Dictionary; 
		eventually this should be phased out in favor of including the
		endings in the words in the dict_line dict
		""" 
		end_one = False
		end_two = False
		end_three = False
		end_four = False

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
					if len_w_p > 0 and not end_one:
						if inf['form'] == "PRES  ACTIVE  IND  1 S":
							word['parts'][0] = word['parts'][0] + inf['ending']
							end_one = True

					# Pres act inf
					if len_w_p > 1 and not end_two:
						if inf['form'] == "PRES  ACTIVE  INF  0 X":
							word['parts'][1] = word['parts'][1] + inf['ending']
							end_two = True

					# Perf act ind first singular
					if len_w_p > 2 and not end_three:
						if inf['form'] == "PERF  ACTIVE  IND  1 S":
							word['parts'][2] = word['parts'][2] + inf['ending']
							end_three = True

					# Perfect passive participle
					if len_w_p > 3 and not end_four:
						if inf['form'] == "NOM S M PRES PASSIVE PPL":
							word['parts'][3] = word['parts'][3] + inf['ending']
							end_four = True


				# If the word is a noun or adjective, get the nominative and genetive singular forms
				elif word['pos'] in ["N", "ADJ"]:
					# Nominative singular 
					if len_w_p > 0 and not end_one:
						if inf['form'].startswith("NOM S"):
							word['parts'][0] = word['parts'][0] + inf['ending']
							end_one = True

					# Genitive singular 
					if len_w_p > 1 and not end_two:
						if inf['form'].startswith("GEN S"):
							word['parts'][1] = word['parts'][1] + inf['ending']
							end_two = True

				# Otherwise, think of something better to do later
				else:
					pass

		# Finish up a little bit of standardization for forms
		if word['pos'] in ["V", "VPAR"]:
			if len_w_p > 2 and not end_three:
				for inf in self.inflects:
					if inf['form'] == "PERF  ACTIVE  IND  1 S" and inf['n'] == [0,0]:
						word['parts'][2] = word['parts'][2] + inf['ending']
						break

			if len_w_p > 3 and not end_four:
				for inf in self.inflects:
					if inf['form'] == "NOM S M PERF PASSIVE PPL" and inf['n'] == [0,0]:
						word['parts'][3] = word['parts'][3] + inf['ending']
						break

		return word

	def sanitize(self, input_string):
		"""
		Sanitize the input string from all punct and numbers, make lowercase
		"""

		s = input_string
		s = s.translate(self.punctuation_transtable).lower()
		s = s.replace("—", "")
		s = re.sub("\d", "", s)	

		return s

	def _reduce(self, s):
		"""Reduce the stem with suffixes and try again"""
		out = [] 
		is_unique = False
		found_new_match = False
		infls = []
		# For each inflection match, check prefixes and suffixes
		for prefix in self.addons['prefixes']:
			if s.startswith( prefix['orth'] ):
				s = re.sub ( "^" + prefix['orth'], "", s )
				out.append({ 'w' : prefix, 'stems' : [], 'addon' : "prefix" })
				break
		for suffix in self.addons['suffixes']:
			if s.endswith( suffix['orth'] ):
				s = re.sub ( suffix['orth'] + "$", "", s )
				out.append({ 'w' : suffix, 'stems' : [], 'addon' : "suffix" })
				break

		# Find forms with the 'reduced' flag set to true
		out = self._find_forms( s, True )

		# Has reducing input string given us useful data? 
		# If not, return false
		for word in out: 
			if len(word['stems']) > 0: 
				found_new_match = True

		if not found_new_match:
			out = False

		return out 

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
			except KeyError:
				obj['orth'] = [word['w']['orth']]

			for stem in word['stems']:
				infls = []
				for infl in stem['infls']:
					infls.append({
							'ending' : infl['ending'],
							'form' : infl['form']
						})

				obj['infls'].extend(infls)

			if len(obj['infls']) == 0:
				obj['infls'] = [{'forms': word['w']['form'], 'ending':''}]

			new_out.append( obj )

		return new_out 
