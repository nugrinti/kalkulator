# main.py
import sys
import numpy as np
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
                               QDialog, QSizePolicy, QTableWidget, QHeaderView, QPushButton, QInputDialog)
import qdarktheme

# UI Imports
from ui_menu_kalkulator import Ui_MainWindow
from ui_history_matrix import Ui_Dialog as Ui_MatrixHistory
from ui_spl_matrix import Ui_Dialog as Ui_SPLHistory
from ui_vektor_matrix import Ui_Dialog as Ui_VectorHistory

# Logic Imports (Pastikan file logic sudah di-update sesuai diskusi sebelumnya)
from matrix_logic import MatObj, format_matobj
from spl_logic import read_table_to_matrix, solve_gaussian, solve_inverse, solve_cramer
# Import fungsi vektor baru
from vektor_logic import (dot_product, cross_product, angle_between, 
                          vector_add, vector_sub, vector_norm, vector_projection)
from io_utils import export_to_file, import_from_file
from history_manager import add_history, load_history, clear_history
from quiz_manager import generate_matrix_quiz, generate_spl_quiz, generate_vector_quiz

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Kalkulator Scientific: Matriks, SPL, Vektor")
        self.setMinimumSize(1000, 750)
        
        # Inisialisasi dictionary objek
        self.objects = {}

        # Setup Tabs
        self.setup_matrix_tab()
        self.setup_spl_tab()
        self.setup_vector_tab()

    # ---------------------------
    # TAB 1: MATRIX
    # ---------------------------
    def setup_matrix_tab(self):
        # Tombol Operasi Dasar
        self.pushButton_add.clicked.connect(self.add_matrix_object)
        self.pushButton_evaluate.clicked.connect(self.evaluate_expression)
        
        # Tombol Manajemen File & History (Mapping nama tombol yang agak acak dari UI)
        self.btn_checkIdentity_2.clicked.connect(self.import_matrix)       # Import
        self.btn_checkIdentity_3.clicked.connect(self.export_matrix)       # Export
        self.btn_checkIdentity_4.clicked.connect(self.show_matrix_history) # History
        self.btn_checkIdentity_5.clicked.connect(self.quiz_matrix)         # Quiz
        self.btn_clearOutput.clicked.connect(lambda: self.textEdit_result.clear())

        # Tombol Analisis Matriks (Soal 1f)
        # Kita hubungkan semua tombol cek ke fungsi analisis umum karena logika baru sudah lengkap
        self.btn_checkIdentity.clicked.connect(self.analyze_matrix_properties)
        self.btn_checkLower.clicked.connect(self.analyze_matrix_properties)
        self.btn_checkUpper.clicked.connect(self.analyze_matrix_properties)
        self.btn_checkSparse.clicked.connect(self.analyze_matrix_properties)
        self.btn_checkZero.clicked.connect(self.analyze_matrix_properties)
        
        # Fitur Display (Opsional)
        self.btn_displayMatrix.clicked.connect(self.display_selected_matrix)

        # Setup Tabel Input
        self.tableWidget_matrix.setRowCount(self.spinBox_rows.value())
        self.tableWidget_matrix.setColumnCount(self.spinBox_cols.value())
        self.tableWidget_matrix.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.spinBox_rows.valueChanged.connect(self.update_matrix_table_size)
        self.spinBox_cols.valueChanged.connect(self.update_matrix_table_size)

        self.textEdit_result.setVisible(False)   # Kotak teks output hilang
        self.text_result.setVisible(False)       # Label "OUTPUT" hilang
        self.btn_clearOutput.setVisible(False)   # Tombol Clear hilang (tidak butuh lagi)

    def update_matrix_table_size(self):
        self.tableWidget_matrix.setRowCount(self.spinBox_rows.value())
        self.tableWidget_matrix.setColumnCount(self.spinBox_cols.value())

    def add_matrix_object(self):
        name = self.lineEdit_name.text().strip()
        if not name:
            QMessageBox.warning(self, "Input Error", "Nama objek harus diisi (misal: A, B).")
            return

        type_choice = self.comboBox_type.currentText()
        
        try:
            if type_choice == "Skalar":
                # --- LOGIKA SKALAR ---
                val = float(self.doubleSpinBox_scalar.value())
                obj = MatObj(val)
                
                self.objects[name] = obj
                self.listWidget_objects.addItem(f"{name} ({type_choice})")
                QMessageBox.information(self, "Berhasil", f"Skalar '{name}' bernilai {val} disimpan.")
                
            else:
                # --- LOGIKA MATRIKS (BACA DARI TABEL) ---
                rows = self.tableWidget_matrix.rowCount()
                cols = self.tableWidget_matrix.columnCount()
                data = []
                
                # Loop untuk membaca setiap sel tabel
                for i in range(rows):
                    row_data = []
                    for j in range(cols):
                        item = self.tableWidget_matrix.item(i, j)
                        # Ambil teks, jika kosong anggap 0.0
                        val = float(item.text()) if item and item.text() else 0.0
                        row_data.append(val)
                    data.append(row_data)
                
                obj = MatObj(np.array(data))
                
                self.objects[name] = obj
                self.listWidget_objects.addItem(f"{name} ({type_choice})")
                QMessageBox.information(self, "Berhasil", f"Matriks '{name}' disimpan sesuai input tabel.")
                
        except ValueError:
            QMessageBox.warning(self, "Error", "Pastikan input berupa angka valid.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Terjadi kesalahan: {e}")

    def evaluate_expression(self):
        expr = self.lineEdit_expression.text()
        if not expr:
            return
        try:
            context = self.objects.copy()
            context['np'] = np 
            
            result = eval(expr, {"__builtins__": None}, context)
            formatted_res = format_matobj(result)
            
            # Simpan ke history tetap jalan
            add_history("matrix", expr, formatted_res)
            
            # TAMPILKAN POP-UP HASIL
            # Kita gunakan style sheet minimalis agar font matriks (monospace) terlihat rapi
            msg = QMessageBox(self)
            msg.setWindowTitle("Hasil Evaluasi")
            msg.setText(f"Hasil '{expr}':")
            msg.setInformativeText(formatted_res)
            # Opsional: Set font monospace agar matriks lurus
            font = msg.font()
            font.setFamily("Courier New") 
            msg.setFont(font)
            msg.exec()
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error pada ekspresi:\n{e}")

    def analyze_matrix_properties(self):
        name = self.lineEdit_name.text().strip()
        if name in self.objects:
            obj = self.objects[name]
            # Memanggil method check_type() yang baru Anda buat di matrix_logic
            try:
                info = obj.check_type() 
                QMessageBox.information(self, f"Analisis {name}", f"Jenis Matriks: {info}")
            except AttributeError:
                 QMessageBox.warning(self, "Error", "Fungsi check_type belum ada di matrix_logic.py")
        else:
            QMessageBox.warning(self, "Error", "Nama matriks tidak ditemukan. Input nama di kolom 'Nama' lalu SET dulu, atau ketik nama yang sudah ada.")

    def display_selected_matrix(self):
        name = self.lineEdit_name.text().strip()
        if name in self.objects:
            content = str(self.objects[name])
            QMessageBox.information(self, f"Isi {name}", content)
        else:
            QMessageBox.warning(self, "Info", "Matriks belum dipilih/tidak ditemukan.")

    def import_matrix(self):
        file, _ = QFileDialog.getOpenFileName(self, "Import File", "", "Text Files (*.txt);;All Files (*)")
        if file:
            data = import_from_file(file)
            QMessageBox.information(self, "Data Loaded", f"Isi File:\n{data}")

    def export_matrix(self):
        file, _ = QFileDialog.getSaveFileName(self, "Export File", "", "Text Files (*.txt);;All Files (*)")
        if file:
            # Pastikan ekstensi .txt ada
            if not file.endswith('.txt'):
                file += '.txt'
            
            history_data = load_history()["matrix"]
            content = "=== HISTORY MATRIKS ===\n\n"
            for h in history_data:
                content += f"[{h['time']}]\nInput : {h['expression']}\nHasil :\n{h['result']}\n{'-'*30}\n"

            msg = export_to_file(file, content) # Kirim string content langsung
            QMessageBox.information(self, "Export", msg)

    def show_matrix_history(self):
        self.show_history_dialog(Ui_MatrixHistory, "matrix")

    def quiz_matrix(self):
        self.run_interactive_quiz("Kuis Matriks", generate_matrix_quiz)

    # ---------------------------
    # TAB 2: SPL
    # ---------------------------
    def setup_spl_tab(self):
        self.btn_displayMatrix_3.clicked.connect(self.solve_gaussian) # Gaussian
        self.btn_displayMatrix_4.clicked.connect(self.solve_inverse)  # Inverse
        self.btn_displayMatrix_5.clicked.connect(self.solve_cramer)   # Cramer
        
        self.btn_displayMatrix_13.clicked.connect(self.show_spl_history)
        self.btn_displayMatrix_18.clicked.connect(self.quiz_spl)
        self.btn_displayMatrix_6.clicked.connect(lambda: self.textEdit_result_3.clear())
        self.btn_displayMatrix_11.clicked.connect(self.import_spl)  # <--- Tombol Import
        self.btn_displayMatrix_12.clicked.connect(self.export_spl)  # <--- Tombol Export

        # Setup Tabel SPL
        self.tableWidget_matrix_3.setColumnCount(self.spinBox.value() + 1) # n variabel + 1 konstanta
        self.tableWidget_matrix_3.setRowCount(self.spinBox_2.value())
        self.tableWidget_matrix_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.spinBox.valueChanged.connect(self.update_spl_table)
        self.spinBox_2.valueChanged.connect(self.update_spl_table)

    def import_spl(self):
        file, _ = QFileDialog.getOpenFileName(self, "Import SPL", "", "Text Files (*.txt);;All Files (*)")
        if file:
            data = import_from_file(file)
            QMessageBox.information(self, "Data Loaded", f"Isi File:\n\n{data}")

    def export_spl(self):
        file, _ = QFileDialog.getSaveFileName(self, "Export SPL", "", "Text Files (*.txt);;All Files (*)")
        if file:
            if not file.endswith('.txt'): file += '.txt'
            # Ambil history SPL untuk diekspor
            history_data = load_history()["spl"]
            content = "=== HISTORY SPL ===\n\n"
            for h in history_data:
                content += f"[{h['time']}]\nMetode: {h['expression']}\nHasil:\n{h['result']}\n{'-'*30}\n"
            
            msg = export_to_file(file, content)
            QMessageBox.information(self, "Export", msg)

    def update_spl_table(self):
        rows = self.spinBox_2.value() # Jumlah Persamaan
        cols = self.spinBox.value()   # Jumlah Variabel
        self.tableWidget_matrix_3.setRowCount(rows)
        self.tableWidget_matrix_3.setColumnCount(cols + 1)
        
        # Set Header
        headers = [f"x{i+1}" for i in range(cols)] + ["="]
        self.tableWidget_matrix_3.setHorizontalHeaderLabels(headers)

    def solve_gaussian(self):
        A, B = read_table_to_matrix(self.tableWidget_matrix_3)
        res = solve_gaussian(A, B)
        self.textEdit_result_3.setText(f"Hasil Eliminasi Gauss:\n{res}")
        add_history("spl", "Gauss", str(res))

    def solve_inverse(self):
        A, B = read_table_to_matrix(self.tableWidget_matrix_3)
        res = solve_inverse(A, B)
        self.textEdit_result_3.setText(f"Hasil Matriks Invers:\n{res}")
        add_history("spl", "Inverse", str(res))

    def solve_cramer(self):
        A, B = read_table_to_matrix(self.tableWidget_matrix_3)
        res = solve_cramer(A, B)
        self.textEdit_result_3.setText(f"Hasil Aturan Cramer:\n{res}")
        add_history("spl", "Cramer", str(res))

    def show_spl_history(self):
        self.show_history_dialog(Ui_SPLHistory, "spl")

    def quiz_spl(self):
        self.run_interactive_quiz("Kuis SPL", generate_spl_quiz)

    # ---------------------------
    # TAB 3: VEKTOR
    # ---------------------------
    def setup_vector_tab(self):
        # Tombol Bawaan UI
        self.btn_displayMatrix_8.clicked.connect(self.vec_dot)
        self.btn_displayMatrix_7.clicked.connect(self.vec_cross)
        self.btn_displayMatrix_10.clicked.connect(self.vec_angle)
        
        self.btn_displayMatrix_16.clicked.connect(self.show_vector_history)
        self.btn_displayMatrix_17.clicked.connect(self.quiz_vector)
        self.btn_displayMatrix_9.clicked.connect(lambda: self.textEdit_result_4.clear())

        # --- MENAMBAHKAN TOMBOL YANG HILANG SECARA PROGRAMATIS ---
        # Karena UI Designer belum punya tombol +, -, Proyeksi, dll
        
        # Tombol Tambah (A + B)
        self.btn_vec_add = QPushButton("A + B")
        self.gridLayout_4.addWidget(self.btn_vec_add, 6, 0) 
        self.btn_vec_add.clicked.connect(self.vec_add)

        # Tombol Kurang (A - B)
        self.btn_vec_sub = QPushButton("A - B")
        self.gridLayout_4.addWidget(self.btn_vec_sub, 6, 1)
        self.btn_vec_sub.clicked.connect(self.vec_sub)

        # Tombol Proyeksi (Proj u v)
        self.btn_vec_proj = QPushButton("Proyeksi A ke B")
        self.gridLayout_4.addWidget(self.btn_vec_proj, 6, 2)
        self.btn_vec_proj.clicked.connect(self.vec_proj)

        # Tombol Panjang/Norm (Norm A)
        self.btn_vec_norm = QPushButton("|A| (Norm)")
        self.gridLayout_4.addWidget(self.btn_vec_norm, 5, 2) # Taruh di sebelah angle/quiz
        self.btn_vec_norm.clicked.connect(self.vec_norm_a)

        self.btn_vec_norm_b = QPushButton("|B| (Norm)")     # <--- TOMBOL BARU: Norm B
        self.gridLayout_4.addWidget(self.btn_vec_norm_b, 5, 3)
        self.btn_vec_norm_b.clicked.connect(self.vec_norm_b)

        # Tombol Kombinasi Linear (Solusi Soal 4a: 3u - 2v)
        self.btn_vec_lin_comb = QPushButton("k1.A + k2.B")  # <--- TOMBOL BARU
        self.gridLayout_4.addWidget(self.btn_vec_lin_comb, 6, 3)
        self.btn_vec_lin_comb.clicked.connect(self.vec_linear_combination)

        self.btn_displayMatrix_14.clicked.connect(self.import_vector) # <--- Tombol Import
        self.btn_displayMatrix_15.clicked.connect(self.export_vector) # <--- Tombol Export

    # 2. Tambahkan fungsi logika baru ini di dalam class MainApp:
    def import_vector(self):
        file, _ = QFileDialog.getOpenFileName(self, "Import Vektor", "", "Text Files (*.txt);;All Files (*)")
        if file:
            data = import_from_file(file)
            QMessageBox.information(self, "Data Loaded", f"Isi File:\n\n{data}")

    def export_vector(self):
        file, _ = QFileDialog.getSaveFileName(self, "Export Vektor", "", "Text Files (*.txt);;All Files (*)")
        if file:
            if not file.endswith('.txt'): file += '.txt'
            # Ambil history Vektor untuk diekspor
            history_data = load_history()["vector"]
            content = "=== HISTORY VEKTOR ===\n\n"
            for h in history_data:
                content += f"[{h['time']}]\nOperasi: {h['expression']}\nHasil:\n{h['result']}\n{'-'*30}\n"
            
            msg = export_to_file(file, content)
            QMessageBox.information(self, "Export", msg)

    def get_vectors(self):
        return self.lineEdit.text(), self.lineEdit_2.text()

    def vec_add(self):
        a, b = self.get_vectors()
        res = vector_add(a, b)
        self.textEdit_result_4.setText(f"A + B =\n{res}")
        add_history("vector", "Add", str(res))

    def vec_sub(self):
        a, b = self.get_vectors()
        res = vector_sub(a, b)
        self.textEdit_result_4.setText(f"A - B =\n{res}")
        add_history("vector", "Sub", str(res))
    
    def vec_dot(self):
        a, b = self.get_vectors()
        res = dot_product(a, b)
        self.textEdit_result_4.setText(f"Dot Product =\n{res}")
        add_history("vector", "Dot", str(res))

    def vec_cross(self):
        a, b = self.get_vectors()
        res = cross_product(a, b)
        self.textEdit_result_4.setText(f"Cross Product =\n{res}")
        add_history("vector", "Cross", str(res))

    def vec_angle(self):
        a, b = self.get_vectors()
        res = angle_between(a, b)
        self.textEdit_result_4.setText(f"Sudut =\n{res}")
        add_history("vector", "Angle", str(res))

    def vec_proj(self):
        a, b = self.get_vectors()
        res = vector_projection(a, b) # Proyeksi A ke B
        self.textEdit_result_4.setText(f"Proyeksi A ke B =\n{res}")
        add_history("vector", "Projection", str(res))

    def vec_norm_a(self):
        a, _ = self.get_vectors()
        res = vector_norm(a)
        self.textEdit_result_4.setText(f"Panjang (Norm) A =\n{res}")
        add_history("vector", "Norm", str(res))

    def vec_norm_b(self):   # <--- FUNGSI BARU
        _, b = self.get_vectors()
        res = vector_norm(b)
        self.textEdit_result_4.setText(f"Panjang (Norm) B =\n{res}")
        add_history("vector", "Norm B", str(res))
        
    def vec_linear_combination(self): # <--- SOLUSI SOAL 4a (3u - 2v)
        a_str, b_str = self.get_vectors()
        
        # Minta input Skalar k1 (untuk A)
        k1, ok1 = QInputDialog.getDouble(self, "Input Skalar A", "Masukkan nilai k1 (untuk k1 * A):", 1.0, -1000, 1000, 2)
        if not ok1: return

        # Minta input Skalar k2 (untuk B)
        k2, ok2 = QInputDialog.getDouble(self, "Input Skalar B", "Masukkan nilai k2 (untuk k2 * B):", 1.0, -1000, 1000, 2)
        if not ok2: return

        try:
            # Panggil fungsi logic untuk hitung (parse -> kali -> tambah)
            # Kita lakukan manual disini menggunakan fungsi parse_vector dari vektor_logic
            from vektor_logic import parse_vector # Import lokal agar aman
            
            vec_a = parse_vector(a_str)
            vec_b = parse_vector(b_str)
            
            # Operasi: (k1 * A) + (k2 * B)
            result = (k1 * vec_a) + (k2 * vec_b)
            
            output_msg = f"Hasil {k1}A + {k2}B =\n{result}"
            self.textEdit_result_4.setText(output_msg)
            add_history("vector", f"{k1}A + {k2}B", str(result))
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal menghitung kombinasi linear:\n{e}")

    def show_vector_history(self):
        self.show_history_dialog(Ui_VectorHistory, "vector")

    def quiz_vector(self):
        self.run_interactive_quiz("Kuis Vektor", generate_vector_quiz)

    # ---------------------------
    # HELPER UMUM
    # ---------------------------
    def show_history_dialog(self, UiClass, mode):
        dialog = QDialog(self)
        ui = UiClass()
        ui.setupUi(dialog)
        
        # Load history
        data = load_history()[mode]
        # Sesuaikan nama widget textEdit yang beda-beda di tiap file UI
        text_widget = getattr(ui, "textEdit", None) or getattr(ui, "textEdit_2", None)
        
        if text_widget:
            content = "\n".join(f"[{h['time']}] {h['expression']} = {h['result']}" for h in data)
            text_widget.setPlainText(content)
        
        # Tombol Clear & Close (sesuaikan nama tombol di UI masing-masing)
        # Mencoba menebak nama tombol berdasarkan pola yang ada
        btn_clear = getattr(ui, "pushButton_add_2", None) or getattr(ui, "pushButton_add_4", None)
        btn_close = getattr(ui, "pushButton_add_3", None) or getattr(ui, "pushButton_add_5", None)

        if btn_clear:
            btn_clear.clicked.connect(lambda: [clear_history(mode), text_widget.clear()])
        if btn_close:
            btn_close.clicked.connect(dialog.close)
            
        dialog.exec()

    # --- HELPER BARU UNTUK KUIS INTERAKTIF ---
    def run_interactive_quiz(self, title, quiz_generator):
        """Menampilkan soal dulu, jawaban muncul setelah klik tombol"""
        q, ans = quiz_generator()
        
        # 1. Buat Dialog Soal
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(f"SOAL:\n{q}")
        msg.setIcon(QMessageBox.Question)
        
        # 2. Bikin Tombol Custom
        # Ganti tombol OK standar jadi "Lihat Jawaban"
        btn_lihat = msg.addButton("Jawaban", QMessageBox.AcceptRole)
        btn_tutup = msg.addButton("Menyerah", QMessageBox.RejectRole)
        
        # 3. Tampilkan Dialog
        msg.exec()
        
        # 4. Cek Tombol mana yang diklik user
        if msg.clickedButton() == btn_lihat:
            # Tampilkan Jawaban di Pop-up baru
            QMessageBox.information(self, f"Jawaban {title}", f"Jawabannya adalah:\n\n{ans}")
# -------------------------------
# ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))
    window = MainApp()
    window.show()
    sys.exit(app.exec())