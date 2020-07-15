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
1. <code>hash.py</code> : este archivo contiene las funciones para hashear los datos usando keccak256
2. <code>nibble_path.py</code> : en este archivo se encuentra la clase NibblePath que se encarga de trabajar con los caminos de nibbles compuestos por las ramas y nodos del arbol. 
3. <code>node.py</code> : en este archivo se encuentra la clase Nodo, con subclases Hoja, Extensión y Rama (leaf, extension y branch). cada subclase posee métodos de encoding/decoding que utilizan la librería rlp (recurvise lenght prefix) de Python. Cada una de las subclases tiene una estructura distinta, que sigue el estándar de Ethereum: nodos Hoja guardan lo que resta de su key dado el camino subyacente (en este caso llamado path) y el dato almacenado. Las ramas branches guarda un arreglo de largo 16 que da lugar a cada uno de los hijos que puede tener este nodo. Además, se mantine un espacio para guardar datos, en caso de que el camino desde la raiz al nodo Branch sea una key.  Finalmente los nodos de extensión guardan un prefijo (que comparten todos los caminos hijos desde el nodo en cuestión) y una referencia a un siguiente nodo (que será un nodo Rama)
3. <code>mpt.py</code> : finalmente, este archivo arma la estructura del Patricia Merkle Trie que permite crear un arbol, añadir/actualizar/eliminar pares (key, value) en el arbol, obtener el hash del arbol (asociado a su raiz). 
## Modificaciones
* Se agrega el archivo <code>Demo.ipynb</code> para tener un demo interactivo de la librería
* Se agregan métodos <code>\_\_repr\_\_</code> para los objetos de la clase <code> Node </code>

## Demo de uso
El archivo <code> Demo.ipynb </code> contiene una demo del uso de la libreria. Para correr el notebook basta tener los requerimientos instalados y el código base. En la demo se agregan 3 pares (key,value) y se obtiene el siguiente MPT:

![Demo MPT](https://user-images.githubusercontent.com/26121579/87588379-8fa9c380-c6b1-11ea-8fff-a68fc78b6683.png)


