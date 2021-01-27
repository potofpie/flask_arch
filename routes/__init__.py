import json
import use_cases
import flask
import libs 

from routes.makeStringManipulationRoutes import makeStringManipulationRoutes

def makeRoutes(path):
    makeStringManipulationRoutes(libs,use_cases,f'{path}/stringManipulation')