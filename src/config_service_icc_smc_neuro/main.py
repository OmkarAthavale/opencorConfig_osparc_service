import json

with open(inputs)

config = {
  "simulation": {
    "Starting point": 60,
    "Ending point": 180,
    "Point interval": 1
  },
  "parameters": {
    "neural_input/x_i": 0.5,
    "neural_input/x_e": 0.5
  },
  "output": [
    "active_tension/T",
  ]
}

with open('config.json', 'w') as outfile:
    json.dump(config, outfile)