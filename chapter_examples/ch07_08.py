### Example 7-8: Keeping track of a value between calls

def findnext(string, substring, startpos=0):
    """Return the position of the next nonoverlapping occurrence of
    substring in string, beginning at startpos where substring
    appears"""
    pos = string.find(substring, startpos)
    if pos < 0:
        return -1, -1
    else:
        return pos, pos + len(substring)

def findeach(string, substring):
    positions = []
    pos, startpos = findnext(string, substring)
    while pos >= 0:
        positions.append(pos)
        pos, startpos = findnext(string, substring, startpos)
    return positions

if __name__ == '__main__':
    seq = """
MPPCSEKTLKDIEEIFLKFRRKKKWEDLIRYLKYKQPKCVKTFNLTGTGHKYHAMWAYNPITDKREKKQI
SLDVMKIQELHRITNNNSKLYVEIRKIMTDDHRCPCEEIKNYMQQIAEYKNNRSNKVFNTPPTKIVPNAL
EKILKNFTINLMIDKKPKKKITKSAHTIKHPPVLNIDYEHTLEFAGQTTVKEICKHASLGDTIEIQNRSF
DEMVNLYTTCVQCKQMYKIQ"""
    seq = seq.replace('\n', '')
    subseq = 'KKK'

    startpos, endpos = findnext(seq, subseq)
    assert_equal((21, 24), (startpos, endpos))
    startpos, endpos = findnext(seq, subseq, endpos)
    assert_equal((157, 160), (startpos, endpos))
    print('Done.')
          
