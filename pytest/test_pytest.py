from rock_paper_scissors import play
from sys import stderr, stdin, stdout
import io

def testGame(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('r'))
    play()
    stdout , stderr = capsys.readouterr()
    assert stdout == 'Tie buddy'