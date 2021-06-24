import os
import sys

def test_a():
    print('yep')

def subset_with_comprehension(in_fp, out_fp, desired_index):
    try:
        fh = open(in_fp, 'r')
        fw = open(out_fp, 'w')

        for line in fh:
            print(line)
            elements = line.split('\t')
            print(elements)
            #selected = [element.rstrip() for i, element in enumerate(line.split(sep='\t').rstrip(), 0)]
            print(selected)
            fw.writelines(selected)

    finally:
        fh.close()
        fw.close()

if __name__ == '__main__':
    
    in_fp = sys.argv[1]
    out_fp = sys.argv[2]
    desired_index = [0, 2,]
    subset_with_comprehension(in_fp=in_fp,out_fp=out_fp, desired_index=desired_index)
