import math
#import music21

chords = {
	'I':{
		'root': 48, 
		'arpeggio':[60, 64, 67, 72]
	},
	'vi':{
		'root': 57, 
		'arpeggio':[60, 64, 69, 72]
	},
	'IVc':{
		'root': 53,
		'arpeggio':[60, 65, 69, 72]
	},
	'ii7':{
		'root': 50,
		'arpeggio':[62, 65, 69, 72]
	},
	'IVb':{
		'root': 53,
		'arpeggio':[57, 60, 65, 69]
	},
	'iic':{
		'root': 50,
		'arpeggio':[57, 62, 65, 69]
	},
	'V7c':{
		'root': 55,
		'arpeggio':[62, 65, 67, 71]
	},
	'V7/V':{
		'root': 50,
		'arpeggio':[62, 66, 69, 72]
	},
	'V7/ii':{
		'root': 57,
		'arpeggio':[57, 61, 64, 67]
	},
	'V7c/vi':{
		'root': 62,
		'arpeggio':[59, 62, 64, 68]
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
				'chord': 'ii',
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
				'chord': 'ii',
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
	print 'Current state {}'.format(state)
	for command in commandlist:
		if command in state_transitions[state]['transitions']:
			transition = state_transitions[state]['transitions'][command]
			new_state = transition['destination']
			chord = transition['chord']
			transitionType = transition['transitionType']
			print 'Transition: {} -> {}, playing {} in {} pattern'.format(state, new_state, chord, transitionType)
			state = new_state
		else:
			print 'Invalid command {} in state {}. No transition performed.'.format(command, state)
	print 'Finished parsing commands'


traverse([1, 3, 5, 1, 3, 5, 1])

