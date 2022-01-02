import rock_paper_scissors
from sys import stderr, stdin, stdout
import io

def testGame(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('r'))
    rock_paper_scissors.play()
   # monkeypatch.setattr('sys.stdin', io.StringIO('r'))
    captured = capsys.readouterr()
    assert captured.out == "Input choice: 'r' for rock, 'p' for paper, 's' for scissors.\nRock it is!\n"