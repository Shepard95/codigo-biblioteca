class Libro:
    def __init__(self, id, titulo, autor, isbn, disponibilidad):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponibilidad = disponibilidad

    # Getters class libro
    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_isbn(self):
        return self._isbn

    def get_disponibilidad(self):
        return self._disponibilidad

    # Setters
    def set_id(self, id):
        self._id = id

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_autor(self, autor):
        self._autor = autor

    def set_isbn(self, isbn):
        self._isbn = isbn

    def set_disponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad

    # Método para buscar por ISBN
    @staticmethod
    def buscar_por_isbn(lista_libros, isbn):
        for libro in lista_libros:
            if libro.get_isbn() == isbn:
                return libro
        return None
