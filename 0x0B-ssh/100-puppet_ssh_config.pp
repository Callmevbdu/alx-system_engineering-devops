file { '/home/callmevbdu/.ssh/config':
  content => "
    Host 34.239.107.230
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}

