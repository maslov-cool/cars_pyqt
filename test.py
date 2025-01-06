import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QPointF, QRectF

design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>300</width>
    <height>300</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>300</width>
    <height>300</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>300</width>
    <height>300</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Машинки</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="lbl">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>140</y>
      <width>49</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Car(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(design)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.setMouseTracking(True)
        self.setGeometry(300, 300, 300, 300)

        self.A = ['car1.png', 'car2.png', 'car3.png']
        self.current_image_index = 0
        self.pixmap = QPixmap(self.A[self.current_image_index])
        self.lbl.setPixmap(self.pixmap)

    # Обработка движения мыши
    def mouseMoveEvent(self, event):
        if event.pos().x() <= 250 and event.pos().y() <= 250:
            self.lbl.move(event.pos().x(), event.pos().y())

    def keyPressEvent(self, event):
        # Проверяем, была ли нажата клавиша пробела
        if event.key() == Qt.Key.Key_Space:
            self.current_image_index += 1
            if self.current_image_index == len(self.A):
                self.current_image_index = 0
            self.pixmap = QPixmap(self.A[self.current_image_index])
            self.lbl.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Car()
    program.show()
    sys.exit(app.exec())
