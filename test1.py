# Test 1
# ------
#
# Given the 2 lists a and b, produce a distinct list c that contains only the
# words that are shared by the 2 lists and let the list be sorted by number of
# characters in the words. Shortest words first in the list.


def common_obj(list_a, list_b):
    """ function produces list with common entries sorted by number of characters """
    c = {x for x in list_a if x in list_b}
    return sorted(c, key=len)


if __name__ == '__main__':
    a = ['century', 'customer', 'democratic', 'Congress', 'customer', 'evening',
         'often', 'outside', 'reveal', 'weight', 'western', 'century']
    b = ['weapon', 'western', 'traditional', 'guess', 'customer', 'exist',
         'democratic', 'Congress', 'evening', 'finish', 'western', 'executive']
    print(common_obj(a, b))
