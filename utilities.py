import math
import music21

initial_tempo = 50

chords = {
	'I':{
		'root': 48, 
		'chord':[60, 64, 67, 72]
	},
	'vi':{
		'root': 57, 
		'chord':[60, 64, 69, 72]
	},
	'IVc':{
		'root': 53,
		'chord':[60, 65, 69, 72]
	},
	'ii7':{
		'root': 50,
		'chord':[62, 65, 69, 72]
	},
	'IVb':{
		'root': 53,
		'chord':[57, 60, 65, 69]
	},
	'iic':{
		'root': 50,
		'chord':[57, 62, 65, 69]
	},
	'V7c':{
		'root': 55,
		'chord':[62, 65, 67, 71]
	},
	'V7/V':{
		'root': 50,
		'chord':[62, 66, 69, 72]
	},
	'V7/ii':{
		'root': 57,
		'chord':[57, 61, 64, 67]
	},
	'V7c/vi':{
		'root': 62,
		'chord':[59, 62, 64, 68]
	}
}


state_transitions = {
	1:{
		'turn': 1,
		'transitions':{
			1:{
				'destination': 2,
				'chord': 'I',
				'transitionType': 'major',
			},
			2:{
				'destination': 3,
				'chord': 'vi',
				'transitionType': 'minor',
			}
		}
	},
	2:{
		'turn': 2,
		'transitions':{
			3:{
				'destination': 4,
				'chord': 'IVc',
				'transitionType': 'major',
			},
			4:{
				'destination': 5,
				'chord': 'ii7',
				'transitionType': 'major',
			}
		}
	},
	3:{
		'turn': 2,
		'transitions':{
			3:{
				'destination': 6,
				'chord': 'IVb',
				'transitionType': 'minor',
			},
			4:{
				'destination': 7,
				'chord': 'iic',
				'transitionType': 'minor',
			}
		}
	},
	4:{
		'turn': 3,
		'transitions':{
			5:{
				'destination': 8,
				'chord': 'V7c',
				'transitionType': 'major',
			},
			6:{
				'destination': 9,
				'chord': 'V7/V',
				'transitionType': 'major',
			}
		}
	},
	5:{
		'turn': 3,
		'transitions':{
			5:{
				'destination': 10,
				'chord': 'V7/V',
				'transitionType': 'major',
			},
			6:{
				'destination': 11,
				'chord': 'V7c',
				'transitionType': 'major',
			}
		}
	},
	6:{
		'turn': 3,
		'transitions':{
			5:{
				'destination': 12,
				'chord': 'V7/ii',
				'transitionType': 'minor',
			},
			6:{
				'destination': 13,
				'chord': 'V7c/vi',
				'transitionType': 'minor',
			}
		}
	},
	7:{
		'turn': 3,
		'transitions':{
			5:{
				'destination': 14,
				'chord': 'V7c/vi',
				'transitionType': 'minor',
			},
			6:{
				'destination': 15,
				'chord': 'V7/ii',
				'transitionType': 'minor',
			}
		}
	},
	8:{
		'turn': 1,
		'transitions':{
			1:{
				'destination': 17,
				'chord': 'I',
				'transitionType': 'major_cadence',
			},
			2:{
				'destination': 18,
				'chord': 'vi',
				'transitionType': 'minor_deceptive',
			}
		}
	},
	9:{
		'turn': 1,
		'transitions':{
			1:{
				'destination': 16,
				'chord': 'I',
				'transitionType': 'major_modulation',
			},
			2:{
				'destination': 18,
				'chord': 'vi',
				'transitionType': 'minor_deceptive',
			}
		}
	},
	10:{
		'turn': 1,
		'transitions':{
			1:{
				'destination': 16,
				'chord': 'I',
				'transitionType': 'major_modulation',
			},
			2:{
				'destination': 18,
				'chord': 'vi',
				'transitionType': 'minor_deceptive',
			}
		}
	},
	11:{
		'turn': 1,
		'transitions':{
			1:{
				'destination': 17,
				'chord': 'I',
				'transitionType': 'major_cadence',
			},
			2:{
				'destination': 18,
				'chord': 'vi',
				'transitionType': 'minor_deceptive',
			}
		}
	},
	12:{
		'turn': 1,
		'transitions':{
			1:{
				'destination': 19,
				'chord': 'I',
				'transitionType': 'major_deceptive',
			},
			2:{
				'destination': 21,
				'chord': 'vi',
				'transitionType': 'minor_modulation',
			}
		}
	},
	13:{
		'turn': 1,
		'transitions':{
			1:{
				'destination': 19,
				'chord': 'I',
				'transitionType': 'major_deceptive',
			},
			2:{
				'destination': 20,
				'chord': 'vi',
				'transitionType': 'minor_cadence',
			}
		}
	},
	14:{
		'turn': 1,
		'transitions':{
			1:{
				'destination': 19,
				'chord': 'I',
				'transitionType': 'major_deceptive',
			},
			2:{
				'destination': 20,
				'chord': 'vi',
				'transitionType': 'minor_cadence',
			}
		}
	},
	15:{
		'turn': 1,
		'transitions':{
			1:{
				'destination': 19,
				'chord': 'I',
				'transitionType': 'major_deceptive',
			},
			2:{
				'destination': 21,
				'chord': 'vi',
				'transitionType': 'minor_modulation',
			}
		}
	},
	16:{
		'turn': 2,
		'transitions':{
			3:{
				'destination': 4,
				'chord': 'IVc',
				'transitionType': 'major',
			},
			4:{
				'destination': 5,
				'chord': 'ii7',
				'transitionType': 'major',
			}
		}
	},
	17:{
		'turn': 2,
		'transitions':{
			3:{
				'destination': 4,
				'chord': 'IVc',
				'transitionType': 'major',
			},
			4:{
				'destination': 5,
				'chord': 'ii7',
				'transitionType': 'major',
			}
		}
	},
	18:{
		'turn': 2,
		'transitions':{
			3:{
				'destination': 6,
				'chord': 'IVb',
				'transitionType': 'minor',
			},
			4:{
				'destination': 7,
				'chord': 'iic',
				'transitionType': 'minor',
			}
		}
	},
	19:{
		'turn': 2,
		'transitions':{
			3:{
				'destination': 4,
				'chord': 'IVc',
				'transitionType': 'major',
			},
			4:{
				'destination': 5,
				'chord': 'ii7',
				'transitionType': 'major',
			}
		}
	},
	20:{
		'turn': 2,
		'transitions':{
			3:{
				'destination': 6,
				'chord': 'IVb',
				'transitionType': 'minor',
			},
			4:{
				'destination': 7,
				'chord': 'iic',
				'transitionType': 'minor',
			}
		}
	},
	21:{
		'turn': 2,
		'transitions':{
			3:{
				'destination': 6,
				'chord': 'IVb',
				'transitionType': 'minor',
			},
			4:{
				'destination': 7,
				'chord': 'iic',
				'transitionType': 'minor',
			}
		}
	},
}


def traverse(commandlist, state=1):
	maximum_parts = 2
	tempo = initial_tempo	
	score = music21.stream.Score()
	parts = [music21.stream.Part(), music21.stream.Part()]	
	openMeasure = False
	match = 1
	print 'Current state {}'.format(state)
	for idx,command in enumerate(commandlist):
		turn = state_transitions[state]['turn']
		if turn == 1 and not openMeasure:
			openMeasure = True
			for i in range(maximum_parts):
				if i == 0:
					measures = [music21.stream.Measure()]
				else:
					measures.append(music21.stream.Measure())
				measures[i].timeSignature = music21.meter.TimeSignature('3/4')				
				
		if command in state_transitions[state]['transitions']:
			transition = state_transitions[state]['transitions'][command]
			new_state = transition['destination']
			chord = transition['chord']
			transitionType = transition['transitionType']
			instruments = getInstruments(transitionType)
			tempo = getTempo(transitionType, tempo)
			print 'Transition: {} -> {}, playing {} with {} and {}, in {} pattern'.format(state, new_state, chord, instruments[0], instruments[1], transitionType)
			state = new_state
			voice_list = musicalizeTransition(chords[chord]['root'], chords[chord]['chord'], transitionType)
			for idx,voice in enumerate(voice_list):
				measures[idx].append(voice)				
			for idx in range(maximum_parts):			
				measures[idx].insert(float(turn-1), instruments[idx])
			if turn == 3:
				measures[0].insert(0.0, music21.tempo.MetronomeMark(number=tempo))
				parts[0].append(measures[0])
				parts[1].append(measures[1])
				openMeasure = False
		else:
			print 'Invalid command {} in state {}. No transition performed.'.format(command, state)
	print 'Finished parsing commands'
	if openMeasure:
		parts[0].append(measures[0])
		parts[1].append(measures[1])
	score.append(parts)
	#score.makeMeasures(inPlace=True)
	score.show()


def getTempo(transitionType, tempo):
	if transitionType == 'major_deceptive' or transitionType == 'minor_deceptive':
		tempo = tempo+10
	if transitionType == 'major_cadence' or transitionType == 'minor_cadence' or transitionType == 'major_modulation' or transitionType == 'minor_modulation':
		tempo = initial_tempo
	return tempo


def getInstruments(transitionType):
	instruments = []
	if transitionType == 'major' or transitionType == 'major_cadence' or transitionType == 'major_deceptive' or transitionType == 'major_modulation':
		instruments.append(music21.instrument.Harp())
		instruments.append(music21.instrument.Harp())
	elif transitionType == 'minor' or transitionType == 'minor_cadence' or transitionType == 'minor_deceptive' or transitionType == 'minor_modulation':
		instruments.append(music21.instrument.Harp())
		instruments.append(music21.instrument.Harp())
	return instruments
'''
def traverse_all(state=1):
	print 'Starting from state {}'.format(state)
	for transitionCmd in state_transitions[state]['transitions']:
		transition = state_transitions[state]['transitions'][transitionCmd]
		new_state = transition['destination']
		chord = transition['chord']
		transitionType = transition['transitionType']		
		print ''
'''

def musicalizeTransition(root=0, chord=[], transitionType='major'):
	bassnote = music21.pitch.Pitch(root+12)
	notelist = [music21.pitch.Pitch(x+12) for x in chord]
	rh = []
	lh = []

	if len(notelist) != 4:
		print 'Warning: I will only consider the first 4 notes of the chord'
	if transitionType == 'major' or transitionType == 'minor' or transitionType == 'major_deceptive' or transitionType == 'minor_deceptive':
		rh.append(music21.note.Rest(type='32nd'))
		rh.append(music21.note.Note(notelist[0], type='32nd'))
		rh.append(music21.note.Note(notelist[1], type='32nd'))
		rh.append(music21.note.Note(notelist[2], type='32nd'))
		rh.append(music21.note.Note(notelist[3], type='32nd'))
		rh.append(music21.note.Note(notelist[2], type='32nd'))
		rh.append(music21.note.Note(notelist[1], type='32nd'))
		rh.append(music21.note.Note(notelist[0], type='32nd'))
		lh.append(music21.note.Note(bassnote, type='quarter'))
	elif transitionType == 'major_cadence' or transitionType == 'minor_cadence' or transitionType == 'major_modulation' or transitionType == 'minor_modulation':
		rh.append(music21.note.Rest(type='32nd'))
		rh.append(music21.note.Note(notelist[0], type='32nd'))
		rh.append(music21.note.Note(notelist[1], type='32nd'))
		rh.append(music21.note.Note(notelist[2], type='32nd'))
		rh.append(music21.note.Note(notelist[3], type='32nd'))
		rh.append(music21.note.Note(notelist[2], type='32nd'))
		rh.append(music21.note.Note(notelist[1], type='32nd'))
		rh.append(music21.note.Note(notelist[0], type='32nd'))
		lh.append(music21.chord.Chord([bassnote]+notelist, type='16th'))
		lh.append(music21.note.Rest(type='16th'))
		lh.append(music21.note.Rest(type='16th'))
		lh.append(music21.note.Rest(type='16th'))
	return [rh, lh]


traverse([1,3,5,2,3,5,1,3,5,2,3,5,6])

traverse([
	1,3,5,
	1,3,5,
	2,3,5,
	2,3,5,
	1,3,6,
	1,3,6,
	2,3,6,
	2,3,6,
	1,4,5,
	1,4,5,
	2,4,5,
	2,4,5,
	1,4,6,
	1,4,6,
	2,4,6,
	2,4,6,])