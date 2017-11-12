"""

From Whitaker:

This file lists, in human readable and editable form, a set of
"ADDONS" for the LATIN program.  ADDONS are prefixes, suffixes
and enclitic type fragments used in latin word formation.

While this "word formation" ability is, in principle, very powerful,
in practice, most of the common constructed words are in the dictionary
by themselves, so the number of prefix hits are smaller than might be
anticipated.  When there is a hit, that is, the full word was not found
in the dictionary but the base stem was found after removing the ADDON,
the resulting word/meaning is correct and fairly clear about 75 percent of
the time.  In many of the remaining cases, the construction is true,
but the usage of the word has strayed a bit and it may be a stretch to
make the association.  In about 10 precent of the cases, the construction is
just wrong, the word was simply derived from a different root.

The present algorithms can handle one prefix, one suffix, and one tackon
in the same word, i.e., a two suffix situation (if such exists) will fail.
{Need to make an exception for the formation of COMP, SUPER, ADV from ADJ}

The question remains as to whether there are too many, especially suffixes,
so that excessive aritficial words are created - are we too imaginative?
We will do a number of experiments when there is a sufficient data base.

This list can be modified by the user.  It is read in each time
the latin program is initiated, so is always current.


PREFIX is a fragment added to the beginning of a stem to modify or
reinforce the meaning.  "ante" added to a verb gives the meaning
"before" (ante-cedo = before-move => precede).  This does not
impact the addition of inflections on the end of the word.

Each PREFIX entry leads off with the identifier "PREFIX".

This is followed (separated by a space) by the prefix itself.

In the formulation used by this program, there may be a connecting
character associated with the prefix.  For example, the prefix "ad",
meaning "to", when applied to a word beginning with "c" changes to "ac".
Thus with curro (run) we get ac-curro, "run to".  The CONNECT character,
if any, is placed after the prefix, on the same line.

Prefixes may be thought of as not changing the base part of
speech.  "ante" is applied to a verb stem and converts it to
another verb stem.  The same prefix may have different meanings
when applied to different parts.  "sub" applied to an adjective
adds the meaning "somewhat", when applied to a verb it means "under".
The parts of speech (from and to) are listed on the second line,
but are always the same.  The redundency is the result of a generality
built into the data structure initially and never changed.

The third line gives the meaning, using 78 characters or less.

There is provision for AGE, AREA, GEO, FREQ, or SOURCE flags.

The order of this list is important.  The program checks in order.
One should check to see if "extra" is possible before trying "ex".
The longer prefix should be placed earlier in the list.
Otherwise prefixes are listed in alphabetical order.

Most prefixes transform V to V in this system.
The same prefixes can usually be applied to N and ADJ, especially those
suffix derived from verbs.  The word formation algorithm will usually
make the two steps necessary.  In almost all cases the ADJ ADJ prefixes
apply to those ADV derived from the adjective, but are not so listed here.

X X prefixes are interpreted by the program as applying to N, ADJ, ADV, abd V.
The program will not attempt to apply them to PRON, NUM, INTERJ or CONJ.

One could make all prefixes X X.  This would asure that no case was missed,
and generally that is the philosophy of the program.  However, that might
also produce excessive nonsense interpretations.  Probably the way to
proceed is to check the master dictionary (when it is sufficiently large)
to see if there are proper formations with that prefix of other parts of
speach, and to target in a similar manner.  If that prefix is never seen
in classical Latin in a particular formation, the ADDONS table should
probably ignore it.  This is yet to be done, which is one of the reasons
that ADDONS are not coded but left text for easy change.


"""


LatinAddons = {


	#
	# TICKONS
	# These are applied to a class of PRON which in the code are designated as PACKons.
	#
	'tickons' : [
			{
				'orth' : "ec",
				'pos' : "PACK PACK",
				'senses' : ["is there any...that? does any? (w/qui, sometimes w/nam) (passionate interrogation);"]
			},
			{
				'orth' : "ne",
				'pos' : "PACK PACK",
				'senses' : ["not (introducing negative clause, w/qui); verily, truely  (affirmative particle);"]
			},
			{
				'orth' : "nescio",
				'pos' : "PACK PACK",
				'senses' : ["(w/qui/quis) nescioquis=> some (unknown/unspecified), one/someone or other;"]
			},
			{
				'orth' : "neu",
				'pos' : "PACK PACK",
				'senses' : ["nor, and..not, neither..nor (adding a alternative or prohibition, w/qui);"]
			},
			{
				'orth' : "seu",
				'pos' : "PACK PACK",
				'senses' : ["or if (w/qui);"]
			},
			{
				'orth' : "si",
				'pos' : "PACK PACK",
				'senses' : ["if, when, in so much, even if (assumed fact/wish/unfinished, w/qui);"]
			}
		],


	#
	#  Pure PREFIXES
	#
	'prefixes' : [{"pos": "X", "form": "X X", "senses": ["- away, off; - aside;"], "orth": "abs"}, {"pos": "V", "form": "V V", "senses": ["- away, off; - aside;"], "orth": "ab"}, {"pos": "X", "form": "X X", "senses": ["- to, towards, near, for, together (adeo => go to);"], "orth": "ac c"}, {"pos": "X", "form": "X X", "senses": ["- to, towards, near, for, together (adeo => go to);"], "orth": "ac q"}, {"pos": "X", "form": "X X", "senses": ["- to, towards, near, for, together (adeo => go to);"], "orth": "ad"}, {"pos": "X", "form": "X X", "senses": ["having to do with buildings/temples;"], "orth": "aedi"}, {"pos": "X", "form": "X X", "senses": ["equi-, equal;"], "orth": "aequi"}, {"pos": "X", "form": "X X", "senses": ["- to, towards, near, for, together (adeo => go to);"], "orth": "af f"}, {"pos": "X", "form": "X X", "senses": ["- to, towards, near, for, together (adeo => go to);"], "orth": "ag g"}, {"pos": "X", "form": "X X", "senses": ["high, lofty;"], "orth": "alti"}, {"pos": "X", "form": "X X", "senses": ["around, round about; having two;"], "orth": "ambi"}, {"pos": "X", "form": "X X", "senses": ["around, round about; having two;"], "orth": "amb"}, {"pos": "X", "form": "X X", "senses": ["having two/double, (on) both/opposite (sides), front and back;"], "orth": "amphi"}, {"pos": "X", "form": "X X", "senses": ["around, round about; having two;"], "orth": "am"}, {"pos": "X", "form": "X X", "senses": ["ante-, - before;"], "orth": "ante"}, {"pos": "X", "form": "X X", "senses": ["anti-, counter-, against, contrary, opposite/opposed to; for ante-/before;"], "orth": "anti"}, {"pos": "X", "form": "X X", "senses": ["around, round about; having two;"], "orth": "an"}, {"pos": "X", "form": "X X", "senses": ["- to, towards, near, for, together (adeo => go to);"], "orth": "ap p"}, {"pos": "X", "form": "X X", "senses": ["arch-, chief-, first, master; great; extremely, very;"], "orth": "archi"}, {"pos": "X", "form": "X X", "senses": ["- to, towards, near, for, together (adeo => go to);"], "orth": "as s"}, {"pos": "X", "form": "X X", "senses": ["- to, towards, near, for, together (adeo => go to);"], "orth": "at t"}, {"pos": "X", "form": "X X", "senses": ["golden, gold-; of gold, gold-colored;"], "orth": "auri"}, {"pos": "X", "form": "X X", "senses": ["- away, off (aufero => make off with, carry away); - aside;"], "orth": "au f"}, {"pos": "V", "form": "V V", "senses": ["- away, off; - aside;"], "orth": "a"}, {"pos": "V", "form": "V V", "senses": ["well, good"], "orth": "bene"}, {"pos": "V", "form": "V V", "senses": ["well, good;"], "orth": "beni"}, {"pos": "X", "form": "X X", "senses": ["two, twice; double; having two;"], "orth": "bis"}, {"pos": "X", "form": "X X", "senses": ["two, twice; double; having two;"], "orth": "bi"}, {"pos": "X", "form": "X X", "senses": ["sweet-, soothing-, smooth-, charming, flattering;"], "orth": "blandi"}, {"pos": "X", "form": "X X", "senses": ["cardio-, pertaining to the heart;"], "orth": "cardio"}, {"pos": "X", "form": "X X", "senses": ["hundred (numerical prefix);"], "orth": "centi"}, {"pos": "X", "form": "X X", "senses": ["hundred (numerical prefix);"], "orth": "centu"}, {"pos": "X", "form": "X X", "senses": ["- around, about, near;"], "orth": "circum"}, {"pos": "X", "form": "X X", "senses": ["- together, completely, forcibly, strongly;"], "orth": "col  l"}, {"pos": "X", "form": "X X", "senses": ["- together, completely, forcibly, strongly;"], "orth": "com"}, {"pos": "X", "form": "X X", "senses": ["- together, completely, forcibly, strongly;"], "orth": "conn  e"}, {"pos": "X", "form": "X X", "senses": ["- together, completely, forcibly, strongly;"], "orth": "conn  i"}, {"pos": "X", "form": "X X", "senses": ["- against;"], "orth": "contra"}, {"pos": "X", "form": "X X", "senses": ["- together; completely, strongly, forcibly, violently;"], "orth": "con"}, {"pos": "X", "form": "X X", "senses": ["- together; completely, strongly, forcibly, violently;"], "orth": "co"}, {"pos": "X", "form": "X X", "senses": ["ten (numerical prefix);"], "orth": "decem"}, {"pos": "X", "form": "X X", "senses": ["ten (numerical prefix);"], "orth": "decu"}, {"pos": "V", "form": "V V", "senses": ["- down, off, away, from; not; removal, reversal; utterly/completely (intensive);"], "orth": "de"}, {"pos": "V", "form": "V V", "senses": ["- apart/asunder, in different directions; separation/dispersal/process reversal;"], "orth": "dif f"}, {"pos": "V", "form": "V V", "senses": ["- apart/asunder, in different directions; separation/dispersal/process reversal;"], "orth": "dir"}, {"pos": "V", "form": "V V", "senses": ["- apart/asunder, in different directions; separation/dispersal/process reversal;"], "orth": "dis"}, {"pos": "N", "form": "N N", "senses": ["two-;"], "orth": "di"}, {"pos": "V", "form": "V V", "senses": ["- apart/asunder, in different directions; separation/dispersal/process reversal;"], "orth": "di"}, {"pos": "N", "form": "NUM NUM", "senses": ["- less two/two less than (numerical prefix); (duodeviginti => 20 less 2 = 18);"], "orth": "duode"}, {"pos": "N", "form": "NUM NUM", "senses": ["two more than (numerical prefix); (duoetviginti => two more than twenty = 22);"], "orth": "duoet"}, {"pos": "X", "form": "X X", "senses": ["two (numerical prefix);"], "orth": "du"}, {"pos": "V", "form": "V V", "senses": ["- out, away from; beyond; completely;"], "orth": "ef f"}, {"pos": "X", "form": "X X", "senses": ["electro-; electrical; electronic;"], "orth": "electro"}, {"pos": "V", "form": "V V", "senses": ["- outside;"], "orth": "extra"}, {"pos": "V", "form": "V V", "senses": ["- out, away from; beyond; completely;"], "orth": "ex"}, {"pos": "V", "form": "V V", "senses": ["- out, away from; beyond; completely;"], "orth": "e"}, {"pos": "X", "form": "X X", "senses": ["umequal;"], "orth": "inaequi"}, {"pos": "V", "form": "V V", "senses": ["between, within; at intervals, to pieces;"], "orth": "inter"}, {"pos": "N", "form": "N N", "senses": ["between, within; at intervals, to pieces;"], "orth": "inter"}, {"pos": "V", "form": "V V", "senses": ["within, inside; - between, at intervals, to pieces;"], "orth": "intra"}, {"pos": "V", "form": "V V", "senses": ["within, inside; - between, at intervals, to pieces;"], "orth": "intro"}, {"pos": "V", "form": "V V", "senses": ["- in, - on, - against; not -, un-;"], "orth": "ig n"}, {"pos": "N", "form": "N N", "senses": ["two-; second; (Roman numeral for 2); [IIviri/duoviri => 2 man board];"], "orth": "II"}, {"pos": "V", "form": "V V", "senses": ["- in, - on, - against; not -, un-;"], "orth": "il l"}, {"pos": "V", "form": "V V", "senses": ["- in, - on, - against; not -, un-;"], "orth": "im b"}, {"pos": "V", "form": "V V", "senses": ["- in, - on, - against; not -, un-;"], "orth": "im m"}, {"pos": "V", "form": "V V", "senses": ["- in, - on, - against; not -, un-;"], "orth": "im p"}, {"pos": "V", "form": "V V", "senses": ["- in, - on, - against; not -, un-;"], "orth": "in"}, {"pos": "A", "form": "ADJ ADJ", "senses": ["not -, un-, -less;"], "orth": "in"}, {"pos": "V", "form": "V V", "senses": ["- in, - on, - against; not -, un-;"], "orth": "ir r"}, {"pos": "V", "form": "V V", "senses": ["ill, bad;"], "orth": "male"}, {"pos": "N", "form": "N N", "senses": ["much, many;"], "orth": "multi"}, {"pos": "A", "form": "ADV ADV", "senses": ["not;"], "orth": "ne"}, {"pos": "V", "form": "V V", "senses": ["not;"], "orth": "non"}, {"pos": "V", "form": "V V", "senses": ["- towards, to meet, in opposition;"], "orth": "ob"}, {"pos": "X", "form": "X X", "senses": ["eight (numerical prefix);"], "orth": "octu"}, {"pos": "V", "form": "V V", "senses": ["- towards, to meet, in opposition;"], "orth": "of f"}, {"pos": "A", "form": "ADJ ADJ", "senses": ["all-, - everywhere;"], "orth": "omni"}, {"pos": "V", "form": "V V", "senses": ["- towards, to meet, in opposition;"], "orth": "op p"}, {"pos": "V", "form": "V V", "senses": ["- towards, to meet, in opposition;"], "orth": "os t"}, {"pos": "A", "form": "ADJ ADJ", "senses": ["very -, - completely, - thoroughly;"], "orth": "per"}, {"pos": "V", "form": "V V", "senses": ["- through, thoroughly, completely, very; adds to the force of the verb;"], "orth": "per"}, {"pos": "V", "form": "V V", "senses": ["- forward;"], "orth": "por"}, {"pos": "X", "form": "X X", "senses": ["past or by; (drive past, drive by, flow past, flow by);"], "orth": "praeter"}, {"pos": "X", "form": "X X", "senses": ["pre-, before -, in front of -; forth; very -, - completely, - thorughly;"], "orth": "prae"}, {"pos": "N", "form": "N N", "senses": ["before -, in front of -;"], "orth": "pro"}, {"pos": "V", "form": "V V", "senses": ["- forward; before; in front of; forth [pro-cedo => go forth, proceed, continue];"], "orth": "pro"}, {"pos": "X", "form": "X X", "senses": ["pseudo-, false; fallacious, deceitful; sperious; imitation of;"], "orth": "pseudo"}, {"pos": "X", "form": "X X", "senses": ["four (numerical prefix);"], "orth": "quadri"}, {"pos": "X", "form": "X X", "senses": ["four (numerical prefix);"], "orth": "quadru"}, {"pos": "X", "form": "X X", "senses": ["five (numerical prefix);"], "orth": "quincu"}, {"pos": "X", "form": "X X", "senses": ["five (numerical prefix);"], "orth": "quinqu"}, {"pos": "X", "form": "X X", "senses": ["five (numerical prefix);"], "orth": "quinti"}, {"pos": "V", "form": "V V", "senses": ["- back, - again;"], "orth": "red"}, {"pos": "X", "form": "X X", "senses": ["- back, - again;"], "orth": "re"}, {"pos": "V", "form": "V V", "senses": ["- apart, apart from; away;"], "orth": "sed"}, {"pos": "X", "form": "X X", "senses": ["semi-, half, partly;"], "orth": "semi"}, {"pos": "X", "form": "X X", "senses": ["seven (numerical prefix);"], "orth": "septem"}, {"pos": "X", "form": "X X", "senses": ["seven (numerical prefix);"], "orth": "septu"}, {"pos": "X", "form": "X X", "senses": ["one and half (numerical); one plus aliquot fraction; (sesqui-septimus = 8/7);"], "orth": "sesque"}, {"pos": "X", "form": "X X", "senses": ["one and half (numerical); one plus aliquot fraction; (sesqui-septimus = 8/7);"], "orth": "sesqui"}, {"pos": "X", "form": "X X", "senses": ["one and half (numerical); one plus aliquot fraction; (sesqui-septimus = 8/7);"], "orth": "sexqui"}, {"pos": "X", "form": "X X", "senses": ["six-;"], "orth": "ses"}, {"pos": "X", "form": "X X", "senses": ["six (numerical prefix);"], "orth": "sexti"}, {"pos": "X", "form": "X X", "senses": ["six (numerical prefix);"], "orth": "sextu"}, {"pos": "X", "form": "X X", "senses": ["six-;"], "orth": "sex"}, {"pos": "-", "form": "--V V", "senses": ["--- apart, apart from; away (se-cedo = go away, withdraw, secede);"], "orth": "-- se      --  conflict with semet"}, {"pos": "X", "form": "X X", "senses": ["one (numerical prefix), single, simple;"], "orth": "sim"}, {"pos": "V", "form": "V V", "senses": ["sub-; - up to, - under, up from under; to the aid;"], "orth": "sub"}, {"pos": "N", "form": "N N", "senses": ["sub-; somewhat -/-ish/rather -; under, from under/below; lesser/assistant/vice;"], "orth": "sub"}, {"pos": "A", "form": "ADJ ADJ", "senses": ["sub-; somewhat -/-ish/rather -; under, from under/below; lesser/assistant/vice;"], "orth": "sub"}, {"pos": "V", "form": "V V", "senses": ["- up to, - under, up from under; to the aid;"], "orth": "suc  c"}, {"pos": "N", "form": "N N", "senses": ["sub-; somewhat -/-ish/rather -; under, from under/below; lesser/assistant/vice;"], "orth": "suc c"}, {"pos": "A", "form": "ADJ ADJ", "senses": ["sub-; somewhat -/-ish/rather -; under, from under/below; lesser/assistant/vice;"], "orth": "suc c"}, {"pos": "X", "form": "X X", "senses": ["super-, over, above, upon; from above; over and above;"], "orth": "super"}, {"pos": "X", "form": "X X", "senses": ["supra-, over, above, upon, on top of; earlier than; beyond; superior to;"], "orth": "supra"}, {"pos": "X", "form": "X X", "senses": ["number plus 4/5; one plus aliquot fraction; (superquadripartiens = 9/5);"], "orth": "superquadri"}, {"pos": "V", "form": "V V", "senses": ["super-, over, above;"], "orth": "sur"}, {"pos": "V", "form": "V V", "senses": ["- up to, - under, up from under; to the aid;"], "orth": "sus s"}, {"pos": "V", "form": "V V", "senses": ["- across, - over;"], "orth": "trans"}, {"pos": "V", "form": "V V", "senses": ["- across, - over;"], "orth": "tra"}, {"pos": "V", "form": "V V", "senses": ["- across, - over;"], "orth": "tre i"}, {"pos": "X", "form": "X X", "senses": ["three; (also used to represent many times, persistant, extreme, gross);"], "orth": "tri"}, {"pos": "N", "form": "N N", "senses": ["beyond; exceeding; over; more than;"], "orth": "ultra"}, {"pos": "A", "form": "ADJ ADJ", "senses": ["extremely; more; overly; more than;"], "orth": "ultra"}, {"pos": "N", "form": "NUM NUM", "senses": ["- less one, one less than; (undetriginta => thirty less one = 29);"], "orth": "unde"}, {"pos": "A", "form": "ADJ ADJ", "senses": ["one-; having (only/but) one ~; (being) of one ~;"], "orth": "uni"}, {"pos": "A", "form": "ADJ ADJ", "senses": ["not- (vegrandis => small), without; very (vepallidus => very pale);"], "orth": "ve"}, {"pos": "N", "form": "N N", "senses": ["five-; fifth; (Roman numeral for 5);"], "orth": "V"}, {"pos": "N", "form": "N N", "senses": ["ten-; tenth; (Roman numeral for 10);"], "orth": "X"}],

	#
	# SUFFIX is a fragment added to the end of a stem to modify or
	# reinforce the meaning.  "tor" added to a verb gives the meaning
	# "doer of the action" (vincere = conquer, vic-tor = conqueror).  This
	# does not impact the addition of inflections on the end of the word.
	#
	# Each SUFFIX entry leads off with the identifier "SUFFIX".
	#
	# This is followed (separated by a space) by the suffix itself.
	#
	# In the formulation used by this program, there may be a connecting
	# character associated with the suffix.  For example, the prefix "itudo",
	# givs a noun adding the meaning "-ness", when applied to an adjective
	# stem.  If the adjective stem ends in "i", then the suffix is "ietudo".
	# The CONNECT character, if any, is placed after the suffix, on the same
	# line.
	#
	# Suffixes may be thought of as associated with a certain parts of
	# speech.  In many cases application of the suffix converts a stem
	# from one part of speech to a stem for another part of speech.
	# Further, the resulting verb, noun or adjective is of a particular
	# conjugation or declension.  This information is included on the
	# second line of the suffix record.
	#
	# The third line gives the meaning, using 78 characters or less.
	#
	# The order of this list is important.  The program checks in order.
	# The longer suffix should be placed earlier in the list.
	# This list is ordered on last character of suffix, but that is not significant.
	#
	# TO DO
	# ADJ derived from N could also be derived from ADJ (try to include N roots)
	# V can be formed from N stem, no suffix (Denominatives - to do/make _)
	# null suffixes Sinkovich p246
	#
	'suffixes' : [{"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "atic", "senses": ["-ic; -en; --ery; -al; made of; belonging to; has property of; is like;"]}, {"pos": "N", "form": "N 2 N 3 1 M P   2", "orth": "ific", "senses": ["denotes one who makes (the source noun), master of, professional in;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "tic", "senses": ["-ic; -en; --ery; -al; made of; belonging to; has property of; is like;"]}, {"pos": "V", "form": "V 4 N 3 1 F p  2", "orth": "ric", "senses": ["-or; -er; indicates the doer; one who preforms the action of the verb (act.or);"]}, {"pos": "V", "form": "V 2 V 3 1 X  1", "orth": "esc", "senses": ["begin to -, grow - (Inceptive or Inchoative) (esp. on 2nd declension verbs);"]}, {"pos": "V", "form": "V 2 V 3 1 X  2", "orth": "esc", "senses": ["begin to -, grow - (Inceptive or Inchoative) (esp. on 2nd declension verbs);"]}, {"pos": "X", "form": "X 2 ADJ 3 1 POS 2", "orth": "ac", "senses": ["-ing; having a tendency;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "ic", "senses": ["-ic; of, pertaining/belonging to; connected with; derived/coming from (place);"]}, {"pos": "V", "form": "V 2 V 3 1 X  1", "orth": "sc", "senses": ["begin to -, grow - (Inceptive or Inchoative);"]}, {"pos": "V", "form": "V 2 V 3 1 X  2", "orth": "sc", "senses": ["begin to -, grow - (Inceptive or Inchoative);"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "c i", "senses": ["-ic; of, pertaining/belonging to; connected with; derived/coming from (place);"]}, {"pos": "V", "form": "V 2 ADJ 1 1 POS 0", "orth": "abund", "senses": ["-bund; -ent; -ful; -ing; characteristic of; verbal ADJ of active force w/object;"]}, {"pos": "V", "form": "V 2 ADJ 1 1 POS 0", "orth": "ebund", "senses": ["-bund; -ent; -ful; -ing; characteristic of; verbal ADJ of active force w/object;"]}, {"pos": "V", "form": "V 2 ADJ 1 1 POS 0", "orth": "ibund", "senses": ["-bund; -ent; -ful; -ing; characteristic of; verbal ADJ of active force w/object;"]}, {"pos": "V", "form": "V 2 ADJ 1 1 POS 0", "orth": "cund", "senses": ["-ent; -ful; -ing; characteristic of; capacity or inclination;"]}, {"pos": "V", "form": "V 2 ADJ 1 1 POS 0", "orth": "id", "senses": ["-ous; tending to, in a condition of, in a state of;"]}, {"pos": "A", "form": "ADJ 2 ADV SUPER 0", "orth": "issime", "senses": ["-estily; -estly; most -ly, much -ly, very -ly;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "ace", "senses": ["of/made of (material); resembling (material); similar to, -like;"]}, {"pos": "N", "form": "N 2 ADV POS 1", "orth": "ose", "senses": ["-fully, -ily, -ly; -tiously;"]}, {"pos": "A", "form": "ADJ 4 ADV SUPER 0", "orth": "me", "senses": ["-estily; -estly; most -ly, much -ly, very -ly;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "e", "senses": ["make of;"]}, {"pos": "A", "form": "ADJ 2 ADV POS 1", "orth": "e", "senses": ["-ily; -ly;"]}, {"pos": "V", "form": "V 1 ADJ 0 0 SUPER 0", "orth": "antissi", "senses": ["most -ing, much -ing, makes ADJ SUPER of verb, ('a' stem is for V 1 0);"]}, {"pos": "V", "form": "V 1 ADJ 0 0 SUPER 0", "orth": "entissi", "senses": ["most -ing, much -ing, makes ADJ of verb, ('e' stem is for V 2/3);"]}, {"pos": "N", "form": "N 1 N 2 2 N t 0", "orth": "cini", "senses": ["-ing, -age; forms activity/profession of person (latro.cinium => brigandage);"]}, {"pos": "A", "form": "ADJ 2 ADJ 0 0 SUPER 4", "orth": "issi", "senses": ["-est, most ~, much ~, makes SUPER;"]}, {"pos": "V", "form": "V   4 ADJ 0 0 SUPER 4", "orth": "issi", "senses": ["makes a verb PERF PPL into an adjective SUPER (amat.issimus => most/much loved);"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "boni", "senses": ["of good;"]}, {"pos": "V", "form": "V 2 N 1 1 F t 0", "orth": "moni", "senses": ["-monia; act of; means of; result of;"]}, {"pos": "V", "form": "V 2 N 2 2 N t 0", "orth": "moni", "senses": ["-monia; act of; means of; result of;"]}, {"pos": "V", "form": "V 1 N 1 1 F t 0", "orth": "anti", "senses": ["-ance; state of; quality of; act of; (with 1st conj verbs);"]}, {"pos": "V", "form": "V 1 ADJ 0 0 COMP 0", "orth": "anti         --  Conflicts with another -anti-", "senses": ["more -ing, makes ADJ COMP of verb, ('a' stem is for V 1 0);"]}, {"pos": "V", "form": "V 1 N 1 1 F t 0", "orth": "enti", "senses": ["-ence; state of; quality of; act of; (with other than 1st conj verbs);"]}, {"pos": "V", "form": "V 1 ADJ 0 0 COMP 0", "orth": "enti", "senses": ["more -ing, makes ADJ COMP of verb, ('e' stem is for V 2/3);"]}, {"pos": "N", "form": "N 2 N 1 1 F t  0", "orth": "ari", "senses": ["place where (argent.aria = money place, bank); female agent (rare);"]}, {"pos": "N", "form": "N 2 N 2 2 N t  0", "orth": "ari", "senses": ["-arium, -ary; place where;"]}, {"pos": "N", "form": "N 2 N 2 1 M p  0", "orth": "ari", "senses": ["-er; -ist; dealer in thing, maker/artisan (argent.arius = money/silver changer);"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "ari", "senses": ["of, pertaining/belonging to; connected with; derived from; made of; -like;"]}, {"pos": "N", "form": "NUM 3 ADJ 1 1 POS 0", "orth": "ari", "senses": ["consisting of/containing X things; X each; (with number X); of X; digits wide;"]}, {"pos": "N", "form": "N 2 N 2 2 N t  0", "orth": "ori", "senses": ["-orium, -ory, -or; place where;"]}, {"pos": "V", "form": "V 4 ADJ 1 1 POS 0", "orth": "ori", "senses": ["-orous, -ory; having to do with, pretaining to; tending to;"]}, {"pos": "A", "form": "ADJ 2 N 1 1 F t  0", "orth": "iti", "senses": ["-ity, -ship, -ance, ility, ness; makes abstract noun of the adjective;"]}, {"pos": "A", "form": "ADJ 2 N 5 1 F t  0", "orth": "iti", "senses": ["-ity, -ship, -ance, ility, ness; makes abstract noun of the adjective;"]}, {"pos": "V", "form": "V   2 N 2 2 N t  0", "orth": "iti", "senses": ["-ity, -ship, -ance, ility, ness; makes abstract noun of the verb;"]}, {"pos": "A", "form": "ADJ 2 ADJ 0 0 SUPER 4", "orth": "li  l", "senses": ["-est, most ~, much ~, makes ADJ with stem ending in 'l' SUPER;"]}, {"pos": "A", "form": "ADJ 1 ADJ 0 0 SUPER 4", "orth": "ri  r", "senses": ["-est, most ~, much ~, makes ADJ with stem ending in 'r' SUPER;"]}, {"pos": "A", "form": "ADJ 2 N 1 1 F t  0", "orth": "ti", "senses": ["-ness, makes abstract noun;"]}, {"pos": "V", "form": "V 4 ADV POS 1", "orth": "i                      --  ?????????????", "senses": ["-ly; (use imagination! run -> hastily; strive -> eagerly; stand -> immediately);"]}, {"pos": "A", "form": "ADJ 2 N 1 1 F t  0", "orth": "i", "senses": ["-ness, -es, makes abstract noun;"]}, {"pos": "N", "form": "N 2 N 1 1 F t  0", "orth": "i", "senses": ["art or craft done by the person (abstract noun of person); office of, -ship;"]}, {"pos": "V", "form": "V 2 N 2 2 N t  0", "orth": "i", "senses": ["makes abstract noun of the verb; place/instrument/result of verb action;"]}, {"pos": "A", "form": "ADJ 2 ADJ 0 0 COMP 3", "orth": "i", "senses": ["-er, makes adjective comparative;"]}, {"pos": "V", "form": "V   4 ADJ 0 0 COMP 3", "orth": "i", "senses": ["makes a verb PERF PPL into an adjective COMP (amat.ior => more loved);"]}, {"pos": "X", "form": "X 2 ADJ 3 2 POS  0", "orth": "abil", "senses": ["-able, -ble; having the passive quality, able to, able to be;"]}, {"pos": "N", "form": "N 2 ADJ 3 2 POS 0", "orth": "atil", "senses": ["-il; of a, pertaining to a, in a condition of, in a state of;"]}, {"pos": "V", "form": "V 2 ADJ 3 2 POS  0", "orth": "ibil", "senses": ["-able, -ble; having the passive quality, able to, able to be; -ful;"]}, {"pos": "N", "form": "N 2 N 1 1 F x 0", "orth": "icul", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 2 1 M x 0", "orth": "icul", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 2 2 N x 0", "orth": "icul", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "V", "form": "V 2 ADJ 3 2 POS  0", "orth": "bil", "senses": ["-able, -ble; having the passive quality, able to, able to be; having ability;"]}, {"pos": "X", "form": "X 2 N 1 1 F t 0", "orth": "bul", "senses": ["forms noun of means, instrument; place;"]}, {"pos": "X", "form": "X 2 N 2 2 N t 0", "orth": "bul", "senses": ["forms noun of means, instrument; place;"]}, {"pos": "N", "form": "N 2 N 1 1 M p 0", "orth": "col", "senses": ["denotes one who inhabits/tills/worships;"]}, {"pos": "V", "form": "V 2 N 2 2 N t 0", "orth": "cul", "senses": ["denotes means or instrument or place for special purpose for action of V;"]}, {"pos": "N", "form": "N 2 N 1 1 F x 0", "orth": "ell", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl; !!!!!!!!"]}, {"pos": "N", "form": "N 2 N 2 1 M x 0", "orth": "ell", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 2 2 N x 0", "orth": "ell", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 1 1 F x 0", "orth": "ill", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 2 1 M x 0", "orth": "ill", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 2 2 N x 0", "orth": "ill", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 ADJ 3 2 POS 0", "orth": "al", "senses": ["-al; of a ~, pertaining to a ~, in a condition of ~, in a state of ~;"]}, {"pos": "V", "form": "V 2 ADJ 3 2 POS 0", "orth": "il", "senses": ["-able, -ble; having the passive quality, able to, able to be;"]}, {"pos": "N", "form": "N 2 ADJ 3 2 POS 0", "orth": "il", "senses": ["-il; of a ~, pertaining to a ~, in a condition of ~, in a state of ~;"]}, {"pos": "N", "form": "N 2 N 1 1 F x 0", "orth": "ol", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 2 1 M x 0", "orth": "ol", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 2 2 N x 0", "orth": "ol", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 1 1 F x 0", "orth": "ul", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 2 1 M x 0", "orth": "ul", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 N 2 2 N x 0", "orth": "ul", "senses": ["little, small, -let (Diminutive) target is of gender of root => decl;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "ul", "senses": ["-ulus; of a, pertaining to a, in a condition of, in a state of;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "itim", "senses": ["-itime, -tine, -tane; of, belonging to (esp. of place and time);"]}, {"pos": "X", "form": "X 2 ADV POS 1", "orth": "atim", "senses": ["_ by _; eg. step by step; little by little;"]}, {"pos": "X", "form": "X 2 ADV POS 1", "orth": "itim", "senses": ["_ by _; eg. vir.itim => man by man;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "tim", "senses": ["-itime, -tine, -tane; of, belonging to  (esp. of place and time);"]}, {"pos": "X", "form": "X 2 N 2 1 M T   0", "orth": "ism", "senses": ["-ism; makes noun of action/ideology/association/fellowship;"]}, {"pos": "A", "form": "ADJ 1 ADV POS 1", "orth": "um", "senses": ["-ly;"]}, {"pos": "A", "form": "ADJ 2 N 3 1 F t  2", "orth": "udin  t", "senses": ["-ness; makes abstract noun;"]}, {"pos": "V", "form": "V 4 N 3 1 F t  2", "orth": "sion", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  2", "orth": "sion", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 4 N 3 1 F t  2", "orth": "tion", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  2", "orth": "tion", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "N", "form": "N 2 N 2 1 M p 0", "orth": "ian", "senses": ["of/belonging to  [N -> ADJ] (Cicero -> Ciceronianus);"]}, {"pos": "V", "form": "V 2 N 3 2 N t 1", "orth": "men", "senses": ["act of; means of; result of;"]}, {"pos": "N", "form": "NUM 3 NUM 1 4 DIST 0 3", "orth": "ten", "senses": ["each/apiece/times/fold; (NUM DIST to a late Latin form, Xceni -> Xcenteni);"]}, {"pos": "V", "form": "V 2 N 3 2 N t 2", "orth": "min", "senses": ["act of; means of; result of;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  1", "orth": "don", "senses": ["act of or result of the action of the verb;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  1", "orth": "gon", "senses": ["act of or result of the action of the verb;"]}, {"pos": "V", "form": "V 4 N 3 1 F t  2", "orth": "ion", "senses": ["-ing, -ion, -ery; indicates the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  2", "orth": "ion", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "urn", "senses": ["-urnal, -ily, -y, -ing; of, belonging to  (esp. of place and time);"]}, {"pos": "N", "form": "NUM 2 N 2 1 M p 0", "orth": "an", "senses": ["soldiers of the Nth Legion;"]}, {"pos": "A", "form": "ADJ 2 ADJ 1 1 POS 0", "orth": "an", "senses": ["-anus; (indicates former gens when adopted into another, Sejus -> Sejanus);"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "an", "senses": ["-an, -ain; of, pertaining/belonging to; connected with; derived/coming from;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "en", "senses": ["-en, -ene; of, pertaining/belonging to; connected with; derived/coming from;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "in", "senses": ["-ine; -in; of, pertaining/belonging to; connected with; derived/coming from;"]}, {"pos": "N", "form": "N 2 N 1 1 F t 0", "orth": "in", "senses": ["-ing; art or craft (medic.ina = art of doctoring);"]}, {"pos": "A", "form": "ADJ 2 N 3 1 F t  1", "orth": "udo  t", "senses": ["-ness; makes abstract noun;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  1", "orth": "sio", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 4 N 3 1 F t  1", "orth": "sio", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  1", "orth": "tio", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 4 N 3 1 F t  1", "orth": "tio", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  1", "orth": "do", "senses": ["act of or result of the action of the verb;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  1", "orth": "go", "senses": ["act of or result of the action of the verb;"]}, {"pos": "V", "form": "V 2 N 3 1 F t  1", "orth": "io", "senses": ["-ing, -ion, -ery; the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 4 N 3 1 F t  1", "orth": "io", "senses": ["-ing, -ion, -ery; indicates the action or result of the action of the verb;"]}, {"pos": "V", "form": "V 2 ADV POS 1", "orth": "abiliter", "senses": ["-abaly;"]}, {"pos": "V", "form": "V 2 ADV POS 1", "orth": "ibiliter", "senses": ["-ibaly;"]}, {"pos": "N", "form": "N 2 ADV POS 1", "orth": "aliter", "senses": ["-ality, -ally;"]}, {"pos": "V", "form": "V 1 ADV POS 1", "orth": "anter", "senses": ["-ingly;"]}, {"pos": "V", "form": "V 1 ADV POS 1", "orth": "enter", "senses": ["-ingly;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 1", "orth": "ester", "senses": ["-urnal, -ily, -y, -ing; of, belonging to  (esp. of place and time);"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 2", "orth": "estr", "senses": ["-y; of the, of, belonging to  (esp. of place and time);"]}, {"pos": "A", "form": "ADJ 2 ADV POS 1", "orth": "iter", "senses": ["-ily; -ly;"]}, {"pos": "A", "form": "ADJ 2 ADJ 0 0 COMP  3", "orth": "ior", "senses": ["-er, more ~; makes ADJ POS into ADJ COMP;"]}, {"pos": "N", "form": "N 2 N 3 1 M P 0", "orth": "por", "senses": ["-'s boy; (slave's name adding -por for -puer to anme of master);"]}, {"pos": "X", "form": "X 2 N 3 4 N t 0", "orth": "ar", "senses": ["means/instrument/place for special purpose of N/V (calco/calcar - tread/spur);"]}, {"pos": "N", "form": "N 2 ADJ 3 2 POS 0", "orth": "ar", "senses": ["-ary; of a, pertaining to a; (-like?);"]}, {"pos": "V", "form": "V 2 N 2 2 N t 0", "orth": "br", "senses": ["denotes means or instrument;"]}, {"pos": "V", "form": "V 2 N 2 2 N t 0", "orth": "cr", "senses": ["denotes means or instrument or place for special purpose for action of V;"]}, {"pos": "A", "form": "ADJ 2 ADV POS 1", "orth": "er  t", "senses": ["-ly;"]}, {"pos": "V", "form": "V 4 N 3 1 M p  0", "orth": "or", "senses": ["-or; -er; indicates the doer; one who performs the action of the verb (act.or);"]}, {"pos": "V", "form": "V 2 N 3 1 M p  0", "orth": "or", "senses": ["the thing of the verb; result of; (abstract noun) amor = love, timor = fear;"]}, {"pos": "V", "form": "V 2 N 2 2 N t 0", "orth": "tr", "senses": ["means, instrument; place;"]}, {"pos": "N", "form": "N 2 N 1 1 F t  0", "orth": "ur", "senses": ["-ure, pertaining to, use of;"]}, {"pos": "N", "form": "N 4 N 1 1 F t  0", "orth": "ur", "senses": ["-ure, pertaining to, use of;"]}, {"pos": "A", "form": "ADJ 2 N 3 1 F t  1", "orth": "etas i", "senses": ["-ness, makes abstract noun;"]}, {"pos": "A", "form": "ADJ 2 N 3 1 F t  1", "orth": "itas", "senses": ["-ity; -ness, makes abstract noun of quality or condition;"]}, {"pos": "N", "form": "N 2 N 3 1 F t  1", "orth": "itas", "senses": ["-ness, condition of being; makes abstract noun (civ.itas = citizenship);"]}, {"pos": "X", "form": "X 2 ADV POS 1", "orth": "itus", "senses": ["of _; from the _; -ing;"]}, {"pos": "N", "form": "N 2 N 3 1 F t  1", "orth": "tas", "senses": ["-ness, condition of being; makes abstract noun;"]}, {"pos": "N", "form": "N 2 N 3 1 F t  1", "orth": "tus", "senses": ["-liness, makes abstract noun;"]}, {"pos": "V", "form": "V 1 ADJ 3 1 POS  1", "orth": "ans", "senses": ["-ing, makes ADJ of verb, equivalent to PRES ACTIVE PPL ('a' stem is for V 1 0);"]}, {"pos": "V", "form": "V 1 ADJ 3 1 POS  1", "orth": "ens", "senses": ["-ing, makes ADJ of verb, equivalent to PRES ACTIVE PPL ('e' stem is for V 2/3);"]}, {"pos": "N", "form": "N 2 N 1 1 F p 0", "orth": "iss", "senses": ["female (whatever the noun base was);"]}, {"pos": "A", "form": "ADJ 2 ADV COMP 0", "orth": "ius", "senses": ["more -ly; -ier;"]}, {"pos": "X", "form": "X 2 ADV POS 1", "orth": "tus", "senses": ["of _; from the _;"]}, {"pos": "N", "form": "N 2 N 3 1 F t 1", "orth": "es", "senses": ["result of; place of; (abstract noun);"]}, {"pos": "N", "form": "N 2 N 3 1 F t 2", "orth": "is", "senses": ["result of; place of; (abstract noun);"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "os", "senses": ["-ous, -ose; -some, full of; prone to; rich in; abounding in;"]}, {"pos": "A", "form": "ADJ 2 ADV POS  1", "orth": "us", "senses": ["-ly;"]}, {"pos": "A", "form": "ADJ 3 ADV COMP 0", "orth": "us", "senses": ["more -ly; -lier;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "olent", "senses": ["-olent; full of; prone to; rich in; abounding in;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "ulent", "senses": ["-ulent; full of; prone to; rich in; abounding in;"]}, {"pos": "V", "form": "V 2 N 2 2 N t 0", "orth": "ament", "senses": ["-ment; -ion; act of; instrument/equipment/means for ~ing; result of ~ing;"]}, {"pos": "V", "form": "V 2 N 2 2 N t 0", "orth": "ment", "senses": ["-ment; -ion; act of; instrument/equipment/means for ~ing; result of ~ing;"]}, {"pos": "V", "form": "V 4 N 3 1 F t  2", "orth": "etat i", "senses": ["-ness, makes abstract noun;"]}, {"pos": "A", "form": "ADJ 2 N 3 1 F t  2", "orth": "itat", "senses": ["-ity; -ness, makes abstract noun of quality or condition;"]}, {"pos": "N", "form": "N 2 N 3 1 F t  1", "orth": "itat", "senses": ["-ness, condition of being; makes abstract noun (civ.itas = citizenship);"]}, {"pos": "N", "form": "N 2 N 3 1 F t  1", "orth": "tat", "senses": ["-ness, condition of being; makes abstract noun;"]}, {"pos": "A", "form": "ADJ 2 N 3 1 F t  2", "orth": "tat", "senses": ["-ness, makes abstract noun;"]}, {"pos": "V", "form": "V 2 V 1 1 X 4", "orth": "tat", "senses": ["try to do -, keep doing -;"]}, {"pos": "N", "form": "N 2 N 3 1 F t  2", "orth": "tut", "senses": ["-liness, makes abstract noun;"]}, {"pos": "V", "form": "V 1 ADJ 3 1 POS  2", "orth": "ant", "senses": ["-ing, makes ADJ of verb, equivalent to PRES ACTIVE PPL ('a' stem is for V 1 0);"]}, {"pos": "V", "form": "V 1 ADJ 3 1 POS  2", "orth": "ent", "senses": ["-ing, makes ADJ of verb, equivalent to PRES ACTIVE PPL ('e' stem is for V 2/3);"]}, {"pos": "N", "form": "N 2 N 4 1 M t  0", "orth": "at", "senses": ["-ate, -ship, the office of; official body (consul.atus = consulate, consulship);"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "at", "senses": ["-ed, having, having a, provided with; -able;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "it", "senses": ["-ed, having, having a, provided with; -able;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "ut", "senses": ["-ed, having, having a, provided with; -able;"]}, {"pos": "V", "form": "V 4 V 1 1 X 1", "orth": "it", "senses": ["try to do -, keep doing - (Intensive/Iterative - forcible or iterative action);"]}, {"pos": "V", "form": "V 2 V 1 1 X 1", "orth": "it", "senses": ["try to do -, keep doing - (Intensive/Iterative - forcible or iterative action);"]}, {"pos": "V", "form": "V 2 V 1 1 X 1", "orth": "t", "senses": ["try to do -, keep doing - (Intensive/Iterative - forcible or iterative action);"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "t", "senses": ["-ed, having, having a, provided with; -able;"]}, {"pos": "N", "form": "N 2 ADJ 1 1 POS 0", "orth": "ativ", "senses": ["-ative; capable/worthy of;"]}, {"pos": "V", "form": "V 2 V 1 1 X 3", "orth": "tav", "senses": ["try to do -, keep doing -;"]}, {"pos": "V", "form": "V 2 ADJ 1 1 POS 0", "orth": "iv", "senses": ["-ive, -ed; tending to, pretaining to;"]}, {"pos": "V", "form": "V 4 ADJ 1 1 POS 0", "orth": "iv", "senses": ["-ive, -ed; having the passive tendency; having been ...-ed;"]}, {"pos": "N", "form": "N 2 N 3 1 M P   1", "orth": "ifex", "senses": ["denotes one who makes (the source noun), master of, professional in;"]}, {"pos": "V", "form": "V 4 N 3 1 F p  1", "orth": "rix", "senses": ["-ess, -or; -er; indicates the doer; one who performs action of verb (act.ess);"]}, {"pos": "X", "form": "X 2 ADJ 3 1 POS 1", "orth": "ax", "senses": ["-ing; having a tendency/ability;"]}],

	#
	# TACKON is a fragment added to the end of a word, after inflection
	# has been applied.  Just removing the tackon will give a reasonable word.
	# This does not impact the addition of inflections,
	# as opposed to SUFFIX, which is applied before the inflection.
	#
	# Each TACKON entry leads off with the identifier "TACKON".
	#
	# This is followed (separated by a space) by the tackon itself.
	#
	# The second line gives a PART_ENTRY, information on where this is tacked.
	# A TACKON does not change the part of speech or case from its base.
	#
	# The third line gives the meaning, using 78 characters or less.
	#
	# The order of this list is significant.  The program checks in order.
	# The longer or less frequent tackon should be placed earlier in the list.

	'tackons' : [
			{
				'orth' : "que",
				'pos' : "X",
				'senses' : ["-que = and (enclitic, translated before attached word); completes plerus/uter;"]
			},
			{
				'orth' : "ne",
				'pos' : "X",
				'senses' : ["-ne = is it not that (enclitic); or ...(introduces a question or alternative);"]
			},
			{
				'orth' : "ve",
				'pos' : "X",
				'senses' : ["-ve = or if you will (enclitic); or as you please; or; (rare)"]
			},
			{
				'orth' : "est",
				'pos' : "PRON 4 1 X",
				'senses' : ["-est = is, in a contraction; (idest = it/that is); (rare)"]
			}
		],

	#
	# TACKONS  that are not PACKONS   not w/qu PRONS
	#
	'not_packons' : [
			{
				'orth' : "cumque",
				'pos' : "ADJ 0 0 POS",
				'senses' : ["-ever/-soever; (for generalized/indefinite force); (what/how -> what/however);"]
			},
			{
				'orth' : "cunque",
				'pos' : "ADJ 0 0 POS",
				'senses' : ["-ever/-soever; (for generalized/indefinite force); (what/how -> what/however);"]
			},
			{
				'orth' : "cine",
				'pos' : "PRON 3 1 ADJECT",
				'senses' : ["TACKON w/hic this?   (hic + ce + ne (enclitic));"]
			},
			{
				'orth' : "pte",
				'pos' : "ADJ 1 0 POS",
				'senses' : ["TACKON ! (emphatic particle w/personal ADJ); (usually with ABL, suapte);"]
			},
			{
				'orth' : "ce",
				'pos' : "PRON 3 1 ADJECT",
				'senses' : ["TACKON w/hic this;"]
			},
			{
				'orth' : "modi",
				'pos' : "PRON 3 1 ADJECT",
				'senses' : ["TACKON w/GEN of ~ kind, sort, nature; (w/hic); [huiusmodi => of this sort];"]
			},
			{
				'orth' : "dem",
				'pos' : "PRON 4 2 DEMONS",
				'senses' : ["TACKON w/i-ea-id   idem => same;"]
			},
			{
				'orth' : "cum",
				'pos' : "PRON 5 0 PERS",
				'senses' : ["TACKON with (enclitic with PRON 5 0); [w/ABL  mecum => at my house/with me];"]
			},
			{
				'orth' : "vis",
				'pos' : "ADJ  1 1 POS",
				'senses' : ["TACKON (what)-ever (w/quantus) [quantusvis => of whatever size you like];"]
			},
			{
				'orth' : "met",
				'pos' : "PRON 5 0 PERS",
				'senses' : ["TACKON w/personal self, own; on subst PERS [meamet/egomet => my own/myself];"]
			},
			{
				'orth' : "familias",
				'pos' : "N  3 0 C P",
				'senses' : ["TACKON of the family/household; (archaic GEN); [pater~ => head of household];"]
			}
		],

	#
	# PACKONS
	# A special class of TACKONS, applied to qu- pronouns called PACKons
	#
	'packons' : [
			{
				'orth' : "cumque",
				'pos' : "PACK    1  0 REL",
				'senses' : ["PACKON w/qui => whoever; whatever; everyone who, all that, anything that;"]
			},
			{
				'orth' : "cunque",
				'pos' : "PACK    1  0 REL",
				'senses' : ["PACKON w/qui => whoever; whatever; everyone who, all that, anything that;"]
			},
			{
				'orth' : "que",
				'pos' : "PACK    1  0 INDEF",
				'senses' : ["PACKON w/qui => whoever it be; whatever; each, each one; everyone, everything;"]
			},
			{
				'orth' : "piam",
				'pos' : "PACK    1  0 INDEF",
				'senses' : ["PACKON w/qui =>  any/somebody, any, some, any/something;"]
			},
			{
				'orth' : "quam",
				'pos' : "PACK    1  0 INDEF",
				'senses' : ["PACKON w/quis =>  any; any man/person, anybody/anyone, any whatever, anything;"]
			},
			{
				'orth' : "dam",
				'pos' : "PACK    1  0 INDEF",
				'senses' : ["PACKON w/qui => certain; a certain (one); a certain thing;"]
			},
			{
				'orth' : "nam",
				'pos' : "PACK    1  0 INTERR",
				'senses' : ["PACKON w/qui => who then/in the world; which, I insist/meant; why/what pray;"]
			},
			{
				'orth' : "cum",
				'pos' : "PACK    1  0 INTERR",
				'senses' : ["PACKON w/qui pron with ABL => with what, with whom;"]
			},
			{
				'orth' : "vis",
				'pos' : "PACK    1  0 INDEF",
				'senses' : ["PACKON w/qui whoever it be, whomever you please; any/anything whatever;"]
			},
			{
				'orth' : "libet",
				'pos' : "PACK    1  0 INDEF",
				'senses' : ["PACKON w/qui-anyone; -whatever; what you will; no matter which;"]
			},
			{
				'orth' : "lubet",
				'pos' : "PACK    1  0 INDEF",
				'senses' : ["PACKON w/qui -anyone; -whatever; what you will; no matter which;"]
			},
		]
}
