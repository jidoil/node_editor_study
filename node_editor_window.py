import math
from PySide2.QtCore import QLine
from PySide2.QtGui import QColor, QBrush, QPen
from PySide2.QtWidgets import QGraphicsScene


class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 세팅
        self.gridSize = 20
        self.gridSquares = 5
        self._color_background = QColor("#393939")

        self._color_light = QColor("#2f2f2f")
        self._color_dark = QColor("#292929")

        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)

        self.scene_width, self.scene_height = 64000, 64000
        self.setSceneRect(-self.scene_width//2, -self.scene_height//2, self.scene_width, self.scene_height)


        self.setBackgroundBrush(QBrush(self._color_background))



    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)
        lines_light, lines_dark = [], []

        left = int(math.floor(rect.left()))
        right = int(math.floor(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.floor(rect.bottom()))

        first_left = left - (left % self.gridSize)
        first_top = top - (top % self.gridSize)

        for x in range(first_left, right, self.gridSize):
            if x % (self.gridSize * self.gridSquares) != 0 :
                lines_light.append(QLine(x, top, x, bottom))
            else :
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.gridSize):
            if y % (self.gridSize * self.gridSquares) != 0 :
                lines_light.append(QLine(left, y, right, y))
            else :
                lines_dark.append(QLine(left, y, right, y))

        painter.setPen(self._pen_light)
        painter.drawLines(lines_light)
        painter.setPen(self._pen_dark)
        painter.drawLines(lines_dark)