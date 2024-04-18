# Define an exec resource to increase open files limit
exec { 'increase_nginx_open_files' :
  environment => { 'PATH' => '/usr/bin:/bin' },
  command     => 'ulimit -n 15000',
  user        => 'nginx',
  unless      => 'ulimit -n | grep -q 15000',
  path        => ['/usr/bin', '/bin'],
  returns     => [0],
}

# Ensure Nginx service restarts after limit change
service { 'nginx':
  ensure => running,
  subprovider => 'systemd',
  requires => Exec['increase_nginx_open_files'],
}
