from ..base import DBTestCase, sqlite_only, postgres_only
from ..example_project.tables import Band


class TestInstance(DBTestCase):
    """
    Test instantiating Table instances
    """

    @postgres_only
    def test_insert_postgres(self):
        Pythonistas = Band(name="Pythonistas")
        self.assertEqual(
            Pythonistas.__str__(), "(DEFAULT,null,'Pythonistas',0)"
        )

    @sqlite_only
    def test_insert_sqlite(self):
        Pythonistas = Band(name="Pythonistas")
        self.assertEqual(
            Pythonistas.__str__(), "(null,null,'Pythonistas',0)"
        )

    def test_non_existant_column(self):
        with self.assertRaises(ValueError):
            Band(name="Pythonistas", foo="bar")
