import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # create a QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.showMaximized()
        self.setWindowIcon(QIcon("web/hack.png"))
        
        

        self.home_url = "https://www.startpage.com/"

        # Create a new tab and set it as the current tab
        self.add_new_tab(self.home_url, "Home")
        

        # create a navigation toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction(QIcon('web/left.png'),'', self)
        back_btn.triggered.connect(self.tabs.currentWidget().back)
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon('web/right.png'),'', self)
        forward_btn.triggered.connect(self.tabs.currentWidget().forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon('web/refresh.png'),'', self)
        reload_btn.triggered.connect(self.tabs.currentWidget().reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon('web/home.png'),'', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        new_tab_btn = QAction(QIcon('web/newtab.png'),'', self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        navbar.addAction(new_tab_btn)

        

        image_tab_btn = QAction(QIcon('web/image'),'', self)
        image_tab_btn.triggered.connect(self.add_image_tab)
        navbar.addAction(image_tab_btn)
        
        
        
        # create a search bar
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search)
        navbar.addWidget(self.search_bar)


        news_tab_btn = QAction(QIcon('web/hack.png'),'', self)
        news_tab_btn.triggered.connect(self.add_news_tab)
        navbar.addAction(news_tab_btn)

        fire_tab_btn = QAction(QIcon('web/duckgo.png'),'', self)
        fire_tab_btn.triggered.connect(self.add_fire_tab)
        navbar.addAction(fire_tab_btn)


    def add_image_tab(self, url="", title="Images"):
        browser = QWebEngineView()
        self.images_url = "https://www.startpage.com/?sc=CPDjWH8rfhdl20&t=device&cat=images"
        self.add_new_tab(self.images_url, "Images")

    def add_news_tab(self, url="", title="News"):
        browser = QWebEngineView()
        self.news_url = "https://thehackernews.com/"
        self.add_new_tab(self.news_url, "News")

    
    def add_fire_tab(self, url="", title="Go"):
        browser = QWebEngineView()
        self.fire_url = "https://duckduckgo.com/"
        self.add_new_tab(self.fire_url, "Go")


    def add_new_tab(self, url=None, title="Custom Tab"):
        browser = QWebEngineView()

        # set url if given
        if url:
            browser.setUrl(QUrl(url))

        # create a new tab and set browser as its widget
        tab_index = self.tabs.addTab(browser, title)

        # make the new tab the current tab
        self.tabs.setCurrentIndex(tab_index)

        # update the url bar
        browser.urlChanged.connect(self.update_url)

    def search(self):
        url = self.search_bar.text()
        current_tab = self.tabs.currentWidget()
        current_tab.setUrl(QUrl(f"https://www.startpage.com/search?q={url}"))

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl(self.home_url))

    def update_url(self, q):
        self.search_bar.setText(q.toString())




app = QApplication(sys.argv)
QApplication.setApplicationName('EagleEye ')
window = MainWindow()
app.exec_()



