# main.py
import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QSizePolicy, QTableWidget, QHeaderView
import qdarktheme

# UI dan modul logic
from ui_menu_kalkulator import Ui_MainWindow
from ui_history_matrix import Ui_Dialog as Ui_MatrixHistory
from ui_spl_matrix import Ui_Dialog as Ui_SPLHistory
from ui_vektor_matrix import Ui_Dialog as Ui_VectorHistory

from matrix_logic import MatObj, penjumlahan, pengurangan, perkalian, format_matobj
from spl_logic import read_table_to_matrix, solve_gaussian, solve_inverse, solve_cramer
from vektor_logic import dot_product, cross_product, angle_between
from io_utils import export_to_file, import_from_file
from history_manager import add_history, load_history, clear_history
from quiz_manager import generate_matrix_quiz, generate_spl_quiz, generate_vector_quiz


# -------------------------------
#  KELAS UTAMA
# -------------------------------
class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Kalkulator Multifungsi: Matriks, SPL, Vektor")
        # Perbesar ukuran jendela utama
        self.setMinimumSize(1000, 700)
        # Atur tab Matriks agar layout menyesuaikan
        self.tabWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Event handler untuk setiap tab
        self.setup_matrix_tab()
        self.setup_spl_tab()
        self.setup_vector_tab()

    # ---------------------------
    # TAB 1: MATRIX
    # ---------------------------
    def setup_matrix_tab(self):
        self.pushButton_add.clicked.connect(self.add_matrix_object)
        self.pushButton_evaluate.clicked.connect(self.evaluate_expression)
        self.btn_checkIdentity_2.clicked.connect(self.import_matrix)
        self.btn_checkIdentity_3.clicked.connect(self.export_matrix)
        self.btn_checkIdentity_4.clicked.connect(self.show_matrix_history)
        self.btn_checkIdentity_5.clicked.connect(self.quiz_matrix)
        self.btn_clearOutput.clicked.connect(lambda: self.textEdit_result.clear())

        # Pastikan tabel bisa diisi manual
        self.tableWidget_matrix.setRowCount(self.spinBox_rows.value())
        self.tableWidget_matrix.setColumnCount(self.spinBox_cols.value())
        self.tableWidget_matrix.setEditTriggers(QTableWidget.AllEditTriggers)
        self.tableWidget_matrix.setSelectionBehavior(QTableWidget.SelectItems)
        self.tableWidget_matrix.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_matrix.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.spinBox_rows.valueChanged.connect(self.update_matrix_table_size)
        self.spinBox_cols.valueChanged.connect(self.update_matrix_table_size)

        self.objects = {}

    def update_matrix_table_size(self):
        rows = self.spinBox_rows.value()
        cols = self.spinBox_cols.value()
        self.tableWidget_matrix.setRowCount(rows)
        self.tableWidget_matrix.setColumnCount(cols)

    def add_matrix_object(self):
        name = self.lineEdit_name.text().strip()
        if not name:
            QMessageBox.warning(self, "Input Error", "Nama objek harus diisi.")
            return

        type_choice = self.comboBox_type.currentText()
        if type_choice == "Skalar":
            value = float(self.doubleSpinBox_scalar.value())
            obj = MatObj(value)
        else:
            m = self.spinBox_rows.value()
            n = self.spinBox_cols.value()
            data = np.random.randint(1, 10, (m, n))  # sementara auto-random
            obj = MatObj(data)

        self.objects[name] = obj
        self.listWidget_objects.addItem(name)
        QMessageBox.information(self, "Berhasil", f"{type_choice} '{name}' ditambahkan.")

    def evaluate_expression(self):
        expr = self.lineEdit_expression.text()
        if not expr:
            QMessageBox.warning(self, "Error", "Masukkan ekspresi terlebih dahulu.")
            return
        try:
            safe_locals = {**self.objects, "penjumlahan": penjumlahan,
                           "pengurangan": pengurangan, "perkalian": perkalian}
            expr_eval = expr.replace("+", ".__add__(").replace("-", ".__sub__(").replace("*", ".__mul__(")
            result = eval(expr, {"__builtins__": None}, self.objects)
            self.textEdit_result.setText(format_matobj(result.value))
            add_history("matrix", expr, format_matobj(result.value))
        except Exception as e:
            self.textEdit_result.setText(f"Error: {e}")

    def import_matrix(self):
        file, _ = QFileDialog.getOpenFileName(self, "Import File", "", "JSON Files (*.json)")
        if file:
            data = import_from_file(file)
            self.textEdit_result.setText(str(data))

    def export_matrix(self):
        file, _ = QFileDialog.getSaveFileName(self, "Export File", "", "JSON Files (*.json)")
        if file:
            content = self.textEdit_result.toPlainText()
            msg = export_to_file(file, {"result": content})
            QMessageBox.information(self, "Export", msg)

    def show_matrix_history(self):
        dialog = QDialog(self)
        ui = Ui_MatrixHistory()
        ui.setupUi(dialog)

        data = load_history()["matrix"]
        ui.textEdit.setPlainText("\n".join(f"{h['time']} | {h['expression']} = {h['result']}" for h in data))

        ui.pushButton_add_2.clicked.connect(lambda: [clear_history("matrix"), ui.textEdit.clear()])
        ui.pushButton_add_3.clicked.connect(dialog.close)
        dialog.exec()

    def quiz_matrix(self):
        q, ans = generate_matrix_quiz()
        QMessageBox.information(self, "Kuis Matriks", f"{q}\n\nJawaban:\n{ans}")

    # ---------------------------
    # TAB 2: SPL
    # ---------------------------
    def setup_spl_tab(self):
        self.btn_displayMatrix_3.clicked.connect(self.solve_gaussian)
        self.btn_displayMatrix_4.clicked.connect(self.solve_inverse)
        self.btn_displayMatrix_5.clicked.connect(self.solve_cramer)
        self.btn_displayMatrix_13.clicked.connect(self.show_spl_history)
        self.btn_displayMatrix_18.clicked.connect(self.quiz_spl)

    def solve_gaussian(self):
        A, B = read_table_to_matrix(self.tableWidget_matrix_3)
        result = solve_gaussian(A, B)
        self.textEdit_result_3.setText(str(result))
        add_history("spl", "Gaussian", str(result))

    def solve_inverse(self):
        A, B = read_table_to_matrix(self.tableWidget_matrix_3)
        result = solve_inverse(A, B)
        self.textEdit_result_3.setText(str(result))
        add_history("spl", "Inverse", str(result))

    def solve_cramer(self):
        A, B = read_table_to_matrix(self.tableWidget_matrix_3)
        result = solve_cramer(A, B)
        self.textEdit_result_3.setText(str(result))
        add_history("spl", "Cramer", str(result))

    def show_spl_history(self):
        dialog = QDialog(self)
        ui = Ui_SPLHistory()
        ui.setupUi(dialog)
        data = load_history()["spl"]
        ui.textEdit.setPlainText("\n".join(f"{h['time']} | {h['expression']} = {h['result']}" for h in data))
        ui.pushButton_add_2.clicked.connect(lambda: [clear_history("spl"), ui.textEdit.clear()])
        ui.pushButton_add_3.clicked.connect(dialog.close)
        dialog.exec()

    def quiz_spl(self):
        q, ans = generate_spl_quiz()
        QMessageBox.information(self, "Kuis SPL", f"{q}\n\nJawaban:\n{ans}")

    # ---------------------------
    # TAB 3: VECTOR
    # ---------------------------
    def setup_vector_tab(self):
        self.btn_displayMatrix_8.clicked.connect(self.dot)
        self.btn_displayMatrix_7.clicked.connect(self.cross)
        self.btn_displayMatrix_10.clicked.connect(self.angle)
        self.btn_displayMatrix_16.clicked.connect(self.show_vector_history)
        self.btn_displayMatrix_17.clicked.connect(self.quiz_vector)

    def dot(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        res = dot_product(a, b)
        self.textEdit_result_4.setText(str(res))
        add_history("vector", "Dot", str(res))

    def cross(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        res = cross_product(a, b)
        self.textEdit_result_4.setText(str(res))
        add_history("vector", "Cross", str(res))

    def angle(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        res = angle_between(a, b)
        self.textEdit_result_4.setText(str(res))
        add_history("vector", "Angle", str(res))

    def show_vector_history(self):
        dialog = QDialog(self)
        ui = Ui_VectorHistory()
        ui.setupUi(dialog)
        data = load_history()["vector"]
        ui.textEdit_2.setPlainText("\n".join(f"{h['time']} | {h['expression']} = {h['result']}" for h in data))
        ui.pushButton_add_4.clicked.connect(lambda: [clear_history("vector"), ui.textEdit_2.clear()])
        ui.pushButton_add_5.clicked.connect(dialog.close)
        dialog.exec()

    def quiz_vector(self):
        q, ans = generate_vector_quiz()
        QMessageBox.information(self, "Kuis Vektor", f"{q}\n\nJawaban:\n{ans}")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))
    window = MainApp()
    window.show()
    sys.exit(app.exec())
