class Category:
    """Класс для представления категории расходов/доходов."""

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Category({self.name})"