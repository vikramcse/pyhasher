import hashlib
import sys
import getopt

hasher = hashlib.md5()
BLOCK_SIZE = 65536

def hash_file(file_name):
	with open(file_name, 'rb') as the_file_in_binary:
		buffer = the_file_in_binary.read(BLOCK_SIZE)
		if len(buffer) > 0:
			hasher.update(buffer)
			buffer = the_file_in_binary.read(BLOCK_SIZE)

	return hasher.hexdigest()

def hash_with_match(file_name, hash):
	file_hash = hash_file(file_name)
	if file_hash == hash:
		print 'matched'
	else:
		print 'match failed :('

def print_help():
	print 'hasher -f <inputfile>'
	print 'hasher -f <inputfile> -m <hashstring>'

def parse_args():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:m:")
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)

    file_name = None
    hash = None
    is_hash = False

    for o in opts:
    	if o[0] == '-h':
    		print_help()
    	elif o[0] == '-f':
    		file_name = o[1]
    	elif o[0] == '-m':
    		is_hash = True
    		hash = o[1]

    if is_hash and hash and file_name:
    	hash_with_match(file_name, hash)
    elif not is_hash and file_name:
    	print hash_file(file_name)
    else:
    	print_help()

parse_args()