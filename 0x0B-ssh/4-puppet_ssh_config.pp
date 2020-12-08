# modify the file configuration of the client ssh :)
exec { '/etc/ssh/ssh_config':
    path    => '/usr/bin',
    command =>  'echo  "IdentityFile ~/.shh/holberton" >> /etc/ssh/ssh_config; echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
