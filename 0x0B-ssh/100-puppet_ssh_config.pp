file { '/home/callmevbdu/.ssh/config':
  ensure => present,
  owner  => 'callmevbdu',
  group  => 'callmevbdu',
  mode   => '0644',
  content => "
    Host 34.239.107.230
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}

