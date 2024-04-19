# Define an exec resource to increase open files limit
exec { 'increase_nginx_open_files' :
  environment => { 'PATH' => '/etc/default/nginx' },
  command     => 'ulimit -n 15000',
  user        => 'nginx',
  unless      => 'ulimit -n | grep -q 15000',
  path        => ['/usr/bin', '/bin'],
  returns     => [0],
}
