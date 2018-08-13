import arcpy
import pythonaddins

num = None


class ButtonClass10(object):
    """Implementation for Addin2_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        ComboBoxClass7.value = 555
        combo = ComboBoxClass7()
        combo.refresh()
        print ComboBoxClass7.value
        pass

class ButtonClass6(object):
    """Implementation for Addin2_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        ComboBoxClass7.value = "8"
        combo = ComboBoxClass7()
        combo.refresh()
        
        print combo.value
        pass

class ComboBoxClass7(object):
    """Implementation for Addin2_addin.combobox (ComboBox)"""
    def __init__(self):
        #self.value = "Hello" 
        self.items = [1,2,3]
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWWWW'
        
    def onSelChange(self, selection):
        pass
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        pass
    def refresh(self):
       # self.refresh()
        print 'selfRfresh'
        #self.value = 8
        pass

class ToolClass9(object):
    """Implementation for Addin2_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        print 
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass
