# Define an exec resource to increase open files limit for holberton user
exec { 'increase_open_files_holberton' :
  environment => ['DIR=/etc/default/nginx',
                  'OLD=ULIMIT="-n 15"',
                  'NEW=ULIMIT="-n 15000"'],
  command     => 'ulimit -n 1024 -u holberton',
  unless      => 'ulimit -n | grep -q 1024',
  path        => ['/usr/bin', '/bin'],
}
