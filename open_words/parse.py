"""
Parse.py (relating to Words's parse.adb)

Parse a word or list of input words and return word form and
definition

"""

__author__ = "Luke Hollis <luke@archimedes.digital>"
__license__ = "MIT License. See LICENSE."

import string
import re
import pdb
from copy import deepcopy
from open_words.dict_line import WordsDict
from open_words.addons import LatinAddons
from open_words.stem_list import Stems
from open_words.uniques import Uniques
from open_words.inflects import Inflects


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
		self.punctuation_transtable = {ord(c): " " for c in string.punctuation}

		# Sort by length
		self.stems.sort(key=len)

		# Sort by length of ending
		self.inflects.sort(key=lambda x: len(x['ending']))

		return

	def parse_line(self, line):
		"""Parse a line of words delimited by spaces"""
		out = []
		line = self.sanitize( line )
		for word in line.split(" "):
			if len(word):
				out.append( self.parse( word ) )
		return out

	def parse(self, input_string, direction="latin_to_english", formatted=True):
		"""
		Parse an input string as a Latin word and look it up in the Words dictionary.

		Return dictionary and grammatical data formatted in a similar manner as original
		Words program.

		"""
		out = []

		s = input_string

		# Do the lookup based on the direction of the parse
		if direction == "latin_to_english":
			out = self.latin_to_english(s)

		else:
			out = self.english_to_latin(s)

		if formatted:
			out = self._format_output(out)

		return { 'word' : s, 'defs' : out }

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
		print(" -- Still need to build English to Latin")
		return out

	def _find_forms(self, s, reduced=False):
		infls = []
		out = []

		# Check against inflection list
		for infl in self.inflects:
			if s.endswith( infl['ending'] ):

				# If we've already found the longest inflection
				if len( infls ) > 0 and ( len( infls[0]['ending'] ) > len( infl['ending'] ) ):
						break
				else:
					infls.append( infl )

		# Run against stems
		stems = self._check_stems( s, infls )

		# Lookup dict info
		if reduced:
			# If it is reduced, we don't need to lookup the word ends
			# (or we'll end up with some pretty wonky words)
			out = self._lookup_stems( stems, out, False )
		else:
			out = self._lookup_stems( stems, out )

		# If not already reduced, reduce the word and recurse
		if len( out ) == 0 and not reduced:
			r_out = self._reduce( s )

			# If there's useful data after reducing, extend out w/data
			if r_out:
				out.extend( r_out )


		return out


	def _check_stems(self, s, infls):
		"""
		For each inflection that was a match, remove the inflection from
		the end of the word string and then check the resulting stem
		against the list of stems loaded in __init__
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
								infl['pos'] == "VPAR"
							and stem['pos'] == "V"
							)
						):

						# Ensure the inflections apply to the correct stem decl/conj/etc
						if infl['n'][0] == stem['n'][0]:
							is_in_match_stems = False

							# If this stem is already in the match_stems list, add infl to that stem (if not already an infl in that stem list)
							for i, mst in enumerate(match_stems):
								if stem == mst['st']:
									is_in_match_stems = True

									# So the matches a stem in the match_stems.  Is it unique to that stem's infls. If so, append it to that stem's infls.
									is_in_stem_infls = False
									for stem_infl in mst['infls']:
										if stem_infl['form'] == infl['form']:
											is_in_stem_infls = True
											# we found a match, stop looking
											break

									if not is_in_stem_infls:
										mst['infls'].append( infl )



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
						if (
								'id' in w['w'] and word['id'] == w['w']['id']
							or
								w['w']['orth'] == word['orth']
							):

							# It is in the out list already, flag and then check if the stem is already in the stems
							is_in_out = True

							# Ensure the stem is not already in the out word stems
							is_in_out_word_stems = False
							for st in out[i]['stems']:
								if st == stem:
									is_in_out_word_stems = True
									# We have a match, break the loop
									break

							if not is_in_out_word_stems:
								out[i]['stems'].append(stem)
							# If we matched a word in the out, break the loop
							break

					# If the word isn't in the out yet
					if not is_in_out:

						# Check the VPAR / V relationship
						if word['pos'] == "V":

							# If the stem doesn't match the 4th principle part, it's not VPAR
							if word['parts'].index( stem['st']['orth'] ) == 3:

								# Remove "V" infls
								stem = self._remove_extra_infls(stem, "V")

							else:
								# Remove "VPAR" infls
								stem = self._remove_extra_infls(stem, "VPAR")



						# Lookup word ends
						# Need to Clone this object - otherwise self.dict is modified
						word_clone = deepcopy( word )
						if get_word_ends:
							word_clone = self._get_word_endings( word_clone )

						# Finally, append new word to out
						out.append( { 'w': word_clone, 'stems': [ stem ] } )

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

		for infl in self.inflects:
			# If the conjugation/declesion is a match AND the part of speech is a match (regularize V/VPAR)
			if (
					infl['n'] == word['n']
				and (
						infl['pos'] == word['pos']
					or (
							infl['pos'] in ["V", "VPAR"]
						and word['pos'] in ["V", "VPAR"]
						)
					)
				):

				# If the word is a verb, get the 4 principle parts
				if word['pos'] in ["V", "VPAR"]:
					# Pres act ind first singular
					if len_w_p > 0 and not end_one and ( len( word['parts'][0] ) > 0 and word['parts'][0] != "-" ):
						if infl['form'] == "PRES  ACTIVE  IND  1 S":
							word['parts'][0] = word['parts'][0] + infl['ending']
							end_one = True

					# Pres act inf
					if len_w_p > 1 and not end_two and ( len( word['parts'][1] ) > 0 and word['parts'][1] != "-" ):
						if infl['form'] == "PRES  ACTIVE  INF  0 X":
							word['parts'][1] = word['parts'][1] + infl['ending']
							end_two = True

					# Perf act ind first singular
					if len_w_p > 2 and not end_three and ( len( word['parts'][2] ) > 0 and word['parts'][2] != "-" ):
						if infl['form'] == "PERF  ACTIVE  IND  1 S":
							word['parts'][2] = word['parts'][2] + infl['ending']
							end_three = True

					# Perfect passive participle
					if len_w_p > 3 and not end_four and ( len( word['parts'][3] ) > 0 and word['parts'][3] != "-" ):
						if infl['form'] == "NOM S M PRES PASSIVE PPL":
							word['parts'][3] = word['parts'][3] + infl['ending']
							end_four = True


				# If the word is a noun or adjective, get the nominative and genetive singular forms
				elif word['pos'] in ["N", "ADJ", "PRON"]:
					# Nominative singular
					if len_w_p > 0 and not end_one:
						if infl['form'].startswith("NOM S") and ( len( word['parts'][0] ) > 0 and word['parts'][0] != "-" ):
							word['parts'][0] = word['parts'][0] + infl['ending']
							end_one = True

					# Genitive singular
					if len_w_p > 1 and not end_two:
						if infl['form'].startswith("GEN S") and ( len( word['parts'][1] ) > 0 and word['parts'][1] != "-" ):
							word['parts'][1] = word['parts'][1] + infl['ending']
							end_two = True


		# Finish up a little bit of standardization for forms
		# For Verbs
		if word['pos'] in ["V", "VPAR"]:
			if len_w_p > 0 and not end_one:
				for inf in self.inflects:
					if infl['form'] == "PRES  ACTIVE  IND  1 S" and infl['n'] == [0,0] and ( len( word['parts'][0] ) > 0 and word['parts'][0] != "-" ):
						word['parts'][0] = word['parts'][0] + infl['ending']
						break

			if len_w_p > 1 and not end_two:
				for inf in self.inflects:
					if infl['form'] == "PRES  ACTIVE  INF  0 X" and infl['n'] == [0,0] and ( len( word['parts'][1] ) > 0 and word['parts'][1] != "-" ):
						word['parts'][1] = word['parts'][1] + infl['ending']
						break

			if len_w_p > 2 and not end_three:
				for inf in self.inflects:
					if infl['form'] == "PERF  ACTIVE  IND  1 S" and infl['n'] == [0,0] and ( len( word['parts'][2] ) > 0 and word['parts'][2] != "-" ):
						word['parts'][2] = word['parts'][2] + infl['ending']
						break

			if len_w_p > 3 and not end_four:
				for inf in self.inflects:
					if infl['form'] == "NOM S M PERF PASSIVE PPL" and infl['n'] == [0,0] and ( len( word['parts'][3] ) > 0 and word['parts'][3] != "-" ):
						word['parts'][3] = word['parts'][3] + infl['ending']
						break

		# Finish for nouns
		elif word['pos'] in ["N", "ADJ", "PRON"]:
			# Nominative singular
			if len_w_p > 0 and not end_one and infl['n'] == [0,0] and ( len( word['parts'][0] ) > 0 and word['parts'][0] != "-" ):
				for inf in self.inflects:
					if infl['form'].startswith("NOM S"):
						word['parts'][0] = word['parts'][0] + infl['ending']
						end_one = True

			# Genitive singular
			if len_w_p > 1 and not end_two and infl['n'] == [0,0] and ( len( word['parts'][1] ) > 0 and word['parts'][1] != "-" ):
				for inf in self.inflects:
					if infl['form'].startswith("GEN S"):
						word['parts'][1] = word['parts'][1] + infl['ending']
						end_two = True

		# If endings really don't exist, fall back to default
		if word['pos'] in ["V", "VPAR"]:
			if len_w_p > 0 and not end_one and ( len( word['parts'][0] ) > 0 and word['parts'][0] != "-" ):
				word['parts'][0] = word['parts'][0] + "o"
			if len_w_p > 1 and not end_two and ( len( word['parts'][1] ) > 0 and word['parts'][1] != "-" ):
				word['parts'][1] = word['parts'][1] + "?re"
			if len_w_p > 2 and not end_three and ( len( word['parts'][2] ) > 0 and word['parts'][2] != "-" ):
				word['parts'][2] = word['parts'][2] + "i"
			if len_w_p > 3 and not end_four and ( len( word['parts'][3] ) > 0 and word['parts'][3] != "-" ):
				word['parts'][3] = word['parts'][3] + "us"

		return word

	def sanitize(self, input_string):
		"""
		Sanitize the input string from all punct and numbers, make lowercase
		"""

		s = input_string
		s = s.translate(self.punctuation_transtable).lower()
		s = s.replace("—", " ")
		s = re.sub("\d", " ", s)

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

	def _remove_extra_infls(self, stem, remove_type="VPAR"):
		"""Remove Vs or VPARs from a list of inflections"""
		stem_infls_copy = stem['infls'][:]

		for infl in stem_infls_copy:
			if infl['pos'] == remove_type:
				stem['infls'].remove(infl)

		return stem

	def _format_output(self, out, type="condensed"):
		"""Format the output in the designated type"""
		new_out = []

		for word in out:
			obj = {
					'orth': [],
					'senses': word['w']['senses'],
					'infls': []
				}

			# Format the orth of the new object
			if 'parts' in word['w']:
				obj['orth'] = word['w']['parts']
			else:
				obj['orth'] = [word['w']['orth']]

			# Format the stems / inflections of the new object
			if 'stems' in word:
				for stem in word['stems']:
					to_add_infls = []
					for infl in stem['infls']:

						# Ensure the infl isn't already in the infls
						is_in_formatted_infls = False
						for formatted_infl in to_add_infls:
							if infl['form'] == formatted_infl['form']:
								is_in_formatted_infls = True

						if not is_in_formatted_infls:
							to_add_infls.append({
									'ending' : infl['ending'],
									'pos' : infl['pos'],
									'form' : infl['form']
								})

					for formatted_infl in to_add_infls:
						if formatted_infl not in obj['infls']:
							obj['infls'].append(formatted_infl)

			else:
				word['w']['form'] = word['w']['pos']

			# If we still don't have any inflections associated with the object
			if len(obj['infls']) == 0:
				obj['infls'] = [ {
						'form': word['w']['form'],
						'ending': '',
						'pos': word['w']['pos']
					} ]

			# Format the morphological data for the word forms into a more useful output
			obj = self._format_morph( obj )

			new_out.append( obj )


		return new_out

	def _format_morph(self, word):
		"""
		Format the morphological data of the word forms into a more semantically useful model
		"""

		for infl in word['infls']:
			# Translate form
			infl['form'] = self._format_form( infl['form'], infl['pos'] )

			# Set part of speech
			if infl['pos'] == "N":
				infl['pos'] = "noun"
			elif infl['pos'] == "V":
				infl['pos'] = "verb"
			elif infl['pos'] == "VPAR":
				infl['pos'] = "participle"
			elif infl['pos'] == "ADJ":
				infl['pos'] = "adjective"
			elif infl['pos'] == "PREP":
				infl['pos'] = "adjective"
			elif infl['pos'] == "PRON":
				infl['pos'] = "pronoun"
			elif infl['pos'] == "INTERJ":
				infl['pos'] = "interjection"
			elif infl['pos'] == "NUM":
				infl['pos'] = "number"
			elif infl['pos'] == "CONJ":
				infl['pos'] = "conjunction"
			elif infl['pos'] == "PREP":
				infl['pos'] = "preposition"

		return word

	def _format_form(self, form, pos):
		"""
		Format form data to be more useful and relevant

		Nouns, Verbs, Adjectives, Participles(, Adverbs, Conjunctions, Prepositions)

		Nouns, Adjectives
		 - declension: nominative, vocative, genitive, accusative, dative, ablative, locative
		 - gender: male, female, neuter
		 - number: singular, plural

		Verbs
		 - person: 1, 2, 3
		 - number: singular, plural
		 - mood: indicative, subjunctive
		 - voice: active, passive
		 - tense: present, imperfect, perfect, future, future perfect, pluperfect, infinitive, imperative

		Participles
		 - declension: nominative, vocative, genitive, accusative, dative, ablative, locative
		 - gender: male, female, neuter
		 - number: singular, plural
		 - tense: present, perfect, future
		 - voice: active, passive

		"""
		formatted = {}

		if pos in ["N", "PRON", "ADJ", "NUM"]:
			# Ex. "ACC S C"
			form = form.split(" ")
			if len( form ) == 3:
				formatted = {
					'declension' : self._trans_declension( form[0] ),
					'number' : self._trans_number( form[1] ),
					'gender' : self._trans_gender( form[2] )
				}
			else:
				formatted = {
					'form' : form
				}

		elif pos == "V":
			# Ex: "FUT   ACTIVE  IND  3 S"
			if len( form ) == 22:
				formatted = {
					'tense' : self._trans_tense( form[0:6].strip() ),
					'voice' : self._trans_voice( form[6:14].strip() ),
					'mood' : self._trans_mood( form[14:19].strip() ),
					'person' : int( form[19:21].strip() ),
					'number' : self._trans_number( form[21:].strip() )
				}
			else:
				formatted = {
					'form' : form
				}

		elif pos == "VPAR":
			# Ex: "VOC P N PRES ACTIVE  PPL"
			if len( form ) == 24:
				formatted = {
					'declension' : self._trans_declension( form[0:4].strip() ),
					'number' : self._trans_number( form[4:6].strip() ),
					'gender' : self._trans_gender( form[6:8].strip() ),
					'tense' : self._trans_tense( form[8:13].strip() ),
					'voice' : self._trans_voice( form[13:21].strip() )
				}
			else:
				formatted = {
					'form' : form
				}

		elif pos in ["ADV", "INTERJ", "CONJ", "PREP", "X", "P"]:
			formatted = {
				'form' : form
			}

		else:
			formatted = {
				'form' : form
			}

		return formatted

	def _trans_declension(self, abb):
		w = ''
		declensions = {
			'NOM' : "nominative",
			'VOC' : "vocative",
			'GEN' : "genitive",
			'DAT' : "dative",
			'ACC' : "accusative",
			'LOC' : "locative",
			'ABL' : "ablative",
			'X' : ""
		}

		w = declensions[ abb ]

		return w

	def _trans_number(self, abb):
		w = ''
		numbers = {
			'S' : "singular",
			'P' : "plural",
			'X' : ""
		}

		w = numbers[ abb ]

		return w

	def _trans_gender(self, abb):
		w = ''
		genders = {
			'M' : "masculine",
			'F' : "feminine",
			'N' : "neuter",
			'C' : "C",
			'X' : ""
		}

		w = genders[ abb ]

		return w

	def _trans_mood(self, abb):
		w = ''
		moods = {
			'IND' : "indicative",
			'SUB' : "subjunctive",
			'IMP' : "imperative",
			'INF' : "infinitive",
			'X' : ""
		}

		w = moods[ abb ]

		return w

	def _trans_voice(self, abb):
		w = ''
		voices = {
			'ACTIVE' : "active",
			'PASSIVE' : "passive",
			'X' : ""
		}

		w = voices[ abb ]

		return w

	def _trans_tense(self, abb):
		w = ''

		tenses = {
			'PRES' : "present",
			'IMPF' : "imperfect",
			'PERF' : "perfect",
			'FUT' : "future",
			'FUTP' : "future perfect",
			'PLUP' : "pluperfect",
			'INF' : "infinitive",
			'X' : ""
		}

		w = tenses[ abb ]

		return w
