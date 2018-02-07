import arcpy



class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [FirstScript]


class FirstScript(object):

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "First script"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input layer",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")
        param1 = arcpy.Parameter(
            displayName="Fields",
            name="in_Fields",
            datatype="GPString",
            parameterType="Required",
            multiValue = True,
            direction="Input")
       # param1.parameterDependencies = [param0.name]
        param1.filter.type = 'ValueList'
        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        if parameters[0].value:
            parameters[1].enabled = True
            futureFields = []
            for field in arcpy.ListFields(parameters[0].value):
                if field.type in ('Integer','SmallInteger','Single','Double','String'):
                    futureFields.append(field.name)
            parameters[1].filter.list = futureFields


        else:
            parameters[1].enabled = False
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        if len(str(parameters[1].value).split(';'))<2:
            parameters[1].setErrorMessage('minimum 2 fields')
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        myshape = parameters[0].value
       # arcpy.addMessage(myshape)
        myFields = parameters[1].valueAsText
       # arcpy.addMessage(myFields)
        listFields = myFields.split(';')
        arcpy.addMessage(listFields)
        arcpy.DeleteField_management(myshape,listFields)

        return
