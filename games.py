class Games:
    def __init__(self, data, codes_set):
        self.data = data
        self.codes_set = codes_set

    def get_game_options(self, code):
        options = {}

        for row in range(self.data['Код'].shape[0]):
            if self.data['Код'][row] == code:
                for key in self.data:
                    options[key] = self.data[key][row]

        return options
