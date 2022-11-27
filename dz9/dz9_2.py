class TextProcessor(object):
    str_punctuation = ".,;:-!?""()/"

    @classmethod
    def __is_punctuation(cls, sym):
        if sym in TextProcessor.str_punctuation:
            s = True
        else:
            s = False
        return s

    def get_clean_string(self, text):
        clean_text = ""
        for sym in text:
            if self.__is_punctuation(sym):
                continue
            clean_text += sym
        return clean_text


class TextLoader(TextProcessor):
    def set_clean_text(self, text):
        self.__clean_string = self.get_clean_string(text)

    @property
    def clean_string(self):
        print(f"Output the cleaned text: {self.__clean_string}")
        return self.__clean_string


class DataInterface(TextLoader):
    def process_texts(self, texts):
        clean_text = []
        for text in texts:
            self.set_clean_text(text)
            clean = self.clean_string
            clean_text.append(clean)
        return clean_text


d = DataInterface()
text = ["P.y,t;h:o-n", "П.a(й)т!о?н", "D.a,t;a: S.c,i/e!n?c-e"]
d.process_texts(text)
