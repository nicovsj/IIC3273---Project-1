# Modified Merkle Paticia Trie

El código base es de: https://github.com/popzxc/merkle-patricia-trie 

## Requerimientos
* cytoolz==0.9.0.1
* eth-hash==0.2.0
* eth-typing==2.0.0
* eth-utils==1.4.1
* pycryptodome==3.7.3
* rlp==1.1.0
* toolz==0.9.0

## Estructura del codigo
El codigo está separado en cuatro archivos de código: 
1. <code>hash.py</code>
2. <code>nibble_path.py</code>
3. <code>node.py</code>
3. <code>mpt.py</code>

## Demo de uso
El archivo <code> Demo.ipynb </code> contiene una demo del uso de la libreria. Para correr el notebook basta tener los requerimientos instalados y el código base. 

## Modificaciones
* Se agrega el archivo <code>Demo.ipynb</code> para tener un demo interactivo de la librería
* Se agregan métodos <code>\_\_repr\_\_</code> para los objetos de la clase <code> Node </code>
