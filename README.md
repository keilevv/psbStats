# psbStats
Para la ejecución de este servico se utiliza Python 3.X.

## Pasos para calcular estadísticas.
1. [Ejecutar PSB API](https://github.com/skilletComatose/PSBapp)
2. Ingresar datos a la API por medio de POST. En list.py hay ejemplos de objetos JSON que se pueden utilizar para POST.
2. Crear ambiente virtual con python -m venv env
3. Ejecutar pip install -r requirements.txt
4. Ejecutar python stats.py
5. Para obtener estadísticas generales, ingresar a localhost:8000/psb/statistics 
6. Para obtener estadísticas específicas de un PSB, ingresar a localhost:8000/psb/statistics/<latitud>/<longitud>
  
 
