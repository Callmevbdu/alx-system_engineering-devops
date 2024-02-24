# File: 2-execute_a_command.pp
# Puppet manifest to kill a process named "killmenow"

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin',
  refreshonly => true,
}

