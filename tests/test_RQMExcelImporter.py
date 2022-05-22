import unittest
from os.path import exists
from src import RQMExcelImporter

class TestConvertWithTwoFiles(unittest.TestCase):

    def test_with_two_files_example(self):

        files = [
            'exampleFiles/Pesquisar_curso.rqms',
            'exampleFiles/Pesquisar_disciplina_pre-requisito.rqms'
        ]

        RQMExcelImporter.convert(files[0], 'result01')
        RQMExcelImporter.convert(files[1], 'result02')

        self.assertEqual(
            exists('result01.xlsx') and exists('result02.xlsx'), 
            True, 
            "Should be two excel files"
        )