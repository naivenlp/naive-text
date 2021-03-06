import unittest

from naive_text.sentence import SentenceSegmenter


class SentenceSegmenterTest(unittest.TestCase):

    def test_cut_sentence(self):
        s = SentenceSegmenter()
        paragraph = [
            "史卡肯表示:「我今天打的和当初在温布登打的一样, 除了这一次幸运之神落在我这边以外。",
            "他说:「其实在温布登时最后的胜利也有可能属于我,因为当时打到了第五盘却仍然僵持在二十比十八的对峙。",
            "菲利普西斯在当初的温布登比赛中,在面对史卡肯时曾经发出四十四个爱司球,但是为他搏得「重炮手」美誉的发球,并没有在今天的球赛中助他一臂之力。",
            "菲利普西斯在第一盘第七局以三十比四十落后时,竟然击出双发失误;另外在第九局他又再度犯下双发失误球,让史卡肯得以坐拥两次的破发点,并且顺利赢得第一盘。",
            "在这场历时六十六分钟的比赛里,史卡肯表示:「我大力主攻他的第二发球,同时我也对他的第一发球施压,使我取得更多的机会。」",
            "这也是史卡肯和菲利普西斯在六度对峙中的第二次获胜。"]
        for idx, sent in enumerate(s.cut(''.join(paragraph))):
            print('No.{} sentence: {}'.format(idx, sent))


if __name__ == "__main__":
    unittest.main()
