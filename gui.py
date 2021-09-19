from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QPushButton, QLineEdit, QComboBox
import pytube as pt
import sys


def search(text):
    yt = pt.Search(text)

    # Filter and show user the results
    results_code = yt.results
    results_name = yt.completion_suggestions
    results_length = len(results_name)
    new_results_name = filter_name(results_name)
    return new_results_name, results_code, results_length


def filter_code(results_code):
    new_result_code = []

    for string in results_code:
        new_string = str(string).replace("<pytube.__main__.YouTube object: videoId=", "")
        new_string = new_string.replace(">", "")
        new_result_code.append(new_string)
    return new_result_code


def filter_name(results_name):
    number = 0
    new_results = ""
    options_name = ""

    for string in results_name:
        number += 1
        options_name = str(number) + ". " + string + " \n"
        new_results = new_results + options_name
        new_results = new_results.title()

    return new_results


def generate_link(user_choice, final_code):
    link = "https://www.youtube.com/watch?v=" + final_code[int(user_choice) - 1]
    return link


def download(final_link):
    video = pt.YouTube(final_link)
    video = video.streams.get_highest_resolution()
    video.download()


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.search_button = QPushButton('Search', self)
        self.search_box = QLineEdit(self)
        self.title = 'pyYouTube Downloader'
        self.left = 650
        self.top = 250
        self.width = 700
        self.height = 500
        self.start_gui()

    def start_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create search bar
        self.search_box.move(20, 20)
        self.search_box.resize(600, 40)

        # Create search button in the window
        self.search_button.move(20, 80)

        # connect search button to function search_click
        self.search_button.clicked.connect(self.search_click)
        self.show()

    def search_click(self):
        final_link = ""
        textbox_value = self.search_box.text()
        final_name, final_code, final_length = search(text=textbox_value)
        final_code = filter_code(final_code)
        print(final_code)
        user_choice, proceed = QInputDialog.getText(self, 'Choose video', 'These are the results:\n\n' + final_name +
                                                    '\n\nWhich one you want?')
        if proceed:
            final_link = generate_link(user_choice, final_code)
            print(final_link)
            download(final_link)
            return final_link


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
