import simplejson as json

test_dict = {'1':95}

print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))