file { '/home/callmevbdu/.ssh/config':
  ensure  => present,
  mode    => '0600',
  owner   => 'callmevbdu',
  group   => 'callmevbdu',
  content => "\
Host 34.239.107.230
  HostName 34.239.107.230
  User 421391-web-01
  IdentityFile ~/.ssh/school
  PasswordAuthentication no\n",
}

