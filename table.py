class Table():
    def generate_graph(self, sauration, nodes):
        if saturation > 1 and sauration < 0:
            print("Saturation must be a value between [0, 1].")
            return None
        