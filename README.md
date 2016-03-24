# pyhasher
command line md5 hash maker and checker

```sh
python hasher.py -f file.txt
// -> 1700f2a5a6d64e12857041c0d11db5dc

python hasher.py -f file.txt -m 1700f2a5a6d64e12857041c0d11db5dc
// -> matched
```

## Usage
```
	hasher -h
	hasher -f <inputfile>
	hasher -f <inputfile> -m <hashstring>
```

- `inputfile`: A file that you want to create hash
- `hashstring`: A hash string for matching with given file

