from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QToolBar, QAction, QMenuBar, QFileDialog
import sys


class TextEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Text Editor")
        self.resize(600, 540)

        self.menubar = QMenuBar(self)
        fileMenu = self.menubar.addMenu('File')
        openAction = QAction('Open...', self)
        saveAction = QAction('Save', self)
        saveAsAction = QAction('Save as...', self)
        printAction = QAction('Print...', self)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(printAction)

        self.toolbar = QToolBar(self)
        boldAction = QAction('Bold', self)
        self.toolbar.addAction(boldAction)
        italicAction = QAction('Italic', self)
        self.toolbar.addAction(italicAction)

        self.textEdit = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.menubar)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.textEdit)
        self.setLayout(layout)

        openAction.triggered.connect(self.open)
        saveAction.triggered.connect(self.save)
        saveAsAction.triggered.connect(self.save_as)
        boldAction.triggered.connect(self.bold)
        italicAction.triggered.connect(self.italic)
        printAction.triggered.connect(self.print)

        self.fileFilename = None

    def open(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', '', "Text files (*.html)")[0]
        with open(fname) as f:
            data = f.read()
            self.textEdit.setHtml(data)
            f.close()
        self.fileFilename = fname

    def save_as(self):
        save_name = QFileDialog.getSaveFileName(self, 'Save file')[0]
        file = open(save_name, 'w')
        text = self.textEdit.toHtml()
        file.write(text)
        file.close()
        self.fileFilename = save_name

    def save(self):
        if not self.fileFilename is None:
            file = open(self.fileFilename, 'w')
            text = self.textEdit.toHtml()
            file.write(text)
            file.close()
        else:
            self.save_as()

    def bold(self):
        cursor = self.textEdit.textCursor()
        text = self.textEdit.toPlainText()
        self.textEdit.setHtml(
            f'{text[:cursor.selectionStart()]}<b>{text[cursor.selectionStart(): cursor.selectionEnd()]}</b>{text[cursor.selectionEnd():]}')

    def italic(self):
        cursor = self.textEdit.textCursor()
        text = self.textEdit.toPlainText()
        self.textEdit.setHtml(
            f'{text[:cursor.selectionStart()]}<i>{text[cursor.selectionStart(): cursor.selectionEnd()]}</i>{text[cursor.selectionEnd():]}')

    def print(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditor()
    win.show()
    sys.exit(app.exec_())
