import collections

ValidatorRecord = collections.namedtuple(
    'ValidatorRecord', ['validator', 'holder', 'sem_types'])

SemanticTypeRecord = collections.namedtuple(
    'SemanticTypeRecord', ['semantic_type', 'plugin', 'validators'])

class Holder:
    def __init__(self, name):
        self.name = name

        self.validators = {}
        self.semantic_types = {}

    def reg_sem(self, sem_type):
        if sem_type in self.semantic_types:
            print('%s already in %s' % (sem_type, self.semantic_types))
        else:
            self.semantic_types[sem_type] = SemanticTypeRecord(
                semantic_type=sem_type, plugin=self, validators =[])

    def reg_val(self, sem_types: list):

        def decorator(validator):

            for semantic_type in sem_types:
                if semantic_type not in self.semantic_types:
                    raise TypeError("%s is not a semantic_type" %
                                    semantic_type)

                self.semantic_types[semantic_type][2].append(validator)
            return validator

        return decorator

if __name__ == '__main__':

    g = Holder(name='g')

    example_list = ['a', 'b', 'c']

    for exp in example_list:
        g.reg_sem(exp)

    @g.reg_val(example_list)
    def check_even(in_list: list):
        for each in in_list:
            if each % 2 == 0:
                continue
            else:
                return False

        return True

    print(g.__dict__)

    even_checked_expected_good = g.validators['check_even'][0]([2, 4, 6])
    even_checked_expected_bad = g.validators['check_even'][0]([0, 3, 5])

    print(even_checked_expected_good)
    print(even_checked_expected_bad)
