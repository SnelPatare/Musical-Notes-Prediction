#constants
SIXTEENTH = '16'
EIGHTH = '8'
QUARTER = '4'
HALF = '2'
WHOLE = '1'

A1 = 'a'
B1 = 'b'
C1 = 'c'
D1 = 'd'
E1 = 'e'
F1 = 'f'
G1 = 'g'

A2 = 'a\''
B2 = 'b\''
C2 = 'c\''
D2 = 'd\''
E2 = 'e\''
F2 = 'f\''
G2 = 'g\''

class LilyPondHandler():
    def __init__(self,file_text=None,file_name=None,version=None):
        self.file_text = file_text
        self.file_name = file_name
        self.version = version
        if (version is None):
            self.version = '2.22.2'

    def create_file(self, file_name=None):
        if (file_name is not None):
            self.file_name = file_name
        else:
            file_name = self.file_name
        if (file_name[-3:] != ".ly"):
            print(f"Warning: {file_name} does not end in .ly.")
        self.file_text = "\\version \"" + self.version + "\"\n{ "

    def save_file(self):
        with open(self.file_name,"w") as f:
            f.write(self.file_text + "}\n")

    def append_note(self, note, duration):
        self.file_text += note + duration + " "
