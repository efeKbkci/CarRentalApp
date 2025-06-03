from PyQt6.QtGui import QFontDatabase

class FontFamilies:
    
    """
        Bir custom font Qt Designer uygulamasından seçilse bile 
        eğer QFontDatabase ile uygulamaya dahil edilmemişse etkili olmayacaktır. 
    """

    @staticmethod
    def loadFonts() -> None:
        QFontDatabase.addApplicationFont(r"assets\fonts\static\RobotoMono-ExtraLight.ttf")
        QFontDatabase.addApplicationFont(r"assets\fonts\static\RobotoMono-Light.ttf")
        QFontDatabase.addApplicationFont(r"assets\fonts\static\RobotoMono-Medium.ttf")  
        QFontDatabase.addApplicationFont(r"assets\fonts\static\RobotoMono-SemiBold.ttf")
        QFontDatabase.addApplicationFont(r"assets\fonts\static\RobotoMono-Bold.ttf")      