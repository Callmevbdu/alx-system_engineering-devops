# Puppet manifest to kill a process named "killmenow" using pkill

exec { 'killmenow':
  command     => 'pkill -f killmenow || true',
  path        => ['/bin', '/usr/bin'],
  logoutput   => true,
  refreshonly => true,
}

