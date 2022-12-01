# Poetry
## Configurar poetry para local
configurar poetry para virtualenv local
```python
poetry config virtualenvs.in-project true --local
```
configurar poetry para criar um virtualenv caso não exista ainda local
```python
poetry config virtualenvs.create true --local
```
## Exportar libs para o formato requirements
exportar requirements.txt
```python
poetry export > requirements.txt --without dev --without-hashes
```
exportar requirements-dev.txt
```python
poetry export > requirements-dev.txt --only dev --without-hashes
```