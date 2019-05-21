# N-reinas

## Problema 

Poner N reinas sin que se amenacen mutuamente  
https://es.wikipedia.org/wiki/Problema_de_las_ocho_reinas  

## Descripción solución:

- app.py : implementación de algoritmo y conexión a base de datos
- main.py: ejecución del programa e inserción en base de datos  
- test_8queen.py : implementación de pruebas

## Evaluación algoritmos

Se evaluaron dos algoritmos :  

- Fuerza bruta (https://github.com/snazrul1/PyRevolution/blob/master/Puzzles/N_Queen_Problem.ipynb)  
- Backtracking (https://github.com/edorado93/Save-The-Queens/blob/master/n-queens-backtracking-optimized.py)  

Basado en el análisis realizado se optó por usar bactracking (Para más detalles revisar libreta en directorio doc)


## Ejecución de pruebas de aplicación:
docker-compose -f docker-compose.common.yml -f docker-compose.test.yml build --no-cache  
docker-compose -f docker-compose.common.yml -f docker-compose.test.yml up  

## Ejecución de aplicación:
docker-compose -f docker-compose.common.yml -f docker-compose.prod.yml build  
docker-compose -f docker-compose.common.yml -f docker-compose.prod.yml up  

## Resultados :

Para un tiempo de 10 minutos de ejecución se obtuvo N=13 

## Notas :

- Travis CI : Se reporta error a pesar que las pruebas devuelven exit code 0. No encuentro la solución :(  

## Futuro :
- Implementar tablero a nivel de bits.  
- Evaluar algoritomo genético : https://handcraftsman.wordpress.com/2015/06/20/evolving-a-genetic-solver-in-python-part-2/  





