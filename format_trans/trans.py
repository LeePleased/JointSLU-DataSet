from collections import Counter

def transform(in_file, out_file):

	with open(in_file, 'r') as fr:
		lines = fr.readlines()

	with open(out_file, 'w') as fw:
		start = False
		count = Counter()

		for line in lines:

			if start:
				items = line.strip().split()

				if len(items) > 1:
					fw.write(line)
					count[items[-1]] += 1
				else:
					item = count.most_common(1)[0][0]
					fw.write(item + '\t' + items[0] + '\n')

					count.clear()
					start = False
			else:
				fw.write(line)

				if len(line) > 2:
					start=True

if __name__ == "__main__":
	transform('./error_samples.txt', './test_result.txt')



