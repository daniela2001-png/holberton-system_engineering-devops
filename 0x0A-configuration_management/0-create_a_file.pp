# este archivo puppet crear un archivo holberton y le otroga permisos y escribe en el
file {'/tmp/holberton':
        owner   =>'www-data',
        group   =>'www-data',
        mode    =>'0744',
        content =>'I love Puppet',
}
