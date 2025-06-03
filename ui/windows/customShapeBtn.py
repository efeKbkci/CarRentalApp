from .. import QLabel, QPixmap
from PyQt6.QtGui import QPainterPath, QRegion
from PyQt6.QtCore import QPoint, QPropertyAnimation, QEasingCurve, QRect

class CustomShapeButton(QLabel):
    def __init__(
                    self, 
                    geometry: QRect,
                    bgImagePath:str = None, 
                    bgImageHoverPath:str = None,                     
                    shape:list[QPoint] = [],
                    callback = None,
                    animation: QPropertyAnimation = None,
                    parent = None
                ):
        super().__init__(parent)
        
        self.setGeometry(geometry)

        self.bgImagePath = bgImagePath
        self.bgImageHoverPath = bgImageHoverPath
        self.callback = callback 
        self.animation = animation

        bgImagePath and self.setBackgroundImage(bgImagePath)
        shape and self.adjustClickableArea(shape)

    def adjustClickableArea(self, shape: list[QPoint]):
        # By default all QWidget's have a rectangular shape. 
        # We change the clickable area of our button according to the area of our custom shape.

        self.path = QPainterPath() # Bir 0 vektörü oluşturur
        self.path.moveTo(shape[0]) # Pencere üzerinde vektörün çizime başlayacağı noktaya gelir
        [self.path.lineTo(qPoint) for qPoint in shape[1:]] # Verilen noktalar arasında vektörler çizer
        self.path.closeSubpath() # Çizilen vektörlerden kapalı bir şekil elde eder

        region = QRegion(self.path.toFillPolygon().toPolygon()) # Elde edilen kapalı şekli içi pixellerle dolu bir alana dönüştürür
        self.setMask(region) # Bu alanı widget'a uygulayarak widgetın görünür alanını kısıtlar veya maskeler. 

    def setBackgroundImage(self, bgImagePath: str) -> None:
        pixmap = QPixmap(bgImagePath)
        self.setPixmap(pixmap)
        self.setScaledContents(True)

    def createAnimation(self, initialRect: QRect, targetRect: QRect, duration: int = 150, animationType: bytes = b"geometry"):
        self.animation = QPropertyAnimation(self, animationType)
        self.animation.setDuration(duration)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.animation.setStartValue(initialRect)
        self.animation.setEndValue(targetRect)

    def mousePressEvent(self, ev):
        callable(self.callback) and self.callback()
        return super().mousePressEvent(ev)

    def enterEvent(self, event):        
        self.bgImageHoverPath and self.setBackgroundImage(self.bgImageHoverPath)
        if self.animation:
            self.animation.setDirection(QPropertyAnimation.Direction.Forward)
            self.animation.start()
        return super().enterEvent(event)
    
    def leaveEvent(self, a0):
        self.bgImagePath and self.setBackgroundImage(self.bgImagePath)
        if self.animation:
            self.animation.setDirection(QPropertyAnimation.Direction.Backward)
            self.animation.start()
        return super().leaveEvent(a0)