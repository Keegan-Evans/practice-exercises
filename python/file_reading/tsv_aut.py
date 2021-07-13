import os
import pathlib

_ConcretePath = type(pathlib.Path())

class Eagle(_ConcretePath):
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        return self


class Bald(Eagle):
    def __new__(cls, path):
        self = super().__new__(cls, path)
        return self
    def open(self, mode='r', buffering=-1, encoding=None, errors=None,
             newline=None):
        return super().open(mode=mode, buffering=buffering, encoding=encoding,
                            errors=errors, newline=newline)
    def print_contents(self):
        with self.open() as fh:
            for line in fh:
                print(line)



class Groker(_ConcretePath):
    def __new__(cls, path, *args, **kwargs):
        self = super().__new__(cls, path, *args, **kwargs)
        return self

    def __init__(self, path=None, mode=None, comment_character: str = '#',
            headerless: bool = False, sep: str = '\t'):
        if path is None:
            raise ValueError('Provide path.')
        if mode is None:
            raise ValueError('No mode specified')
        self._path = path
        self._mode = mode
        self._comment_char = comment_character
        self._headerless = headerless
        self._sep = sep

    def open(self, mode='r', buffering=-1, encoding='utf-8', errors=None,
             newline=None):
        return super().open(mode=mode, buffering=buffering, encoding=encoding,
                            errors=errors, newline=newline)

    def print_contents(self):
        with self.open() as fh:
            for line in fh:
                print(line)

    def _get_feature_labels_and_data_index(self):
        with self.open() as fh:
            # givs starting point
            prev_line = self._comment_char

            for i, line in enumerate(fh, 0):
                if prev_line[0] == self._comment_char and line[0] != self._comment_char:
                    self.first_data_line = i
                    self.feature_labels = prev_line.split(sep = self._sep)
                    #self.feature_labels = self._strip_comment_characters(
                    #    self.feature_labels
                    #    )
                    self._strip_comment_characters(self.feature_labels)
                elif line[0] != self._comment_char:
                    prev_line = line
                    continue
                else:
                    prev_line = line
                    print(line)

        print(self.first_data_line)
        print(self.feature_labels)

    # implement this as a descriptor/property so that it automatically does
    # this when you set the feature labels
    def _strip_comment_characters(self, feats):
        for i, element in enumerate(feats, 0):
            feats[i] = element.strip(self._comment_char)




if __name__ == '__main__':
    print('loaded')
    b = Groker(path='tests/data/sample_tsv.tsv', mode='r')
    print(b._mode)
    b.print_contents()

    x = Bald( path='tests/data/sample_csv.csv')

    with x.open() as fh:
        for line in fh:
            print(line)
    x.print_contents()
    b._get_feature_labels_and_data_index()
    y, z = b.first_data_line, b.feature_labels
    print('Index of first dataline: %s' % (y))
    print('All feature columns:')
    for feature in z:
        print(feature)
# sketched logic for data lines
#prev_line = '#'
#    first_data_line = int()
#    feature_labels = []
#    for i, line in enumerate(fh, 0):
#        first_char = line[0]
#        if first_char != '#' and prev_line[0] == '#':
#            first_data_line = i
#            feature_labels = prev_line.split('t')
#            prev_line = line
#            print(line.split('\t'))
#        elif first_char != '#':
#            prev_line = line
#            print(line)
#        else:
#            prev_line = line
#            continue
#    print(first_data_line)
#    print(feature_labels)
#
#
