import unittest

from naive_text.normalizer import TextNormalizer


class NormalizerTest(unittest.TestCase):

    def test_normlize_text(self):
        tn = TextNormalizer()
        for txt in ['當轉換有兩個以上的字詞可能時,程式只會使用第一個。', 'HelloWORLD!']:
            print(tn.normalize(txt, to_simplified=True, to_half_width=True))
            print(tn.normalize(txt, to_simplified=True, to_full_width=True))
            print(tn.normalize(txt, to_simplified=True, to_full_width=True, to_full_width_chars=[',']))


if __name__ == "__main__":
    unittest.main()
