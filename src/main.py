import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
import pyautogui
import keyboard
import time


class ScreenCaptureApp(QWidget):
    def __init__(self):
        super().__init__()

        self.repetitions_label = None
        self.repetitions = None
        self.stop_flag = None
        self.stop_button = None
        self.start_button = None
        self.repetitions_entry = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Screen Capture App")

        # Total Page 입력 칸
        self.repetitions_label = QLabel("Total Page:")
        self.repetitions_entry = QLineEdit()
        repetitions_layout = QHBoxLayout()
        repetitions_layout.addWidget(self.repetitions_label)
        repetitions_layout.addWidget(self.repetitions_entry)

        # Start와 Stop 버튼
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.start_button)
        buttons_layout.addWidget(self.stop_button)

        # 전체 레이아웃
        layout = QVBoxLayout()
        layout.addLayout(repetitions_layout)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        # 버튼에 클릭 이벤트 연결
        self.start_button.clicked.connect(self.start_capture)
        self.stop_button.clicked.connect(self.stop_capture)

        # 초기화
        self.stop_flag = False
        self.repetitions = 0

    def start_capture(self):
        try:
            self.repetitions = int(self.repetitions_entry.text())
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Please enter a valid number for total pages.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        time.sleep(3)
        pyautogui.press('enter')

        for _ in range(self.repetitions):
            if self.stop_flag:
                break

            pyautogui.hotkey('command', 'shift', '5')
            time.sleep(0.2)
            pyautogui.press('enter')
            time.sleep(0.5)
            keyboard.press_and_release('right')
            time.sleep(0.3)

    def stop_capture(self):
        self.stop_flag = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScreenCaptureApp()
    ex.show()
    sys.exit(app.exec_())
