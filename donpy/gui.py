import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QComboBox,
    QPushButton,
    QLabel,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QGridLayout,
)
from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize, Qt
from PIL.ImageQt import ImageQt
from process import process
import bitmap

choosen_key = ""
choosen_cypher_i = 0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Оценка качества шифротекста")
        self.setMinimumSize(QSize(500, 300))

        widgetQCB = QComboBox()  # Здесь выбираем шифрование
        widgetQCB.addItems(["Виженер", "AES-256", "Цезарь", "Плейфер", "Вычислить из файла"])
        widgetQCB.currentIndexChanged.connect(
            self.index_changed
        )  # Отправляет текущий индекс (позицию) выбранного элемента.

        widgetQLE = QLineEdit()
        widgetQLE.setMaxLength(256)
        widgetQLE.setPlaceholderText("Введите ключ")
        widgetQLE.textChanged.connect(self.text_changed)

        self.widgetQLbl = QLabel("Энтропия")
        self.widgetQLbl.setText(
            "Рост энтропии:\n"
            + "Дисперсия N-грамм исходного текста:\n"
            + "Дисперсия N-грамм шифротекста: "
        )

        widgetQBt = QPushButton("Высчитать энтропию")
        widgetQBt.setCheckable(True)
        widgetQBt.clicked.connect(self.the_button_was_clicked)

        self.widgetQLimg1 = QLabel()
        qim = ImageQt(bitmap.bmp_img1)
        pix = QtGui.QPixmap.fromImage(qim)
        self.widgetQLimg1.setPixmap(pix.scaledToWidth(bitmap.height * 2))

        self.widgetQLimg2 = QLabel()
        qim = ImageQt(bitmap.bmp_img2)
        pix = QtGui.QPixmap.fromImage(qim)
        self.widgetQLimg2.setPixmap(pix.scaledToWidth(bitmap.height * 2))

        layout = QGridLayout()
        layout.addWidget(self.widgetQLimg1, 0, 0, 1, 0)
        layout.addWidget(self.widgetQLimg2, 0, 1, 1, 1)
        layout.addWidget(self.widgetQLbl, 0, 2)
        layout.addWidget(widgetQCB, 2, 0)
        layout.addWidget(widgetQLE, 2, 1)
        layout.addWidget(widgetQBt, 2, 2)

        container = QWidget()
        container.setLayout(layout)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print("Clicked!")

        global choosen_key, choosen_cypher_i
        self.widgetQLbl.setText(process(choosen_key, choosen_cypher_i))

        os.startfile(r"text.txt")
        os.startfile(r"encrypted_text.txt")

    def index_changed(self, i):
        print(i)
        if i == 0:
            print()
        global choosen_cypher_i
        choosen_cypher_i = i

    def text_changed(self, s):
        print("Key changed...")
        print(s)
        global choosen_key
        choosen_key = s


def qt_main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    qt_main()
