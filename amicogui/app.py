from os.path import pathsep, abspath, dirname, join as path_join
import sys
from PySide6.QtWidgets import QApplication
from .widgets.main_window import MainWindow
from .widgets.recents_dialog import RecentsDialog
import configparser
from .logger import Logger

def start_app():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    # main_window.setFixedSize(1500, 870)
    main_window.show()

    config = configparser.ConfigParser()
    # config.read('amicogui.cfg')
    config.read(abspath(path_join(dirname(__file__), 'amicogui.cfg')))
    if int(config['N_RECENTS']['n_recents']) > 0:
        recents_dialog = RecentsDialog()
        recents_dialog.show()
        recents_dialog.closeEvent = lambda event: (main_window.load_recent(recents_dialog.recent_section), event.accept())

    # Styling
    # with open('style.qss', 'r') as style_file:
    with open(abspath(path_join(dirname(__file__), 'style.qss')), 'r') as style_file:
        _style = style_file.read()
        app.setStyleSheet(_style)

    sys.stdout = Logger()

    sys.exit(app.exec())